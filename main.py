__author__ = '22208_65138'

import grafo
import Accident
import Victim
import ExtractGraph
import inferencerules
import rdflib
import converter
import SPARQLQueries
#import pySesame
from SPARQLWrapper import SPARQLWrapper, JSON, XML, N3, RDF
from rdflib import ConjunctiveGraph, Namespace, Literal


sesameServer = "http://localhost:8080/openrdf-sesame/repositories/ws"
sesameUpdateServer = "http://localhost:8080/openrdf-workbench/repositories/ws/update"

flag = True
_graph = ConjunctiveGraph()

def isFileLoaded():
    #if len(_graph) == 0:
    #    print ('O gráfico ainda não foi carregado')
    #    return False
    return True

sparql = SPARQLWrapper(sesameServer)
while flag:
    print('\n --=== MENU ===--')
    print('1 - Configurar Repositório Sesame') #Carraga o ficheiro
    print('2 - Dados Gerais') #informação geral sobre os dados
    print('3 - Procurar Acidente/Vitima') # pesquisar dados de determinado acidente
    print('4 - Consultas') #algumas consultas sobre os dados
    print('5 - Aplicar Inferências')
    print('X - Terminar')
    n = input('Opção: ')
    if n.strip().upper() == 'X':
        flag = False
    if n.strip() == '1':
        print("Por favor indique o url do repositório:")
        sesameServer = input("[" + sesameServer+ "]")
        sparql = SPARQLWrapper(sesameServer)
        try:
            #vamos testar o repositorio com os nossos dados.
            results = SPARQLQueries.owlClassCount (sparql,"http://ws_22208_65138.com/ontology/RoadAccident")
            print("url do repositorio definido para: " + sesameServer)
        except:
            print("url do repositório inválido")

    if n.strip() == '2':
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Listar ===--')
            print('1 - Número Total de Acidentes')
            print('2 - Número de Vitimas')
            print('3 - Tipos de Acidentes')
            print('4 - Causas de Acidentes')
            print('5 - Faixas etárias')
            print('X - Menu anterior')
            key = input('Opção')
            if key == '1':
                results = SPARQLQueries.owlClassCount (sparql,"http://ws_22208_65138.com/ontology/RoadAccident")
                for result in results["results"]["bindings"]:
                    acc = result["pCount"]["value"]
                print ('Existiram ' + str(acc) + ' acidentes');
            if key == '2':
                results = SPARQLQueries.owlClassCount (sparql,"http://ws_22208_65138.com/ontology/AccidentVictim")
                for result in results["results"]["bindings"]:
                    acc = result["pCount"]["value"]
                print ('Existiram ' + str(acc) + ' Vitimas');
            if key == '3':
                results = SPARQLQueries.listTypes (sparql,"http://xmlns.com/gah/0.1/", "http://ws_22208_65138.com/ontology/AccType")
                print ("Os tipos de acidentes que existem são:")
                print ("Tipo de acidente  --> Número de acidentes")
                print ("-------------------------------------------")
                for r in results['results']['bindings']:
                    print (r['Descricao']['value']+" --> " + r['count']['value'])
            if key == '4':
                results = SPARQLQueries.listTypes (sparql,"http://xmlns.com/gah/0.1/", "http://ws_22208_65138.com/ontology/AccCause")
                print ("As causas de acidentes existentes são:")
                print ("Causas de acidente  --> Número de acidentes")
                print ("-------------------------------------------")

                for r in results['results']['bindings']:
                    print (r['Descricao']['value']+" --> " + r['count']['value'])
            if key == '5':
                results = SPARQLQueries.listTypes (sparql,"http://xmlns.com/gah/0.1/", "http://ws_22208_65138.com/ontology/VictimAge")
                print ("Faixa etária das vitimas --> Número de Vitimas")
                print ("-------------------------------------------")
                for r in results['results']['bindings']:
                    print (r['Descricao']['value']+" --> " + r['count']['value'])
    if n.strip() == '3':
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Pesquisar ===--')
            print('1 - Acidente')
            print('2 - Vitima')
            print('X - Voltar')
            key = input('Opção: ')
            if key == '1':
                id = input ("Introduza o id do Acidente: ")
                acc = Accident.Accident()
                acc.Data(sparql,id)
            if key == '2':
                id = input ("Introduza o id da Vitima: ")
                acc = Victim.Victim()
                acc.Data(sparql,id)
    if n.strip() == '4':
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Consultar ===--')
            print('1 - Idade das vitimas de um acidente')
            print('2 - Acidentes por Causa')
            print('3 - Vitimas envolvidas em acidentes com determinados veiculos')
            print('4 - Condutores menores de idade')
            print('X - Menu anterior')
            key = input('Opção')

            if key == '1':
                acc = input ("Introduza o id do acidente")
                results = SPARQLQueries.accidentVictimAge(sparql,"http://xmlns.com/gah/0.1/", acc)
                if len (results['results']['bindings']) == 0:
                    print ("Acidente não encontrado")
                else:
                    print ("Esse acidente teve " + str (len (results['results']['bindings'])) + " vitimas:")
                    for c in results['results']['bindings']:
                        print ("A vitima " +c["vitima"]['value'] + " na faixa etária " +  c["descIdade"]['value'])

            if key == '2':
                results = SPARQLQueries.listTypes (sparql,"http://xmlns.com/gah/0.1/", "http://ws_22208_65138.com/ontology/AccCause")
                i=1
                for r in results['results']['bindings']:
                    print ("[" + str (i)+ "]: " + r["Descricao"]["value"])
                    i = i + 1

                acc = input ("Introduza o número correspondente à Causa pretendida:")
                results = SPARQLQueries.accidentsByType(sparql,"http://xmlns.com/gah/0.1/","hasAccCause", results['results']['bindings'][int(acc)-1]["Descricao"]["value"])
                print ("Existem " + str (len (results['results']['bindings'])) + " acidentes")
                if input ("Deseja listar os acidentes (S/N)?").upper() == "S":
                    acc = Accident.Accident()
                    for r in results['results']['bindings']:
                        acc.Data(sparql,r["acidente"]["value"])

            if key == '3':
                results = SPARQLQueries.listTypes (sparql,"http://xmlns.com/gah/0.1/", "http://ws_22208_65138.com/ontology/AccVehicle")
                i=1
                for r in results['results']['bindings']:
                    print ("[" + str (i)+ "]: " + r["Descricao"]["value"])
                    i = i + 1

                vit = input ("Introduza o número correspondente ao veiculo pretendido:")
                results = SPARQLQueries.accidentsByType(sparql,"http://xmlns.com/gah/0.1/","hasAccVehicle", results['results']['bindings'][int(vit)-1]["Descricao"]["value"])
                print ("Existem " + str(len(results['results']['bindings'])) + " vitimas")
                if input ("Deseja listar as vitimas (S/N)?").upper() == "S":
                    vit = Victim.Victim()
                    for r in results['results']['bindings']:
                        vit.Data(sparql,r["acidente"]["value"])

            if key == '4':
                list = g.query ([( "?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge","http://crashmap.okfn.gr/data/accidents/VictimAge/Y0-17"),
                                 ("?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimType", "http://crashmap.okfn.gr/data/accidents/VictimType/Driver")
                ])
                print ("Foram encontrados "  + str (len(list)) + " vitimas.")
                listaRegistos (list,"vitimas", "subacidente")
    if n.strip() == '5':
        dayTimeRule = inferencerules.DayTime()
        underageRule = inferencerules.UnderagePassenger()
        key = 'Z';
        while key.upper() != 'X':
            print('\n --=== Aplicar Inferências ===--')
            print('1 - Altura do dia em que ocorreu o acidente')
            print('2 - Vitimas menores de idade (passageiros)')
            print('X - Menu anterior')
            key = input('Opção')
            if key == '1':
                rule = dayTimeRule
                queries = rule.getqueries()
                #bindings = []
                bindings = SPARQLQueries.happenedDuring(_graph,"http://xmlns.com/gah/0.1/")
                for s,o in bindings:
                    new_triples = rule.maketriples(s,o)
                    for s, p, o in new_triples:
                        ns = Namespace("http://xmlns.com/gah/0.1/")
                        triple = (s, ns["DayTime"], Literal(o))
                        _graph.add(triple)
                print(str(len(bindings)) + ' inferências aplicadas!')

                #_graph.add(dayTimeRule)
            elif key == '2':
                rule = underageRule
                queries = rule.getqueries()
                #bindings = []
                bindings = SPARQLQueries.hasVictimUnderage(_graph,"http://xmlns.com/gah/0.1/")
                for s in bindings:
                    new_triples = rule.maketriples(s)
                    for s, p, o in new_triples:
                        ns = Namespace("http://xmlns.com/gah/0.1/")
                        triple = (rdflib.URIRef(s), ns["UnderagePassenger"], Literal(o))
                        _graph.add(triple)
                print(str(len(bindings)) + ' inferências aplicadas!')
