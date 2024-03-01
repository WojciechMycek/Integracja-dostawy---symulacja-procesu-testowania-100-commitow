# Integracja-dostawy---symulacja-procesu-testowania-100-commitow

# Planned tech-stack
- Robot Framework
- Pytest
- Python
- Docker
- Jenkins
- Linux Ubuntu
- Bash
- Virtual Machines Environment
 
# File Execution

Execute robot file via CLI-terminal:

python3 -m robot -T name_of_test.robot

# Testing Plan

Simulation idea:

1. App is delivered by developer -> written in python
2. Tests are executed:
     - Tests in robot framework check impact on system with app
     - additional checks in Bash / CLI-terminal on defined system
     - Tests defined in .py check functionality of defined functions.
3. Automaziation of all delivary process.
     - Use jobs defined in Jenkins to trigger tests, app delivery
     - Return to developer informatioms about bugs

