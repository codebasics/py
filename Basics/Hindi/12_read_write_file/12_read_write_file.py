# read file
f=open("funny.txt","r")
for line in f:
    print(line)
f.close()

# readlines()
f=open("funny.txt","r")
lines = f.readlines()
print(lines)

# write file
f=open("love.txt","w")
f.write("I love python")
f.close()

# same file when you write i love javascript the previous line goes away
f=open("love.txt","w")
f.write("I love javascript")
f.close()

# You can use append mode to stop having previous lines overwritten
f=open("love.txt","a")
f.write("I love javascript")
f.close()

# show a picture of file open modes (12:12 in old video)

# writelines
f=open("love.txt","w")
f.writelines(["I love C++\n","I love scala"])
f.close()

# with statement
with open("funny.txt","r") as f:
    for line in f:
        print(line)

# https://www.cricketworldcup.com/teams/india/players/107
player_scores = {}
with open("scores.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        player = tokens[0]
        score = int(tokens[1])
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

print(player_scores)

for player, score_list in player_scores.items():
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg:{avg_score}")
