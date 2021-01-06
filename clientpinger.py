from socket import AF_INET,SOCK_DGRAM,socket
import time
serverName="127.0.0.1"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
clientSocket.settimeout(1)
for i in range(10):
    start=time.time()
    message="ping " +str(i+1)+ time.ctime()[11:19]
    try:
        clientSocket.sendto(message.encode(),(serverName,serverPort))
        convertedMessage,address=clientSocket.recvfrom(1024)
        end=time.time()
        print(convertedMessage.decode())
        print("RTT :{:.3f}".format((end-start)*1000))
    except:
        print("timeout")
clientSocket.close()

    
