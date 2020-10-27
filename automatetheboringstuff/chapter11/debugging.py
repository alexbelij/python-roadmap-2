# Chapter 11 Debugging
import random, logging
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(levelname)s - %(message)s')
logging.disable(logging.ERROR)
logging.debug('Start of program.')

guess = ''
while guess not in ('heads', 'tails'):
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    logging.debug('Toss value: %s' % (toss))
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
# Needed indent from here
    # Added heads/tails logic
    if toss == 1:
        toss = 'heads'
    else:
        toss = 'tails'
    if toss == guess:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        # guesss is not used should be guess.
        # guesss = input()
        guess = input()
        logging.debug('guess input %s' % (guess))
        if toss == guess:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')

logging.debug('End of program.')