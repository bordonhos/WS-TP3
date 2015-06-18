__author__ = '22208_65138'
import SPARQLQueries

class Accident():
    def Data (self, sparql, accidentId):
        results = SPARQLQueries.accidentData (sparql,"http://xmlns.com/gah/0.1/",accidentId)
        if len (results["results"]["bindings"]) == 0:
            print ("Acidente não encontrado")
        else:
            r = results["results"]["bindings"][0]
            st = "Dados do acidente: " + accidentId
            if ( "?descVeiculo" in r ):
                st = st + " | Veiculo:" + str(r["descVeiculo"]["value"])
            if ( "descCausa" in r ):
                st = st + " | Causa:" + str(r["descCausa"]["value"])
            if ( "descHora" in r ):
                st = st + " | Intervalo horário:" + str(r["descHora"]["value"])
            if ( "descLocal" in r ):
                st = st + " | Local:" + str(r["descLocal"]["value"])
            if ( "nVitimas" in r ):
                st = st + " | Numero de Vitimas:" + str(r["nVitimas"]["value"])

            print (st)


