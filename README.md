# Gymnastics Association Website

## Overview

The Gymnastics Association Website is a web application developed using Django, designed to automate tasks for a gymnastics association. It allows users to register, create profiles, and add their children as gymnasts. The platform provides the association with easier access to information needed for insurance and other administrative tasks.

## Features

### 1. User Registration and Authentication

- **User Signup**: Allows users to create an account by providing necessary details such as username, email, and password.
- **User Login**: Enables registered users to log in securely to access the platform's features.
- **User Logout**: Allows users to securely log out of their accounts.

### 2. Profile Management

- **User Profile Creation**: Users can create their profiles by providing personal information such as name, contact details, etc.
- **Gymnast Profile Creation**: Users can add their children as gymnasts by providing relevant details such as name, age, level, etc.
- **Profile Editing**: Users can edit their profiles and gymnasts' profiles to update information as needed.

### 3. Administrative Tools

- **Information Management**: Provides the association with easy access to user and gymnast information for administrative purposes.
- **Insurance Management**: Allows the association to manage insurance-related information for members and gymnasts.
- **Task Automation**: Automates tasks such as registration, profile creation, and data management to streamline administrative processes.

## Installation

1. Clone the repository to your local machine:
git clone <repository_url>

2. Install the project dependencies using pip:
pip install -r requirements.txt

3. Apply database migrations to create the necessary database schema:
python manage.py migrate

4. Run the development server:
python manage.py runserver

5. Access the application in your web browser at http://127.0.0.1:8000/

## Usage
1. Register for an account if you're a new user, or log in with your existing credentials.
2. Create your profile and add your children as gymnasts.
3. Explore the platform's features for managing profiles, viewing information, and accessing administrative tools.
4. Log out securely when you're done using the platform.

## Project Structure
- Main App: Contains the core functionalities and main views of the website.
- Users App: Manages user authentication, registration, and profile functionalities.
- Profiles App: Handles the creation and management of user and gymnast profiles.
- Dashboard App: Provides administrative tools and views for managing information and tasks.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Push your branch to your fork.
5. Submit a pull request with a detailed description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- This project was developed using the Django web framework.
- Special thanks to the Django community for their contributions and support.
- For ideas to my README.md, please refer to the [User Experience Design](https://github.com/Gareth-McGirr/Portfolio-Project-4-SizzleAndSteak?tab=readme-ov-file#user-experience-design)
- Additional Inspiration: [YouTube Video Series](https://www.youtube.com/watch?v=dCvkAVN5uas&list=PLXuTq6OsqZjYSa-lrjd5wMGl23zpnhvln) - A YouTube video series that provided inspiration for this project.