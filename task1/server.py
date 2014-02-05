from socket import * 
serverSocket = socket(AF_INET, SOCK_STREAM)
	
port = 12345
host = ''
serverSocket.bind((host, port)) 
serverSocket.listen(1)

while True:
	#Establish the connection 
	print'Yes, Master'	
	connectionSocket, addr = serverSocket.accept()

	try: 
		message = connectionSocket.recv(1024)

		if not message:
			connectionSocket.close() 
			continue

		filename = message.split()[1]
		f = open(filename[1:]) 
		outputdata = f.readlines()

		print 'OK'
		connectionSocket.send('HTTP/1.1 200 OK\n')

		for i in range(0, len(outputdata)): 
			connectionSocket.send(outputdata[i]) 
		connectionSocket.close() 
	except IOError, IndexError: 
		print 'File not found'
		message = "HTTP/1.1 404 Not Found"
		connectionSocket.send(message)
		connectionSocket.close()
serverSocket.close()