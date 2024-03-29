# -*- coding: utf-8 -*-
"""web_app_count_nucleotides.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1KV2FAmpFIJ_voUBKrbOnnJMEo3sxtb_B
"""

! pip install streamlit

import streamlit as st
import pandas as pd
from PIL import Image
import altair as alt

# Commented out IPython magic to ensure Python compatibility.
# %pwd

"""Code to open logo of the web app, and title below it."""

image_point= Image.open('logo.jpg')

st.image(image_point, use_column_width=True)

st.write("""
# DNA nucleotide count web app
Input your query sequence and get count of each nucelotide in the sequence
***
"""
)

"""Code to generate test box that will accept query sequence."""

# generates header
st.header("Enter DNA sequence")

#Generate the text box

sequence=st.text_area("Sequence input",height=250)

#Spliting the sequence and its information

sequence=sequence.splitlines()

#Excluding the initial name of the organism and only considering nucleotides by slicing the list

sequence=sequence[1:]

#combining the list of nucleotides into one string.


sequence=''.join(sequence)

# print the processed query sequence.

st.header("INPUT (DNA)QUERY)")

sequence

#Printing DNA nucleotide count


st.header("Output nucleotide count")

st.subheader("Printing as dictionary")

st.subheader('1. Print dictionary')
def DNA_nucleotide_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d

X = DNA_nucleotide_count(sequence)

st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

st.write('There are ' + str(X['A']) + "adenine(A)")
st.write('There are ' + str(X['T']) + "Thymine (T)")
st.write('There are ' + str(X['G']) + "Guanine (G)")
st.write('There are ' + str(X['C']) + "adenine(C)")

"""Displaying it as dataframe."""

st.subheader("3. Display dataframe")

df=pd.DataFrame.from_dict(X, orient='index')

df=df.rename({0:'Count'}, axis='columns')

df.reset_index(inplace=True)

df=df.rename(columns={'index':'nucleotides'})

st.write(df)



"""Displaying as chart"""

st.subheader("4. Display bar chart")

p= alt.Chart(df).mark_bar().encode(
    x='nucleotides',
    y='Count'
)

p=p.properties(width=alt.Step(80)
                                
                                )

st.write(p)

