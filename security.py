import hashlib
def hasher(passwd):
    # encode string "hello" to bytes
    plaintext = passwd.encode()
    # call the sha256(...) function returns a hash object
    d = hashlib.sha256(plaintext)
    # generate binary hash of "hello" string
    global hash
    hash = d.hexdigest()