oligo1 = ""

for i in range (0,50):
    oligo1 = oligo1 + "A"
oligo1 = oligo1 + "CCGGTTGGCC"

print(oligo1)
print(len(oligo1))


oligo2 = ""

for i in range (0,50):
    oligo2 = oligo2 + "A"
oligo2 = oligo2 + "GGCCAACCGG"

print(oligo2)
print(len(oligo2))

f = open('oligo.txt','w')
f.write(oligo1 + "\n" + oligo2 + "\n")
f.close()
