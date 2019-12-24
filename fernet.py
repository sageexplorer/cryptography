#!/usr/bin/env python
# coding: utf-8

from cryptography.fernet import Fernet

# Generate a Key and Instantiate a Fernet Instance
key = Fernet.generate_key()
f = Fernet(key)
print(key)
# Define our message
plaintext = b"encryption is very useful"
# Encrypt
ciphertext = f.encrypt(plaintext)
print(ciphertext)
# Decrypt
decryptedtext = f.decrypt(ciphertext)
print(decryptedtext)
