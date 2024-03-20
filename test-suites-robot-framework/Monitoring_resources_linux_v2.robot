*** Settings ***
Library           OperatingSystem
Library           Process
Library           Collections

*** Variables ***
${duration}       60s
${cpu_threshold}  90%
${memory_threshold} 90%
${disk_threshold} 90%
${network_threshold} 90%

*** Test Cases ***
Check System Performance Under Load
    Start Stress Tool
    Start Monitoring
    Sleep ${duration}
    Stop Monitoring
    VerifyPerformance

*** Keywords ***
Start Stress Tool
    ${stress_pid}=  Start Process  stress --cpu 8 --io 4 --vm 2 --vm-bytes 128M --timeout ${duration}
    Log  Stress tool started with PID: ${stress_pid}

Start Monitoring
    Run Process    sar -n DEV 1 ${duration} > /tmp/network_monitoring.txt &   # Monitoring network
    Run Process    sar -d 1 ${duration} > /tmp/disk_monitoring.txt &          # Monitoring disk
    Run Process    sar -r 1 ${duration} > /tmp/memory_monitoring.txt &        # Monitoring memory
    Run Process    sar -u 1 ${duration} > /tmp/cpu_monitoring.txt &           # Monitoring CPU

Stop Monitoring
    Run Process    pkill sar

VerifyPerformance
    ${cpu_utilization}=     Get CPU Utilization
    ${memory_utilization}=  Get Memory Utilization
    ${disk_utilization}=    Get Disk Utilization
    ${network_utilization}= Get Network Utilization

    Run Keyword If  ${cpu_utilization} > ${cpu_threshold}   Fail  CPU utilization exceeded threshold: ${cpu_threshold} 
    Run Keyword If  ${memory_utilization} > ${memory_threshold}   Fail  Memory utilization exceeded threshold: ${memory_threshold} 
    Run Keyword If  ${disk_utilization} > ${disk_threshold}   Fail  Disk utilization exceeded threshold: ${disk_threshold} 
    Run Keyword If  ${network_utilization} > ${network_threshold}   Fail  Network utilization exceeded threshold: ${network_threshold} 

Get CPU Utilization
    ${cpu_output}=   Get File  /tmp/cpu_monitoring.txt
    ${cpu_utilization}=  ${cpu_output}[*][-2]
    [Return]  ${cpu_utilization}

Get Memory Utilization
    ${memory_output}=   Get File  /tmp/memory_monitoring.txt
    ${memory_utilization}=  ${memory_output}[*][-2]
    [Return]  ${memory_utilization}

Get Disk Utilization
    ${disk_output}=   Get File  /tmp/disk_monitoring.txt
    ${disk_utilization}=  ${disk_output}[*][-2]
    [Return]  ${disk_utilization}

Get Network Utilization
    ${network_output}=   Get File  /tmp/network_monitoring.txt
    ${network_utilization}=  ${network_output}[*][-2]
    [Return]  ${network_utilization}
