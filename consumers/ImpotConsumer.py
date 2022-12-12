import requests
from .Hosts import Hosts 


class ImpotConsumer:
    
    @staticmethod
    def getConsumer(cin: str):

        try:
            int(cin)
            return requests.get(Hosts.impot_service+"/impot/"+cin).json()
        
        except ValueError:
            return "Valeur de cin doit étre un entier"
        
        