from urllib.request import urlopen
with urlopen('http://www.agilemanifesto.org/') as response:
     for line in response:
         line = line.decode('utf-8')  # Decoding the binary data to text.
         print(line)
