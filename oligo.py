# This is a repeating sequence. The length of the repeat here is 50 bp.
repeat_len = raw_input("How long do you want your repeat to be? ")

oligo = ""

for i in range (0,int(repeat_len)-1):
    oligo = oligo + "A"

sticky = raw_input("What is the sticky end sequence? ")

# This is your sticky end.
oligo = oligo + sticky

#This prints your oligo as an output.
print(oligo)
print(str(len(oligo)) + " bp")

# This also writes your oligo into a text file.
f = open('oligo.txt','w')
f.write(oligo + "\n")
f.close()
