# Reconnect socket if cannot use it for sending anymore (for example server was reseted, after we connected to it)

# initial socket creation
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)  # Buffer size
myserveraddress = (127.0.0.1, int(1337))
mysocket.connect(myserveraddress)



  # then using the socket later with 'try' to see if its working
  try:
      mysocket.send("jacket siblings")
  except Exception:
      global mysocket # we want to use same global var still
      # destroy old socket since its brokened
      mysocket.shutdown(socket.SHUT_RDWR)
      mysocket.close();
      
      # re-connect (have to create new socket, cannot use the old or you get "Errno 9: Bad file descriptor"
      mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
      mysocket.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 8192)  # Buffer size
      myserveraddress = (127.0.0.1, int(1337))
      mysocket.connect(myserveraddress)
      
      # resend the message
      commandsock.send("jacket siblings"))
