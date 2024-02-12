**PROJET 1:  Identification Automatique des Ravageurs du Maïs**

**Maguette Diop**<br>
**Ameth Sylla**<br>
**Ndeye Galass Gaye**<br>
**Omar Sall**<br>
**Ramatoulay Diallo**<br>


**Précisin**
Seul les code source de l'interface utilisateur et la conception du modèle sont televersés dans ce repository. le dossier contenant le projet complet incluant tous les fichiers vous est partagé par lien-drive.

Ci-desous, un guide complet pour visualiser et tester l'interface utilisateur après avoir avoir telechargé le dossier complet.


# Installation

- Deplacez-vous dans le dossier Projet_1_Data_Science/
- Recreez l'environnement virtuel avec la commande 
        python3 -m pip install -r requirements.txt
- Activez l'environnement virtuel avec la commande
    * sur linux
    ```bash
    source .env/bin/activate
    ```
    * sur windows
    ```bash
    \.env\Scripts\activate.bat
    ```

# Lancement du serveur web

- Se rendre dans le dossier Projet_1_Data_Science/App/src/
    ```bash
    cd App/src/
    ```
- Executer la commande
    ```bash
    python3 manage.py runserver
    ```