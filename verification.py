import os
from secrets import SystemRandom, token_hex, compare_digest
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

def compareStrings(tokenOne, tokenTwo):
  if compare_digest(tokenOne, tokenTwo):
    print ("True")
  else:
    print ("Verification error")


def hashFunction(password):
  s = SHA256.new(password.encode('utf-16'))
  return s.digest()

storedPassword = input("Create your first password: ")
pwd2 = input("Enter your password: ")
compareStrings(hashFunction(pwd2), hashFunction(storedPassword))
