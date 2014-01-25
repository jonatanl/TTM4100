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

		filename = message.split()[1]
		f = open(filename[1:]) 
		outputdata = f.readlines()
		
		for i in range(0, len(outputdata)): 
			connectionSocket.send(outputdata[i]) 
		connectionSocket.close() 
	except IOError, IndexError: 
		message = "File not found!"
		connectionSocket.send(message)
		connectionSocket.close()
	#Send response message for file not found 
	#Fill in start 
	#Fill in end 
	#Close client socket 
	#Fill in start 
	#Fill in end 
serverSocket.close()