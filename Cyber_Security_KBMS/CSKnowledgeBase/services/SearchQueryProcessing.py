
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Preforms prepossessing of search_keywords and query set, compares search keywords to query content and returns a list
# of index in order of most relevant
def tf_idf(search_keys, queryset):
    tfidf_vectorizer = TfidfVectorizer()
    concat = str()
    for key in search_keys:
        concat = concat + key + " "

    # processes query results content Learns vocabulary and turns query result content into a term-document matrix
    queryset_weights = tfidf_vectorizer.fit_transform([item.content for item in queryset])
    # processes search keywords returns a term-document matrix
    search_key_weights = tfidf_vectorizer.transform([concat])

    similarity_list = cos_similarity(search_key_weights, queryset_weights)

    order_of_most_relevant = most_relevant(similarity_list, len(queryset))

    return order_of_most_relevant


# Utilizes the id_idf values for search_key and queryset documents and Compares them utilizing cosine similarity to
# measure the similarity of key words to query result content, provided if-idf vectors for query results and key_words
def cos_similarity(search_key_weights, queryset_weights):
    similarity = cosine_similarity(search_key_weights, queryset_weights)
    similarity_list = similarity[0]

    return similarity_list


def most_relevant(similarity_list, number_queries):

    most_relevant_list = []

    while number_queries > 0:
        tmp_index = np.argmax(similarity_list)
        most_relevant_list.append(tmp_index)
        similarity_list[tmp_index] = 0
        number_queries -= 1

    return most_relevant_list


def sort_by_most_relevant(queryset, index_by_order):

    new_queryset = []
    for query_index in index_by_order:
        print(query_index)
        new_queryset.append(queryset[int(query_index)])
    return new_queryset
