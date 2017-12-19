import os
from secrets import SystemRandom, token_hex, compare_digest
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

def compareStringsWithoutCryptography(username1, username2):
  if(username1 == username2):
    print ("True")
    return True
  else: 
    print("False")
    return False

def compareStrings(tokenOne, tokenTwo):
  if compare_digest(tokenOne, tokenTwo):
    print ("True")
  else:
    print ("Verification error")


def hashFunction(password):
  s = SHA256.new(password.encode('utf-16'))
  return s.digest()

storedUsername = input("Create your username")
storedPassword = input("Create your first password: ")
username = ("Enter your username")
pwd2 = input("Enter your password: ")
compareStrings(hashFunction(pwd2), hashFunction(storedPassword))