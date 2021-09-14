try:
    with open('file_14.txt','r') as f:
        print(f.read())
except Exception as e:
    print("Something went wrong", e)
