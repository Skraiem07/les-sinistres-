# les-sinistres-
Actuarial - Tarification - Risque météorologique
# Guide d'installation du projet "Les Sinistres"

Ce guide vous aidera à télécharger, configurer et exécuter le projet "Les Sinistres" sur votre machine. Assurez-vous de suivre attentivement chaque étape pour garantir une installation correcte.

## Étapes :

1. **Télécharger et extraire le projet** :
   Téléchargez le projet "Les Sinistres" depuis [lien_de_téléchargement] et extrayez-le dans un dossier sur votre système.

2. **Ouvrir l'invite de commande** :
   - Sous Windows : Ouvrez l'invite de commande (cmd) et accédez à l'emplacement du projet en utilisant la commande :
     ```
     cd chemin_vers_le_dossier\sinistres
     ```
   - Sous Mac : Ouvrez le terminal et accédez à l'emplacement du projet en utilisant la commande :
     ```
     cd chemin_vers_le_dossier/sinistres
     ```

3. **Créer un environnement virtuel de travail et l'activer** :
   Utilisez la commande suivante pour créer un environnement virtuel:
    ### pour **`macOS`** : 

        ```BASH
        pyenv local 3.11.3
        python -m venv .venv
        source .venv/bin/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
    ### pour **`WindowsOS`**  :

    avec `PowerShell` CLI :

        ```PowerShell
        pyenv local 3.11.3
        python -m venv .venv
        .venv\Scripts\Activate.ps1
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
        
        avec `Git-Bash` CLI :

        ```
        pyenv local 3.11.3
        python -m venv .venv
        source .venv/Scripts/activate
        pip install --upgrade pip
        pip install -r requirements.txt
        ```
4. **Installation des librairies et des dépendances** :
 
    ```
    pip install -r requirements.txt
    ```
    
Note : Cette étape peut prendre un certain temps en raison du grand nombre de librairies à installer.

5. **Lancement du projet** :
Exécutez le fichier principal du projet en utilisant la commande :
    ```
    python flaskblog.py
    ```
    

7. **Accès au site** :
Une fois le projet lancé, ouvrez un navigateur web et entrez le lien suivant :
[http://localhost:5000/](http://localhost:5000/) 

