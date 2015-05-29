__author__ = '22208_65138'

import sys, string, os

def triplestodot(triples,filename):
    out=open(filename,'w',encoding='utf-8')
    out.write('graph "SimpleGraph" {\n')
    out.write('overlap = "scale";\n')
    for t in triples:
        out.write('"%s" -- "%s" [label="%s"]\n'
                  % (t[0],t[2],t[1]))
    out.write('}\n')
    out.close()



