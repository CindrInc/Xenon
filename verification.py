import os
from secrets import SystemRandom, token_hex, compare_digest
from Crypto.Hash import SHA256
from Crypto.Cipher import AES 
from Crypto import Random

def storedPassword():
  pwd1 = input("Create your first password")

def compareStrings(tokenOne,tokenTwo):
  if (compare_digest(tokenOne,tokenTwo) == True):
    print ("True")
  else:
    print ("Verification error")
    
def hashFunction(password,):
  with password
  s = SHA256.new(password.encode('utf-16'))
  return s.digest()
  
storedPassword()
pwd2 = input("Enter your password")
compareStrings(hashFunction(pwd2), hashFunction(storedPassword))


