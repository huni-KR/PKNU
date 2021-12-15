from wordcloud import WordCloud, STOPWORDS
import wikipediaapi
import matplotlib.pyplot as plt

wiki = wikipediaapi.Wikipedia('en')
page = wiki.page('UNESCO')

STOPWORDS.union('work', 'literature', 'call',
                'October', 'State', 'de', 'General')

wordcloud = WordCloud(font_path='font/NanumGothic.ttf',
                      stopwords=STOPWORDS, width=2000, height=2000).generate(page.summary)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud)
plt.show()
