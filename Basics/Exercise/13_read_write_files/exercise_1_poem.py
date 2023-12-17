word_stats={}

with open("poem.txt","r") as f:
    for line in f:
      words=line.split(' ')
      for word in words:
        if word in word_stats:
          word_stats[word]+=1
        else:
          word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print("Max occurances of any word is:",max_count)

print("Words with max occurances are: ")
for word, count in word_stats.items():
    if count==max_count:
        print(word)
#I tried the above code and found the answer to be as follows:
'''Max occurances of any word is: 8
Words with max occurances are: 
I
the'''
#However, when I tried solving the problem on my own, it resulted in the following output at the end:
'''The word with maximum occurrence is 'and' with count 9'''
word_counts={}
with open("C://Users//Tahir//Desktop//poem.txt","r+") as p:
    for line in p:
        tokens=line.lower().split(' ') #to ensure 'The' and 'the' are counted as same words. At the same time tokenize each line.
        for word in tokens:
            word= word.strip(',.!?;:') #remove punctuation so that 'word,' and 'word' are counted same.
            if word in word_counts:
                word_counts[word]+=1
            else:
                word_counts[word]=1
print(word_counts)
max_word=max(word_counts, key=word_counts.get) #key argument tells max() to operate on the word counts instead of keys which are just words here sorted in lexicographical order.
print(f"The word with maximum occurrence is '{max_word}' with count {word_counts[max_word]}")
