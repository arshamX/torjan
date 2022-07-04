from cmath import e
import os
from cryptography.fernet import Fernet

files = list()
for file in os.listdir():
    if  os.path.isfile(file):
        if file != "game.py" and file != "dec.py" and file != "desktop.ini":
            files.append(file)


print("""
                 ..............                                                 
              ...#&&&&&&&&&&&&....                                              
            ...&&&&&&&&&&&&&&&&&(..                                             
           ..*&&&&&.........#&&&&&...                                           
          ..(&&&&#..       ...&&&&&..                                           
         ...&&&&(..          ..&&&&(..                                          
         ..&&&&&..           ...&&&&..                                          
        ..,&&&&...            ..&&&&,..                                         
        ..(&&&%..             ../&&&(..                                         
        ..&&&&/..           . .,,#//(.,................,,,,,,,.                 
        ..&&&&...        .**/////////((((((((((((((((((((((((*,*                
        .........        .**&&&&&&&////////////#############(/,*                
                         .,,&&&&&&&////////////##############/,*                
                         .,*&&&&&&&//////#(((((##############/,*                
                         .,,&&&&&%((((((((((((((((((//(######/,*                
                         .**&&&##(((((((((((((((((((/////(###/,*                
                         .*,&&&##(((((((((((((((((((///(/(#((/,*                
                         .,,&&&&#(((((((((((((((((((/(//####(/,*                
                         ,,,&&&&&&//%(((((((((((((((#########(,,                
                         ,,,&&&&&&&////////////##############(,*                
                         ,,,&&&&&&&///////////////###########((,,                
                         .************,,,,,,,,,,,,,,,,,,,,,,,,** 
----------------------------------decryptor tool----------------------------------              

""")
key = input("Enter keyword  :")
try:
    for file in files:
        the_file = open(file , "rb")
        doc = the_file.read()
        the_file.close()
        encrypted_data = Fernet(key).decrypt(doc)
        with open (file,"wb") as the_file:
            the_file.write(encrypted_data)
    print("check your data if its encrypted try agian  with right key")
except :
    print("invalid parse")

input("\nPress enter to continue")