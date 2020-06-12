from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

"""
    returns 10 cities where population is more than 1 million
"""

sparql.setQuery("""
select * where {
    ?city rdf:type dbo:City ;
    dbo:populationTotal ?pop ;
    dbo:country ?country 
    filter($pop > 1000000) 
}
limit 10
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(result)