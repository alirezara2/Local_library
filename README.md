# 📐 Local Math Library - Calculator Project

A simple modular calculator that demonstrates how to create and use a **local Python package/library** in another script.  
This project includes basic math operations and shows clean code structure, separation of concerns, and user interaction.

---

## 📁 Project Structure

---

## 🧠 How It Works

1. **Library (`FuFile.py`)**  
   Contains four basic mathematical functions:
   - `jam(a, b)` → returns a + b  
   - `maines(a, b)` → returns a - b  
   - `zarb(a, b)` → returns a * b  
   - `taghsem(a, b)` → returns a / b (with a check for division by zero)

2. **Main Application (`app.py`)**  
   - Imports the local library using `import FuFile`  
   - Asks the user to input two numbers and an operation choice  
   - Calls the corresponding function from the library  
   - Displays the result

---

## 🚀 Example Run

---

## 💡 Why This Code Style?

- **Modularity** – Separates logic (library) from user interface (main app).  
- **Reusability** – The library can be imported into any other project.  
- **Readability** – Functions are named clearly, and the code is easy to follow.  
- **Error Handling** – Division checks for zero to avoid crashes.  
- **Local Package Usage** – Shows real-world practice of creating and importing your own modules.

---

## 📦 How to Run

1. Clone the repository or download the files.
2. Make sure both `FuFile.py` and `app.py` are in the same directory.
3. Run the main application:
   ```bash
   python app.py

ساختار پروژه
├── FuFile.py               # کتابخانه محلی شامل توابع ریاضی
├── app.py                  # اسکریپت اصلی برنامه که از کتابخانه استفاده می‌کند
└── README.md               # مستندات پروژه (همین فایل)


عدد اول را وارد کنید: 10
عدد دوم را وارد کنید: 5
عملیات مورد نظر (+, -, *, /): *
نتیجه: 50

