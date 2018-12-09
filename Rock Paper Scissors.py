from random import randint
a = raw_input("Select Rock(r) or Paper(p) or Scissors(s)\n")
comp = {1: "r", 2: "p", 3: "s"}
b = randint(1, 3)
if comp[b] == a:
    print "Draw"
     
else:
    if a == "r":
        if comp[b] == "p":
            print "Comp Wins"
             
        else:
            print "Player Wins"

    if a == "p":
        if comp[b] == "s":
            print "Comp Wins"
             
        else:
            print "Player Wins"

    if a == "s":
        if comp[b] == "r":
            print "Comp Wins"
             
        else:
            print "Player Wins"
