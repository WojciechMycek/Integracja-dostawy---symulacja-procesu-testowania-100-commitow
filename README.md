System Stability Evaluation Automation

![image](https://github.com/WojciechMycek/Integracja-dostawy---symulacja-procesu-testowania-100-commitow/assets/66401382/48398613-67c9-4613-908c-598a40ba4cf4)


Setup plan

![image](https://github.com/WojciechMycek/Integracja-dostawy---symulacja-procesu-testowania-100-commitow/assets/66401382/52cfa44f-e758-42c0-88c1-87b2e3fae6a4)


Configuration and hosting needed images / files

![image](https://github.com/WojciechMycek/Integracja-dostawy---symulacja-procesu-testowania-100-commitow/assets/66401382/4994ce87-f173-41e6-a579-c4723b8fb2cc)


Project split: 

![image](https://github.com/WojciechMycek/Integracja-dostawy---symulacja-procesu-testowania-100-commitow/assets/66401382/216f67bb-cac7-47d3-a563-4d6ecacb6ef9)


# Description:
This project aims to automate the evaluation of system stability through a combination of Robot Framework, Pytest, and Python scripts. The application, delivered by developers in Python, undergoes rigorous testing procedures to assess its impact on the system and validate its functionality. The automation process is orchestrated using Docker for containerization, Jenkins for job scheduling, and Linux Ubuntu as the operating system environment. Bash scripts are utilized for additional system checks, ensuring comprehensive testing coverage

# Planned tech-stack
- Robot Framework
- Unittest
- Python
- Docker
- Jenkins
- Linux Ubuntu
- Bash
- PowerShell
- Virtual Machines Environment

# Testing Plan

- Robot Framework tests evaluate the application's impact on system stability.
- Bash scripts perform additional checks on the defined system parameters.
- Pytest tests validate the functionality of defined functions within the application.

# Automation workflow
- GitHub CI / CD is used for checking potential problems before merging in on master
- Jenkins jobs trigger tests and manage the delivery process.
- Automated feedback is provided to developers regarding detected bugs and system performance.

# Instruction - file execution

Execute robot file via CLI-terminal:

```python3 -m robot -T name_of_test.robot```

Execute python file via CLI-terminal:

```python3 file_name.py```

# Retro games for testing process

# Platform-game

The character can jump across platforms, then by jumping on top of enemies' heads, it will eliminate them. It will earn points for defeating enemies, as well as collect collectibles.

This provides a good foundation for writing subsequent tests for this application.

# Docker image
The next goal is to provide the user with a Docker image of Jenkins that will already be appropriately configured for smooth deployment and execution. This requires preparing suitable documentation explaining the entire CI/CD mechanism, which will then be implemented.

Prepare good image that could be used to run all CI / CD environment.

Link to configured image is going to be provided by onedrive. Also clear instruction to run will be also attached

😝
