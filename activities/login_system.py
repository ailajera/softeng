# START HERE
def login(username, password):
    
    if username == "admin" and password == "1234":
        return("Login Successful")
    else:
        return("Invalid credentials")

##

if __name__ == "__main__":
    uname = None # GET INPUT HERE
    pwd = None # GET INPUT HERE 
    print(login(uname, pwd))
