# Online Learning Management System

`Python` `Flask` `Bootstrap` `Html` `CSS` ``sqlite3`

Welcome to our Online Learning Management System (LMS) project! This system is designed to provide a comprehensive platform for delivering educational content, facilitating collaboration between instructors and learners, and managing administrative tasks related to online education.

![olms_home](https://github.com/Ermi24et/OLMS/blob/master/olms_home.png)

# Introduction

In today's digital age, online learning has become increasingly popular as a flexible and accessible way to acquire new skills, advance careers, and pursue lifelong learning goals. Our Online Learning Management System (LMS) aims to empower educators, engage learners, and streamline administration by offering a robust set of features tailored to the needs of both instructors and students. [OLMS](https://jeremih24.pythonanywhere.com/) allows users to enroll in a courses and it also let adminstrators to manage i.e, create and delete courses.

### Features

- Course Management: Create, organize, and manage courses, modules, and learning materials.
- User Management: Manage user accounts, roles, permissions, and access levels for administrators, instructors, and students.

# Installation

- To be able to test the application you need to install some packages and modules.

```
# create a virtual environment
python3 -m venv .venv
# activate it
source .venv/bin/activate
# install the necessary packages
pip install flask
pip install flask-sqlalchemy
pip install flask-wtf
pip install wtforms
pip install email_validator
pip install flask_bcrypt
pip install flask_login
```

- Once you installed those packages you are all set up.

```
cd OLMS
flask run
```

- Now after you run the above command open your browser with the link http://127.0.0.1:5000/

# Usage

To get started with OLMS, the hosted version of the product can be used. You can get started immediately at ermi24et.pythonanywhere.com/. After the login page, you will be redirected to a list of courses. The website provides with variety of courses and if you want additional information on the product and guides can be found [here](https://jeremih24.pythonanywhere.com/).

```
- Usage: flask run

  Developed by Ermias Teklehaymanot (Github: Ermi24et)
```

# Contributing

Thank you for considering contributing to our Online Learning Management System project! We welcome contributions from everyone, whether you're a beginner or an experienced developer. By contributing, you can help us improve the project and make online education more accessible and effective for learners around the world.

# How to Contribute

### Reporting Bugs

If you encounter any bugs or issues while using our Online Learning Management System, please [open an issue](https://github.com/Ermi24et/OLMS/issues) on GitHub. Be sure to provide detailed information about the problem, including steps to reproduce it and any error messages you encountered.

### Requesting Features

If you have an idea for a new feature or improvement, we'd love to hear about it! You can [open an issue](https://github.com/Ermi24et/OLMS/issues) on GitHub to suggest your ideas and discuss them with the community.

### Contributing Code

We welcome contributions in the form of code changes, bug fixes, or new features. To contribute code to the project, follow these steps:

1, Fork the repository on GitHub.
2, Clone your forked repository to your local machine.

```
git clone https://github.com/Ermi24et/OLMS.git
# create a new branch for your changes
git checkout -b feature-name
# make your changes and commit them to your branch
git add .
git commit -m "Add new feature or fix bug"
# push your changes to your fork on github
git push origin feature-name
# Open a pull request (PR) against the main branch of the original repository. Provide a clear title and description for your PR, explaining the changes you made.
```

### code style guidelines

When contributing code to the project, please follow these guidelines:

- Use consistent coding style and formatting.
- Write clear and descriptive commit messages.
- Write comments and documentation to explain complex code or algorithms.
- Test your changes thoroughly before submitting a pull request.

### Get Help

If you need any help or have questions about contributing to the project, feel free to [contact us](https://www.linkedin.com/in/Ermi24et) or reach out to the maintainers.

We appreciate your contributions and look forward to working together to improve our Online Learning Management System!

# LICENSE

The only exception are the components under the ee (enterprise edition) directory, these are licensed under the [Ermi24et's online learning management system](https://github.com/Ermi24et/OLMS/blob/master/LICENSE) Edition license.
