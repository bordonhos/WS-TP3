__author__ = 'Pedro Bordonhos'
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF

import InsertOntology
#http://localhost:8080/openrdf-workbench/repositories/ws/update
#"http://localhost:8080/openrdf-sesame/repositories/ws
sesameServer = "http://localhost:8080/openrdf-sesame/repositories/ws"
sesameUpdateServer = "http://localhost:8080/openrdf-workbench/repositories/ws/update"
InsertOntology.insertOntologyRoadAccident(sesameServer,sesameUpdateServer,"http://ws_22208_65138.com/ontology/RoadAccident")
InsertOntology.insertOntologyVictim(sesameServer,sesameUpdateServer,"http://ws_22208_65138.com/ontology/AccidentVictim")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"hasVictimType","http://ws_22208_65138.com/ontology/VictimType")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"inVehicle","http://ws_22208_65138.com/ontology/AccVehicle")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"hasVictimAge","http://ws_22208_65138.com/ontology/VictimAge")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"happenedDuring","http://ws_22208_65138.com/ontology/AccTime")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"happenedInRegion","http://ws_22208_65138.com/ontology/AccRegion")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"hasAccCause","http://ws_22208_65138.com/ontology/AccCause")
InsertOntology.insertOntologyOtherType(sesameServer,sesameUpdateServer,"hasAccType","http://ws_22208_65138.com/ontology/AccType")

