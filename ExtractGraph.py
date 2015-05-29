__author__ = '22208_65138'

import sys, string, subprocess, grafo
class ExtractGraph:

    pathGraphViz = "\"C:\Program Files (x86)\Graphviz2.38\bin\neato\""

    def _triplestodot(self, triples,filename):
        out=open(filename,'w',encoding='utf-8')
        out.write('graph "Accident" {\n')
        out.write('overlap = "scale";\n')
        for t in triples:
            out.write('"%s" -- "%s" [label="%s"]\n'
                      % (t[0],t[2],t[1]))
        out.write('}\n')
        out.close()

    def ExecuteGraph (self, triples, id):
        self._triplestodot (triples, "grafo.dot")
        result = subprocess.check_output ("C:\\Program Files (x86)\\Graphviz2.38\\bin\\neato.exe -Tsvg -o " + str(id)+ ".svg grafo.dot")
        #subprocess.check_output ("neato -Tsvg -o " + str(id)+ ".svg grafo.dot")

    def AccidentGraph (self, g, accidentId):

        #primeiro isolar todos os triplo correspondentes ao acidente e suas vitimas
        finalList=[]
        list = g.search ((accidentId, None, None))
        for tuple in list:
            if tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#happenedAt":
                continue
            if tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#belongsToPoliceDpt":
                continue
            finalList.append(tuple)

            if tuple[1] == "http://crashmap.okfn.gr/vocabs/roadAccidentsVocab#hasVictim":
                victim = g.search ((tuple[2], None, None))
                for tupleVit in victim:
                    finalList.append(tupleVit)
        self.ExecuteGraph(finalList,g.CleanUri(accidentId));



