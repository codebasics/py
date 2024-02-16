# Road Not Taken.txt contains famous poem "Road not taken" by poet Robert Frost.
# You have to read this file in your python program and find out words with maximum occurrence.

keywords ={}
with open("Road Not Taken Poem.txt", "r") as f:
    for line in f:
        # Filtration of line removing special characters
        new_line = ''
        for character in line:
            if character.isalnum() or character == ' ' or character == '\'':
                new_line += character

        # splitting new line into words
        items = new_line.split(" ")
        for item in items:
            # confirming that space should not be counted
            if item != '':
                # converting each word into lower case so that case can be matched later
                key = item.lower()
                if key in keywords:
                    keywords[key]+=1
                else:
                    keywords[key] = 1


word = ''
frequency = 0
for keyword, value in keywords.items():
    if value > frequency:
        frequency = value
        word = keyword

print(f"The most frequent used word in the poem is '{word}'. It was repeated {frequency} times")
