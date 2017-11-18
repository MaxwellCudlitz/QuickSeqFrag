import argparse

import struct
#import unicode
import numpy
import dawg

def main():
    """main func"""

    result = parse_args()
    idir = result.i
    odir = result.o

    # read file in
    print("opening file {}\n".format(idir))
    embs = []
    infil = open(idir, "r", encoding="utf-8")

    # format word + embedding for dawg
    for i, line in enumerate(infil):
        if i != 0:
            print("read {}".format(i), end="\r")

            # tokenize string, head word
            tok = line.split(" ")
            wrd = tok[0]

            # remainder of line must be interpreted as float
            # and packed, it is the vector embedding
            vec = tok[1:]
            vec = ",".join(vec)
            vec = numpy.fromstring(vec, dtype=float, sep=",")

            # pack buffer, append word + vec tuple to embeddings
            buf = struct.pack('%sf' % len(vec), *vec)
            tup = (wrd, buf)
            embs.append(tup)

    infil.close()

    # generate BytesDawg from data, write to outfile location
    print("\nGenerating DAWG and writing to {}".format(odir))
    bytesdawg = dawg.BytesDAWG(embs)
    with open(odir, 'wb') as outfil:
        bytesdawg.write(outfil)

def parse_args():
    """return parsed arg object"""

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-i", "--in",
        help="library file being parsed",
        action="store",
        dest="i",
        required=True)

    parser.add_argument(
        "-o", "--out",
        help="output dawg file",
        action="store",
        dest="o",
        required=True)

    res = parser.parse_args()
    return res

if __name__ == '__main__':
    main()
