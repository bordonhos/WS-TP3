__author__ = '22208_65138'
import SPARQLQueries

class Victim():
    def Data (self, g, victimId):
        results = SPARQLQueries.victimData (g,"http://xmlns.com/gah/0.1/",victimId)
        if len (results.bindings) == 0:
            print ("Vitima não encontrada")
        else:
            r = results.bindings[0]
            st = "Dados da vítima: " + victimId
            if ( "?descIdade" in r ):
                st = st + " | Faixa etária:" + str(r["?descIdade"])
            if ( "?descVeiculo" in r ):
                st = st + " | Tipo de Veiculo:" + str(r["?descVeiculo"])
            if ( "?descHora" in r ):
                st = st + " | Tipo de Vítima:" + str(r["?descVitima"])
            if ( "?descLocal" in r ):
                st = st + " | Acidente:" + str(r["?objAcidente"])

            print (st)
