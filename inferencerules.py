__author__ = '22208_65138'

from rdflib.graph import ConjunctiveGraph, Namespace

class InferenceRule:

    def getqueries(self):
        return None

    def maketriples(self, binding):
        return self._maketriples(binding)


class DayTime(InferenceRule):
    def getqueries(self):
        happenedDuring = [('?roadaccident', 'http://xmlns.com/gah/0.1/happenedDuring', '?happenedDuring')]
        return [happenedDuring]

    def maketriples(self, happenedDuring, roadaccident):

        if happenedDuring == 'http://ws_22208_65138.com/AccTime/T13-17':
            daytime = 'http://ws_22208_65138.com/DayTime/afternoon'
        elif happenedDuring == 'http://ws_22208_65138.com/AccTime/T07-09' or happenedDuring == 'http://ws_22208_65138.com/AccTime/T09-13' or happenedDuring == 'http://ws_22208_65138.com/AccTime/T24-07':
            daytime = 'http://ws_22208_65138.com/DayTime/morning'
        elif happenedDuring == 'http://ws_22208_65138.com/AccTime/T17-21' or happenedDuring == 'http://ws_22208_65138.com/AccTime/T21-24':
            daytime = 'http://ws_22208_65138.com/DayTime/evening'
        else:
            daytime = 'http://ws_22208_65138.com/DayTime/unknown'
        #print('Nova inferencia: ' + roadaccident + '  http://ws_22208_65138.com/dayTime  ' + daytime)
        return [(roadaccident,'http://ws_22208_65138.com/DayTime',daytime)]



class UnderagePassenger(InferenceRule):
    def getqueries(self):
        hasVictimType = [('?accidentvictim','http://xmlns.com/gah/0.1/hasVictimType','http://ws_22208_65138.com/VictimType/Passenger')]
        hasVictimAge = [('?accidentvictim', 'http://xmlns.com/gah/0.1/hasVictimAge', 'http://ws_22208_65138.com/VictimAge/Y0-17')]
        return [hasVictimType,hasVictimAge]

    def _maketriples(self, accidentvictim):

        underAge = 'http://ws_22208_65138.com/isUnderagePassenger'
        #print('Nova inferencia: ' + accidentvictim + '  http://ws_22208_65138.com/UnderagePassenger  ' + underAge)
        return [(accidentvictim,'http://ws_22208_65138.com/UnderagePassenger', underAge)]
