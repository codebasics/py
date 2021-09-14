# wapp to read a sentence and sort every word of sentence

def mysort(s):
	ls=sorted(s)
	ns=''.join(ls)
	return ns

s1=input("enter a sentence:")
l1=s1.split(" ")
ns1=""
for m in l1:
	m=m[::-1]
	ns1=ns1+" "+m
print(s1,ns1)

