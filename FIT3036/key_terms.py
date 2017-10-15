import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import MiniBatchKMeans

import db_manager


def extract_email():
    dbu = db_manager.DatabaseUtility()
    messages = dbu.get_communication()

    m_from = []
    m_to = []
    m_subject = []
    m_body = []

    for i in messages:
        m_from.append(i[0])
        m_to.append(i[2])
        m_subject.append(i[3])
        m_body.append(i[4])

    return {'from': m_from,
            'to': m_to,
            'subject': m_subject,
            'body': m_body}


def top_feats_per_cluster(X, y, features, min_tfidf=0.1, top_n=25):
    dfs = []

    labels = np.unique(y)
    for label in labels:
        ids = np.where(y==label)
        feats_df = top_mean_feats(X, features, ids, min_tfidf=min_tfidf, top_n=top_n)
        feats_df.label = label
        dfs.append(feats_df)
    return dfs


def top_mean_feats(X, features, grp_ids=None, min_tfidf=0.1, top_n=25):
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

def find_key_terms():
    email_df = pd.DataFrame(extract_email())
    vect = TfidfVectorizer(analyzer='word', stop_words='english', max_df=0.3, min_df=50)

    X = vect.fit_transform(email_df.body)
    features = vect.get_feature_names()
    print(len(features                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ))

    n_clusters = 5
    clf = MiniBatchKMeans(n_clusters=n_clusters, init_size=1000, batch_size=500, max_iter=100)
    labels = clf.fit_predict(X)

    print(top_feats_per_cluster(X, labels, features, 0.1, 10))


# def term_rank(row, features, limit=20):
#     # Sort and remove rows beyond limit
#     rows = np.argsort(row)[::-1][:limit]
#     terms = [(features[i], row[i]) for i in rows]
#     data_frame = pd.DataFrame(terms, columns=['Term', 'Score'])
#     return data_frame
#
#
# def key_email_term(X, features, row_id, top_n=25):
#     row = np.squeeze(X[row_id].toarray())
#     return top_tfidf_feats(row, features, top_n)


if __name__ == '__main__':
    find_key_terms()