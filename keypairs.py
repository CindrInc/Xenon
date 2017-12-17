import os
from secrets import SystemRandom, token_hex, compare_digests
from Crypto.Hash import SHA256
from Crypto.Cipher import AES 
from Crypto import Random




def encrypt (key, fileName):
  chunksize = 64 *1024 #chunks it reads out of the file
  outputFile = "(encrypted)" + fileName
  filesize = str(os.path.getsize(fileName)).zfill(16)
  IV = Random.new().read(16)
  
  encryptor = AES.new(key, AES.MODE_CBC, IV)
  
  with open(fileName, 'rb') as infile: 
    with open(outputFile, 'wb') as outfile:
            outfile.write(filesize.encode('utf-8'))
            outfile.write(IV)
            
            while True:
              chunk = infile.read(chunksize)
              
              if len(chunk) == 0:
                  break
              elif len(chunk)%16 != 0:
                  chunk += b' ' * (16-(len(chunk)%16))
              
              outfile.write(encryptor.encrypt(chunk))
def decrypt (key, fileName):
  chunksize = 64 * 1024
  outputFile = fileName[11:]
  
  with open(fileName,'rb') as infile:
      filesize = int(infile.read(16))
      IV = infile.read(16)
      decryptor = AES.new(key, AES.MODE_CBC, IV)
      with open(fileName, 'wb') as outfile:
         while True:
            chunk = infile.read(chunksize)
            if len(chunk) == 0:
                  break
            outfile.write(decryptor.decrypt(chunk))
         outfile.truncate(filesize)
            
def getKey(password):
  s = SHA256.new(password.encode('utf-8'))
  return s.digest()

def Main():
  choice = input("Would you like to Encrypt or Decrypt")
  if choice == 'E':
    fileName = input("File to Encrypt")
    password = input("Enter your password")
    encrypt(getKey(password),fileName)
    print("Done.")
  elif choice == 'D':
    fileName = input("File to Decrypt")
    password = input("Enter your password")
    decrypt(getKey(password),fileName)
    print("Done.")
  else:
    print("LOL what bruh")

if __name__ == '__main__':
  Main()
  
 

