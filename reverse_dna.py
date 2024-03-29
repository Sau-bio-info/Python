# -*- coding: utf-8 -*-
"""Reverse_DNA.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uDXg_Pslfd3rxZaXGAh74WMsLwe4bA1R

Printing reverse of a given sequence.
"""

dna="ACATACATACGTCAGACATAGACAGATCGCTCGCGCAGTCCGCTCAGTCGAC"

rev_dna=dna[::-1]

print(rev_dna)

"""If the sequence is qiven as a list."""

dna2=['A','T','T','T','G','C','G','G','A']

dna2_str="".join(dna2)

#print(dna2_str)

rev_dna2=dna2_str[::-1]

print(rev_dna2)

#Using reverse of attribute
rev_dna2=dna2.reverse()
print(rev_dna2)

#rev_dna2 will not print anything because reverse changes the original list
print(dna2)

