# InstaOSINT
InstaOSINT è uno strumento potente per raccogliere e analizzare dati pubblici da profili Instagram. Utilizzando la libreria Instaloader, InstaOSINT consente di ottenere informazioni dettagliate su un profilo Instagram, inclusi i post, le immagini e le statistiche degli account.

# Funzionalità
Raccolta di informazioni di base su un profilo Instagram (username, ID utente, biografia, numero di follower, ecc.)
Estrazione dei post recenti, comprese didascalie, like e commenti
Salvataggio delle informazioni in formato JSON o HTML
Download delle immagini dei post in una cartella dedicata
Requisiti
Python 3.6 o superiore
Librerie Python: instaloader, json, os, datetime, colorama
Installazione
Segui questi passaggi per installare e utilizzare InstaOSINT:

# Clona il repository:

git clone https://github.com/skelegamerYT11/InstaOSINT.git
cd InstaOSINT
# Crea un ambiente virtuale (opzionale ma consigliato):

python -m venv venv
source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
# Installa le dipendenze necessarie:

pip install instaloader colorama

# Esegui il programma:

python insta_osint.py
# Segui le istruzioni a schermo:

Inserisci il nome utente dell'account Instagram da analizzare.
Scegli se salvare le informazioni in formato JSON o HTML.
Decidi se scaricare i post dell'account.
Commands
- addrs           Get all registered addressed by target photos
- fwersemail      Get email of target followers
- fwingsemail     Get email of users followed by target
- fwersnumber     Get phone number of target followers
- fwingsnumber    Get phone number of users followed by target
- info            Get target info
- tagged          Get list of users tagged by target
- follow          Follow target !
- unfollow        Unfollow target !
