from retrieval.hybrid_search import hybrid_search


def precision_at_k(test_queries, k=5):
    correct = 0
    for q in test_queries:
        results = hybrid_search(q["query"], k)
        if q["expected"] in results:
            correct += 1
    return correct / len(test_queries)