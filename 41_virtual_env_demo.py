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
