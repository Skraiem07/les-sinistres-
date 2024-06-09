import datetime
from datetime import datetime, timedelta

import pandas as pd
from ville import lieux

from webscrapping import web_scraping


mois=['test','janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
villes=[("07690","nice-cote-d-azur"),("07481","lyon-st-exupery"),("07156","paris-montsouris"),("07110","brest-guipavas"),("07015","lille-lesquin"),("07190","strasbourg-entzheim"),("07631","toulouse-francazal"),("07130","rennes-st-jacques"),("07650","marseille-marignane-marseille-provence"),("000Z8","aix-en-provence"),("07747","perpignan-rivesaltes"),("07486","grenoble-st-geoirs"),("07510","bordeaux-merignac"),("07645","nimes-courbessac"),("000U5","cannes"),("07230","angers-beaucouze"),("07563","avignon"),("07280","dijon-longvic"),("07460","clermont-ferrand-aulnat"),("07602","biarritz-anglet"),("07090","metz-frescaty"),("07249","orleans-bricy"),("07494","annecy-meythet"),("07168","troyes-barberey"),("07610","pau-uzein"),("07201","quimper-pluguffan"),("07027","caen-carpiquet"),("07037","rouen-boos"),("07434","limoges-bellegarde")]


def prix (CA,pivot,cf,datedeb1,ville1,w):
    datedeb = datetime.strptime(datedeb1,'%d/%m/%Y').date()
    datefin=datedeb.replace(year=datedeb.year + 1)
    #extraction du mois, jour ,année de la date de début
    annee=datedeb.year 
    moisj=datedeb.month   # mois en chiffres
    jour=datedeb.day
    moisl=mois[moisj]     # mois en lettres

    #Initialisation des listes utilisées
    data=[]
    appdata=[]
    l=[]
    ville=lieux(ville1)
    #Extraction de donnée: plt par webscraping
    for v in range(len(villes)):
        if(villes[v][1]==ville):
            code=villes[v][0]
    #print(ville)
            
        
    for m in range(12):
        s=moisj+m
        d=datedeb
        k=datetime.now().year
        if((s)>12):
            d=datedeb.replace(year=datedeb.year-w-1)
            s=s-12
        l.append(d.replace(month=s))
        
    for y in range(len(l)): #len(l) 
        appdata.append(web_scraping(code,mois[l[y].month],str(l[y].year),ville))
        
    appdata = pd.concat(appdata)   #concaténation des df de tous les mois de l'année



    #Réorganisation de la dataframe
    pluie=appdata
    pluie['jour']=''
    #pluie['jour'] = pluie.Date.str.extract('(\d+)') 
    dd=datedeb
    for s in range(len(pluie)):
        pluie['jour'].values[s]=dd
        dd=dd+timedelta(days=1)
        


    pluie["ft"] = ""  
    pluie["CAplt"] = ""
    pluie["Rplt"] = ""




    #Calcul CAplt et Rplt
    CAplt=0
    for i in range(len(pluie)):
        if (pluie['Precip'].values[i]==''):
            plt=float(0)
        else:
            plt=float(pluie['Precip'].values[i])
        ft=(pivot-plt)/pivot
        pluie['ft'].values[i] =ft
        if(plt>pivot):
            CAplt=0
            Rplt=-cf
        elif((plt>0)&(plt<pivot)):
            CAplt=CA*ft
            Rplt=CA*ft-cf
        elif (plt==0):
            CAplt=CA
            Rplt=CA-cf
        pluie['CAplt'].values[i] =CAplt
        pluie['Rplt'].values[i] =Rplt

    #affichage de la Dataframe
    pluie = pluie.reindex(columns=['Date','jour','Precip','ft','CAplt','Rplt'])
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(pluie)


    #Calcul de la prime annuelle à payer
    somme=0
    taux=0.02
    for h in range(len(pluie)):
        if(pluie['Rplt'].values[h]<0):
            somme=somme+abs(pluie['Rplt'].values[i])*(1/(1+taux)**h)
    return(somme)       
    