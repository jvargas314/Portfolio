
def deal(players): 

        cardsout=[] 

        i=1 

        for p in players: 

            print(p) #labels for every player 

            for z in range(1):  

                '''I'm not entirely sure why, but this For Loop is necessary 

                for every player to get different cards''' 

             

                c1=d[order[i]] 

                '''card one is equal to value from dict (d) 

                for first number in list 'order''' 

                c2=d[order[i+1]] 

                '''for card 2: takes second number in 'order' and 

                uses it to get the corresponding value from 'd''' 

                players[p] += (c1) 

                players[p] += (c2) 

                '''adds the two cards to the player in dict 'players''' 

                print(c1,c2) 

                cardsout.append(order[i]) 

                cardsout.append(order[i+1]) 

                '''adds card number (between 1 and 52) to list 'cardsout''' 

                i+=2  

                '''increases value of i for the next iteration 

                (loop through) in order to prevent repeating cards''' 

                print('') 

         

        print(sorted(cardsout)) 

'''cardsout is for us to double check that we did not  

distribute the same card twice''' 

 

def find_value(cards): 

    """It finds the total value of the cards""" 

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
    
            total -= 10

    return card_val 


def bet(pchips):
    
    for p in pchips:
        
        if p != 'p2':
            (pchips[p])-=5
        else:
            try: 

                p2temp = int(input('How many chips would you like to bet?  ')) 

            except ValueError: 

                print("Please enter an interger") 

            if p2temp < 5: 

                    print('Sorry, you must bet a minimum of $5 ')
                    bet(pchips)

            elif p2temp > pchips['p2']: 

                    print('Sorry, your bet cannot exceed {} '.format(chips.total))
                    
            else:
                pchips['p2']-=p2temp
            
            
    print(pchips)

# def bets(chips):

#         try: 

#             p2temp = int(input('How many chips would you like to bet?  ')) 

#         except ValueError: 

#             print("Please enter an interger") 

#         if p2temp < 5: 

#                 print('Sorry, you must bet a minimum of $5 ')
#                 bets(pchips)

#         elif p2temp > pchips['p2']: 

#                 print('Sorry, your bet cannot exceed {} '.format(chips.total))
                
#         else:
#             pchips['p2']-=p2temp
#             print(pchips)
        
import random 


'''creates values and suites. 

uses For Loops to create one kind of every card and 

adds them to the list named 'cards'. 

52 cards in total''' 

 
vals=[2,3,4,5,6,7,8,9,10,'J','Q','K','A'] 

suites=['S','C','H','D'] 

cards=[] 

for v in vals: 

    for s in suites: 

        cards.append([v,s]) 

d=dict(zip(range(1,53),cards)) 

'''d is a dictionary with every card in the deck numbered 1 thru 52. 

you can look in the variable explorer for a visual''' 

order=list(range(1,53))  

random.shuffle(order) 

'''order is a list of numbers 1 thru 52 in random order''' 

 
players={'cpu1':[],'p2':[],'cpu3':[],'cpu4':[],'dealer':[]} 

# continue_var = True
pchips={'cpu1':100,'p2':100,'cpu3':100,'cpu4':100}


deal(players) #Dealing two cards
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
    pchips[max_player] += #TODO: add the user bet
        
    
    
    
    
    
     
 