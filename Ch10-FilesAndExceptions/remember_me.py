import json
username = input("What is your name? >>> ")
filename = 'username.json'
try:
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
except FileNotFoundError:
    print("There is no such file '" + filename + "'!")