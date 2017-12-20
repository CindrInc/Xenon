import os
from secrets import SystemRandom, token_hex, compare_digest
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

def compareStringsWithoutCryptography(username1, username2):
  if(username1 == username2):
    return True
  else:  
    return False

def compareStrings(tokenOne, tokenTwo):
  if compare_digest(tokenOne, tokenTwo):
    return True
  else:
    return False


def hashFunction(password):
  s = SHA256.new(password.encode('utf-16'))
  return s.digest()

storedUsername = input("Create your username: ")
storedPassword = input("Create your first password: ")
username = input("Enter your username: ")
pwd2 = input("Enter your password: ")
a = compareStringsWithoutCryptography(storedUsername, username)
b = compareStrings(hashFunction(pwd2), hashFunction(storedPassword))

if (bool(a) == False):
  print("Verification Errror")
elif (bool(b) == False):
  print("Verification Errror")

elif(bool(b) == True and bool(a) == True ):
  print("Authentification successful, welcome " + storedUsername)
  