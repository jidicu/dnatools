# This is a repeating sequence. The length of the repeat here is 50 bp.

for i in range (0,50):
    oligo = oligo + "A"

# This is your sticky end.
oligo = oligo + "CCGGTTGGCC"

#This prints your oligo as an output.
print(oligo)
print(len(oligo))

# This also writes your oligo into a text file.
f = open('oligo.txt','w')
f.write(oligo + "\n")
f.close()
