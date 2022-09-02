import random

min = 1
max = 100
guess = random.randint(1 , 100)
print("my guess is:" , guess)
print("did number correct? type yes or kuchektar or bozorgtar ")
answer = input()

while answer != 'yes':
        
        if answer == "kuchektar":
                new_guess = random.randint(guess , max)
                print("my new guess is:" , new_guess)
                print("did number correct? type yes or kuchektar or bozorgtar ")
                new_answer = input()
                continue
        elif answer == 'bozorgtar':
                new_guess = random.randint( min , guess)
                print("my new guess is:" , new_guess)
                print("did number correct? type yes or kuchektar or bozorgtar ")
                new_answer = input()
                continue

while answer == 'yes':
        print('i win')
        break








        
        


    
    







        






        

