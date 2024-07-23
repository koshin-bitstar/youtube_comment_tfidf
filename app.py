import os
import google_api_interface
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from janome.tokenizer import Tokenizer

video_id = os.environ["VIDEO_ID"]
comments = google_api_interface.get_youtube_comments(video_id)
print(comments)


def tokenize(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    return " ".join([token.base_form for token in tokens if token.base_form != "*"])


tokenized_documents = [tokenize(doc) for doc in comments]

vectorizer = TfidfVectorizer()

# ドキュメントに適用してTF-IDFスコアを計算
tfidf_matrix = vectorizer.fit_transform(tokenized_documents)

# 特徴量名（単語）を取得
feature_names = vectorizer.get_feature_names_out()

# 各単語のTF-IDFスコアの合計を計算
tfidf_sum = np.sum(tfidf_matrix.toarray(), axis=0)

# 単語とその合計TF-IDFスコアのリストを作成
tfidf_scores = list(zip(feature_names, tfidf_sum))

# TF-IDFスコアが高い順にソート
tfidf_scores = sorted(tfidf_scores, key=lambda x: x[1], reverse=True)

top_n = int(os.environ["TOP_HIGHEST_SCORE_NUMBER"])
top_tfidf_scores = tfidf_scores[:top_n]

for word, score in top_tfidf_scores:
    print(f"Word: {word}, TF-IDF Score: {score:.4f}")
