# 📦 File Un-Zipper (GUI)
A simple Python GUI application to **unzip .zip files** into a selected folder using `PySimpleGUI` and the `zipfile` module.
---

## ✨ Features

- Select a `.zip` archive from your file system
- Choose a destination folder where to extract its contents
- Clear success or error messages using popups
- Simple and user-friendly interface

---

## 🖥️ Requirements

- Python 3.x
- FreeSimpleGUI - a Python Simple GUI software: https://pypi.org/project/FreeSimpleGUI/

---

## 📦 Installation

1. Clone or download the repository
2. Install dependencies:

```bash
pip install FreeSimpleGUI
```

🚀 How to Run
Run the Python script:

```bash
python unzip_gui.py
```

🧠 How It Works

* Browse for the archive: Choose a .zip file from your computer.
* Choose destination: Select a folder where the archive will be extracted.
* Click "UnZipp": The contents will be extracted to the selected folder.

** Success message: You'll get a success message if all goes well. If not, you'll be shown a helpful error popup.

🐛 Error Handling
 - If no file or folder is selected, a popup notifies the user.
 - If the selected file is not a valid zip file, a warning is shown.
 - Any exceptions during extraction are caught and displayed.

📃 License
This project is for educational use. No license restrictions.

🙋‍♀️ Author
Built by Krisztina Visky as a Python learning exercise.
