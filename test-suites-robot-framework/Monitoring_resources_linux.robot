*** Settings ***
Documentation    File to define test in robot framework
...              output / input still needed to be defined
Library    Process

*** Variables *** 

*** Test Cases ***
Running program
    Run Process    ls    -lah

Testing_console_log
    Log To Console    Testing_console_log
    Run Process    ps    -a
    # second pull request

*** Comments *** 

Testing usage of proc memory
    pass

Testing usage of disc 
    pass

Testing usage of gpu
    pass

Testing usage of cpu
    pass

File management 
    pass

*** Keywords ***

