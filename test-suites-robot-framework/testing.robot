*** Settings ***
Library    OperatingSystem
Library    Process

*** Test Cases ***
Test Square Movement App
    Open Application    python    square_movement_app.py
    Wait Until Keyword Succeeds    20s    1s    Check Score    10
    #    testing pull request pipeline
    [Teardown]    Close All Applications

*** Keywords ***
Open Application
    [Arguments]    ${command}    ${file_path}
    ${output}=    Run Process    ${command}    ${file_path}    shell=True
    [Return]    ${output}

Check Score
    [Arguments]    ${expected_score}
    ${score}=    Run Process    python    -c "import tkinter as tk; root = tk.Tk(); label = tk.Label(root, text=''); label.pack(); label['text'] = root.children['!label'].cget('text'); root.after(20000, root.destroy); root.mainloop(); print(label['text'])"
    Should Be Equal As Numbers    ${score}    ${expected_score}
