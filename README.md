
# Vault P

## INTRODUCTION
 'Vault P' is a security-focused password manager built with Python as a learning project to explore password hashing, key derivation, encryption, secure password generation, file-based storage.

## ⚠️ Disclaimer
    This is an educational project created to learn Python and applied cryptography.

    It has not been professionally audited and should not be relied upon to protect highly sensitive or production credentials.

    The project is intended to demonstrate my understanding of software development and security concepts while I continue improving its design and implementation.
## 🚀 Installation & Deployment

To deploy this project run

```bash
  git clone https://github.com/aritrapurkait/password-manager.git cd password-manager
```
```bash
  python -m venv venv
```
```bash
  python -m venv venv
```

Activate the Virtual Environment

Windows:

 ```bash
venv\Scripts\activate
```   

Linux / macOS:
```bash
source venv/bin/activate
```
Install Dependencies 

```bash
pip install -r requirements.txt
```

Run the Application:

```bash
python main.py
```
💡 Make sure the virtual environment is activated before installing dependencies or running the application.


## Features

- 🔑 Master Password Authentication
    - Master password protected using [bcrypt]
    - Salted password hashing
    - Password verification during login
-  🔐 Encrypted Password Vault
    - Website credentials are encrypted before being stored
    - Encryption key derived from the master password using PBKDF2
    - Uses cryptographic salts and IVs/nonces
-  💪 Password Strength Checker
    - Evaluates password strength
    - Checks characteristics such as length and character variety
-  💾 Persistent Storage
    - Credentials stored locally
    - JSON-based data storage
    - Binary cryptographic data encoded using Base64 for JSON compatibility




## 📚 What I'm Learning

Through this project, I'm learning:

    🐍 Python application development
    🧩 Modular programming
    📁 File and JSON handling
    🔐 Password hashing
    🧂 Salting
    🔑 Key derivation
    🛡️ Symmetric encryption
    📌 IVs / nonces
    🔤 Binary data encoding
    🖥️ GUI development
    🐛 Error handling
    🧪 Testing
    🌱 Git & GitHub

## 🧰 Technologies & Libraries

    🐍 Python	Main programming language
    🔐 bcrypt	Master password hashing
    🔑 PBKDF2	Password-based key derivation
    🛡️ PyCryptodome	Cryptographic operations
    💾 JSON	Local data storage
    🔤 Base64	Binary-to-text encoding
    🖥️ CustomTkinter	Graphical user interface


## 🚀 Planned Features
   The project is still under development. Planned improvements include:

  - 🖥️ Add a proper GUI (UI) instead of CLI using CustomTkinter
  - 🎲 Improve password generator (stronger randomness + better customization options)
  - 🧪 Add unit tests for core functionality
  - 🛡️ Improve security-focused error handling and edge-case protection
  - 📦 Project packaging for easier installation and distribution (setup.py / executable build)
## Authors

- [@aritrapurkait](https://github.com/aritrapurkait)

  Built as a personal learning project while studying Computer Science and Artificial Intelligence & Machine Learning.
## 🔗 Links
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/aritra-purkait-889485395/)



## Feedback

If you have any feedback, please reach out to us at aritra.purkait.ai@gmail.com

