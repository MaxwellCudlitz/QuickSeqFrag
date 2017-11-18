# QuickSeqFrag goals
QuickSeqFrag takes in a sequence of partial key candidates to a word2vec dictionary, and quickly maps them into the largest possible distinct key arrangement contained in the loaded word2vec dictionary.


Data processing; (raw) -> W2P(raw) -> W2V(wtp) --> (vec.bin) ----v
                                            `----> (dict.txt) -> BytesDawg --> DawgDict

# Technical notes
* Sequences are parsed one element at a time, and only seek to find key combinations for tokens following themselves; 
    * I.E. with dict `{ 'The', 'The_Fat', 'Fat_Cat, 'Cat' }`, QSF(`"The Fat Cat"`) => `['The_Fat', 'Cat']` 
* Internal DAWG will use a `BytesDawg`, http://dawg.readthedocs.io/en/latest/#bytesdawg, which will store 

