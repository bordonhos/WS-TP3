__author__ = 'Pedro Bordonhos'
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF


def getOntologyTriples (sesameServer, qry):
    sparql = SPARQLWrapper(sesameServer)
    sparql.setReturnFormat(N3)
    sparql.setQuery (qry)
    results = sparql.query()
    return results

def addTriples (sesameServer, triplesList):
    sparqlUpdate = SPARQLWrapper(sesameServer)
    rows=""
    for row in triplesList:
        rows =  rows + row.decode("utf-8") #+ ";"
    #sRow = row.decode("utf-8");
    query = "insert data { " + rows + " }"
    sparqlUpdate.setQuery(query)
    sparqlUpdate.setMethod ("POST")
    sparqlUpdate.query()

def insertOntologyRoadAccident (sesameServer, sesameUpdateServer, ontology):
    qry = 'PREFIX pf: <http://xmlns.com/gah/0.1/> ' \
          'CONSTRUCT { ' \
          '?acidente <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <' + ontology + '>}' \
          'WHERE {' \
          '    OPTIONAL { ?acidente pf:accidentID ?victim.}' \
          'FILTER (bound(?victim))' \
          '}'
    results = getOntologyTriples (sesameServer, qry)
    addTriples(sesameUpdateServer, results)


def insertOntologyVictim (sesameServer, sesameUpdateServer, ontology):
    qry = 'PREFIX pf: <http://xmlns.com/gah/0.1/> ' \
          'CONSTRUCT { ' \
          '?vitima <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <' + ontology + '>}' \
            'WHERE {' \
            '    OPTIONAL { ?vitima pf:hasVictimAge ?age.}' \
            'FILTER (bound(?age))' \
            '}'
    results = getOntologyTriples (sesameServer, qry)
    addTriples(sesameUpdateServer, results)

