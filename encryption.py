import hashlib

def hash_me():
    a = hashlib.new('sha256')   #declares new hash 
    q = input("enter your password to be hashed: ") #updates declared hash with password
    w = bytes(q, 'utf-8')
    a.update(w) #this is stringing q instead of insert q as stored input TODO FIX
    w = a.hexdigest()  #digests and hashes password
    
    

#TODO convert var a back to bytes to then decrypt to test
    #print(q)
    # attempting to decrypt the sha256 for testing
    # fernet = Fernet(a)   
    # print(type(a))
    # encrypted = fernet.decrypt(a)
    # print(a)

hash_me()