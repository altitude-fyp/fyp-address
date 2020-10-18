from helper.nlp.cosine_similarity import cosine_similarity    

def match(target, iterable):

    bestword = 0
    bestscore = 0
    
    for word in iterable:
        
        if word == target:
            return word, 1

        sim = cosine_similarity(target, word)

        if target in word or word in target:
            sim += 1

        if sim > bestscore:
            bestword, bestscore = word, sim

    return bestword, bestscore