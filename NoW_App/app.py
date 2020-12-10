import flask
import os
import pickle
import pandas as pd
import skimage
import re
import nltk 
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import gensim
from gensim.utils import simple_preprocess 
from gensim.parsing.preprocessing import STOPWORDS
from tensorflow.keras.preprocessing.text import one_hot, Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Embedding, Input, LSTM, Conv1D, MaxPool1D, Bidirectional
from tensorflow.keras.models import Model


def to_lower(document): 
    return document.lower()

def remove_punctuation(document):    
    document = re.sub(r'[^\w\s]','',document)
    return document

# def remove_stopword(string):
#     words = word_tokenize(string)
#     accepted_bag = []
#     for element in words:
#         if element not in stopwords:
#             accepted_bag.append(element)
            
#     string = ' '.join(accepted_bag)
    
#     return string

def text_pipeline(input_string):
    input_string = to_lower(input_string)
    input_string = remove_punctuation(input_string)
#     input_string = remove_stopword(input_string)
    return input_string

app = flask.Flask(__name__, template_folder='templates')

path_to_vectorizer = 'models/vectorizer.pkl'
path_to_text_classifier = 'models/naivebayes.pkl'
# path_to_image_classifier = 'models/image-classifier.pkl'

with open(path_to_vectorizer, 'rb') as f:
    vectorizer = pickle.load(f)

with open(path_to_text_classifier, 'rb') as f:
    model = pickle.load(f)

# with open(path_to_image_classifier, 'rb') as f:
#     image_classifier = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))


    if flask.request.method == 'POST':
        # Get the input from the user.
        user_input_text = flask.request.form['user_input_text']

        cleaned_input = text_pipeline(user_input_text)

        # Turn the text into numbers using our vectorizer
        X = vectorizer.transform([cleaned_input])
        
        # Make a prediction 
        x_pred = model.predict(X)
        
        # Get the first and only value of the prediction.
        prediction = x_pred[0]

        # Get the predicted probabs
        predicted_probas = model.predict_proba(X)

        # Get the value of the first, and only, predicted proba.
        predicted_proba = predicted_probas[0]

        # The first element in the predicted probabs is % democrat
        percent_true = predicted_proba[0]

        # The second elemnt in predicted probas is % republican
        percent_fake= predicted_proba[1]

        return flask.render_template('main.html', 
            input_text=user_input_text,
            result=prediction,
            percent_fake=percent_fake,
            percent_true=percent_true)


@app.route('/input_values/', methods=['GET', 'POST'])
def input_values():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('input_values.html'))

    if flask.request.method == 'POST':
        # Get the input from the user.
        var_one = flask.request.form['input_variable_one']
        var_two = flask.request.form['another-input-variable']
        var_three = flask.request.form['third-input-variable']

        list_of_inputs = [var_one, var_two, var_three]

        return(flask.render_template('input_values.html', 
            returned_var_one=var_one,
            returned_var_two=var_two,
            returned_var_three=var_three,
            returned_list=list_of_inputs))

    return(flask.render_template('input_values.html'))


@app.route('/images/')
def images():
    return flask.render_template('images.html')


@app.route('/bootstrap/')
def bootstrap():
    return flask.render_template('bootstrap.html')

if __name__ == '__main__':
    app.run(debug=True)