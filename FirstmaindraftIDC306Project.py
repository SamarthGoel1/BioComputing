#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import matplotlib.pyplot as plt
def fasta(file_path):
    file = open(file_path, 'r')
    lines = file.readlines()
    header = lines[0].strip()
    sequence = ''
    for line in lines[1:]:
        sequence += line.strip()
    file.close()
    return header, sequence
def protein_seq(sequence, codon_table):
    protein = ''
    for i in range(0, len(sequence), 3):
        codon = sequence[i:i+3]
        if codon in codon_table:
            protein += codon_table[codon]
    return protein
def mutate_sequence(sequence):
    nucleotides = ['A', 'C', 'G', 'T']
    position = random.randint(0, len(sequence) - 1)
    new_nucleotide = random.choice(nucleotides)
    mutated_sequence = sequence[:position] + new_nucleotide + sequence[position + 1:]
    return mutated_sequence, position
def simulation(sequence, codon_table, num_steps):
    initial_protein = protein_seq(sequence, codon_table)
    amino_acid_changes = 0
    current_protein = initial_protein
    for _ in range(num_steps):
        mutated_sequence, position = mutate_sequence(sequence)
        if len(protein_seq(mutated_sequence, codon_table)) < len(initial_protein) / 2 or '_' not in protein_seq(mutated_sequence, codon_table):
            sequence = mutated_sequence
            continue
        changes = 0
        for i in range(len(protein_seq(mutated_sequence, codon_table))):
            if current_protein[i] != protein_seq(mutated_sequence, codon_table)[i]:
                changes += 1
        if changes > 0:
            amino_acid_changes += changes
        current_protein = protein_seq(mutated_sequence, codon_table)
        sequence = mutated_sequence
    for i in range(len(initial_protein)):
        if current_protein[i] != initial_protein[i]:
            amino_acid_changes += 1
    return initial_protein, amino_acid_changes

codon_table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
file_path = 'C:\\Users\\samar\\Downloads\\prj14.fasta'
header, sequence = fasta(file_path)
num_steps = 100
num_simulations = 100
amino_acid_changes_list = []
for i in range(num_simulations):
    initial_protein, num_changes = simulation(sequence, codon_table, num_steps)
    amino_acid_changes_list.append(num_changes)
    print(f"After {i + 1} steps: {num_changes} amino acid changes")
plt.plot(range(1, num_simulations + 1), amino_acid_changes_list)
plt.xlabel('Number of Steps')
plt.ylabel('Number of Amino Acid Changes')
plt.title('Amino Acid Changes vs Steps')
plt.show()


# In[ ]:




