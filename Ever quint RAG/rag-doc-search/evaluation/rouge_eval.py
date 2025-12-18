from rouge_score import rouge_scorer


def rouge_score_eval(reference, generated):
    scorer = rouge_scorer.RougeScorer(['rouge1','rouge2','rougeL'])
    return scorer.score(reference, generated)