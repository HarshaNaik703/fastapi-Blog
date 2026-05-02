import bcrypt

class Hash:
    def hash(password : str):
        # converting password into array of bytes
        bytes = password.encode('utf-8')
        # generating salt
        salt = bcrypt.gensalt()
        return bcrypt.hashpw(bytes, salt)
    
    def rehash(password : str, hashed:str):
        userBytes = password.encode('utf-8')
        return bcrypt.checkpw(userBytes, hashed)
