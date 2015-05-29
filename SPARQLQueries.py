__author__ = '22208_65138'

from rdflib.graph import ConjunctiveGraph, Namespace, rdflib

def predicateCount (graph, namespace, predicate):
    ns = Namespace(namespace)
    qry = "SELECT (COUNT(pf:" + predicate + ") as ?pCount) " \
         " WHERE {" \
         "?s pf:" + predicate + " ?o ." \
         "    } "

    results = graph.query( qry, initNs={'pf':ns})
    return results

def listTypes (graph, namespace, type):
    ns = Namespace(namespace)
    qry = "SELECT ?Descricao ( Count (*) as ?count) " \
            " WHERE {" \
            " ?s pf:" + type + " ?Tipo . " \
            " ?Tipo pf:description ?Descricao ." \
            "}" \
            "GROUP BY ?Descricao " \
            "ORDER BY DESC (?count)"
    results = graph.query( qry, initNs={'pf':ns})
    return results


def accidentData (graph, namespace, accidentID):
    ns = Namespace(namespace)
    qry = 'SELECT ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal (count (?idVitima) as ?nVitimas) ' \
    'WHERE{ ' \
    '?idAcidente pf:accidentID "' + accidentID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
    '?idAcidente pf:hasAccVehicle ?idtipoVeiculo. ' \
    '?idtipoVeiculo pf:description ?descVeiculo. ' \
    '?idAcidente pf:hasAccCause ?idCausa. ' \
    '?idCausa pf:description ?descCausa. ' \
    '?idAcidente pf:happenedDuring ?idHora. ' \
    '?idHora pf:description ?descHora. ' \
    '?idAcidente pf:happenedDuring ?idHora. ' \
    '?idHora pf:description ?descHora. ' \
    '?idAcidente pf:happenedInRoadNet ?idLocal. ' \
    '?idLocal pf:description ?descLocal. ' \
    '?idAcidente pf:hasVictim ?idVitima. ' \
    '}' \
    'GROUP BY ?idAcidente ?descVeiculo ?descCausa ?descHora ?descLocal'
    results = graph.query( qry, initNs={'pf':ns})
    return results

def  victimData (graph, namespace, victimID):
    ns = Namespace(namespace)
    qry = 'SELECT ?idVitima ?descIdade ?descVeiculo ?descVitima ?idAcidente ?objAcidente ' \
        'WHERE{ ' \
        '?idVitima pf:victimID "' + victimID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
        '?idVitima pf:hasVictimAge ?idtipoIdade. ' \
        '?idtipoIdade pf:description ?descIdade. ' \
        '?idVitima pf:inVehicle ?idtipoveiculo. ' \
        '?idtipoveiculo pf:description ?descVeiculo. ' \
        '?idVitima pf:hasVictimType ?idtipoVitima. ' \
        '?idtipoVitima pf:description ?descVitima. ' \
        '?idVitima pf:involvedIn ?idAcidente. ' \
        '?idAcidente pf:accidentID ?objAcidente.'\
        '}'
    results = graph.query( qry, initNs={'pf':ns})
    return results

def accidentVictimAge (graph, namespace, accidentID):
    ns = Namespace(namespace)
    qry = 'SELECT  ?vitima ?descIdade ' \
    'WHERE{ ' \
    '?idAcidente pf:accidentID "' + accidentID + '"^^<http://www.w3.org/2001/XMLSchema#int>. ' \
    '?idAcidente pf:hasVictim ?idVitima. ' \
    '?idVitima pf:victimID ?vitima. ' \
    '?idVitima pf:hasVictimAge ?idtipoIdade. ' \
    '?idtipoIdade pf:description ?descIdade. ' \
    '}'

    results = graph.query( qry, initNs={'pf':ns})
    return results

def accidentsByType (graph, namespace, predicate, value ):
    ns = Namespace(namespace)

    qry = 'SELECT  ?acidente ' \
        'WHERE{ ' \
        '?id pf:description "' + value +'". ' \
        '?idAcidente pf:' +predicate + ' ?id . ' \
        '?idAcidente pf:accidentID ?acidente . ' \
        '}'
    results = graph.query( qry, initNs={'pf':ns})

    return results

def happenedDuring(graph, namespace):
    ns = Namespace(namespace)
    results = graph.query("""
                SELECT ?roadaccident ?happenedDuring
                WHERE{
                ?roadaccident pf:happenedDuring ?happenedDuring.
                } 
                    """, \
                          initNs={'pf':ns})
    return results

def hasVictimUnderage(graph, namespace):
    ns = Namespace(namespace)
    vt = rdflib.URIRef("http://ws_22208_65138.com/VictimType/Passenger")
    va = rdflib.URIRef("http://ws_22208_65138.com/VictimAge/Y0-17")

    results = graph.query("""
                SELECT ?accidentvictim
                WHERE{
                ?accidentvictim pf:hasVictimType <http://ws_22208_65138.com/VictimType/Passenger> .
                ?accidentvictim pf:hasVictimAge <http://ws_22208_65138.com/VictimAge/Y0-17> .
                }
                    """, initNs={'pf': ns}) # , 'victimType': vt, 'victimAge': va    "http://ws_22208_65138.com/VictimAge/Y0-17"

    return results