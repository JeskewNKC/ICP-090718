import csv
inputfile = "codon.tsv"
f = open(inputfile, "r")
genetic_code = {}
for row in f:
        columns = row.split()
        genetic_code[columns[0]] = columns[1]

seq = input('Enter a sequence: ')
seq = seq.upper()
seq = seq.replace(" ", "")
# test to see if sequence is divisible by 3 if not ignore last nucleotides until %3 == 0

if len(seq)%3 != 0:
    seq = seq[:-1]
if len(seq)%3 !=0:
    seq = seq[:-1]

# below is list comprehension expression to create a list of 3 nucleotide codons
codons = [seq[i:i+3] for i in range(0, len(seq), 3)]

# Protein translation and appending a.a. to new list [protein_list]
protein_list = []
for aa in codons:
    protein = ([genetic_code[aa]])
    protein_list.append(*protein)

print(protein_list)

# Used list comprehension to create a.a. and a.a count dictionary
d = dict( [(i, protein_list.count(i)) for i in set(protein_list) ])
print (d)
