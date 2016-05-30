# see http://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python


import random

def randomstring (length):
    subset = "ATCG"
    subset_length = len(subset)
    randomstring = ""
    for i in range (0, int(length)):
        randomstring = randomstring + subset[random.randint(0,subset_length)-1]
    print (randomstring)


length = raw_input("How long will your sequence be? ")
if int(length)%3 == 0:
    randomstring(int(length))
else:
    print("Sequence length must be multiple of 3!")
