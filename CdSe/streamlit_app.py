"""
This is where the user interface is made using the streamlit package.
"""

import joblib
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder

#Creating questions with multiple choice answer
RADIO_QUESTIONS_LIST = ['What is your cadmium source?',
                        'What is your carboxylic acid source?',
                        'What is your amine source?',
                        'What is your phosphine source?',
                        'What is your first solvent?',
                        'What is your second solvent?'
                        ]
#Creating multiple choice answers for each question above
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
#Creating questions with slider
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
#Creating sliders for each question above
SLIDER_SELECTIONS = [[0.1, 14.0, 0.15, 0.001],
                     [0.001, 1.0, 0.01, 0.0001],
                     [0.0, 60.0, 10.0, 0.001],
                     [0.0, 40.0, 1.0, 0.001],
                     [0.0, 60.0, 1.0, 0.001],
                     [0.0, 60.0, 10.0, 0.1],
                     [0.0, 60.0, 10.0, 0.1],
                     [45.0, 350.0, 200.0, 1.0],
                     [0.5, 360.0, 50.0, 0.5],]

#Initiate lists for answers
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

#List of answers for multiple choice questions
for i in range(len(RADIO_QUESTIONS_LIST)):
    radio_answers.append(get_radio_input(
        RADIO_QUESTIONS_LIST[i], RADIO_SELECTIONS[i]))

#List of answers for slider questions
for i in range(len(SLIDER_QUESTIONS_LIST)):
    slider_answers.append(get_slider_input(
        SLIDER_QUESTIONS_LIST[i], SLIDER_SELECTIONS[i][0],
        SLIDER_SELECTIONS[i][1], SLIDER_SELECTIONS[i][2],
        SLIDER_SELECTIONS[i][3]))

#Rearange users' choice into a list to input to the ML model
user_input = [slider_answers[7], radio_answers[0], slider_answers[0], slider_answers[1],
              radio_answers[1], slider_answers[2], radio_answers[2], slider_answers[3],
              radio_answers[3], slider_answers[4], radio_answers[4], slider_answers[5],
              radio_answers[5], slider_answers[6], slider_answers[8]
              ]

#Naming each choice in the user input
user_df = pd.DataFrame(np.array(user_input).reshape(1, -1), columns=['Growth Temp (Celsius)',
                                            'Metal_source', 'Metal_mmol (mmol)',
                                            'Chalcogen_mmol (mmol)', 'Carboxylic_Acid',
                                            'CA_mmol (mmol)', 'Amines', 'Amines_mmol (mmol)',
                                            'Phosphines', 'Phosphines_mmol (mmol)',
                                            'Solvent I', 'S_I_amount (g)',
                                            'Solvent II', 'S_II_amount (g)', 'Time_min (min)'
                                            ])
#Print user inputs
st.write(user_df)

#Scaling and encoding user input using the raw dataset
df = pd.read_csv('CdSe - BetterthanRaw.csv')

#Separate out initial DataFrame into the input features and output features
df_input = df.drop(columns =['Injection Temp (Celsius)', 'Metal_amount (g)',
'Metal_concentration (mmol/g)', 'Chalcogen_amount (g)', 'Chalcogen_concentration (mmol/g)',
'Metal/Se_ratio', 'CA_amount (g)', 'Cd/CA_ratio', 'Amines_amount (g)', 'Phosphines_amount (g)',
'Chalcogen/Ph_ratio','Total_amount (g)','Chalcogen_source','Diameter_nm', 'Absorbance max (nm)',
'PL max (nm)', 'Diameter from', 'Citation'],
inplace = False, axis = 1)

#Checks the column names, and ensures that they do not have any leading or trailing spaces
df_input.columns = df_input.columns.str.strip()

#Converts the values in Growth Temperature Column into float types
df_input['Growth Temp (Celsius)'] = df_input['Growth Temp (Celsius)'].astype(float)

#Initializes 2 lists to contain all of the numerical and categorical input columns
input_num_cols = [col for col in df_input.columns if df[col].dtypes !='O']
input_cat_cols = [col for col in df_input.columns if df[col].dtypes =='O']

ct = ColumnTransformer([
    ('step1', StandardScaler(), input_num_cols),
    ('step2', OneHotEncoder(sparse=False, handle_unknown='ignore'), input_cat_cols)
], remainder = 'passthrough')


ct.fit_transform(df_input)

#Use same column transformer on user input
X = ct.transform(user_df)

#Load and use ExtraTrees ML model to predict outcomes
load_Extra_Trees = joblib.load('Extra_Trees.joblib')
predicted = load_Extra_Trees.predict(X)
st.write('Predicted diameter is', predicted[0, 0], '. \n',
         ' Predicted absorbance max is', predicted[0, 1], '. \n',
         ' Predicted emission is', predicted[0, 2], '.')
