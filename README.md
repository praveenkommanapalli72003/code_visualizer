# Multi-Language Code Execution Visualizer

A simple, modular **code execution visualizer** built with **Flask**, **HTML**, and **Tailwind CSS**. The project currently supports **real execution and visualization for Python**
while **C, C++, and Java** are implemented as **planned/demo stubs** to demonstrate extensible architecture.

This repository is ideal for:

* Learning how execution visualization works
* Interview discussions on system design
* Extending to multiple programming languages

---

## 🚀 Features

* 🌐 Clean UI using **HTML + Tailwind CSS**
* 🔁 Language selector (Python, C, C++, Java)
* 🐍 **Python engine** with real code execution and visualization
* 🧱 **Stub engines** for C / C++ / Java (demo output)
* 🧩 Modular and extensible backend architecture
* 🎯 Interview-ready project with clear design intent

---

## 🏗️ Architecture (Simple & Modular)

```
Frontend (UI)
   ↓
Backend Router (Flask)
   ↓
Language Engine
   ├── Python Engine (REAL execution)
   ├── C Engine (Stub / Planned)
   └── Java Engine (Stub / Planned)
```

Each language is isolated into its own engine, making the system easy to extend in the future.

---

## 📁 Folder Structure

```
multi_lang_visualizer/
├── app.py
├── templates/
│   └── index.html
└── static/
    └── script.js
```

---

## ⚙️ Tech Stack

* **Backend:** Python, Flask
* **Frontend:** HTML, Tailwind CSS, JavaScript
* **Execution Engine:** Python (real), C/C++/Java (stub)

---

## ▶️ How to Run the Project

### 1️⃣ Install dependencies

```bash
pip install flask
```

### 2️⃣ Run the application

```bash
python app.py
```

## 🧠 How It Works

1. User enters code and selects a language
2. Frontend sends the request to Flask backend
3. Backend routes the request to the selected language engine
4. Python engine executes code and returns step-wise output
5. Other languages return demo/planned responses

---


## 🧩 Extending to Other Languages

To add real execution for C / C++ / Java:

* Create a new engine module
* Compile and execute code safely (e.g., using Docker or sandboxing)
* Return structured execution steps to the frontend

The architecture already supports this without UI changes.

---

## 💬 Interview Gold Line

> **"Execution visualization is language-specific. I implemented a modular architecture with Python execution support and extensible engines for other languages."**

---

## 📌 Project Status

* ✅ UI: Completed
* ✅ Backend routing: Completed
* ✅ Python execution engine: Implemented
* 🟡 C / C++ / Java engines: Stub (planned)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests for:

* New language engines
* Improved visualizations
* Security enhancements

---

## 📄 License

This project is open-source and free to use for learning and educational purposes.

---

⭐ If you like this project, consider giving it a star!
