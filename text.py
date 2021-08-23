from newspaper import Article

#works
url = 'https://www.theguardian.com/us-news/2021/aug/23/mark-sanford-republican-anti-trump'

url2 = 'https://www.straitstimes.com/singapore/courts-crime/doing-more-to-keep-child-sex-offenders-from-making-same-mistake'
article = Article(url2)
article.download()
article.parse()


print(article.text)
#print(article.keywords)