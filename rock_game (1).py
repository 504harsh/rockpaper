import random

lst=['stone','paper','scissor']
count_comp=0
count_player=0
while True:
            chance=input('Enter one from stone, paper, scissor: ')
            player=chance.lower()
            computer=random.choice(lst)
            print('Computer has taken', computer)
            
            if player==computer:
                        print("\nMatch Draw")
            elif player=='stone':
                        if computer=='scissor':
                                    print('\nPlayer wins')
                                    count_player+=1
                        else:
                                    print('\nComputer wins')
                                    count_comp+=1
            elif player=='paper':
                        if computer=='scissor':
                                    print('\nPlayer wins')
                                    count_player+=1
                        else:
                                    print('\nComputer wins')
                                    count_comp+=1
            else:
                        if computer=='paper':
                                    print('\nPlayer wins')
                                    count_player+=1
                        else:
                                    print('\nComputer wins')
                                    count_comp+=1
            print()
            user=input('Do u want to continue (y/n):')
            if user=='y':
                        continue
            else:
                        print('Computer Score=',count_comp)
                        print('Player Score=',count_player)
                        if count_comp<count_player:
                                    print("Player wins")
                        elif count_comp>count_player:
                                    print("Computer wins")
                        else:
                                    print("Draw")
                        break
