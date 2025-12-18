from rank_bm25 import BM25Okapi


def build_bm25(chunks):
    corpus = [c["text"].split() for c in chunks]
    bm25 = BM25Okapi(corpus)
    return bm25