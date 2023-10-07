with open('C://Users//77081//PycharmProjects//Data//poem.txt','r') as f:
    for line in f:
        words = line.split(' ')
        for word in words:
            if word in word_stats:
                word_stats[word]+=1
            else:
                word_stats[word] = 1

print(word_stats)

word_occurances = list(word_stats.values())
max_count = max(word_occurances)
print('Максимум повторяющих слов: ', max_count)

for word,count in word_stats.items():
    if count == max_count:
        print(word)
