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

Technology has made continuous improvements as storage and computing capabalites improve. With increased storage comes increased memory of data. As we all know, Data is king as it has been a biproduct since the advent of technology, but can all data be trusted? On a daily basis individuals are inundated with information from all across the internet. How can we democratize data to provide open access to all those who wish to use it and ensure its validity?   

News of The World is a step towards that direction. This app utilizises two data sets that explore known articles labeled as true or fake. We used these datasets to classify real news vs disinformation dressed up as news. There are many models that will ultimately lead us to the same conclusion, though we decided to use the Naive Bayes approach to handling our data. We performed Exploratory Data Analysis techniques to obtain an understanding of our datasets. Then using feature engineering, we selected features that would allow us to train our machine for understanding the difference between fake and real news. The result yeild a 95% accuracy but there are many aspects to be explored and with deeper analysis, this number can drop down. The way to ensure a better accuracy is to gather more news articles and build a larger data set with fake and real news. 

Using the Naive Bayes approach, we look at the word count of each dataset to determine if an article is real or fake. Other approaches involve neural networks which will be deemed as more efficient due to the model's capabilities to remember more words grouped closeley together. 

That being said, our algorithm can be used by anyone who needs to test the legitimacy of an article and know if it is a product of the fourth estate or an exercise in producing fiction. 

Ultimately we wish to combat fake news by leveraging the techniques used in machine learning and natural language processing to give our users clarity and peace of mind.

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

