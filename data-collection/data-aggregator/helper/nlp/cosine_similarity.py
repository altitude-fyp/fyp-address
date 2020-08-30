def cosine_similarity(a, b):
    """
    input: 2 words
    output: cosine similarity between 2 words
    """
    a, b = a.lower(), b.lower()

    def vectorize(word):
        """
        input: word
        output: vector representation of word
            - unigram and bigram vectors and frequencies
            - eg. apple --> {a:1, p:2, l:1, e:1, ap:1, pp:1, pl:1, le:1}
        """
        out = {}
        for ch in word:
            if ch not in out: out[ch] = 1
            else: out[ch] += 1

        for i in range(len(word)-1):
            bigram = word[i:i+2]

            if bigram not in out: out[bigram] = 1
            else: out[bigram] += 1
        
        return out

    def standardize_vectors(a,b):
        """
        input: vectors a and b
        output: vectors a and b, but standardized
        """

        for k in list(a.keys()) + list(b.keys()):
            if k not in a: a[k] = 0
            if k not in b: b[k] = 0
        
        assert len(a) == len(b)
        return a, b

    def dot(a, b):
        """
        input: standardized vectors a and b (assume keys are the same)
        output: dot product of a and b
        """
        out = 0
        for k in a:
            out += a[k] * b[k]
        return out

    def magnitude(a):
        """
        input: vector a
        output: magnitude of vector
        """
        return sum([i**2 for i in a.values()])**0.5


    a, b = vectorize(a), vectorize(b)
    a, b = standardize_vectors(a, b)

    dot_ab = dot(a,b)
    a, b = magnitude(a), magnitude(b)

    return dot_ab / a / b if 0 not in [a,b] else 0