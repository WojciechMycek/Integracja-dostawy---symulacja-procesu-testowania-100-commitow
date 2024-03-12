# Get processor information
$processorInfo = Get-WmiObject Win32_Processor

# Display processor details
Write-Host "Processor Information:"
Write-Host "-------------------------"
Write-Host "Manufacturer: $($processorInfo.Manufacturer)"
Write-Host "Model: $($processorInfo.Name)"
Write-Host "Number of Cores: $($processorInfo.NumberOfCores)"
Write-Host "Number of Threads: $($processorInfo.NumberOfLogicalProcessors)"
Write-Host "Base Clock Speed: $($processorInfo.MaxClockSpeed) MHz"

