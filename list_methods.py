# List Methods Practice
# Topics: append(), insert(), remove(),
#         pop(), sort(), reverse()

players = ["Virat", "Rohit", "Gill", "Rahul", "Hardik"]

players.append("Jadeja")
print(players)

players.insert(2,"Bhurah")
print(players)

players.remove("Rahul")
print(players)

removed_player = players.pop(4)
print(removed_player)                        
print(players)

players.append("Virat")
print(players)
print(players.count("Virat"))

players.sort()
print(players)

players.reverse() 
print(players)