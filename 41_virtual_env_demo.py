#Virtual Environments & Package Management

1. Introduction
When creating projects in Python, we need different libraries (packages).
Each project can have a different version.
That's why Python uses Virtual Environments —
This creates a separate space for each project where we can install our packages.

2. What is a Virtual Environment?
Definition:
A virtual environment is an isolated workspace for Python projects.
It allows you to install and manage packages for one project, without affecting others.

Example:

Project A → needs numpy 1.25
Project B → needs numpy 1.23
Both can work without conflict if each has its own virtual environment.


3. Benefits of Using Virtual Environments
Keeps your projects separate and clean
Avoids version conflicts between packages
Protects system Python installation
Easier project sharing with others



4. How to Create and Activate a Virtual Environment

      FOR WINDOWS :- python -m venv venv
                      Venv\Scripts\activate


..................................................................................................          
                                   
5. What is Package Management?

Package Management means —
Installing, updating and managing external libraries in Python.

Main tool used: pip (Python Installer Package)


6. Common pip Commands:-
Command	Description
pip install numpy	Install a package
pip uninstall pandas	Uninstall a package
pip list	Show all installed packages
pip freeze > requirements.txt	Save all packages in a file
pip install -r requirements.txt	Install all packages from file                                   

