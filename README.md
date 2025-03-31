# PDFShield - Secure PDF Locker

PDFShield, a secure PDF Locker is a Python-based application with a **Kivy** GUI that allows users to **password-protect PDF files**. The app works on **Windows, macOS, and Android** and provides a user-friendly interface with modern animations and cyber-security-themed graphics.

## Features
- **Password-protect PDF files** with encryption
- **Hide/Unhide password toggle** while entering
- **Animated buttons** and stylish dark theme UI
- **Cross-platform**: Works on **Windows, macOS, and Android**

## Screenshots
#### This is the application interface in macOS.
<img width="800" alt="image" src="https://github.com/user-attachments/assets/eb6419b8-e409-491f-8f30-d84842706587" />

#### Select the PDF file and your preferred directory / folder to store the password-protected PDF.
<img width="792" alt="image" src="https://github.com/user-attachments/assets/3ae7e2af-a35b-4ace-b1fc-205cd803b466" />

#### Please make sure the password length is at least 8 characters.
<img width="797" alt="image" src="https://github.com/user-attachments/assets/61d253c7-b8e8-4c22-aba5-b0b97afa775f" />

#### Nice! You've successfully encrypted your PDF with a strong password. 
<img width="793" alt="image" src="https://github.com/user-attachments/assets/75ee6089-2747-48bd-a6a6-a552508f5f85" />





## Installation
### Windows/macOS (Standalone App)
1. Download the latest `.exe` (Windows) or `.app` (macOS) from the [Releases](https://github.com/aniket-cs/PDFShield/tree/master/Releases/) section.
2. Run the application without needing Python.

### Run from Source Code (Python 3 Required)
1. Clone the repository:
   ```bash
   git clone https://github.com/aniket-cs/PDFShield.git
   cd PDFShield
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python protection.py
   ```

### Android (APK Installation)
1. Download the APK from the [Releases](https://github.com/aniket-cs/PDFShield/tree/master/Releases/).
2. Install it on your Android device.
3. Open the app and start encrypting PDFs!

## Building the Application
### **Windows/macOS: Generate Executable (.exe/.app)**
```bash
pyinstaller --onefile --windowed --icon=logo.jpg protection.py
```
OR, if you don't want to add any image / icon / logo to your app :
```bash
pyinstaller --onefile --windowed protection.py
```
### **Android: Generate APK**
```bash
buildozer -v android debug
```
For a signed APK:
```bash
buildozer android release
```

## Troubleshooting
- If the app **crashes on Android**, check logs using:
  ```bash
  adb logcat | grep python
  ```
- If SSL errors occur, update `certifi`:
  ```bash
  pip install --upgrade certifi
  ```
- If Failed to execute script 'protection' due to unhandled exception: **No module named 'win32timezone'**:
  ```bash
  pip install pywin32
  pyinstaller --onefile --windowed --hidden-import=win32timezone protection.py
  ```

## License
This project is open-source. I welcome all engineers to contribute and make the application cool :)

## Contributors
- Aniket Das (https://github.com/aniket-cs)

------
⭐ **Star this repo** if you found it useful!

