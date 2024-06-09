
import winsound
from speech_recognition import Recognizer, Microphone
def vocal():
    
    recognizer = Recognizer()
    filename = 'record.wav'
    winsound.PlaySound(filename, winsound.SND_FILENAME)

    # On enregistre le son
    with Microphone() as source:
        print("Réglage du bruit ambiant... Patientez...")
        recognizer.adjust_for_ambient_noise(source)
        print("Vous pouvez parler...")
        
        
        
        recorded_audio = recognizer.listen(source,timeout = 2)
        print("Enregistrement terminé !")
        
    # Reconnaissance de l'audio

    try:
        print("Reconnaissance du texte...")
        text = recognizer.recognize_google(
                recorded_audio, 
                language="fr-FR"
            )
        print("Vous avez dit : {}".format(text))

    except Exception as ex:
        print(ex)
    return(text)

def rec(text):
    if(text=='Nice'):
        ville="nice-cote-d-azur"
    elif(text=='Lyon'):
        ville="lyon-st-exupery"
    elif(text=="Paris"):
        ville="paris-montsouris"
    elif(text=="Brest"):
        ville="brest-guipavas"
    elif(text=="Lille"):
        ville="lille-lesquin"
    elif(text=="Strasbourg"):
        ville="strasbourg-entzheim"
    elif(text=="Toulouse"):
        ville="toulouse-francazal"
    elif(text=="Rennes"):
        ville="rennes-st-jacques"
    return ville