__author__ = '22208_65138'
import SPARQLQueries

class Victim():
    def Data (self, sparql, victimId):
        results = SPARQLQueries.victimData (sparql,"http://xmlns.com/gah/0.1/",victimId)
        if len (results["results"]["bindings"]) == 0:
            print ("Vitima não encontrada")
        else:
            r = results["results"]["bindings"][0]
            st = "Dados da vítima: " + victimId
            if ( "descIdade" in r ):
                st = st + " | Faixa etária:" + str(r["descIdade"]["value"])
            if ( "descVeiculo" in r ):
                st = st + " | Tipo de Veiculo:" + str(r["descVeiculo"]["value"])
            if ( "descHora" in r ):
                st = st + " | Tipo de Vítima:" + str(r["descVitima"]["value"])
            if ( "?descLocal" in r ):
                st = st + " | Acidente:" + str(r["objAcidente"]["value"])

            print (st)
