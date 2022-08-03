# python program to generate wordcloud

""" import all the necessary modules: 
        matplotlib (creating/manipulating visualizations),
        pandas ( data analysis & manipulation tool)
        wordcloud (generator lib)
"""
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot
import pandas
import wordcloud

# read csv file

data = pandas.read_csv(r"/home/lawi/Programming/word cloud/Youtube02-KatyPerry.csv", encoding='latin-1')

comment_words = ' '
stopwords = set(STOPWORDS)

# iterate through the CSV file

for val in data.CONTENT:
        # typecaste each value into string(str())
        val = str(val)
        
        # split the value
        tokens = val.split()
        
        # convert to lowercase 
        for i in range(len(tokens)):
                tokens[i] = tokens[i].lower()
        
        comment_words += " ".join(tokens)+ " "
        
wordcloud = WordCloud(width= 800,
                      background_color= 'white',
                      stopwords= stopwords,
                      min_font_size= 10).generate(comment_words)

# plot the wordcloud image 
plot.figure(figsize = (8,8), facecolor = None)
plot.imshow(wordcloud)
plot.axis("off")
plot.tight_layout(pad= 0)

plot.show()
                
        