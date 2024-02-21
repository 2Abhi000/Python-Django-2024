sec_no=9
guess_cnt=0
guess_limit=3
while guess_cnt<guess_limit:
    guess=int(input('Guess: '))
    guess_cnt+=1
    if guess==sec_no:
        print('You Won')
        break
else:
    print("Try Again")
    
