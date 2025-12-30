
test_login_data = [
    {"valid login credentials":("cssupport", "password", "Workspace")},                          #valid login credentials
    {"valid username but invalid password": ("cssupport", "passwor", "Username/Password is not correct.")},   #valid username but invalid password
    {"invalid username but valid password": ("cssuppor", "password", "Username/Password is not correct.")},   #invalid username but valid password
    {"invalid username and invalid password": ("cssuppor", "passwor", "Username/Password is not correct.")},    #invalid username and invalid password
    {"blank username and blank password": ("","","Please enter a Username\nPlease enter password")},        #blank username and blank password
    {"valid username and blank password": ("cssupport","","Please enter password")},                        #valid username and blank password
    {"blank username and valid password": ("","password","Please enter a Username")}                     #blank username and valid password
                   ]

