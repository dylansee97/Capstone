from newspaper import Article
import pandas as pd
import numpy as np
from tqdm import tqdm
from keras.preprocessing.text import Tokenizer
tqdm.pandas(desc="progress-bar")
from gensim.models import Doc2Vec
from sklearn import utils
from sklearn.model_selection import train_test_split
from keras.preprocessing.sequence import pad_sequences
import gensim
from sklearn.linear_model import LogisticRegression
from gensim.models.doc2vec import TaggedDocument
import re
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#works
url = 'https://www.theguardian.com/us-news/2021/aug/23/mark-sanford-republican-anti-trump'

#dont work
url2 = "https://www.bloomberg.com/news/articles/2020-08-01/apple-buys-startup-to-turn-iphones-into-payment-terminals?srnd=premium"
#url2 = 'https://www.straitstimes.com/singapore/courts-crime/doing-more-to-keep-child-sex-offenders-from-making-same-mistake'




article = Article(url)
article.download()
article.parse()



#print(article.keywords)sdadsaddsadsdassaddas

print(article.text)
