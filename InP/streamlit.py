  
"""
This is where the user interface is made using the streamlit package.
"""

import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder


st.title('InP Quantum Dots Synthesis  - Cossairt Laboratory')

st.header('Predicting Properties of InP Quantum Dots')

st.markdown('****')
st.write('Answer the questions below about your InP quandum dots synthesis and we will predict the diameter, absorbance max, and emission wavelength of your dots.')
st.markdown('****')



# Creating indium question

In = st.radio(
                "What is the indium source?",
                ('indium acetate', 
                'indium bromide', 
                'indium chloride', 'indium iodide',
                'indium myristate, 'chloroindium oxalate', 
                'indium oxalate', 'indium palmitate', 
                'indium trifluoroacetate'))

In_amount = st.number_input(label='How much In source is used in mmol? (mmol)', value=0.00)
st.markdown('****')


# Creating phosphorus question

P = st.radio(
                "What is the phosphorus source?",
                ('tris(trimethylsilyl)phosphine - P(TMS)3',
                'tris(dimethylamino)phosphine - P(NMe2)3',
                'tris(diethylamino)phosphine - P(NEt2)3',
                'bis(trimethylsilyl)phosphine'
                'phosphine gas',
                'phosphorus trichloride',
                'white phosphorus',
                'sodium phosphide',))

P_amount = st.number_input(label='How much P source is used in mmol? (mmol)', value=0.00)
st.markdown('****')



# Creating solvent question
sol = st.radio(
                "What is the non-coordinating solvent?",
                ('None',
                'octadecene - ODE',
                'toluene',
                'mesitylene'
                'dimethylformamide - DMF',))

sol_amount = st.number_input(label='How much noncoordinating solvent is used in mL? (mL)', value=0.00)
if sol = 'None':
    sol_amount = 0.00

# Creating TOP question

TOP = st.radio(
                "Do you add trioctylphosphine?",
                ('No',
                'Yes',))

TOP_amount = st.number_input(label='If yes, how much? (mL)', value=0.00)
if TOP = 'No':
    TOP = "None"
    TOP_amount = 0.00


st.markdown('****')


# Creating acid question
acid = st.radio(
                "Do you add any acid?",
                ('None',
                'stearic acid',
                'myristic acid',
                'oleic acid'
                'palmitic acid',))

acid_amount = st.number_input(label='How much acid is used in mmol? (mmol)', value=0.00)

if acid = 'None':
    acid_amount = 0.00
st.markdown('****')

# Creating amine question
amine = st.radio(
                "Do you add any amine?",
                ('None',
                'octylamine',
                'hexadecylamine',
                'dioctylamine'))

amine_amount = st.number_input(label='7. How much amine is used in mmol? (mmol)', value=0.00)
if amine = 'None':
    amine_amount = 0.00
st.markdown('****')

# Creating thiol question
thiol = st.radio(
                "Do you add any thiol?",
                ('None',
                'dodecanethiol'))

thiol_amount = st.number_input(label='How much thiol is used? (mmol)', value=0.00)
if thiol = 'None':
    thiol_amount = 0.00
st.markdown('****')


# Creating zinc question
zinc = st.radio(
                "Do you add any zinc?",
                ('None',
                'zinc chloride',
                'zinc bromide',
                'zinc iodide',
                'zinc acetate',
                'zinc octanoate',
                'zinc oleate',
                'zinc stearate',
                'zinc undecylenate'))

zinc_amount = st.number_input(label='How much zinc is used? (mmol)', value=0.00)
if thiol = 'None':
    thiol_amount = 0.00
st.markdown('****')

# Other
other = st.radio(
                "Do you add any other compound?",
                ('None',
                'trioctylphosphine oxide',
                'superhydride',
                'copper bromide'))

other_amount = st.number_input(label='How much in mmol? (mmol)', value=0.00)
if other = 'None':
    other_amount = 0.00
st.markdown('****')

# Reaction volume
vol = st.number_input(label='What is the total volume of the reaction? (mL)', value=0.00)
temp = st.number_input(label='What is the nucleation temperature? (C)', value=0.00)
time = st.number_input(label='What is the reaction time (min)?', value=0.0)




#Rearange users' choice into a list to input to the ML model
user_input = [ In, In_amount, P, P_amount, sol, sol_amount, 
               TOP, TOP_amount, acid, acid_amount, 
               amine, amine_amount, thiol, thiol_amount,
               zinc, zinc_amount, other, other_amount, 
               vol, temp, time
              ]

#Naming each choice in the user input
user_df = pd.DataFrame(np.array(user_input).reshape(1, -1), columns=['in_source',
                                                                	'in_amount_mmol',
                                                                    'p_source',
                                                                    'p_amount_mmol',
                                                                    'sol',
                                                                    'sol_amount_ml',
                                                                    'TOP',
                                                                    'TOP_amount_mmol',
                                                                    'acid',
                                                                    'acid_amount_mmol',
                                                                    'amine',
                                                                    'amine_amount_mmol',
                                                                    'thiol',
                                                                    'thiol_amount_mmol',
                                                                    'zinc',
                                                                    'zinc_amount_mmol',
                                                                    'other',
                                                                    'other_amount_mmol',
                                                                    'total_volume_ml',
                                                                    'temp_c',
                                                                    'time_min'             ])
#Print user inputs
st.write(user_df)

#Scaling and encoding user input using the raw dataset
df = pd.read_csv('CdSe/CdSe_BetterthanRaw.csv')





st.subheader('Updated 09/06/2021')
st.write('Contact: haon02@uw.edu')