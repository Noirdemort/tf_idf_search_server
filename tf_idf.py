import sys
import os
import pickle
import magic


class TfIdf:
    def __init__(self):
        self.weighted = False
        self.documents = []
        self.corpus_dict = {}

    def add_document(self, doc_name, list_of_words):
        # building a dictionary
        doc_dict = {}
        for w in list_of_words:
            doc_dict[w] = doc_dict.get(w, 0.) + 1.0
            self.corpus_dict[w] = self.corpus_dict.get(w, 0.0) + 1.0

        # normalizing the dictionary
        length = float(len(list_of_words))
        for k in doc_dict:
            doc_dict[k] = doc_dict[k] / length

        # add the normalized document to the corpus
        self.documents.append([doc_name, doc_dict])

    def similarities(self, list_of_words):
        """Returns a list of all the [docname, similarity_score] pairs relative to a
list of words.
        """

        # building the query dictionary
        query_dict = {}
        for w in list_of_words:
            query_dict[w] = query_dict.get(w, 0.0) + 1.0

        # normalizing the query
        length = float(len(list_of_words))
        for k in query_dict:
            query_dict[k] = query_dict[k] / length

        # computing the list of similarities
        sims = []
        for doc in self.documents:
            score = 0.0
            doc_dict = doc[1]
            for k in query_dict:
                if k in doc_dict:
                    score += (query_dict[k] / self.corpus_dict[k]) + (
                      doc_dict[k] / self.corpus_dict[k])
            sims.append([doc[0], score])

        return sims

    def load(self, filename):
        with open(filename + "_documents.pkl", 'rb') as f:
            self.documents = pickle.load(f)

        with open(filename + "_corpus.pkl", 'rb') as f:
            self.corpus_dict = pickle.load(f)

    def save(self, filename):
        with open(filename + "_documents.pkl", 'wb') as f:
            pickle.dump(self.documents, f)

        with open(filename + "_corpus.pkl", 'wb') as f:
            pickle.dump(self.corpus_dict, f)


TRANSFORM = ["$", "%", "^", "&", "*", "(", ")", "_", ".", "[", "]", "{", "}", "?", '\n', '\t', '=', '#', '+', '<', '>', "'", '"']

global table


def purify(k):
    for j in TRANSFORM:
        if j in k:
            k = k.replace(j, " ", k.count(j)).lower()
    return k


def create_dict():
    table = TfIdf()
    for i in os.listdir("./data_files"):
        word = i
        for j in TRANSFORM:
            if j in word:
                word = word.replace(j, " ", word.count(j)).lower()
        word_list = list(word.split(" "))
        try:
            file_type = magic.from_file("./data_files/"+i)
            if file_type in ['ASCII text', 'C source, ASCII text', 'HTML document, ASCII text', "Python script, ASCII text executable", "POSIX shell script, ASCII text executable"]:
                file = open("./data_files/"+i)
                z = []
                xx = list(file.readlines())
                for k in xx:
                    word = purify(k)
                    word1 = word.strip(" ")
                    word1 = list(set(word1.split(" ")))
                    z.extend(word1)
                z.extend(word_list)
                table.add_document(i, z)
        except Exception as e:
            print("------>", e)
            table.add_document(i, word_list)
    return table


def results(query):
    print(query)
    table = create_dict()
    zz = table.similarities(query)
    return zz