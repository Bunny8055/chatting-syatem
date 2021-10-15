import datetime
import pyrebase

config = {
  "apiKey": "apiKey",
  "authDomain": "chat-app-b053e-default-rtdb.firebaseio.com",
  "databaseURL": "https://chat-app-b053e-default-rtdb.firebaseio.com",
  "storageBucket": "chat-app-b053e-default-rtdb.firebaseio.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
print('*'*(200-12))
def enroll():
    
    C = input("Enter your username/loginID:")
    e = input("Enter your password:")
    f = input("Confirm your password:")
    if C == e:
             print("Password and username cannot be same:")
             e = input("Enter your password:")
             f = input("Confirm your password:")
    if len(e) != 4 and len(f) != 4: 
             print("Password must be of 4 characters")
             e = input("Enter your password:")
             f = input("Confirm your password:")
            
    if e == f:
             print("Password confirmed")
             g = {C:int(e)}
             db.child("userdata").update(g)
    else:
            print("Password does not matched..")
            enroll()
    


def message():
    print("Press 1 to receive msg:")
    print("Press 2 to send msg:")
    print("Press 3 to Log-out:")
    print('*'*(200-12))
    a = int(input("Enter the mode:"))
    if a!=1 and a!=2 and a!= 3:
        print("Wrong selection!!! \n Press either 1 or 2")
    elif(a == 3):
        exit() 
    elif(a == 2):
        send()
    elif(a == 1):
        receive()

def receive():
    print("Do you want to receive all the messages at one time ? \n or do you want to receive message from only one user ? \n Press 1 to receive all messages \n Press 2 to receive messages from one user..")
    print('*'*(200-12))
    q = int(input("Enter your choice.."))
    if q!= 1 and q!= 2:
        print("Wrong selection!!! \n Press either 1 / 2 ")
    if q == 1:
        all_users = db.child("Messages").child("Receiver").child(usem).get()
        for user in all_users.each():
            print(user.key())
            print(user.val())
    if q == 2:
        sender = input("Enter the name of user:")
        all_users = db.child("Messages").child("Receiver").child(usem).child(sender).get()
        #print(all_users.key())
        #print(all_users.val())
        if sender == all_users.key():
            users = db.child("Messages").child("Receiver").child(usem).child(sender).get()
            for users in users.each():
                print(users.key())
                print(users.val())
        else:
            print("No messages from this user or the user does not exist on the system..")
        

        
def send():
    receiver = input("Enter the user's name to whom you want to send message..")
    u = db.child("userdata").child(receiver).get()
    y = datetime.datetime.now()
    z = (y.strftime("%I-%M-%p"))
    if receiver == u.key():
        msg = {z:input("Enter your message..")}
        x = db.child("Messages").child("Receiver").child(receiver).child(usem).update(msg)
        
    else:
        print("User does not exist.")

             

while(1):
    print("Press 1 for Sign up:")
    print("Press 2 for Login:")
    print("Press 3 to quit:")
    print('*'*(200-12))
    a = int(input("Enter the mode:"))
    if a!=1 and a!=2 and a!=3:
        print("Wrong selection!!! \n Press either 1 2 or 3")
    elif(a == 1):
        enroll()
    elif(a == 3):
        exit()
    elif(a == 2):
        print("Enter your username:")
        usem = input()

        u = db.child("userdata").child(usem).get()
             #print(u)
        #print(u.val())
        if usem == u.key():
            print("Enter your password:")
            passw = int(input())
            if passw == u.val():
                print("Login Done..")
                print('*'*(200-12))
                while(1):
                    message()
            else:
                print("Wrong password Try again..")
        else:
            print("User does not exist")
            print("Do you want to sign up? Press 1 if 'Yes'")
            d = int(input())
            if d == 1:
                enroll()
            else:
                print("Wrong selection!!!")


             
             
             





