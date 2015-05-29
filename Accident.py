__author__ = '22208_65138'
import SPARQLQueries

class Accident():
    def Data (self, g, accidentId):
        results = SPARQLQueries.accidentData (g,"http://xmlns.com/gah/0.1/",accidentId)
        if len (results.bindings) == 0:
            print ("Acidente não encontrado")
        else:
            r = results.bindings[0]
            st = "Dados do acidente: " + accidentId
            if ( "?descVeiculo" in r ):
                st = st + " | Veiculo:" + str(r["?descVeiculo"])
            if ( "?descCausa" in r ):
                st = st + " | Causa:" + str(r["?descCausa"])
            if ( "?descHora" in r ):
                st = st + " | Intervalo horário:" + str(r["?descHora"])
            if ( "?descLocal" in r ):
                st = st + " | Local:" + str(r["?descLocal"])
            if ( "?nVitimas" in r ):
                st = st + " | Numero de Vitimas:" + str(r["?nVitimas"])

            print (st)


