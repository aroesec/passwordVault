from getpass import getpass
import hashlib

def hash_me():
    raw = hashlib.new('sha256')   #declares new hash
    while True:
        clientPass = getpass("enter your password to be hashed: ") #updates declared hash with password
        checkClientPass = getpass("re-type password: ") #retype password to check for accuracy
        if clientPass != checkClientPass: #check if passwords were entered correctly and match
            print("password did not match, try again:") #if passwords do not match, loop
        else:
            break #if passwords match, break out of loop
    byteTransform = bytes(q, 'utf-8')
    raw.update(w) #this is stringing q instead of insert q as stored input TODO FIX
    close = raw.hexdigest()  #digests and hashes password
    
    

#TODO convert var a back to bytes to then decrypt to test
    #print(q)
    # attempting to decrypt the sha256 for testing
    # fernet = Fernet(a)   
    # print(type(a))
    # encrypted = fernet.decrypt(a)
    # print(a)

hash_me()
