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

bash
Copia codice
git clone https://github.com/your_username/InstaOSINT.git
cd InstaOSINT
# Crea un ambiente virtuale (opzionale ma consigliato):

bash
Copia codice
python -m venv venv
source venv/bin/activate  # Su Windows usa `venv\Scripts\activate`
# Installa le dipendenze necessarie:

bash
Copia codice
pip install instaloader colorama
Utilizzo
# Esegui il programma:

bash
Copia codice
python insta_osint.py
# Segui le istruzioni a schermo:

Inserisci il nome utente dell'account Instagram da analizzare.
Scegli se salvare le informazioni in formato JSON o HTML.
Decidi se scaricare i post dell'account.
