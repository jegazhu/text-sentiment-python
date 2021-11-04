from textblob import TextBlob
from newspaper import Article
import nltk

nltk.download('punkt')
url = 'https://www.amazon.com/product-reviews/B099VMT8VZ/ref=cm_cr_arp_d_viewpnt_rgt?ie=UTF8&filterByStar=critical&reviewerType=all_reviews&pageNumber=1#reviews-filter-bar'
article = Article(url)

article.download()
article.parse()
article.nlp()

text = article.summary
print(text)

blob = TextBlob(text)
sentiment = blob.sentiment.polarity
print(sentiment)