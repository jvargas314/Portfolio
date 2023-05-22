#In an Intro to Python course I took, we were challenged to write a code that would allow a user to play a game of blackjack along with three computer players.
#Below is the code I came up with. I first defined all my functions, then called them individually to commence the game.

def deal(players): 
        cardsout=[] 
        i=1 
        for p in players: 
            print(p) #labels for every player 
            for z in range(1):
                card1=d[order[i]] 
                card2=d[order[i+1]] 
                players[p] += (card1) 
                players[p] += (card2) 
                print(card1,card2) 
                cardsout.append(order[i]) 
                cardsout.append(order[i+1]) 
                i+=2  
                print('') 
        print(sorted(cardsout)) #check

def find_value(cards): 
    card_val = 0
    ace = False 
    value_dict = {'A': 11, 'K': 10, 'Q': 10, 'J': 10, '10': 10, 
    '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, } 
    for i in range(0, len(cards), 2):
        temp = value_dict[str(cards[i])]
        card_val += temp
        if cards[i] == 'A': 
            ace = True
        if card_val > 21 and ace: 
            card_val -= 10
    return card_val 


def bet(pchips):
    for key in pchips:
        if key != 'p2':
            (pchips[key])-=5
        else:
            try: 
                p2temp = int(input('How many chips would you like to bet?  ')) 
            except ValueError: 
                print("Please enter an interger") 
            if p2temp < 5: 
                    print('Sorry, you must bet a minimum of $5 ')
                    bet(pchips)
            elif p2temp > pchips[key]: 
                    print('Sorry, your bet cannot exceed', pchips[key])
                    bet(pchips)
            else:
                pchips['p2']-=p2temp
    print(pchips)

        
import random 

values=[2,3,4,5,6,7,8,9,10,'J','Q','K','A'] 
suites=['S','C','H','D'] 
cards=[] 
for v in values: 
    for s in suites: 
        cards.append([v,s]) 

d=dict(zip(range(1,53),cards)) 
order=list(range(1,53))  
random.shuffle(order) 

players={'cpu1':[],'p2':[],'cpu3':[],'cpu4':[],'dealer':[]} 
pchips={'p2':100,'cpu1':100,'cpu3':100,'cpu4':100}


deal(players) #deals 2 cards
bet(pchips)
max_value = 0
max_player = ""
for player in pchips:
    temp_value = find_value(players[player])
    if (temp_value > max_value):
        max_value = temp_value
        max_player = player
        
if (max_player == "cpu1" or max_player == "cpu3" or max_player == "cpu4"):
    pchips[max_player] += 10
else:
    pchips[max_player] += 7 #Incomplete: add the user bet
        
