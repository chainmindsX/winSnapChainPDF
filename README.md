# 📸 WinSnapChainPDF

WinSnapChainPDF is a smart and lightweight Windows utility developed by [ChainMindsX](#about-chainmindsx) that **automatically captures screenshots whenever the Right Ctrl key is pressed**, and seamlessly **compiles them into a PDF** when the system shuts down or goes to sleep. 

This tool is ideal for professionals who want to log their desktop activity, developers who want to track what they were working on, or anyone who needs a hands-free, organized way to save session visuals.

---

## ✨ Key Features

- 🎯 **Auto Screenshot Capture**
  - Press the **Right Ctrl** key any time during your session to take an instant screenshot.

- 💾 **Smart Session Logging**
  - All screenshots are stored with timestamps in a local folder.

- 📕 **PDF Generation on Shutdown/Sleep**
  - The app detects when your computer is shutting down or going to sleep, and automatically compiles all session screenshots into a **single PDF file**.

- 🖥️ **Minimal GUI**
  - Simple, clean interface to monitor if the tool is running.

- 🔄 **Autostart on Windows Boot**
  - Automatically adds itself to the Windows Startup folder so you never forget to launch it.

- 🧠 **Lightweight & Offline**
  - No internet connection required. Fully offline, low-resource tool.

---

## 📦 Requirements & Dependencies

To run this app on another Windows PC, make sure the following Python packages are installed:

```bash
pip install pyautogui
pip install pynput
pip install pillow
pip install pywin32
pip install winshell
```

### Or install all at once:

```bash
pip install -r requirements.txt
```

> Make sure you're using **Python 3.8+** on **Windows OS**.

---

## 🚀 How to Use

1. **Download or clone this repository:**

```bash
git clone https://github.com/yourusername/winSnapChainPDF.git
cd winSnapChainPDF
```

2. **Run the main program:**

```bash
python main.py
```

3. **How it works:**
   - When the tool is running, press **Right Ctrl** anytime to take a screenshot.
   - Screenshots are saved in the `screenshots/` folder.
   - When you shut down or your PC goes to sleep, the app will **automatically create a PDF** named `Session_Screenshots.pdf`.

---

## 📁 Folder Structure

```
winSnapChainPDF/
├── main.py                  # Entry point with GUI
├── gui.py                   # Minimal tkinter GUI
├── listener.py              # Keyboard hook (Right Ctrl listener)
├── screenshot.py            # Handles taking screenshots
├── shutdown_handler.py      # Detects shutdown/sleep and triggers PDF
├── pdf_generator.py         # Combines screenshots into PDF
├── startup.py               # Adds app to Windows startup
├── screenshots/             # Stores session screenshots
├── dist/main.exe            # Generated EXE (via PyInstaller)
└── requirements.txt         # Dependencies
```

---

## 🔧 Building an EXE

To generate a `.exe` file that runs without Python installed:

```bash
pyinstaller --noconfirm --onefile --windowed main.py
```

The final EXE will be found in the `dist/` folder.

---

## 🏢 About ChainMindsX

Absolutely! Here's a refined, professional introduction for your company **ChainMindsX**, tailored to reflect your focus on **data analysis**, **machine learning**, and **AI-based tools** for real-world computer professionals:

---

### 🧠 About ChainMindsX

**ChainMindsX** is a forward-thinking software company specializing in **data analysis**, **machine learning**, and the development of intelligent, AI-powered software agents. Our mission is to empower modern computer professionals by transforming real-world workflows into automated, efficient, and context-aware digital solutions. We harness the power of structured data and machine learning models to build lightweight, offline-capable tools that enhance productivity, reduce distractions, and simplify complex tasks. Whether it’s desktop utilities, smart monitoring agents, or task-specific AI applications, ChainMindsX is dedicated to crafting intelligent tools that blend seamlessly into the daily routines of developers, analysts, and digital creators — bridging the gap between data, decision-making, and day-to-day computing.


> 🚀 At ChainMindsX, we believe that productivity doesn't need to be loud — it just needs to be smart.

Follow us for more updates, tools, and innovations:
- 🌐 Website: [Coming Soon]
- 📧 Contact: chainmindsx@gmail.com

---

## 🤝 Contribution

Pull requests are welcome! If you have ideas, enhancements, or bug fixes, feel free to fork and contribute.

---


---

## 🙌 Final Thoughts

WinSnapChainPDF is meant to stay out of your way while keeping a log of your work activity, automatically and intelligently. Whether you're a developer, designer, manager, or digital creator — it just *works*.

If you find this useful, give it a ⭐️ and share it with others!

```

---

Let me know if you want me to drop this into a `.md` file or prep a GitHub repo for you directly!
