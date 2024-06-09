from datetime import datetime
from datetime import timedelta
from matplotlib import legend
from matplotlib.pyplot import *
import numpy as np
import pandas as pd
from matplotlib  import *

from webscrapping import web_scraping




mois=['test','janvier','fevrier','mars','avril','mai','juin','juillet','aout','septembre','octobre','novembre','decembre']
villes=[("07690","nice-cote-d-azur"),("07481","lyon-st-exupery"),("07156","paris-montsouris"),("07110","brest-guipavas"),("07015","lille-lesquin"),("07190","strasbourg-entzheim"),("07631","toulouse-francazal"),("07130","rennes-st-jacques"),("07650","marseille-marignane-marseille-provence"),("000Z8","aix-en-provence"),("07747","perpignan-rivesaltes"),("07486","grenoble-st-geoirs"),("07510","bordeaux-merignac"),("07645","nimes-courbessac"),("000U5","cannes"),("07230","angers-beaucouze"),("07563","avignon"),("07280","dijon-longvic"),("07460","clermont-ferrand-aulnat"),("07602","biarritz-anglet"),("07090","metz-frescaty"),("07249","orleans-bricy"),("07494","annecy-meythet"),("07168","troyes-barberey"),("07610","pau-uzein"),("07201","quimper-pluguffan"),("07027","caen-carpiquet"),("07037","rouen-boos"),("07434","limoges-bellegarde")]

def Analyse_Retro(ville1,chiffre_affaire,choix_pivot,couts_fixes):
    CA_Assuré=[]
    CA_NonAssuré=[]
    P=[]
    #nom ville
    if(ville1=='Nice'):
        ville="nice-cote-d-azur"
    elif(ville1=='Lyon'):
        ville="lyon-st-exupery"
    elif(ville1=="Paris"):
        ville="paris-montsouris"
    elif(ville1=="Brest"):
        ville="brest-guipavas"
    elif(ville1=="Lille"):
        ville="lille-lesquin"
    elif(ville1=="Strasbourg"):
        ville="strasbourg-entzheim"
    elif(ville1=="Toulouse"):
        ville="toulouse-francazal"
    elif(ville1=="Rennes"):
        ville="rennes-st-jacques"
    elif(ville1=="Marseille"):
        ville="marseille-marignane-marseille-provence"
    elif(ville1=="Aix-en-Provence"):
        ville="aix-en-provence"
    elif(ville1=="Perpignan"):
        ville="perpignan-rivesaltes"
    elif(ville1=="Grenoble"):
        ville="grenoble-st-geoirs"
    elif(ville1=="Bordeaux"):
        ville="bordeaux-merignac"
    elif(ville1=="Nîmes"):
        ville="nimes-courbessac"
    elif(ville1=="Cannes"):
        ville="cannes"
    elif(ville1=="Angers"):
        ville="angers-beaucouze"
    elif(ville1=="Avignon"):
        ville="avignon"
    elif(ville1=="Dijon"):
        ville="dijon-longvic"
    elif(ville1=="Clermont-Ferrand"):
        ville="clermont-ferrand-audlnat"
    elif(ville1=="Biarritz"):
        ville="biarritz-anglet"
    elif(ville1=="Metz"):
        ville="metz-frescaty"
    elif(ville1=="Orléans"):
        ville="orleans-bricy"
    elif(ville1=="Annecy"):
        ville="annecy-meythet"
    elif(ville1=="Troyes"):
        ville="troyes-barberey"
    elif(ville1=="Pau"):
        ville="pau-uzein"
    elif(ville1=="Quimper"):
        ville="quimper-pluguffan"
    elif(ville1=="Caen"):
        ville="cean-carpiquet"
    elif(ville1=="Rouen"):
        ville="rouen-boos"
    elif(ville1=="Limoges"):
        ville="limoges-bellegarde"
    
    
    datedeb = datetime.strptime('01/02/2000','%d/%m/%Y').date()
    CA=chiffre_affaire    #CA: chiffre d'affaire max en une journée
    pivot=choix_pivot  #niveau de pluie journalier pivot
    cf=couts_fixes    #couts fixes en une journée avec CA>cf
    datefin=datedeb.replace(year=datedeb.year + 1)
    ville= ville
    
    for y in range(22): 
        vardate=datedeb.replace(year=datedeb.year+y)
        print(vardate)

        

        #extraction du mois, jour ,année de la date de début
        annee=vardate.year 
        moisj=vardate.month   # mois en chiffres
        jour=vardate.day
        moisl=mois[moisj]     # mois en lettres

        #Initialisation des listes utilisées
        data=[]
        appdata=[]
        l=[]

        #Extraction de donnée: plt par webscraping
        for v in range(len(villes)):
            if(villes[v][1]==ville):
                code=villes[v][0]

        for m in range(12):
            s=moisj+m
            d=vardate
            if((s)>12):
                d=vardate.replace(year=vardate.year+1)
                s=s-12
            l.append(d.replace(month=s))

        for y in range(len(l)): #len(l) 
            appdata.append(web_scraping(code,mois[l[y].month],str(l[y].year),ville))

        appdata = pd.concat(appdata)   #concaténation des df de tous les mois de l'année

        #Réorganisation de la dataframe
        pluie=appdata
        pluie['jour']=''
        #pluie['jour'] = pluie.Date.str.extract('(\d+)') 
        dd=vardate
        for s in range(len(pluie)):
            pluie['jour'].values[s]=dd
            dd=dd+timedelta(days=1)

            pluie["ft"] = ""  
            pluie["CAplt"] = ""
            pluie["Rplt"] = ""
            pluie["Pertes"] = ""
            pluie["Rplt_Prime"] = ""

        #Calcul CAplt, Rplt, Rplt_Prime, et des pertes

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
                Pertes=-cf
                Rplt_Prime=0
            elif((plt>0)&(plt<pivot)):
                CAplt=CA*ft
                Rplt=CA*ft-cf
                Pertes=0
                Rplt_Prime=CA*ft-cf
            elif (plt==0):
                CAplt=CA
                Pertes=0
                Rplt=CA-cf
                Rplt_Prime=CA-cf

            pluie['CAplt'].values[i] =CAplt
            pluie['Rplt'].values[i] =Rplt
            pluie['Pertes'].values[i] =Pertes
            if pluie['Rplt'].values[i]<0:
                pluie['Rplt_Prime'].values[i]=0
            else:
                pluie['Rplt_Prime'].values[i]=Rplt_Prime

        #affichage de la Dataframe
        pluie = pluie.reindex(columns=['Date','jour','Precip','ft','CAplt','Rplt','Pertes','Rplt_Prime'])
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            print(pluie)


        #Calcul de la prime annuelle à payer
        somme=0
        taux=0.02
        for h in range(len(pluie)):
            if(pluie['Rplt'].values[h]<0):
                somme=somme+abs(pluie['Rplt'].values[i])*(1/(1+taux)**h)

        print("prime à payer",somme,'euros') 

        CA_Assuré.append(pluie['Rplt_Prime'].sum())
        CA_NonAssuré.append(pluie['Rplt'].sum())
        P.append(somme-abs(pluie['Pertes'].sum()))
        print(CA_Assuré,'\n')
        
        
    print('Votre CA au fil des années en étant assuré est de :',CA_Assuré, '\n')
    print('Votre CA au fil des années en étant non assuré est de :',CA_NonAssuré, '\n')
    print('Votre Bénéfice/Déficit au fil des années en étant assuré est de :',P, '\n')
    periode=np.arange(2000,2022,1)
    plot(periode,CA_Assuré,label='CA annuel en étant assuré',color="green")
    plot(periode,CA_NonAssuré,label='CA annuel sans assurance',color="blue")
  
    ylabel("Montant (en €)")
    xlabel('Années')
    title("Comparaisons du chiffre d'affaires annuel")
    show()
    
    plot(periode, P, "-rs")
    ylabel("Montant (en €)")
    xlabel('Années')
    title("Bénéfice/Déficit")
    show()
  