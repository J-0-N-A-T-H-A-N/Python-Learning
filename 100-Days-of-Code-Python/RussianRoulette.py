import random

num_of_bullets = 6

rand_num=random.randint(1,6)

for x in range(0,num_of_bullets):
    fire=input('Press any key to fire')

    if x == rand_num:
        print("Bang! You're dead. Game Over!")
        exit()
    else:
        print("Click! Empty!")