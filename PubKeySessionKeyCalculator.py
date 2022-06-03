#!/usr/bin/env python
# coding: utf-8

# # Welcome to the Diffie-Hellmann public key und session key calculator
# ## This calculator works  with the square and multiply algorithm (not optimized) 
# ### Input:
# #### prime number "p"
# #### together-agreed number "g"
# #### from person A chosen private key "a"
# #### from person B chosen private key "b"
# ### Output: 
# #### public key of person A
# #### public key of person B
# #### their session key.



# initializing

p = None
g = None
key_prv_a = None
key_prv_b = None
key_pub_a = None
key_pub_b = None
session_key = None

# Exception-Handling & Input

while(type(p) != int):
    try:
        print("\nPlease enter a valid Integer: ")
        p = int(input("prime number p: "))
    except Exception as e:
        print("\nError: ", e)

while(type(g) != int):
    try:
        print("\nPlease enter a valid Integer: ")
        g = int(input("together-agreed number g: "))
    except Exception as e:
        print("\nError: ", e)

while(type(key_prv_a) != int):
    try:
        print("\nPlease enter a valid Integer: ")
        key_prv_a = int(input("private key of Person A: "))
    except Exception as e:
        print("\nError: ", e)
        
while(type(key_prv_b) != int):
    try:
        print("\nPlease enter a valid Integer: ")
        key_prv_b = int(input("private key of Person B: "))
    except Exception as e:
        print("\nError: ", e)


# ### Calculation of the public key of Person A


max_exponent_a = 0
temp_key_prv_a = key_prv_a
list_of_exponents_a = []

while(1):
    max_exponent_a = max_exponent_a + 1
    #print("max_exponent_a: ", max_exponent_a)
    if(key_prv_a < 2**max_exponent_a): # Look for the highest exponent with base 2 of key_prv_a
        break


while(max_exponent_a >= 0 and type(max_exponent_a) == int): 
    
    if(temp_key_prv_a >= 2**max_exponent_a): # if the prv key is bigger then 2**max_exponent_a
        temp_key_prv_a = temp_key_prv_a - (2**max_exponent_a) # subtracting the privat key with the value that it can be multiplied with with the base 2 to get the original privat key 
        list_of_exponents_a.append(max_exponent_a)
        #print("List of exponents: ", list_of_exponents_a)
    else:
        max_exponent_a = max_exponent_a -1
    
    #print("temp_key_prv_a: ", temp_key_prv_a)
    #print("max_exponent_a: ", max_exponent_a)
    
print("List of exponents: ", list_of_exponents_a)


# #### Now we have a list of exponents with the base of 2 which, multiplied, will result to the private key of person A



index_of_exponents_a = len(list_of_exponents_a) - 1
key_pub_a = 1

while(index_of_exponents_a >= 0):
    key_pub_a = (key_pub_a * (g**(2**list_of_exponents_a[index_of_exponents_a])) % p) % p
    
    #print("Public key of Person A: ", key_pub_a)
    #print("Index of Exponent: ", index_of_exponents_a)
    index_of_exponents_a = index_of_exponents_a - 1

print("Public key of Person A: ", key_pub_a)


# ### Calculation of the public key of Person B


max_exponent_b = 0
temp_key_prv_b = key_prv_b
list_of_exponents_b = []

while(1):
    max_exponent_b = max_exponent_b + 1
    #print("max_exponent_b: ", max_exponent_b)
    if(key_prv_b < 2**max_exponent_b): # Look for the highest exponent with base 2 of key_prv_b
        break


while(max_exponent_b >= 0 and type(max_exponent_b) == int): 
    
    if(temp_key_prv_b >= 2**max_exponent_b): # if the prv key is bigger then 2**max_exponent_b
        temp_key_prv_b = temp_key_prv_b - (2**max_exponent_b) # subtracting the privat key with the value that it can be multiplied with with the base 2 to get the original privat key 
        list_of_exponents_b.append(max_exponent_b)
        #print("List of exponents: ", list_of_exponents_b)
    else:
        max_exponent_b = max_exponent_b -1
    
    #print("temp_key_prv_b: ", temp_key_prv_b)
    #print("max_exponent_b: ", max_exponent_b)
    
print("List of exponents: ", list_of_exponents_b)


# #### Now we have a list of exponents with the base of 2 which, multiplied, will result to the private key of person B


index_of_exponents_b = len(list_of_exponents_b) - 1
key_pub_b = 1

while(index_of_exponents_b >= 0):
    key_pub_b = (key_pub_b * (g**(2**list_of_exponents_b[index_of_exponents_b])) % p) % p
    
    #print("Public key of Person B: ", key_pub_b)
    #print("Index of Exponent: ", index_of_exponents_b)
    index_of_exponents_b = index_of_exponents_b - 1

print("Public key of Person B: ", key_pub_b)


# ### Session key calculation


index_of_exponents_a = len(list_of_exponents_a) - 1
session_key_a = 1

while(index_of_exponents_a >= 0):
    session_key_a = (session_key_a * (key_pub_b**(2**list_of_exponents_a[index_of_exponents_a])) % p) % p
    
    #print("Session key of Person A: ", session_key_a)
    #print("Index of Exponent: ", index_of_exponents_a)
    index_of_exponents_a = index_of_exponents_a - 1

print("Session key of Person A: ", session_key_a)


index_of_exponents_b = len(list_of_exponents_b) - 1
session_key_b = 1

while(index_of_exponents_b >= 0):
    session_key_b = (session_key_b * (key_pub_a**(2**list_of_exponents_b[index_of_exponents_b])) % p) % p
    
    #print("Session key of Person B: ", session_key_b)
    #print("Index of Exponent: ", index_of_exponents_b)
    index_of_exponents_b = index_of_exponents_b - 1

print("Session key of Person B: ", session_key_b)


if(session_key_a == session_key_b):
    session_key = session_key_a
    print("The session key is: ", session_key)
else:
    print("\nError: session_keys are not the same. Something is wrong.")