
# Password Manager

This is a simple and secure password manager that allows the user to store, view and delete passwords in an encrypted form. The application uses AES encryption to guarantee the security of passwords.

## Features

- Add a new password: Allows you to add a new password associated with a service.
- See all passwords: Displays all services for which passwords are stored. You can select a specific service to see the corresponding password.
- Delete password: Allows you to delete a password associated with a specific service.
- Exit: Exits the application.


## Important

- Keep the key.bin and encrypted.bin files together with the executable: The application depends on these files to encrypt and decrypt passwords. Be sure to store them in a safe location and make backups if necessary.
- Master Password: The application requests a master password to access the stored passwords. Use a secure and easy-to-remember password. The master password is required to derive the encryption key, so it is not possible to recover data if the master password is forgotten.

## Security
This project uses AES encryption with PBKDF2 key derivation to ensure passwords are stored securely. Keep key.bin and encrypted.bin files secure to prevent unauthorized access to data.


## Compiling the Executable

If you want to compile the executable from source code, follow the steps below:

Instale o PyInstaller:
```bash
pip install pyinstaller
```

Compile o executável:
```bash
pyinstaller --onefile --name password_manager main.py
```

The executable will be generated in the dist folder.