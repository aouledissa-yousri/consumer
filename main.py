from consumers import ImpotConsumer
from consumers import VisiteConsumer

#enter le cin d'un conducteur

cin = input("entrer un cin: ")

result = ImpotConsumer.getConsumer(cin)

if(result["paye"]):
    result = VisiteConsumer.validerVisite(cin)

    if(result["valide"]):
        print("Visite validé")
    
    else:
        print("Visite n'est pas validé")


elif(result["paye"] == False):
    print("L'impot de conducteur n'est pas paye")