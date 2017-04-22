import random

def coin_toss(tosses):
    print "Starting the program..."
    print ""

    attempt_count = 0
    head_count = 0
    tail_count = 0
    for each_toss in range(tosses):
        attempt_count += 1
        rand_flip = random.randint(0,1)
        # print rand_flip, "--> checking random number; what side of coin [0=head | 1=tails]?"
        if rand_flip == 0:
            head_count +=1
            print "Attemp #", attempt_count, ":  Throwing a coin... It's a head!...Got", head_count, " head(s) so far and", tail_count, " tail(s) so far."
            # print head_count, "--> checking head_count"
        elif rand_flip == 1:
            tail_count +=1
            print "Attemp #", attempt_count, ":  Throwing a coin... It's a tail!...Got", head_count, " head(s) so far and", tail_count, " tail(s) so far."
    print "End of Program. Thank you..."


coin_toss(5000)
