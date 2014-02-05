from socket import * 

msg = '\r\n I love computer networks!' 
endmsg = '\r\n.\r\n'
mailserver = 'smtp.stud.ntnu.no'
port = 25

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))

recv = clientSocket.recv(1024) 
print recv 
if recv[:3] != '220': 
	print '220 reply not received from server.' 

heloCommand = 'HELO Alice\r\n' 
clientSocket.send(heloCommand) 
recv1 = clientSocket.recv(1024) 
print recv1 
if recv1[:3] != '250': 
	print '250 reply not received from server.' 
	
clientSocket.send('MAIL FROM: jonatanl@stud.ntnu.no\r\n')
clientSocket.send('RCPT TO: jonatanl@stud.ntnu.no\r\n') 
clientSocket.send('DATA\r\n')
clientSocket.send('Subject: test\r\n')
clientSocket.send(msg + endmsg)
print clientSocket.recv(1024) 
clientSocket.send('QUIT\r\n')
print clientSocket.recv(1024)
clientSocket.close()