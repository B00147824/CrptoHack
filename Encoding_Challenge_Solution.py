import telnetlib
import json
import codecs
import base64
from Crypto.Util.number import *

HOST = "socket.cryptohack.org"
PORT = 13377

tn = telnetlib.Telnet(HOST, PORT)

def readline():
    return tn.read_until(b"\n")

def json_recv():
    line = readline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    tn.write(request)

def decoder(kind,text):
    if kind == 'hex':
        return bytes.fromhex(text).decode('utf-8')
    
    elif kind == 'utf-8':
        answer = ""
        for n in text:
            answer += chr(n)
        return answer
    
    elif kind == 'rot13':
        return codecs.decode(text, "rot13")
    
    elif kind == 'base64':
        return base64.b64decode(text).decode()

    elif kind ==  'bigint':
        return long_to_bytes(int(text, 16)).decode()


for i in range(1,101):
    received = json_recv()
    
    #print(f"Question {i}")
    #print(f"Received type: {received['type']}")
    #print(f"Received encoded value: {received['encoded']}")

    to_send = {"decoded": decoder(received["type"],received["encoded"])}
    
    #print(f"Answer: {to_send} \n")

    json_send(to_send)


json_recv()
    
    
