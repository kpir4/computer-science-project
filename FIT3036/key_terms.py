import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans
from sklearn.cluster import Birch

import main_actors


def extract_email():
    actors = main_actors.EnronGraph()
    messages = actors.net.connections
    actors.find_top_actors(5)

    m_from = []
    m_to = []
    m_body = []
    m_mid = set()

    for i in messages:
        if i[4] not in m_mid:
            if i[0] in actors.top_actors or i[1] in actors.top_actors:
                m_from.append(i[0])
                m_to.append(i[2])
                m_body.append(i[3])
                m_mid.add(i[4])

    return {'from': m_from,
            'to': m_to,
            'body': m_body}


def top_feats_per_cluster(X, y, features, min_tfidf, top_n):
    dfs = []

    labels = np.unique(y)
    for label in labels:
        ids = np.where(y == label)
        feats_df = top_mean_feats(X, features, ids, min_tfidf=min_tfidf, top_n=top_n)
        feats_df.label = label
        feats_df = feats_df.values
        dfs.append(feats_df)
    return dfs


def top_mean_feats(X, features, grp_ids, min_tfidf, top_n):
    if grp_ids:
        D = X[grp_ids].toarray()
    else:
        D = X.toarray()

    D[D < min_tfidf] = 0
    tfidf_means = np.mean(D, axis=0)
    return top_tfidf_feats(tfidf_means, features, top_n)


def top_tfidf_feats(row, features, top_n=20):
    topn_ids = np.argsort(row)[::-1][:top_n]
    top_feats = [(features[i], row[i]) for i in topn_ids]
    df = pd.DataFrame(top_feats, columns=['features', 'score'])
    return df


def find_key_terms(type):
    try:
        if type == "kmeans":
            terms = np.load("kmeans.npy")
            return terms
        else:
            terms = np.load("birch.npy")
            return terms
    except:
        email_df = pd.DataFrame(extract_email())
        vect = TfidfVectorizer(analyzer='word', stop_words='english', max_df=0.3, min_df=15)

        X = vect.fit_transform(email_df.body)
        features = vect.get_feature_names()

        n_clusters = 5

        if type == "kmeans":
            clf = MiniBatchKMeans(n_clusters=n_clusters, init_size=1000, batch_size=500, max_iter=100)
        else:
            clf = Birch()
        labels = clf.fit_predict(X)

        terms = top_feats_per_cluster(X, labels, features, 0.1, 10)
        np.save(type, terms)

        return terms


if __name__ == '__main__':
    print(find_key_terms("kmeans"))
