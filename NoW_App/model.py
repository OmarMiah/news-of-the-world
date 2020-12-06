# Saving model
# import libraries used to develop the model

# Import pandas for data handling
import pandas as pd

# Import our text vectorizers
from sklearn.feature_extraction.text import TfidfVectorizer

# Import our classifiers
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer

# Import our metrics to evaluate our model
import os
import pickle #saves our trained model to the disk 
import requests
import json

# compiling both csvs into one 

# print("DIRECTORY: " + "Github\news-of-the-world\data\Fake.csv")

df_concat = pd.read_csv("D:\\Github\\news-of-the-world\\data\\merged_df.csv")


X = df_concat['cleaned_text'].values

y = df_concat['isfake'].values

# from sklearn.feature_extraction.text import TfidfVectorizer
# # Initialize our vectorizer
vectorizer = TfidfVectorizer()

vectorizer.fit(X)

X = vectorizer.transform(X)

model = MultinomialNB(alpha = .05)

model.fit(X,y)


pickle.dump(vectorizer, open('models/vectorizer.pkl','wb'))

pickle.dump(model, open('models/naivebayes.pkl','wb'))
# # print(X.shape, type(X))

# X_train, X_test, y_train, y_test = train_test_split(
# X, y, test_size = 0.2, random_state = 42)



# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)

# # save_classifier = open("naivebayes.pickle","wb")
# # pickle.dump(model,save_classifier) #saving our trained model to be used by the server
# # save_classifier.close()

# # pickle.load(open('model.pkl','rb'))
# # print(model.predict([[1.8]]))
# # #pickle.load will open the method and saves the deserialized bytes to model

# # y_pred_proba = model.predict_proba(X_test)



# # print("Model Accuracy: %f" % accuracy)

# # print(classification_report(y_test, y_pred, target_names=model.classes_))

# # to open 
# classifier_f = open("naivebayes.pickle","rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()

# accuracy = model.score(X_test, y_test)

# article = "trump wins at karate"

# article = text_pipeline(article)
# X = vectorizer.transform([article])
# x_pred = model.predict(X)
# print( article, '=', x_pred)