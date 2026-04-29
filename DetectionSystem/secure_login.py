import re
import datetime
import uuid
try:
    with open("attempt.txt", "r") as file:
        attempts= int(file.read())
except:
    attempts = 0
def sqli_detection(user_input): 
    data = user_input.lower()
    keywords = ["or","select","drop","union","insert","delete"] 
    
    for word in keywords: 
        pattern = r"\b" + word + r"\b"
        if re.search(pattern,data):
            return True

    if "'" in data or "--" in data or ";" in data : 
        return True 
    return False

def risk_level(user_input):
    data = user_input.lower()
    if ( 
        re.search(r"\bdrop\b",data) or 
    re.search(r"\bunion\b",data) or 
    re.search(r"\binsert\b",data) or 
    re.search(r"\bdelete\b",data) or
    re.search(r"\bselect\b",data)
    ):
        return "HIGH"
    elif re.search(r"\bor\b",data):
        return "MEDIUM"
    else:
        return "LOW"
    ##Dummy DB
correct_username = "admin"
correct_password = "1234"

session_id = uuid.uuid4()
username = input("Enter username : ")
password = input("Enter password : ")

if sqli_detection(username) or sqli_detection(password):
    if attempts < 3:
        attempts += 1
        with open("attempt.txt" ,"w") as file:
            file.write(str(attempts))
    risk = risk_level(username  + password )

    print("SQL Injection Detected! Access Denied")
    print(f"Attempt Count: {attempts}")

    if attempts >= 3:
        status = "BLOCKED"
    else:
        status = "DETECTED"

    with open("sqli_logs.txt", "a") as file:
      file.write(f"""
      =====================
      Time : {datetime.datetime.now()}
      SessionID : {session_id}
      Risk Level :{risk}
      Attempts: {attempts} 
      Username : {username},
      Password : {"*" *len(password)}
      Status   : {status}
      ======================
      """)
else:
    if username == correct_username and password == correct_password:
      print("Login Successful")
    else:
        print("Invalid Credentials")

if attempts>=3:
    print("User temporarily blocked due to multiple attempts")
    exit()

