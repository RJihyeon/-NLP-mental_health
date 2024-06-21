import nltk
from nltk.collocations import *
from nltk.tokenize import RegexpTokenizer
import pandas as pd

df = pd.read_csv('preprocessed_done.csv')

# Assuming df['cleaned_content'] contains the preprocessed reviews
tokenizer = RegexpTokenizer(r'\w+')

# Tokenize each review and convert to lowercase
df['tokens'] = df['preprocessed'].apply(lambda x: tokenizer.tokenize(x.lower()))

from gensim.models.ldamodel import LdaModel
from gensim.models.callbacks import CoherenceMetric
from gensim import corpora
from gensim.models.callbacks import PerplexityMetric

import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


# 사전 생성 및 코퍼스 준비
# 사전 생성
dictionary = corpora.Dictionary(df['tokens'])

# 코퍼스 생성
corpus = [dictionary.doc2bow(text) for text in df['tokens']]

num_topics = 3
chunksize = 2000
passes = 20
iterations = 400
eval_every = None

temp = dictionary[0]
id2word = dictionary.id2token

model = LdaModel(
    corpus=corpus,
    id2word=id2word,
    chunksize=chunksize,
    alpha='auto',
    eta='auto',
    iterations=iterations,
    num_topics=num_topics,
    passes=passes,
    eval_every=eval_every
)

top_topics = model.top_topics(corpus) #, num_words=20)

# Average topic coherence is the sum of topic coherences of all topics, divided by the number of topics.
avg_topic_coherence = sum([t[1] for t in top_topics]) / num_topics
print('Average topic coherence: %.4f.' % avg_topic_coherence)

from pprint import pprint
pprint(top_topics)

import pickle
import pyLDAvis.gensim_models as gensimvis
import pyLDAvis
from gensim.models.coherencemodel import CoherenceModel
import matplotlib.pyplot as plt

lda_visualization = gensimvis.prepare(model, corpus, dictionary, sort_topics=False)
pyLDAvis.save_html(lda_visualization, 'display_topics.html')
