"""
This is where the user interface is made using the streamlit package.
"""

import numpy as np
import pandas as pd
import streamlit as st
import pathlib

st.title('InP Quantum Dots Synthesis Project  - Cossairt Laboratory')
st.subheader('Department of Chemistry - University of Washington')


User = st.text_input(label='0. What\'s your name?')
st.markdown('****')

st.header('Data Input')
st.markdown(
    'In this section, you will input synthetic conditions and some properties of the quantum dots.')
st.markdown(
    'First, you will need to paste the DOI of the paper you are about to use. Check if someone has already inputted that paper.')
st.markdown('****')

st.markdown('Please enter EVERYTHING in lowercase!')
st.markdown('Type "None" if the paper doesn\'t provide the information')
st.markdown('****')

DOI = st.text_input(
    label='1. Type or paste a DOI name into the text box below. E.g. 10.1000/xyz123')
st.markdown('****')

#DOI input
# Rearange users' choice into a list to input to the ML model
doi_input = [DOI, User]

doi_df = pd.DataFrame(np.array(doi_input).reshape(1, -1), columns=['DOI', 'User'])

st.write(doi_df)

DOI_LIST = 'doi_list.csv'
st.write(pd.read_csv(DOI_LIST))
if st.button('Check your DOI'):
    st.write(doi_df)
#     if pathlib.Path(DOI_LIST).exists():
#         doi_df.to_csv(DOI_LIST, mode='a', header=False)
#         st.write('This paper has already been input.')
#     else:
#         doi_df.to_csv(DOI_LIST, mode='a', header=True)
#         st.write('DOI list is updated')


# st.write(pd.read_csv(DOI_LIST))



st.markdown('****')
In_source = st.text_input(label='2. What is the indium source?')
In_amount = st.slider('3. How much In source is used? (mmol)', 0, 150, 25)
st.markdown('****')

P_source = st.text_input(label='4. What is the phosphorus source?')
P_amount = st.slider('5. How much phosphorus source is used? (mmol)', 0, 150, 25)
st.markdown('****')

Sol_1 = st.text_input(label='6. What is the first solvent?')
Sol_1_am = st.slider('7. How much of the first solvent is used? (mg)', 10, 1000, 100)
st.markdown('****')

Sol_2 = st.text_input(label='8. What is the second solvent?')
Sol_2_am = st.slider('9. How much of the second is used? (mg)', 10, 1000, 100)
st.markdown('****')

Acid_source = st.text_input(label='10. What acid is used?')
Acid_amount = st.slider('11. How much acid is used? (mmol)', 0, 150, 25)
st.markdown('****')

Amine_source = st.text_input(label='12. What amine is used?')
Amine_amount = st.slider('13. How much amine is used? (mmol)', 0, 150, 25)
st.markdown('****')

Other1 = st.text_input(label='14. Other compound 1')
Other1_amount = st.slider('15. Amount? (mmol)', 0, 130, 25)
st.markdown('****')

Other2 = st.text_input(label='16. Other compound 2')
Other2_amount = st.slider('17. Amount? (mmol)', 0, 130, 25)
st.markdown('****')

Temp = st.slider('14. What is the growth temperature? (Celcius)', 30, 400, 200)
st.markdown('****')

Time = st.text_input(label='15. What is the growth time? (minute)')
st.markdown('****')

Dia = st.slider('16. What is the reported diameter? (nm)', 0.0, 15.0, 2.0, 0.1)
Abs = st.slider('17. What is the reported absorbance max? (nm)', 400, 700, 500)
Em = st.slider('18. What is the reported emission? (nm)', 400, 700, 500)







# Creating questions with multiple choice answer
RADIO_QUESTIONS_LIST = ['What is your cadmium source?',
                        'What is your carboxylic acid source?',
                        'What is your amine source?',
                        'What is your phosphine source?',
                        'What is your first solvent?',
                        'What is your second solvent?'
                        ]
# Creating multiple choice answers for each question above
RADIO_SELECTIONS = [['cadmium stearate', 'cadmium oxide', 'dimethylcadmium',
                     'cadmium acetate', 'cadmium acetate dihydrate'],
                    ['None', 'myrstic acid', 'oleic acid', 'stearic acid',
                     'benzoic acid', 'dodecylphosphonic acid',
                     'ethylphosphonic acid', 'lauric acid'],
                    ['None', '2-6-dimethylpyridine', 'aniline', 'benzylamine',
                     'dioctylamine/hexadecylamine', 'dodecylamine',
                     'heptylamine', 'hexadecylamine', 'octadecylamine',
                     'octylamine', 'oleylamine', 'pyridine', 'trioctylamine'],
                    ['None', 'diphenylphosphine', 'tributylphosphine',
                     'trioctylphosphine', 'triphenylphosphine'],
                    ['None', 'liquid parafin', 'octadecene',
                     'phenyl ether', 'trioctylphosphine oxide'],
                    ['None', 'phosphinic acid', 'trioctylphosphine oxide']
                    ]
# Creating questions with slider
SLIDER_QUESTIONS_LIST = ['How much Cadmium do you plan to use? (mmol)',
                         'Selenium power is used; how much Selenium do you plan to use? (mmol)',
                         'How much carboxylic acid  do you plan to use? (mmol)',
                         'How much amine do you plan to use? (mmol)',
                         'How much phosphine do you plan to use? (mmol)',
                         'How much first solvent do you plan to use? (g)',
                         'How much second solvent do you plan to use? (g)',
                         'What is the growth temperature? (Degree Celsius)',
                         'How long do you plan to grow the quantum dots (minute)?'
                         ]
# Creating sliders for each question above
SLIDER_SELECTIONS = [[0.1, 14.0, 0.15, 0.001],
                     [0.001, 1.0, 0.01, 0.0001],
                     [0.0, 60.0, 10.0, 0.001],
                     [0.0, 40.0, 1.0, 0.001],
                     [0.0, 60.0, 1.0, 0.001],
                     [0.0, 60.0, 10.0, 0.1],
                     [0.0, 60.0, 10.0, 0.1],
                     [45.0, 350.0, 200.0, 1.0],
                     [0.5, 360.0, 50.0, 0.5], ]

# Initiate lists for answers
radio_answers = []
slider_answers = []


def get_radio_input(question, selection):
    """
    This function creates questions and
    multiple choice answers in the user interface.
    """
    answer = st.radio(question, selection)
    return answer


def get_slider_input(question, mmin_val, max_val, default_val, interval):
    """
    This function creates questions and
    slider answers in the user interface.
    """
    answer = st.slider(question, mmin_val, max_val, default_val, interval)
    return answer


# # Get DOI
# DOI_FILE_NAME = 'doi_list.txt'
# DEFAULT_DOI = '10.1000/xyz123\n'

# #  check if file not exist
# if not pathlib.Path(DOI_FILE_NAME).exists():
#     with open(DOI_FILE_NAME, 'w') as fp:
#         pass
# with open(DOI_FILE_NAME, 'r+') as f:
#     doi_lists = f.readlines()

# # current_doi = st.text_input(label='Type or paste a DOI name, e.g., 10.1000/xyz123, into the text box below',
# #                             value=DEFAULT_DOI,
# #                             help='Be sure to enter all of the '
# #               'characters before and after the slash. Do not include extra characters, or sentence punctuation '
# #               'marks.')

# # if current_doi != DEFAULT_DOI:
# #     current_doi += '\n'
# # st.write(doi_lists)
# # if current_doi in doi_lists and current_doi != DEFAULT_DOI:
# #     st.write(f'The paper with this DOI "{current_doi}" has already been submitted.')
# # elif current_doi != DEFAULT_DOI:
# #     with open(DOI_FILE_NAME, 'a') as f:
# #         f.write(current_doi)
# #         f.close()



# List of answers for multiple choice questions

for i in range(len(RADIO_QUESTIONS_LIST)):
    radio_answers.append(get_radio_input(
        RADIO_QUESTIONS_LIST[i], RADIO_SELECTIONS[i]))

# List of answers for slider questions
for i in range(len(SLIDER_QUESTIONS_LIST)):
    slider_answers.append(get_slider_input(
        SLIDER_QUESTIONS_LIST[i], SLIDER_SELECTIONS[i][0],
        SLIDER_SELECTIONS[i][1], SLIDER_SELECTIONS[i][2],
        SLIDER_SELECTIONS[i][3]))

# Rearange users' choice into a list to input to the ML model
user_input = [slider_answers[7], radio_answers[0], slider_answers[0], slider_answers[1],
              radio_answers[1], slider_answers[2], radio_answers[2], slider_answers[3],
              radio_answers[3], slider_answers[4], radio_answers[4], slider_answers[5],
              radio_answers[5], slider_answers[6], slider_answers[8]
              ]

# Naming each choice in the user input
user_df = pd.DataFrame(np.array(user_input).reshape(1, -1), columns=['Growth Temp (Celsius)',
                                                                     'Metal_source', 'Metal_mmol (mmol)',
                                                                     'Chalcogen_mmol (mmol)', 'Carboxylic_Acid',
                                                                     'CA_mmol (mmol)', 'Amines', 'Amines_mmol (mmol)',
                                                                     'Phosphines', 'Phosphines_mmol (mmol)',
                                                                     'Solvent I', 'S_I_amount (g)',
                                                                     'Solvent II', 'S_II_amount (g)', 'Time_min (min)'
                                                                     ])

# Print user inputs
st.write(user_df)

# Scaling and encoding user input using the raw dataset
FILE_NAME = 'InP_data.csv'
st.write('Click submit when you\'re done')
if st.button('Submit Data'):
    if pathlib.Path(FILE_NAME).exists():
        user_df.to_csv(FILE_NAME, mode='a', header=False)
    else:
        user_df.to_csv(FILE_NAME, mode='a', header=True)
    st.write('Data submitted!')

st.write(pd.read_csv(FILE_NAME))
