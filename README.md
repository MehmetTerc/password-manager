# Password Manager 🗝️

A simple and secure **Password Manager** built using Python and Tkinter. It allows users to generate random passwords, save them for various websites, and securely store these details in a text file.

## Features ✨

- **Generate Random Passwords**: Create strong and secure passwords with a mix of letters, numbers, and symbols.
- **Save Passwords**: Store passwords associated with websites along with the username/email in a text file.
- **Clipboard Copy**: Automatically copies the generated password to the clipboard for easy pasting.
- **User Interface**: Simple and clean interface for managing passwords with Tkinter.

## How It Works 🔑

1. **Password Generator**:
   - Generates a random password consisting of letters (uppercase and lowercase), numbers, and symbols.
   - The length of the password is between 8 to 10 characters.
   
2. **Save Password**:
   - You can save the generated password along with the website and username/email into a local file (`data.txt`).
   - If any fields are left empty, a warning message will prompt the user.

3. **Clipboard Support**:
   - The generated password is copied to the clipboard for easy use.

## UI Overview 📱

- **Website**: Enter the website or service for which you're saving the password.
- **Email/Username**: Input the email or username linked to the website.
- **Password**: Generated or manually entered password.
- **Generate Password**: Click to generate a random password.
- **Add**: Save the website, username, and password to a text file.

## Files

- **logo.png**: A simple image to represent the password manager.
- **data.txt**: The text file where saved passwords are stored (in the format: `website | username | password`).

## Screenshots 📸

![grafik](https://github.com/user-attachments/assets/3fc37d05-3221-4933-8e9e-79f5e0b08f2f)

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more information.
