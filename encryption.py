import hashlib

def hash_me():
    raw = hashlib.new('sha256')   #declares new hash 
    clientPass = input("enter your password to be hashed: ") #updates declared hash with password
    byteTransform = bytes(q, 'utf-8')
    raw.update(raw) #this is stringing q instead of insert q as stored input TODO FIX
    close = raw.hexdigest()  #digests and hashes password
return password
##This program should output the password and then the hashed password should be imported into the create_database file


hash_me()