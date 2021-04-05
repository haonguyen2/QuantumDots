"""Nose tests for user interface main.py module"""

from itertools import chain

import numpy as np
import pandas as pd

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
                         'How long do you plan to grow the quantum dots (min)?'
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
radio_answers = ['cadmium oxide', 'oleic acid', 'None', 'None', 'None', 'phenyl ether']
slider_answers = [50, 1, 1, 1, 1, 1, 1, 1, 50]


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

def test_answers1():
    """number of answers must equal number of questions"""
    assert len(user_input)==len(RADIO_QUESTIONS_LIST)+len(SLIDER_QUESTIONS_LIST), (
    "User has missed a question!")

def test_answers2():
    """all values must be positive"""
    assert all(i >= 0 for i in slider_answers) is True, (
    "All numerical answers must be positive!")

def test_answers3():
    """all selected answers must come from given options"""
    assert all(ans in chain(*RADIO_SELECTIONS) for ans in radio_answers) is True, (
    "At least one selection is wrong")

def test_answers4():
    """Time must be less than 350 seconds"""
    assert 0<slider_answers[7]<350, "Overcooked!"

def test_answers5():
    """temp must be between 44 and 360C"""
    assert 44<slider_answers[8]<360, "Temperature is too high or too low"

def test_answers6():
    """user must use cadmium and selenium to make CdSe quantum dots"""
    assert slider_answers[0]>0 and slider_answers[1]>0, (
    "User needs cadmium and selenium to make CdSe!")
