from gensim.models.keyedvectors import KeyedVectors

VEC_FILE_IN  = 'Data/Embeddings/vectors_150_window10_iter3.bin'
VEC_FILE_OUT = 'Data/Embeddings/vectors_150_window10_iter3.txt'

model = KeyedVectors.load_word2vec_format(VEC_FILE_IN, binary=True)
model.save_word2vec_format(VEC_FILE_OUT, binary=False)