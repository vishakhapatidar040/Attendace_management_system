<!-- Animated Title + Short Description -->
<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=26&duration=2200&pause=800&color=F7A700&center=true&vCenter=true&multiline=true&width=900&height=140&lines=Smart+Attendance+Management+System;Replace+manual+attendance+registers+with+a+smart+web+app;Admin+login%2C+student+management%2C+daily+attendance;Instant+attendance+percentage+reports+for+every+student" alt="Smart Attendance Management System Animated Description" />
</p>

---

## About the Project

The **Smart Attendance Management System** turns a traditional paper register into a modern, browser-based dashboard. With secure admin login, a simple student management interface, and date-wise attendance tracking, it lets you view clean percentage reports for every student in just a few clicks.  
Designed for teachers and institutes who want fast, error-free attendance — without Excel chaos. ✨

---

## Key Features

- 🔐 **Admin login** with secure password hashing  
- 👨‍🎓 **Student management** — add, edit, or remove students easily  
- 📆 **Daily attendance marking** — select a date and mark present/absent  
- 📊 **Auto-generated reports** with attendance percentage per student  
- 🧾 **Attendance history** for each student, viewed anytime  

---

## Built With

| Technology | Purpose             |
|-----------|---------------------|
| Python    | Core language       |
| Flask     | Web framework       |
| HTML/CSS  | User interface      |
| SQLite    | Lightweight database|

---

## Getting Started

Follow these steps to run the project on your local machine.

### Prerequisites

Make sure you have:

- Python installed (3.x recommended)  
- Git installed (optional but useful for cloning the repo)  

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/Attendance_management_system.git
   cd Attendance_management_system
   ```

2. **Create and activate a virtual environment** (optional but recommended)

   ```bash
   python -m venv venv
   # Mac/Linux:
   source venv/bin/activate
   # Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py    # agar tumhara main Flask file ka naam kuch aur hai, yaha change karo
   ```

5. **Open in browser**

   - Go to: `http://127.0.0.1:5000`  
   - Login as admin, add students, and start marking attendance.

---

## Folder Structure

A typical structure looks like:

```text
Attendance_management_system/
├─ app.py
├─ README.md
├─ requirements.txt
├─ templates/
│  ├─ index.html
│  ├─ login.html
│  ├─ dashboard.html
├─ static/
│  ├─ css/
│  ├─ js/
└─ database/
   └─ attendance.db
```

*(Exact files may differ based on your implementation.)*

---

## Future Improvements

- 📌 Role-based access for teachers and admins  
- 📈 Visual dashboards with charts for attendance analytics  
- 📤 Export attendance data as PDF/Excel  
- ✉️ Email or SMS alerts for low attendance  

---

## License

This project is licensed under the **MIT License**.  
You’re free to use, modify, and improve it for learning or production use. 🚀
