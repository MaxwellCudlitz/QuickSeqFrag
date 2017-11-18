from gensim.models import KeyedVectors

VEC_FILE = '../Data/Embeddings/vectors_64_window8_min50_iter4.bin'

def in_model(words, model):
    """returns true if for each word in words the model contains that key"""
    return all(word in model.vocab for word in words)

def most_similar(pos_words, neg_words, model):
    """return most similar words with the composition of positive words and negative words"""
    if in_model(pos_words, model) and in_model(neg_words, model):
        return model.most_similar(positive=pos_words, negative=neg_words)
    return [("keyerror", 0)]

def load_model():
    """Load pretrained model"""
    print("Loading model....")
    model = KeyedVectors.load_word2vec_format(VEC_FILE, binary=True)
    print("Done loading.")
    return model

def query_inputs(model):
    """query user input for words to check against the model"""
    positive_words = input("input positive words: ")
    negative_words = input("input negative words: ")
    word_vec = most_similar(positive_words.split(), negative_words.split(), model)
    for embedding in word_vec:
        print('{:20s} {:4.8f}'.format(embedding[0], embedding[1]))

def main():
    """main"""
    model = load_model()
    while True:
        query_inputs(model)

if __name__ == "__main__":
    main()
