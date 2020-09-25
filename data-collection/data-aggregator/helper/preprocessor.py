def preprocess(embeddings):
    """
    1. Makes sure all countries have the same fields
    2. removes features where more than 50% of values are null
    3. fills in rest of null values with average of non-null feature values
    """

    def clean_null(embeddings, threshold=0.5):
        """
        removes features with less than threshold percentage of number values 
        """

        def standardize(embeddings):
            """
            ensures all countries have same features
                - for missing features, add null as value
            """

            features = set()
            for cname, cdata in embeddings.items():
                for k,v in cdata.items():
                    features.add(k)
            
            for cname, cdata in embeddings.items():
                for feature in features:
                    if feature not in cdata:
                        cdata[feature] = None
                
                assert len(cdata) == len(features)

            return embeddings, features

        def get_null_report(embeddings, features):
            """
            returns report on percentage of null values for features in embeddings
            """

            out = {f:{"number":0, "non-number":0} for f in features}
            
            for cname, cdata in embeddings.items():
                for k, v in cdata.items():
                    if type(v) in [int, float]:
                        out[k]["number"] += 1
                    else:
                        out[k]["non-number"] += 1
            
            return out

        embeddings, features = standardize(embeddings)
        null_report = get_null_report(embeddings, features)

        purge = []
        for fname, report in null_report.items():
            number = report["number"]
            nonnumber = report["non-number"]
            proportion = number / (number + nonnumber)

            if proportion < threshold:
                purge.append(fname)

        for cname, cdata in embeddings.items():
            for fname in purge:
                del cdata[fname]

        return embeddings

    def fill_null(embeddings):
        """
        fill null values with average values
        """

        def get_averages(embeddings):
            """
            gets averages of each feature
            """

            out = {}
            for cname, cdata in embeddings.items():
                for k,v in cdata.items():

                    if k not in out:
                        out[k] = []

                    if type(v) in [float, int]:
                        out[k].append(v)
            
            out = {k:sum(v)/len(v) for k,v in out.items()}
            return out

        averages = get_averages(embeddings)

        for cname, cdata in embeddings.items():
            for k, v in cdata.items():
                
                if type(v) not in [float, int]:
                    cdata[k] = averages[k]

        return embeddings

    embeddings = clean_null(embeddings)
    embeddings = fill_null(embeddings)

    return embeddings


def check_preprocess(data):
    """
    asserts that 
        1. every field in every country is the same
        2. no null values at all
    """

    fields = None
    for cname, cdata in data.items():
        fields = tuple(sorted(list(cdata.keys())))
        break

    for cname, cdata in data.items():
        assert tuple(sorted(list(cdata.keys()))) == fields

        for k,v in cdata.items():
            assert type(v) in [float, int]