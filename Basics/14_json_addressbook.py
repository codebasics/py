import json
f = open("C:\\data\\book.txt","w+")
phone_book = {}
command = ""
while command != 'exit':
    command = input('Enter a command(options: new,get,save): ')
    if command == "new":
        name = input('Enter name of the person')
        p = input('Phone number: ')
        a = input('Address: ')
        phone_book[name] = {'phone': p, 'address': a}
    elif command == 'get':
        name = input('Enter name of the person')
        if name in phone_book:
            print(phone_book[name])
        else:
            print('person not found in address book')
    elif command == 'save':
        f.write(json.dumps(phone_book))
