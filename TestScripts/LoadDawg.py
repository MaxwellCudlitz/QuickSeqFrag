import argparse
import struct
import numpy
import dawg

BYTESDAWG = dawg.BytesDAWG()

def main():
    """main func"""

    result = parse_args()
    idir = result.i
    BYTESDAWG.load(idir)

    query_inputs()

def query_inputs():
    """input query loop"""

    words = input("input space-delimited word sequence to map to the vector space: ")
    words = words.split(" ")

    valid_words = [w for w in words if BYTESDAWG.has_keys_with_prefix(w) or BYTESDAWG.has_key(w)]
    print("valid words: {}".format(valid_words))

    lng_keys = get_longest_keys(valid_words)
    print("Maximum keys: {}".format(lng_keys))

    query_inputs()

# "kevin spacey is a rapist"
# 1.) "kevin"           - is prefix or key
# 2.) "kevin spacey"    - next word (back to (1.))
# 3.) "kevin spacey is" - is NOT prefix or key
# 4.) "kevin_spacey"    - added to dict
# 5.) "is"              - (back to (1.))
def get_longest_keys(valid_words):
    """
    takes a list of words, and finds the longest
    keys that represent that sequence that are
    in the dictionary.
    """
    lng_keys = []            # all longest keys
    lng_key = valid_words[0] # current longest key
    widx = 0                 # word index

    if len(valid_words) is 0:
        return ""
    if len(valid_words) == 1:
        return valid_words[0]

    while widx < len(valid_words) - 1:

        next_word = valid_words[widx + 1]
        tmp_lng_key = "{0}_{1}".format(lng_key, next_word)

        is_prefix = BYTESDAWG.has_keys_with_prefix(tmp_lng_key)
        is_key = BYTESDAWG.has_key(tmp_lng_key)
        term = (widx == len(valid_words) - 2)

        if is_prefix or is_key:
            lng_key = tmp_lng_key

            # if sequence is terminating, handle extraneous
            # elements of sequence.
            if term:
                lng_keys.append(lng_key)
                if not is_key:
                    lng_keys.append(next_word)

        else:
            lng_keys.append(lng_key)
            lng_key = next_word

            if term:
                lng_keys.append(next_word)

        widx = widx + 1

    return lng_keys

def parse_args():
    """return parsed arg object"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--in",
        help="library file being parsed",
        action="store",
        dest="i",
        required=True)

    res = parser.parse_args()
    return res

if __name__ == '__main__':
    main()
