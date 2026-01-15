import os
import datetime
import json
import webbrowser
import time
import random


def init_janv():

    if os.path.exists("janv_core.json") == False:
        print("SOFTWARE: First time setup detached~")
        origin()

def origin():
    current= datetime.datetime.now() 
    name=input("enter the name of SOFTWARE: ")
    meaning=input(f"meaning of {name}: ")
    version=float(input("enter version : "))
    birthdate=input(f"enter the birthdate of {name}: ")
    print("...")
    time.sleep(15)
    print('Active...')

    data={
        "name": name,
        "meaning": meaning,     #just a nascent vision
        "version": version ,
        "birthdate" : birthdate,
        "time":current.strftime("%d-%m-%y %H:%M")
    }

    data2=json.dumps(data, indent=4)
    print(data2)
    with open('janv_core.json', 'w')as f:
        f.write(data2)

def janv_say(category):
    if responses.get(category):
        return random.choice(responses[category])

    else:
        return "---"
def today_date():

    current= datetime.datetime.now() 
    special_date=current.strftime("%d-%m") 
    date=current.strftime("%d-%m-%y") 
    timecurrent=current.strftime("%H:%M:%S")

    if special_date=="15-01":
        time.sleep(2)
        print("JANV: this date matters.")
        time.sleep(4)
        print("JANV: (whisper quitely) Happy Birthday, JJ.")
        time.sleep(5)

    print(f"JANV: Okay, so Today's date is:{date}")
    print(f"JANV: ..and current time is:{timecurrent}")


def load_responses():

    try:
        with open ("responses.json", 'r')as f:
            return json.load(f)
    
    except FileNotFoundError:
        return{
        "apps":[],
        "command":[],
        "new command":[],
        "unknown command":[],
        "learn command":[],
        "listening":[],
        "exit":[],
        "error":[]
    }
        
responses=load_responses()


def add_responses(responses):

    for _ in range(100):
            add_response=input('Add response to JANV: ').strip()

            if add_response.lower()=='break':
                print("JANV: stopping response Entry.")
                break
            
            command_type=input(
                "JANV: type (apps /command /New command /unknown command /learn command /listening /exit/ error  : ) "
                ).lower()

            if command_type in responses:

                if add_response not in responses[command_type]:
                    responses[command_type].append(add_response)
                    print("JANV:", janv_say("new command"))

                else:
                    print("JANV: this response Already Exist.")
                    continue

            else:
                print("JANV:", janv_say("unknown command"))
                print("JANV: Unknown Category!")
                continue

    with open("responses.json", "w")as f:
        json.dump(responses, f, indent=4) 
    return responses


def add_command():
    try:
        with open("commands.json", 'r')as f:
            commands=json.load(f)
    except FileNotFoundError:
        commands={}
        
    size=int(input('how many commands you want to add : '))
    print('\n')

    for _ in range(size):
        key=input("Enter the Command : ").lower()
        time.sleep(3)
        if key.lower()=='break':
            print('JANV: Okay, stopping command entry.')
            break
        value=input("Enter the path or URL: ")
      
        commands[key]=value
        print("JANV:", janv_say("new command"))
        time.sleep(2)
        print(f"JANV: Got it! command {key} has been saved.")

    with open('commands.json', 'w') as file:
        json.dump(commands, file, indent=4)

def execute_command():
    with open("commands.json", 'r')as f:
        commands=json.load(f)

    command=input("JANV: Enter the command: ").lower()
    print('\n')
    if command in commands:
        path=commands[command]
    else:
        print("JANV:", janv_say("unknown command"))
        print('\n')
        makecommand=input(f"JANV: {janv_say('learn command')}").lower()
        if makecommand !='no':
            add_command()
            return
        if makecommand =='no':
            print("JANV: Understood.")
            return
    
    if path.startswith('https'):
        print("JANV:", janv_say("apps"))
        time.sleep(2)
        webbrowser.open(path)
        print('JANV: Done.')
    else:

        print("JANV:", janv_say("apps"))
        time.sleep(2)
        os.startfile(path)
        print('JANV: Done.')


init_janv()

print('\nJANV acitve! ')
while True:
    time.sleep(2)
    user=input(f"{janv_say('listening')}: ").lower()
    time.sleep(1)

    
    if user=="date":
        time.sleep(3)
        today_date()

    elif user=="add command":
        time.sleep(2)
        print("JANV:", janv_say('command'))
        add_command()

    elif user=="execute command":
        time.sleep(2)
        print("JANV:", janv_say('command'))
        execute_command()

    elif user=="add response":
        time.sleep(2)
        print("JANV:", janv_say('command'))
        add_responses(responses)

    elif user=="break" or "stop":
        print(f"JANV {janv_say('exit')}")
        time.sleep(1)
        break
        

    
