from getpass import getpass
import hashlib
https://www.psycopg.org/docs/usage.html#passing-parameters-to-sql-queries
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
    raw.update(raw) #this is stringing q instead of insert q as stored input TODO FIX
    close = raw.hexdigest()  #digests and hashes password
return password
##This program should output the password and then the hashed password should be imported into the create_database file


hash_me()
