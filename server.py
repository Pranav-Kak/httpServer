import socket
from media import *
s = socket.socket()
host = input('Enter your IP address: ')
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, 80))
s.listen(5)
print('Server is ready')
while True:
    conn, addr = s.accept()
    request = conn.recv(1024).decode()
    print(request)
    request = request.split(' ')
    method = request[0]  # First string is a method
    request = request[1]  # Second string is request file
    query = request.partition("?")[2]
    request = request.partition("?")[0]
    if request == '/':
        request = '/index.html'
    try:
        file = open('www' + request, 'rb')
        response = file.read()
        file.close()
    except:
        error = "<htm><p>Error 404: Page not Found<p><html>"
        response = error.encode()
    media = mediatype(request)
    header = 'HTTP/1.1 200 OK\nContent-Type: ' + str(media) + '\n\n'
    Response = header.encode('utf-8')
    Response += response
    conn.send(Response)
    conn.close()
