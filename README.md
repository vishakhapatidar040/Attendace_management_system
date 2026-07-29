#Attendance_management_system

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Smart Attendance Management System</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;600&display=swap');

  :root{
    --bg: #0d1021;
    --bg2: #161a35;
    --cyan: #4fd1ff;
    --violet: #a78bfa;
    --pink: #ff6fb0;
    --text: #e7e9f5;
    --muted: #9aa0c3;
  }

  *{box-sizing:border-box;}

  body{
    margin:0;
    background: radial-gradient(circle at 20% 0%, var(--bg2), var(--bg) 60%);
    color: var(--text);
    font-family: 'Inter', sans-serif;
    padding: 60px 20px;
    overflow-x:hidden;
  }

  .wrap{
    max-width: 760px;
    margin: 0 auto;
  }

  .eyebrow{
    display:inline-block;
    font-family:'Space Grotesk', sans-serif;
    font-size: 13px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--cyan);
    border: 1px solid rgba(79,209,255,0.35);
    padding: 6px 14px;
    border-radius: 999px;
    opacity: 0;
    animation: rise 0.6s ease forwards;
  }

  h1{
    font-family: 'Space Grotesk', sans-serif;
    font-size: clamp(34px, 6vw, 56px);
    line-height: 1.1;
    margin: 18px 0 10px;
    background: linear-gradient(90deg, var(--cyan), var(--violet) 50%, var(--pink));
    background-size: 200% auto;
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    animation: rise 0.6s ease 0.1s forwards, shine 6s linear infinite;
    opacity:0;
  }

  .tagline{
    color: var(--muted);
    font-size: 18px;
    max-width: 560px;
    opacity:0;
    animation: rise 0.6s ease 0.2s forwards;
  }

  .badges{
    display:flex;
    gap:10px;
    flex-wrap:wrap;
    margin: 22px 0 40px;
    opacity:0;
    animation: rise 0.6s ease 0.3s forwards;
  }
  .badge{
    font-family:'Space Grotesk', sans-serif;
    font-size: 12px;
    font-weight:700;
    padding: 6px 12px;
    border-radius: 8px;
    color: #0d1021;
  }
  .b1{ background: var(--cyan); }
  .b2{ background: var(--violet); }
  .b3{ background: var(--pink); }

  h2{
    font-family:'Space Grotesk', sans-serif;
    font-size: 22px;
    margin: 42px 0 16px;
    color: var(--cyan);
  }

  p{ color: var(--muted); line-height:1.7; }

  .grid{
    display:grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-top: 10px;
  }
  @media (max-width:520px){ .grid{ grid-template-columns: 1fr; } }

  .card{
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 18px;
    opacity:0;
    transform: translateY(14px);
    animation: rise 0.5s ease forwards;
    transition: transform .25s ease, border-color .25s ease;
  }
  .card:hover{
    transform: translateY(-4px);
    border-color: var(--violet);
  }
  .card .icon{ font-size: 22px; }
  .card h3{
    font-family:'Space Grotesk', sans-serif;
    font-size: 15px;
    margin: 10px 0 6px;
    color: var(--text);
  }
  .card p{ font-size: 13.5px; margin:0; }

  .grid .card:nth-child(1){ animation-delay: 0.35s; }
  .grid .card:nth-child(2){ animation-delay: 0.42s; }
  .grid .card:nth-child(3){ animation-delay: 0.49s; }
  .grid .card:nth-child(4){ animation-delay: 0.56s; }

  .steps{ margin-top: 10px; }
  .step{
    display:flex;
    align-items:center;
    gap: 14px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    opacity:0;
    animation: rise 0.5s ease forwards;
  }
  .step:nth-child(1){ animation-delay:0.4s; }
  .step:nth-child(2){ animation-delay:0.48s; }
  .step:nth-child(3){ animation-delay:0.56s; }
  .step:nth-child(4){ animation-delay:0.64s; }
  .num{
    font-family:'Space Grotesk', sans-serif;
    font-weight:700;
    color: var(--bg);
    background: linear-gradient(135deg, var(--cyan), var(--pink));
    width: 30px; height:30px;
    border-radius: 50%;
    display:flex; align-items:center; justify-content:center;
    flex-shrink:0;
    font-size: 13px;
  }

  footer{
    margin-top: 50px;
    text-align:center;
    color: var(--muted);
    font-size: 13px;
    opacity:0;
    animation: rise 0.6s ease 0.8s forwards;
  }

  @keyframes rise{
    from{ opacity:0; transform: translateY(14px); }
    to{ opacity:1; transform: translateY(0); }
  }
  @keyframes shine{
    to{ background-position: 200% center; }
  }

  @media (prefers-reduced-motion: reduce){
    *{ animation: none !important; opacity:1 !important; transform:none !important; }
  }
</style>
</head>
<body>
  <div class="wrap">
    <span class="eyebrow">Final Year Project</span>
    <h1>Smart Attendance<br>Management System</h1>
    <p class="tagline">A fast, reliable way to track attendance — built to cut manual errors and save everyone's time.</p>

    <div class="badges">
      <span class="badge b1">Active</span>
      <span class="badge b2">Python 3.10</span>
      <span class="badge b3">MIT License</span>
    </div>

    <h2>✨ Key Features</h2>
    <div class="grid">
      <div class="card"><div class="icon">✅</div><h3>Real-time tracking</h3><p>Attendance updates instantly as it's marked.</p></div>
      <div class="card"><div class="icon">📊</div><h3>Auto reports</h3><p>Generates summaries and analytics on demand.</p></div>
      <div class="card"><div class="icon">🔐</div><h3>Secure access</h3><p>Role-based login for admins and teachers.</p></div>
      <div class="card"><div class="icon">⏰</div><h3>Smart alerts</h3><p>Notifies on shortage or irregular attendance.</p></div>
    </div>

    <h2>🚦 How It Works</h2>
    <div class="steps">
      <div class="step"><div class="num">1</div><p>Admin or teacher logs in</p></div>
      <div class="step"><div class="num">2</div><p>Attendance is marked or scanned</p></div>
      <div class="step"><div class="num">3</div><p>Records update automatically</p></div>
      <div class="step"><div class="num">4</div><p>Reports are generated instantly</p></div>
    </div>

    <footer>Made with ❤️ and lots of ☕</footer>
  </div>
</body>
</html>
