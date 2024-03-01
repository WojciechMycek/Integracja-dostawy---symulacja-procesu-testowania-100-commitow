# Integracja-dostawy---symulacja-procesu-testowania-100-commitow

# File Execution

Execute robot file via CLI-terminal:

python3 -m robot -T name_of_test.robot

# Testing Plan

Simulation idea:

1. App is delivered by developer -> written in python
2. Tests are executed:
     - Tests in robot framework check impact on system with app
     - Tests defined in .py check functionality of defined functions.
3. Automaziation of all delivary process.
     - Use jobs defined in Jenkins to trigger tests, app delivery
     - Return to developer informatioms about bugs

