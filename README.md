# Password Manager 🗝️  

A simple and secure Password Manager built using Python and Tkinter. It allows users to generate random passwords, save them for various websites, and securely manage these details using a JSON file.  

## Features ✨  

- **Generate Random Passwords**: Create strong and secure passwords with a mix of letters, numbers, and symbols.  
- **Save Passwords**: Store passwords associated with websites along with the username/email in a JSON file.  
- **Search Saved Passwords**: Quickly find saved passwords by entering a website name.  
- **Clipboard Copy**: Automatically copies the generated password to the clipboard for easy pasting.  
- **User Interface**: Simple and clean interface for managing passwords with Tkinter.  

## How It Works 🔑  

### Password Generator  
- Generates a random password consisting of letters (uppercase and lowercase), numbers, and symbols.  
- The length of the password is between 8 to 10 characters.  
- Automatically copies the generated password to the clipboard for convenience.  

### Save Password  
- Save the generated password along with the website and username/email into a JSON file (`data.json`).  
- If the file doesn't exist, it is created automatically.  
- Existing data is updated with new entries while keeping all previously saved passwords intact.  
- A warning appears if required fields are left empty.  

### Search Password  
- Search for saved login details by entering the website name.  
- Displays the email/username and password for the website if found.  
- Notifies the user if no details exist for the entered website or if the data file is missing.  

## UI Overview 📱  

- **Website**: Enter the website or service for which you're saving the password.  
- **Email/Username**: Input the email or username linked to the website.  
- **Password**: Generated or manually entered password.  
- **Generate Password**: Click to generate a random password.  
- **Add**: Save the website, username, and password to the JSON file.  
- **Search**: Retrieve saved password data by entering a website name.  

## Files  

- **logo.png**: A simple image to represent the password manager.  
- **data.json**: The file where saved passwords are stored in JSON format. Each entry includes:  
  - **Website**: The name of the website or service.  
  - **Email**: The associated email or username.  
  - **Password**: The stored password.  

## Screenshots 📸

![grafik](https://github.com/user-attachments/assets/4504699b-78c4-4433-a29a-79c575f76d8e)

## License 📜

This project is licensed under the MIT License. See the `LICENSE` file for more information.
