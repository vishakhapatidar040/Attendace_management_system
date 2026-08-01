from datetime import date
from functools import wraps
import platform
import sqlite3
import sys
from pathlib import Path

from flask import Flask, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "attendance.db"

app = Flask(__name__)
app.secret_key = "attendance-management-system"
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = generate_password_hash("admin123")


def login_required(view_function):
    @wraps(view_function)
    def wrapped_view(*args, **kwargs):
        if not session.get("admin_logged_in"):
            return redirect(url_for("login"))
        return view_function(*args, **kwargs)

    return wrapped_view


def get_db():
    database = getattr(g, "_database", None)
    if database is None:
        database = g._database = sqlite3.connect(DATABASE_PATH)
        database.row_factory = sqlite3.Row
    return database


def init_db():
    database = sqlite3.connect(DATABASE_PATH)
    cursor = database.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            roll_no TEXT NOT NULL UNIQUE,
            section TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS attendance (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            attendance_date TEXT NOT NULL,
            status TEXT NOT NULL CHECK(status IN ('Present', 'Absent')),
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(student_id, attendance_date),
            FOREIGN KEY(student_id) REFERENCES students(id) ON DELETE CASCADE
        )
        """
    )

    database.commit()
    database.close()


@app.teardown_appcontext
def close_db(_error):
    database = getattr(g, "_database", None)
    if database is not None:
        database.close()


def fetch_students():
    database = get_db()
    return database.execute("SELECT * FROM students ORDER BY name COLLATE NOCASE").fetchall()


def fetch_attendance_for_date(attendance_date):
    database = get_db()
    return database.execute(
        """
        SELECT student_id, status
        FROM attendance
        WHERE attendance_date = ?
        """,
        (attendance_date,),
    ).fetchall()


@app.context_processor
def inject_globals():
    database = get_db()
    total_students = database.execute("SELECT COUNT(*) AS count FROM students").fetchone()["count"]
    total_present_today = database.execute(
        """
        SELECT COUNT(*) AS count
        FROM attendance
        WHERE attendance_date = DATE('now') AND status = 'Present'
        """
    ).fetchone()["count"]
    return {
        "today": date.today().isoformat(),
        "total_students": total_students,
        "total_present_today": total_present_today,
        "admin_logged_in": session.get("admin_logged_in", False),
    }


@app.route("/")
def index():
    students = fetch_students()
    recent_students = students[:5]
    return render_template("index.html", recent_students=recent_students)


@app.route("/settings")
def settings():
    system_info = {
        "application": "Smart Attendance Management System",
        "python_version": sys.version.split()[0],
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "database": str(DATABASE_PATH.name),
        "database_location": str(DATABASE_PATH),
        "flask_debug": app.debug,
    }
    return render_template("settings.html", system_info=system_info)


@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get("admin_logged_in"):
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")

        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session["admin_logged_in"] = True
            flash("Welcome back, admin.", "success")
            return redirect(url_for("dashboard"))

        flash("Invalid username or password.", "error")

    return render_template("login.html")


@app.route("/logout")
def logout():
    session.clear()
    flash("You have been logged out.", "success")
    return redirect(url_for("login"))


@app.route("/dashboard")
@login_required
def dashboard():
    database = get_db()
    summary = database.execute(
        """
        SELECT
            COUNT(DISTINCT students.id) AS students_count,
            SUM(CASE WHEN attendance.status = 'Present' THEN 1 ELSE 0 END) AS present_count,
            SUM(CASE WHEN attendance.status = 'Absent' THEN 1 ELSE 0 END) AS absent_count
        FROM students
        LEFT JOIN attendance ON attendance.student_id = students.id
        """
    ).fetchone()

    latest_records = database.execute(
        """
        SELECT students.name, students.roll_no, attendance.attendance_date, attendance.status
        FROM attendance
        JOIN students ON students.id = attendance.student_id
        ORDER BY attendance.attendance_date DESC, students.name ASC
        LIMIT 10
        """
    ).fetchall()

    return render_template("dashboard.html", summary=summary, latest_records=latest_records)


@app.route("/students")
@login_required
def students():
    return render_template("students.html", students=fetch_students())


@app.route("/students/add", methods=["GET", "POST"])
@login_required
def add_student():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll_no = request.form.get("roll_no", "").strip()
        section = request.form.get("section", "").strip()

        if not name or not roll_no:
            flash("Name and roll number are required.", "error")
            return redirect(url_for("add_student"))

        database = get_db()
        try:
            database.execute(
                "INSERT INTO students (name, roll_no, section) VALUES (?, ?, ?)",
                (name, roll_no, section),
            )
            database.commit()
            flash("Student added successfully.", "success")
            return redirect(url_for("students"))
        except sqlite3.IntegrityError:
            flash("Roll number must be unique.", "error")
            return redirect(url_for("add_student"))

    return render_template("add_student.html")


@app.route("/students/<int:student_id>/edit", methods=["GET", "POST"])
@login_required
def edit_student(student_id):
    database = get_db()
    student = database.execute("SELECT * FROM students WHERE id = ?", (student_id,)).fetchone()

    if student is None:
        flash("Student not found.", "error")
        return redirect(url_for("students"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        roll_no = request.form.get("roll_no", "").strip()
        section = request.form.get("section", "").strip()

        if not name or not roll_no:
            flash("Name and roll number are required.", "error")
            return redirect(url_for("edit_student", student_id=student_id))

        try:
            database.execute(
                "UPDATE students SET name = ?, roll_no = ?, section = ? WHERE id = ?",
                (name, roll_no, section, student_id),
            )
            database.commit()
            flash("Student updated successfully.", "success")
            return redirect(url_for("students"))
        except sqlite3.IntegrityError:
            flash("Roll number must be unique.", "error")
            return redirect(url_for("edit_student", student_id=student_id))

    return render_template("add_student.html", student=student)


@app.route("/students/<int:student_id>/delete", methods=["POST"])
@login_required
def delete_student(student_id):
    database = get_db()
    database.execute("DELETE FROM students WHERE id = ?", (student_id,))
    database.execute("DELETE FROM attendance WHERE student_id = ?", (student_id,))
    database.commit()
    flash("Student deleted successfully.", "success")
    return redirect(url_for("students"))


@app.route("/attendance", methods=["GET", "POST"])
def attendance():
    database = get_db()
    selected_date = request.form.get("attendance_date") if request.method == "POST" else request.args.get("date")
    selected_date = selected_date or date.today().isoformat()
    students = fetch_students()
    attendance_rows = fetch_attendance_for_date(selected_date)
    attendance_map = {row["student_id"]: row["status"] for row in attendance_rows}

    if request.method == "POST":
        for student in students:
            status = request.form.get(f"student_{student['id']}", "Absent")
            database.execute(
                """
                INSERT INTO attendance (student_id, attendance_date, status)
                VALUES (?, ?, ?)
                ON CONFLICT(student_id, attendance_date)
                DO UPDATE SET status = excluded.status
                """,
                (student["id"], selected_date, status),
            )
        database.commit()
        flash("Attendance saved successfully.", "success")
        return redirect(url_for("attendance", date=selected_date))

    return render_template(
        "attendance.html",
        students=students,
        selected_date=selected_date,
        attendance_map=attendance_map,
    )


@app.route("/reports")
@login_required
def reports():
    database = get_db()
    report_rows = database.execute(
        """
        SELECT
            students.id,
            students.name,
            students.roll_no,
            students.section,
            COUNT(attendance.id) AS total_marked,
            SUM(CASE WHEN attendance.status = 'Present' THEN 1 ELSE 0 END) AS present_count,
            SUM(CASE WHEN attendance.status = 'Absent' THEN 1 ELSE 0 END) AS absent_count
        FROM students
        LEFT JOIN attendance ON attendance.student_id = students.id
        GROUP BY students.id
        ORDER BY students.name COLLATE NOCASE
        """
    ).fetchall()

    return render_template("reports.html", report_rows=report_rows)


if __name__ == "__main__":
    init_db()
    app.run(debug=True)