# 🩺 AI-Based Medical Training Simulator

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-F7DF1E?logo=javascript&logoColor=black)
![AI](https://img.shields.io/badge/Generative%20AI-Gemini%20API-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> An AI-powered medical training platform that generates realistic virtual patient scenarios, enabling medical students to practice clinical reasoning, diagnosis, and treatment planning in a safe learning environment.

---

## 📖 Overview

The **AI-Based Medical Training Simulator** is a web application developed to help medical students improve their diagnostic skills through interactive AI-generated patient cases.

The simulator creates realistic patient conversations, evaluates the student's diagnosis, suggests investigations, and provides educational feedback using Generative AI.

---

## ✨ Features

- 🧑‍⚕️ AI-generated virtual patients
- 💬 Interactive doctor-patient conversation
- 🩺 Symptom-based clinical scenarios
- 🧪 Investigation recommendations
- 📋 Diagnosis evaluation
- 💊 Treatment suggestions
- 📊 Instant feedback and learning support
- 🌐 User-friendly web interface

---

## 🏗️ System Architecture

```text
Medical Student
        │
        ▼
Flask Web Application
        │
        ▼
Generative AI API (Gemini/Mistral)
        │
        ▼
Patient Scenario Generator
        │
        ▼
Diagnosis Evaluation
        │
        ▼
Feedback & Treatment Recommendation
```

---

## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Backend | Python, Flask |
| Frontend | HTML, CSS, JavaScript |
| AI | Gemini API / Mistral API |
| IDE | Visual Studio Code |
| Version Control | Git & GitHub |

---

## 📂 Project Structure

```text
Medical-Training-Simulator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── templates/
│      └── index.html
│
├── static/
│      ├── style.css
│      ├── script.js
│      └── images/
│
├── screenshots/
│      ├── home.png
│      ├── patient_case.png
│      ├── diagnosis.png
│      └── feedback.png
│
├── report/
│      └── AI_Medical_Training_Simulator_Report.pdf
│
├── sample_io/
│      ├── sample_input.txt
│      └── sample_output.txt
│
├── dataset/
│
└── prompts/
       └── prompt_templates.md
```

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Medical-Training-Simulator.git
```

Navigate to the project folder

```bash
cd Medical-Training-Simulator
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open your browser

```
http://127.0.0.1:5000
```

---

## 📸 Application Screenshots

### 🏠 Home Page

![Home](screenshots/home.png)

---

### 👤 Patient Scenario

![Patient](screenshots/patient_case.png)

---

### 🩺 Diagnosis Interface

![Diagnosis](screenshots/diagnosis.png)

---

### ✅ AI Feedback

![Feedback](screenshots/feedback.png)

---

## 📝 Sample Input

```text
Patient Name: Rajesh

Age: 45

Symptoms:
• Fever
• Chest Pain
• Persistent Cough
• Shortness of Breath

Student Diagnosis:
Community Acquired Pneumonia
```

---

## 📤 Sample Output

```text
Diagnosis Score : 92%

Correct Diagnosis:
Community Acquired Pneumonia

Recommended Tests:
• CBC
• Chest X-ray
• CRP

Treatment:
• Azithromycin
• Hydration
• Rest

AI Feedback:
Excellent clinical reasoning.
```

---

## 🎯 Learning Objectives

- Improve diagnostic reasoning
- Practice patient interviewing
- Learn differential diagnosis
- Recommend investigations
- Develop treatment planning skills

---

## 🚀 Future Enhancements

- 🎤 Voice-based patient interaction
- 🩻 Medical image interpretation
- 📈 Performance analytics dashboard
- 🌍 Multi-language support
- ☁️ Cloud deployment
- 👨‍🏫 Faculty assessment module

---

## 👨‍💻 Author

**Syed Abuthahir**

Biomedical Engineering Student

Dr. N.G.P Institute of Technology

---

## 📄 License

This project is intended for educational and academic purposes.

MIT License

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
