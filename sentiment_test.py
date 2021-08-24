import nltk
nltk.download('vader_lexicon')
from newspaper import Article
from nltk.sentiment.vader import SentimentIntensityAnalyzer

new_words = {
    'crushes': 10,
    'beats': 5,
    'misses': -5,
    'trouble': -10,
    'falls': -100,
    'bankrupt': -100,
    'fraud': -100,
    'crime': -100,
    'prison': -100,
    'embezzlement': -100,
    'money_trail':-100,
    'jail': -100,
    'sentenced':-100,
    'forfeiture': -100,
    'ill-gotten gain':-100,
    'laundering':-100



}


vader = SentimentIntensityAnalyzer()

vader.lexicon.update(new_words)
#does not work
#url2 = "https://www.bloomberg.com/news/articles/2020-08-01/apple-buys-startup-to-turn-iphones-into-payment-terminals?srnd=premium"

#works
#url2 = "https://hbswk.hbs.edu/item/white-collar-crime-enforcement"
#works
#url2 = 'https://www.straitstimes.com/singapore/courts-crime/doing-more-to-keep-child-sex-offenders-from-making-same-mistake'

najib_news = "https://www.theedgemarkets.com/article/najib-received-massive-rm2973-billion-says-prosecution-forfeiture-hearing"

article = Article(najib_news)
article.download()
article.parse()

news_text = article.text

ss = vader.polarity_scores(news_text)

print(ss)