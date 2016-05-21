def transcribe(dna_seq):
    rna_seq = dna_seq.replace('T','U')
    print(rna_seq)

# DNA sequence you want to make into RNA:
transcribe("ATCGCTAGCTAC")
