cmd=""
while cmd !='quit':
    cmd=input('> ').lower()
    if cmd =='start':
        print('Car Started')
    elif cmd =='stop':
        print('Car stopped')
    elif cmd == 'help':
        print("""
start- to start
stop -to stop
quit -to quit""")
        break
    else:
        print("I don't nderstand")
