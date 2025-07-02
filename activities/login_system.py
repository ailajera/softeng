# START HERE
def login(username, password):
    
    if username == "admin" and password == "1234":
        return("Login Successful")
    else:
        return("Invalid credentials")
# napipikon na ko kanina pa ko nagbabago. di ko alam bat failed bye. 
#antok na ko bukas na to
##

if __name__ == "__main__":
    uname = None # GET INPUT HERE
    pwd = None # GET INPUT HERE 
    print(login(uname, pwd))
