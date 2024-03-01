# System Stability Evaluation Automation

# Description:
This project aims to automate the evaluation of system stability through a combination of Robot Framework, Pytest, and Python scripts. The application, delivered by developers in Python, undergoes rigorous testing procedures to assess its impact on the system and validate its functionality. The automation process is orchestrated using Docker for containerization, Jenkins for job scheduling, and Linux Ubuntu as the operating system environment. Bash scripts are utilized for additional system checks, ensuring comprehensive testing coverage

# Planned tech-stack
- Robot Framework
- Pytest
- Python
- Docker
- Jenkins
- Linux Ubuntu
- Bash
- Virtual Machines Environment

# Testing Plan

- Robot Framework tests evaluate the application's impact on system stability.
- Bash scripts perform additional checks on the defined system parameters.
- Pytest tests validate the functionality of defined functions within the application.

# Automation workflow

- Jenkins jobs trigger tests and manage the delivery process.
- Automated feedback is provided to developers regarding detected bugs and system performance.

# File Execution

Execute robot file via CLI-terminal:

python3 -m robot -T name_of_test.robot
