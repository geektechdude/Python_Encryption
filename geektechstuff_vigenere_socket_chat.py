#!/usr/bin/python3
# GeekTechStuff

# Libraries to import
# socket handles the connection between devices
import socket
from datetime import datetime

# encryption keys (lower case)
enc_key = "test"
dec_key = enc_key
# Alphabet needed for encryption / decryption
alphabet = "abcdefghijklmnopqrstuvwxyz"

def message_server():
    # Details of the device running the server
    # HOST is an IP address (requires "")
    HOST = "192.168.0.48"
    PORT = 44441
    MAX_SIZE = 2048
    NOW = datetime.now()

    # Establising the connections
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((HOST,PORT))

    print("Server Starting: ", NOW)
    print("Awaiting Client...")
    print("Send /q to client to exit")

    s.listen(1)
    client,addr = s.accept()

    # While loop to keep connection open
    while True:
        data = client.recv(MAX_SIZE)
        message_received = data.decode('utf-8')
        decrypted = vigenere_dec(message_received)
        if decrypted == '/q':
            break
        print(NOW," Message Received: ")
        print(decrypted)
        message_to_client = input("Enter message to send: ")
        message_to_client = message_to_client.lower()
        encrypted = vigenere_enc(message_to_client)
        message_to_client_encoded = encrypted.encode('utf-8')
        client.send(message_to_client_encoded)
        if message_to_client == '/q':
            encrypted = vigenere_enc(message_to_client)
            message_to_client_encoded = encrypted.encode('utf-8')
            client.send(message_to_client_encoded)
            break
    # closing connection
    client.close()
    s.close()
    return()

def message_client():
    # Details of the device to connect to
    # HOST is an IP address (requires "")
    HOST = "192.168.0.48"
    PORT = 44441
    MAX_SIZE = 2048
    NOW = datetime.now()
   
    # Establising the connections
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((HOST,PORT))

    # Informing user that connection is being established
    print("Client Starting: ", NOW)
    print(" To exit send /q to server!")
    print("Awaiting Server...")

    # While loop to keep connection open
    while True:
        message_to_server = input("Enter message to server: ")
        message_to_server = message_to_server.lower()
        encrypted = vigenere_enc(message_to_server)
        # UTF-8 is the dominant encoding for the world wide web
        # https://en.wikipedia.org/wiki/UTF-8
        message_to_server_encoded = encrypted.encode('utf-8')
        s.send(message_to_server_encoded)
        if message_to_server == '/q':
            break
        data = s.recv(MAX_SIZE)
        if data.decode('utf-8') == '/q':
            break
        print(NOW," Message Received: ")
        message_received = data.decode('utf-8')
        decrypted = vigenere_dec(message_received)
        print(decrypted)

    # Closing connection
    s.close()
    return()

def vigenere_enc(message):
    input_string = ""
    enc_string = ""

    # Takes string from user
    input_string = message
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = enc_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + enc_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position + key_character_position
            if new_position > 26:
                new_position = new_position - 26
            new_character = alphabet[new_position]
            enc_string = enc_string + new_character
        else:
            enc_string = enc_string + letter
    return(enc_string)

def vigenere_dec(message):
    input_string = ""
    dec_string = ""

    # Takes string from user
    input_string = message
    input_string = input_string.lower()

    # Lengths of input_string
    string_length = len(input_string)

    # Expands the encryption key to make it longer than the inputted string
    expanded_key = dec_key
    expanded_key_length = len(expanded_key)

    while expanded_key_length < string_length:
        # Adds another repetition of the encryption key
        expanded_key = expanded_key + dec_key
        expanded_key_length = len(expanded_key)

    key_position = 0

    for letter in input_string:
        if letter in alphabet:
            # cycles through each letter to find it's numeric position in the alphabet
            position = alphabet.find(letter)
            # moves along key and finds the characters value
            key_character = expanded_key[key_position]
            key_character_position = alphabet.find(key_character)
            key_position = key_position + 1
            # changes the original of the input string character
            new_position = position - key_character_position
            if new_position > 26:
                new_position = new_position + 26
            new_character = alphabet[new_position]
            dec_string = dec_string + new_character
        else:
            dec_string = dec_string + letter
    return(dec_string)

message_server()