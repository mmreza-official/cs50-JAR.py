# 🍪 CS50P – Jar.py  

---

## 🧠 Overview | مروری کوتاه

This project is my solution to Harvard’s **CS50P – “Jar”** problem.  
It uses **Object-Oriented Programming (OOP)** in Python to simulate a cookie jar that can store, add, or remove cookies safely.  

این پروژه راه‌حل من برای تمرین **Jar** از دوره‌ی CS50P دانشگاه هاروارد است.  
در آن از **برنامه‌نویسی شیءگرا (OOP)** برای شبیه‌سازی یک ظرف کلوچه استفاده شده که ظرفیت مشخصی دارد و می‌توان در آن کلوچه اضافه یا کم کرد.

---

## ⚙️ Features | ویژگی‌ها

- Defines a class **`Jar`** with a customizable **capacity**  
- Supports **deposit** (add cookies) and **withdraw** (remove cookies)  
- Uses **property decorators** for clean attribute access  
- Raises **ValueError** for invalid actions (e.g., overfill, empty jar)

---

## 💡 Example | مثال

```python
from jar import Jar

jar = Jar(5)
jar.deposit(3)
print(jar)        # 🍪🍪🍪
jar.withdraw(1)
print(jar)        # 🍪🍪

---

## Errors:

jar.deposit(10)   # ValueError: Too many cookies
jar.withdraw(5)   # ValueError: Not enough cookies

---

🧑‍💻 Author | نویسنده

Mohammad Reza Abdollah
📧 mohammadenor@gmail.com
🌐 GitHub Profile
