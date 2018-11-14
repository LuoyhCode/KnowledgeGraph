from sklearn.datasets import fetch_20newsgroups
news=fetch_20newsgroups(subset='all')
print(len(news.data))
print(news.data[0])