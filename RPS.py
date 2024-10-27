from getpass import getpass #a module use for password as it here use it to hide entry

def rps():
 print('''
____________________________________
|                                  |
|          WELCOME TO THE          |
|       ROCK PAPER SCISSORS        |
|              GAME                |
|__________________________________|

''')
 print('''
For ROCK -- 'R'or'r'
For PAPER -- 'P'or'p'
For SCISSORS -- 'S'or's'
''')
 s_p1=0
 s_p2=0
 for i in range(0,100):
    player1=getpass("Enter your element player1: ").upper() #setting it by default in uppercase for not having any futher confusion and getpass funtion for hiding entry
    player2=getpass("Enter your element player2: ").upper()

    if player1=='R':
        if player1==player2:
            print("Draw")
        elif player2=='S':
            s_p1+=1
            print("Player1 win.")
        elif player2=='P':
            s_p2+=1
            print('Player2 win.')
        else:
            print('Anyone type wrong input!')
        
    elif player1=='S':
        if player1==player2:
            print("Draw")
        elif player2=='P':
            s_p1+=1
            print("Player1 win.")
        elif player2=='R':
            s_p2+=1
            print('Player2 win.')
        else:
            print('Anyone type wrong input!')

    elif player1=='P':
        if player1==player2:
            print("Draw")
        elif player2=='R':
            s_p1+=1
            print("Player1 win.")
        elif player2=='S':
            s_p2+=1
            print('Player2 win.')
        else:
            print('Anyone type wrong input!')

    elif player1!=('S','R','P'):
       print('Anyone type wrong input.')

    if s_p1==5:
      print('Player1 win the game.')
      cmp()
    if s_p2==5:
      print('Player2 win the game.')
      cmp() 
      
def cmp(): #playing it in loop until you stop
     k=input("Do you want to play again(1.Yes/2.No): ").lower()
     if k in ('1','y','yes'):
          rps()
     elif k in ('2','n','no'):
          print("THANK YOU FOR PLAYING :)")
          exit()          
     else:
         cmp()
if __name__=='__main__':
    rps()
