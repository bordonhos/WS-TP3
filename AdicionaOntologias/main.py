__author__ = 'Pedro Bordonhos'
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF

import InsertOntology
#http://localhost:8080/openrdf-workbench/repositories/ws/update
#"http://localhost:8080/openrdf-sesame/repositories/ws
sesameServer = "http://localhost:8080/openrdf-sesame/repositories/ws"
sesameUpdateServer = "http://localhost:8080/openrdf-workbench/repositories/ws/update"
InsertOntology.insertOntologyRoadAccident(sesameServer,sesameUpdateServer,"http://ws_22208_65138.com/ontology#RoadAccident")
InsertOntology.insertOntologyVictim(sesameServer,sesameUpdateServer,"http://ws_22208_65138.com/ontology#Victim")

