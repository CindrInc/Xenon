
from Crypto.Hash import SHA256
s = SHA256.new()

s.update(b"Nobody inspects")
s.update(b" the spammish repetition")
s.digest()

