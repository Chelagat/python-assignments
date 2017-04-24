#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Norah Borus
SUNet: nborus

Replace this with a description of the program.
"""
import utils
ALPHA_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

# Caesar Cipher

def encrypt_caesar(plaintext):
	decrypted_text = ""
	displacement = 3
	for letter in plaintext:
		index = ALPHA_UPPER.find(letter);
		if index != -1:
			decrypted_text += ALPHA_UPPER[(index + displacement) % 26]
		else:
			decrypted_text +=letter
		
	return decrypted_text



def decrypt_caesar(ciphertext):
	encrypted_text = ""
	displacement  = 3
	for letter in ciphertext:
		index = ALPHA_UPPER.find(letter);
		if index != -1:
			if index < displacement:
				index+=26
			encrypted_text += ALPHA_UPPER[index - displacement]
		else:
			encrypted_text +=letter
	
	return encrypted_text


# Vigenere Cipher

def encrypt_vigenere(plaintext, keyword):
	index = 0
	encrypted_text = ""
	for char in plaintext:

		keyChar = (keyword[index % len(keyword)])
		val1 = ord(char)
		val2 = ord(keyChar)
		int_val = (val1 + val2 -65)
		if int_val > 90:
			int_val = int_val - 26	
		letter = chr(int_val)
		encrypted_text += letter
		index += 1
	return encrypted_text.upper()

def decrypt_vigenere(ciphertext, keyword):


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r × w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

