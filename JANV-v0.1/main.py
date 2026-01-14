import os
import datetime
import json
import webbrowser
import time

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
        
def today_date():

    current= datetime.datetime.now() 
    special_date=current.strftime("%d-%m") 
    date=current.strftime("%d-%m-%y") 
    time=current.strftime("%H:%M:%S")

    if special_date=="15-01":
        print("JANV: this date matters.")
        print("JANV: (whisper quitly)Happy Birthday Janhavi.")
        # time.sleep(4)

    print(f"JANV: Okay, so Today's date is:{date}")
    # time.sleep(2)
    print(f"JANV: ..and current time is:{time}")


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
            print('JANV: Okay, stoppping command entry.')
            break
        value=input("Enter the path or URL: ")
      
        commands[key]=value
        print('wait a second working on it!')
        time.sleep(3)
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
        print('JANV: This command is not in the file!')
        print('\n')
        makecommand=input("JANV:I don't know this command yet,\n You want me to learn this?: ").lower()
        if makecommand !='no':
            add_command()
            return
        if makecommand =='no':
            print("JANV: okay. you can do tihs later.")
            return
    
    if path.startswith('https'):
        print('JANV: working on it..')
        time.sleep(2)
        webbrowser.open(path)
        print('JANV: Done.')
    else:

        print('JANV: Got it..')
        time.sleep(2)
        os.startfile(path)
        print('JANV: Done.')


# origin()

print('JANV acitve! ')
while True:
    time.sleep(2)
    user=input('JANV: hey Gaurav what can i do for you.: ').lower()
    time.sleep(1)

    
    if user=="todays date":
        today_date()

    elif user=="add command":
        print("JANV: Got it..")
        print('\n')
        add_command()

    elif user=="execute command":
        print("JANV: Got it..")
        print('\n')
        execute_command()
    
