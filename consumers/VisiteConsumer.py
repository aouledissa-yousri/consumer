import requests
from .Hosts import Hosts 

class VisiteConsumer:
    
    
    @staticmethod
    def validerVisite(cin: str):

        try:
            int(cin)
            return requests.patch(Hosts.visite_service+"/visite/"+cin+"/valider").json()
        
        except ValueError:
            return "Visite n'est pas valide"