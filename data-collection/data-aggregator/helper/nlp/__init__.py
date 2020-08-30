from helper.nlp.cosine_similarity import cosine_similarity

def clean(word):
    def clean_brackets(word):
        for i,ch in enumerate(word):
            if ch in "[{(":
                return word[:i].strip()
        return word.strip()

    def clean_space(word):
        return word.replace(" ", "_")
    
    return clean_space(clean_brackets(word))
    

def match(target, iterable):
    target = clean(target)
    bestword = 0
    bestscore = 0
    
    for word in iterable:
        
        if word in target:
            return word, 2

        sim = cosine_similarity(target, word)
        if sim > bestscore:
            bestword, bestscore = word, sim

    return bestword, bestscore