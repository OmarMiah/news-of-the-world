# New of The World
> An App towards combating the spread of misinformation with Machine Learning and data.

## Table of Contents
* [Introduction](#Introduction)
* [Technology](#Technology)
* [Dependencies](#Dependencies)
* [Getting Started](#Getting-started)
* [Training](#Training)
* [Results](#Training)
* [Extra Resources](#Extra-Resources)
* [Credits](#Credits)

## Introduction

The internet power comes from the ease of access to thousands of sources of information. It’s the reason the 21st century will be clonality know as the information age. But what happens when a source of information is not true. We know that no central authority can or should police the internet, and so the responsibility of the user to verify incoming data. Many people unfortunately don’t have the time, skills or recourses to do proper source verification. To assist everyday humans, we built News of the World, Because the truth needs an algorithm. 

How does News of the World work? Our algorithm uses two data sets. the data sets are separated by their main classification, one set is filled with fake news articles and the other with true news articles. All the articles have been verified for their accuracy or lack thereof. The model we are using to predict if inputted information is true or not is by using Naive Bayes. With the Naive Bayes approach the word count of the submitted article is compares to the unique word count of articles we have in our data sets. If unique words match words in fake articles it is predicted to be fake and the same process is used for the truth. 

For the future we plan on using more complex models but as a first-time approach to this problem we usaed Naive Bayes as a prof of concept to solve the problem straight on. In addition, we would like to add a sentiment analysis that will match up an article with a known publication. This can provide more in site about the writing as all publications have a different approach to writing the news. 

News of the world has one simple message, nothing is more important to a democracy then a well-informed electorate. It is clear, the truth needs an algorithm. 

## Technology 

> Demo video explaining how to use this app (insert_link_here) 

* Jupyter Notebook
  * https://jupyter.org/
* Flask
  * https://flask.palletsprojects.com/en/1.1.x/
* Visual Studio Code
  * https://code.visualstudio.com/
* Github
  * https://github.com/

## Dependencies
> List of project dependencies

* pandas
* nltk
  * word_tokenize()
  * stopwords()
* pickle
* sklearn.naive_bayes
  * MultinomialNB()
* sklearn.metrics
  * classification_report()
* sklearn.feature_extraction.text
  * TfidVectorizer()

## Getting Started
> Get this code running on your machine

1. Fork this project to a local repository on your machine 
2. Make sure to install all the programs found in [technology](#Technology)
3. Open up the jupter notebook and play with the model
4. You can build the app by opening a terminal in the folder and typing the following command: 
   > ./app.py

## Extra Resources
> Extra reading on this topic (updated as often as possible)
* Examples of Vectorizers: https://towardsdatascience.com/a-complete-exploratory-data-analysis-and-visualization-for-text-data-29fb1b96fb6a
* TechTalks GPT-3: https://bdtechtalks.com/2020/08/17/openai-gpt-3-commercial-ai/

## Credits
A special thanks to the CUNY Tech Prep staff for guiding us on our journey in becoming better Data Scientist.

