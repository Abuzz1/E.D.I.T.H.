from bj import Blackjack

def blackjack(a1, d):
    hand = Blackjack(a1)
    dealer = d

    h_value = hand.hand_value()
    print(' Perfect Strategy Blackjack\n', '-'*26, '\n'*2)
    print(f" YOUR CARDS VALUE: {h_value}\n DEALER'S CARD: {dealer}")



# make it loop 
# and be used with edithMemory
    try:
        if h_value <= 8: 
            print('hit')

        elif h_value == 9:
            if dealer == 2:
                print('hit')
            elif dealer in range(3, 6): # check
                print('double down')
            elif dealer >= 6:
                print('hit')

        elif h_value == 10:
            if dealer <= 9: # check
                print('hit')
            elif dealer >= 9: 
                print('hit')

        elif h_value == 11:
            print('double down')

        elif h_value == 12:
            if dealer <= 3:
                print('hit')
            elif dealer in range(4, 6): 
                print('stand')
            else:
                print('hit')

        elif h_value in range(13, 16):
            if dealer <= 6: 
                print('stand')
            else: 
                print('hit')

        else:
            if h_value != 21:
                print("stand")
            else:
                print("END GAME")
    except:
        if dealer == 'a': 
            print('hit')