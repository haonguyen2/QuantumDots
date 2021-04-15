"""
This is where the user interface is made using the streamlit package.
"""
import base64
import numpy as np
import pandas as pd
import streamlit as st
import pathlib

from datetime import date

today = date.today()

#Title
st.title('InP Quantum Dots Synthesis Project  - Cossairt Laboratory')
st.header('Department of Chemistry - University of Washington')

#User's name
User = st.text_input(label='What\'s your name?')
st.markdown('****')

#Text explaining
st.subheader('Data Input')
st.markdown(
    'In this section, you will input synthetic conditions and some properties of the quantum dots.')
st.markdown('Some rules before we start:')
st.markdown('Please enter EVERYTHING in lowercase!')
st.markdown('Type "None" if the paper doesn\'t provide the information')
st.markdown('Please do not enter any information twice')
st.markdown('If there are additional important details in the paper that you do not see a place to enter, please let Hao or Florence know')
st.markdown('For numerical entries, please follow the unit in parentheses and ONLY type in the number. You may have to do some calculations')
st.markdown('****')

st.markdown(
    'First, you will need to paste the DOI of the paper you are about to use. Check if someone has already input that paper.')

#getting user's doi
DOI = st.text_input(
    label='1. Type or paste a DOI name into the text box below. E.g. 10.1000/xyz123')

#putting doi and user's name in a list then convert to a class
doi_input = [DOI, User]

doi_df = pd.DataFrame(np.array(doi_input).reshape(1, -1), columns=['DOI', 'User'])

#Check if doi exists in current doi list and deposit new doi
df = pd.read_csv('InP/doi.csv')

st.write('Your DOI:')
st.write(doi_df)
if st.button('Click here to check your DOI'):
    if (df['DOI'] == DOI).any():
        st.markdown('**This paper has already been used. Please make sure NOT to repeat entries!**')
    else:
        doi_df.to_csv('InP/doi.csv', mode='a', header=False, index=False)
        st.markdown('**DOI list is updated**')

st.write('Current DOI list:')
st.write(pd.read_csv('InP/doi.csv'))
st.markdown('****')

#Questions for synthetic conditions
st.subheader('Precursors')

In_source = st.text_input(label='2. What is the indium source? (e.g. indium acetate, indium chloride, etc.)')
In_amount = st.text_input(label='3. How much In source is used? (mmol)')
st.markdown('****')

Acid_source = st.text_input(label='4. What acid is used? (e.g. lauric acid, mystiric acid, palmitic acid, etc.)')
Acid_amount =  st.text_input(label='5. How much acid is used? (mmol)')
st.markdown('****')

P_source = st.text_input(label='6. What is the phosphorus source? (e.g. tris(trimethylsilyl)phosphine, tris(dimethylamino)phenol, etc.)')
P_amount =  st.text_input(label='7. How much phosphorus source is used? (mmol)')
st.markdown('****')

st.subheader('Solvents')

Sol_1 = st.text_input(label='8. What is the first solvent? (e.g. octadecene, trioctylphosphine, etc.)')
Sol_1_amount =  st.text_input(label='9a. How much of the first solvent is used?')
Sol_1_unit = st.text_input(label='9b. What unit? (g or mL)')
st.markdown('****')

Sol_2 = st.text_input(label='10. What is the second solvent? (e.g. octadecene, trioctylphosphine, etc.)')
Sol_2_amount =  st.text_input(label='11a. How much of the second is used?')
Sol_2_unit = st.text_input(label='11b. What unit? (g or mL)')
st.markdown('****')

st.subheader('Ligands - If this was already entered as a solvent, please do not re-enter')

Amine_source = st.text_input(label='12. What amine is used? (e.g. oleylamine, etc.)')
Amine_amount =  st.text_input(label='13. How much amine is used? (mmol)')
st.markdown('****')

st.subheader('Other reagents')

Other1 = st.text_input(label='14. Other compound 1 (e.g. zinc chloride)')
Other1_amount = st.text_input(label='15. Amount (mmol)')
st.markdown('****')

Other2 = st.text_input(label='16. Other compound 2 (e.g. zinc chloride)')
Other2_amount = st.text_input(label='17. Amount (mmol)')
st.markdown('****')

st.subheader('Conditions')

Temp =  st.text_input(label='14. What is the growth temperature? (Celsius)')

Time = st.text_input(label='15. What is the growth time? (minute)')
st.markdown('****')

#Outcomes
st.subheader('Properties')

Diameter = st.text_input(label='16. What is the reported diameter? (nm)')
Abs = st.text_input(label='17. What is the reported absorbance max? (nm)')
Emission = st.text_input(label='18. What is the reported emission? (nm)')
PLQY = st.text_input(label='19. What is the reported quantum yield? (%)')
st.markdown('****')

#Converting user's inputs to a datarow
user_input = [ User, DOI, In_source, In_amount, P_source, P_amount, Sol_1, Sol_1_amount, Sol_1_unit,
               Sol_2, Sol_2_amount, Sol_2_unit, Acid_source, Acid_amount, Amine_source,
               Amine_amount, Other1, Other1_amount, Other2, Other2_amount,
               Temp, Time, Diameter, Abs, Emission, PLQY, today
             ]

user_df = pd.DataFrame(np.array(user_input).reshape(1, -1), columns=[
        'User', 'DOI', 'In_source',	'In_amount_mmol',	'P_source',	'P_amount_mmol',
        'First_sol',	'First_sol_amount', 'First_sol_unit',	'Second_sol',	'Second_sol_amount', 'Second_sol_unit',
        'Acid',	'Acid_amount_mmol',	'Amine',	'Amine_amount_mmol',
        'Other_1',	'Other_1_amount_mmol',	'Other_2',	'Other_2_amount_mmol',
        'Temp_C',	'Time_min',	'diameter_nm',	'Abs_nm',	'Emission_nm',
        'PLQY_percentage', 'Date input'                           ])


#Print user inputs
st.write('Double-check your input, maybe?')
st.write(user_df)

#Inputing user's input to current InP csv
st.write('Click submit when you\'re done')

if st.button('Submit Data'):
    user_df.to_csv('InP/InP_data.csv', mode='a', header=False, index=False)
    st.markdown('***Data submitted!***')

st.write('Current InP data:')
st.write(pd.read_csv('InP/InP_data.csv'))
st.markdown('****')

df = pd.read_csv('InP/InP_data.csv')

csv = df.to_csv(index=False)

b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
# href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
href = f'<a href="data:file/csv;base64,{b64}" download="InP_data.csv">Download csv file</a>'
st.markdown(href, unsafe_allow_html=True)


st.write('Please let Hao know if something needs to be fixed.')
st.write('Thank you!')

st.write('Updated 04/15/2021')
