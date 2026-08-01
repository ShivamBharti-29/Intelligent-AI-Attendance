# 🎓 Intelligent AI Attendance System

An AI-powered attendance management system that automates classroom attendance using **Face Recognition** and **Voice Recognition**. The system enables teachers to create subjects, generate QR-based class invitations, and allows students to register, enroll, and mark attendance securely through AI.

## 🚀 Live Demo

### 🌐 Landing Page
> https://intelligent-ai-attendance-onzf5s5rw-shivambharti-29s-projects.vercel.app/

### 🤖 AI Attendance Application
> https://intelligent-ai-attendance-fnl5cwown9lpmxsyveum5y.streamlit.app/

---

# ✨ Features

### 👨‍🏫 Teacher Module
- Secure teacher registration and login
- Create and manage subjects
- View enrolled students
- Mark attendance using AI
- View attendance history
- Generate QR code and class join links

### 👨‍🎓 Student Module
- Face-based login
- New student registration
- Optional voice enrollment
- Join classes using QR code or invitation link
- View enrolled subjects
- View attendance statistics
- Unenroll from subjects

### 🤖 AI Features
- Face Recognition using **Dlib**
- Face Embedding Generation
- Voice Embedding using **Resemblyzer**
- Automatic Face Recognition
- AI-based Student Identification
- QR Code Based Enrollment

---

# 🏗️ Project Architecture

```
                    Landing Page (Vercel)
                            │
                            ▼
                  Streamlit AI Application
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
 Face Recognition     Voice Recognition     Supabase
      (Dlib)           (Resemblyzer)        Database
```

---

# 🛠️ Tech Stack

## Frontend
- HTML5
- CSS3
- JavaScript
- Flask
- Vercel

## Backend
- Streamlit
- Python

## Artificial Intelligence
- Dlib
- Scikit-Learn
- NumPy
- Resemblyzer
- Librosa

## Database
- Supabase

## Other Libraries
- Pillow
- Segno (QR Code)
- BCrypt

---

# 📂 Project Structure

```
Intelligent_AI_Attendance/
│
├── backend/
│   ├── src/
│   │   ├── components/
│   │   ├── database/
│   │   ├── pipelines/
│   │   ├── screens/
│   │   └── ui/
│   ├── app.py
│   └── requirements.txt
│
├── frontend/
│   ├── static/
│   ├── templates/
│   ├── app.py
│   ├── requirements.txt
│   └── vercel.json
│
├── README.md
└── .gitignore
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Intelligent-AI-Attendance.git
cd Intelligent-AI-Attendance
```

---

## Backend Setup

```bash
cd backend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

streamlit run app.py
```

---

## Frontend Setup

```bash
cd frontend

python -m venv .venv

# Windows
.venv\Scripts\activate

pip install -r requirements.txt

python app.py
```

---

# 🔐 Environment Variables

Create a `.env` file inside the **backend** directory.

```env
SUPABASE_URL=YOUR_SUPABASE_URL
SUPABASE_KEY=YOUR_SUPABASE_ANON_KEY
```

---

# 📸 Screenshots

## Landing Page

> Add screenshot here

---

## Home Screen

> Add screenshot here

---

## Teacher Dashboard

> Add screenshot here

---

## Student Dashboard

> Add screenshot here

---

## QR Code Enrollment

> Add screenshot here

---

## Face Recognition Login

> Add screenshot here

---

## Voice Enrollment

> Add screenshot here

---

# 🚀 Deployment

### Frontend
- Vercel

### Backend
- Streamlit Community Cloud

### Database
- Supabase

---

# 🔮 Future Improvements

- Email Notifications
- Attendance Analytics Dashboard
- Multi-Class Scheduling
- Liveness Detection
- Mobile Application
- Attendance Export (PDF/Excel)
- Face Recognition Performance Optimization
- Voice Authentication Improvements

---

# 👨‍💻 Author

**Shivam Bharti**

GitHub: https://github.com/ShivamBharti-29

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
