def rna2dna(rna_seq):
    dna_seq = rna_seq.replace('U','T')
    print(dna_seq)
# RNA sequence that you want to make into DNA
rna2dna("AUGAUGCUC")
