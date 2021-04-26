import socket
 
def readMyFile(fname):
    try:
        f = open(fname,'r')
        str = ""
        for x in f:
            str+=x
        f.close()
        return str
    except:
        return "FILE DOESNT EXIST "
def addContent(fname,content):
    f = open(fname,'a')
    f.write(content)
    print("content added successfully")
    f.close()
    z = input("Open file:")
    log = open(z, "r").read()
    print(log)
 
if __name__=='__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 12000))
    s.listen(5)
    while True:
        cs, add = s.accept()
        print("connection from {add} has been established")
        val = ""
        
        while val != "exit":
            msg = cs.recv(1024)
            fname = str(msg.decode("utf-8"))
            print("client requesting: " + msg.decode("utf-8"))
            
            val = readMyFile(fname)
            cs.send(bytes(val, "utf-8"))
            if(val!="FILE DOESNT EXIST ON SERVER"):
                msg = cs.recv(1024)
                content = str(msg.decode("utf-8"))
                addContent(fname,content)
