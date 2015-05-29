__author__ = '22208_65138'

import grafo
import Accident
import Victim
import ExtractGraph
import inferencerules
import rdflib
import converter
import SPARQLQueries

from rdflib import ConjunctiveGraph, Namespace, Literal


#https://docs.python.org/2/tutorial/datastructures.html
def list(list):
    #TODO: Format print
    print(list)

#https://docs.python.org/2/tutorial/datastructures.html#list-comprehensions
def filter(element, list):
    return [item for item in list if element in item]


def exists(element, list):
    if any(element in tuple for tuple in list):
        return True
    return False

def readTuple():
    e1 = input('1º Elemento: ')
    if e1.strip() == "":
        e1 = None
    e2 = input('2º Elemento: ')
    if e2.strip() == "":
        e2 = None
    e3 = input('3º Elemento: ')
    if e3.strip() == "":
        e3 = None
    tuple = (e1,e2,e3)
    return tuple

def listDistinctValues (list):
    values = []
    for tuple in list:
        if not g.CleanUri (tuple[2]) in values:
            values.append( g.CleanUri (tuple[2]))
    for st in values:
        print (st)


def listaRegistos (list, tipo, campo):
#    dados = None;
    if tipo == 'acidentes':
        dados = Accident.Accident()
    elif tipo == 'vitimas':
        dados = Victim.Victim()
    key="X"
    while key.upper() != 'S' and key.upper() != 'N':
        key = input ("Deseja listar " + str(tipo) + " (S/N)?")
        if key.upper() == 'S':
            for c in list:
                print (dados.Data (g, c[campo]))


flag = True
_graph = ConjunctiveGraph()

def isFileLoaded():
    if len(_graph) == 0:
        print ('O gráfico ainda não foi carregado')
        return False
    return True

while flag:
    print('\n --=== MENU ===--')
    print('1 - Carregar Ficheiro') #Carraga o ficheiro
    print('2 - Dados Gerais') #informação geral sobre os dados
    print('3 - Procurar Acidente/Vitima') # pesquisar dados de determinado acidente
    print('4 - Consultas') #algumas consultas sobre os dados
    print('5 - Aplicar Inferências')
    print('X - Terminar')
    n = input('Opção: ')
    if n.strip().upper() == 'X':
        flag = False
    if n.strip() == '1':
        _graph.parse("Dados\\roadaccidents.nt", format="nt")
    if n.strip() == '2' and isFileLoaded():
        if(isFileLoaded()):
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
                    results = SPARQLQueries.predicateCount (_graph,"http://xmlns.com/gah/0.1/","accidentID")
                    for r in results:
                        acc = r[0]
                    print ('Existiram ' + str(acc) + ' acidentes');
                if key == '2':
                    results = SPARQLQueries.predicateCount (_graph,"http://xmlns.com/gah/0.1/","victimID")
                    for r in results:
                        acc = r[0]
                    print ('Existiram ' + str(acc) + ' Vitimas');
                if key == '3':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccType")
                    print ("Os tipos de acidentes que existem são:")
                    print ("Tipo de acidente  --> Número de acidentes")
                    print ("-------------------------------------------")
                    for r in results:
                        print (r[0] +" --> " + r[1])
                if key == '4':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccCause")
                    print ("As causas de acidentes existentes são:")
                    print ("Causas de acidente  --> Número de acidentes")
                    print ("-------------------------------------------")

                    for r in results:
                        print (r[0] +" --> " + r[1])
                if key == '5':
                    results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasVictimAge")
                    print ("Faixa etária das vitimas --> Número de Vitimas")
                    print ("-------------------------------------------")
                    for r in results:
                        print (r[0] +" --> " + r[1])
    if n.strip() == '3' and isFileLoaded():
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
                acc.Data(_graph,id)
            if key == '2':
                id = input ("Introduza o id da Vitima: ")
                acc = Victim.Victim()
                acc.Data(_graph,id)
    if n.strip() == '4' and isFileLoaded():
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
                results = SPARQLQueries.accidentVictimAge(_graph,"http://xmlns.com/gah/0.1/", acc)
                if len (results.bindings) == 0:
                    print ("Acidente não encontrado")
                else:
                    print ("Esse acidente teve " + str(len (results.bindings)) + " vitimas:")
                    for c in results.bindings:
                        print ("A vitima " +c["?vitima"] + " na faixa etária " +  c["?descIdade"])

            if key == '2':
                results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccCause")
                i=1
                for r in results:
                    print ("[" + str (i)+ "]: " + r[0])
                    i = i + 1

                acc = input ("Introduza o número correspondente à Causa pretendida:")
                results = SPARQLQueries.accidentsByType(_graph,"http://xmlns.com/gah/0.1/","hasAccCause", results.bindings[int(acc)-1]["?Descricao"])
                print ("Existem " + str(len(results.bindings)) + " acidentes")
                if input ("Deseja listar os acidentes (S/N)?").upper() == "S":
                    acc = Accident.Accident()
                    for r in results:
                        acc.Data(_graph,r[0])

            if key == '3':
                results = SPARQLQueries.listTypes (_graph,"http://xmlns.com/gah/0.1/", "hasAccVehicle")
                i=1
                for r in results:
                    print ("[" + str (i)+ "]: " + r[0])
                    i = i + 1

                vit = input ("Introduza o número correspondente ao veiculo pretendido:")
                results = SPARQLQueries.accidentsByType(_graph,"http://xmlns.com/gah/0.1/","hasAccVehicle", results.bindings[int(vit)-1]["?Descricao"])
                print ("Existem " + str(len(results.bindings)) + " vitimas")
                if input ("Deseja listar as vitimas (S/N)?").upper() == "S":
                    vit = Victim.Victim()
                    for r in results:
                        vit.Data(_graph,r[0])

            if key == '4':
                list = g.query ([( "?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimAge","http://crashmap.okfn.gr/data/accidents/VictimAge/Y0-17"),
                                 ("?subacidente", "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictimType", "http://crashmap.okfn.gr/data/accidents/VictimType/Driver")
                ])
                print ("Foram encontrados "  + str (len(list)) + " vitimas.")
                listaRegistos (list,"vitimas", "subacidente")
    if n.strip() == '5' and isFileLoaded():
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
