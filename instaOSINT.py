import instaloader
import json
import os
from datetime import datetime
from colorama import init, Fore

# Inizializza Colorama
init(autoreset=True)

LOGO = f"""{Fore.CYAN}
.___                 __          ________    _________.___ __________________
|   | ____   _______/  |______   \_____  \  /   _____/|   |\      \__    ___/
|   |/    \ /  ___/\   __\__  \   /   |   \ \_____  \ |   |/   |   \|    |   
|   |   |  \\___ \  |  |  / __ \_/    |    \/        \|   /    |    \    |   
|___|___|  /____  > |__| (____  /\_______  /_______  /|___\____|__  /____|   
         \/     \/            \/         \/        \/             \/         
"""

def collect_instagram_data(username):
    # Creazione dell'istanza di Instaloader
    L = instaloader.Instaloader()

    try:
        # Caricamento del profilo Instagram
        profile = instaloader.Profile.from_username(L.context, username)

        # Raccolta delle informazioni di base
        profile_info = {
            "username": profile.username,
            "user_id": profile.userid,
            "full_name": profile.full_name,
            "biography": profile.biography,
            "external_url": profile.external_url,
            "followers": profile.followers,
            "followees": profile.followees,
            "is_private": profile.is_private,
            "is_verified": profile.is_verified,
            "media_count": profile.mediacount,
            "profile_pic_url": profile.profile_pic_url,
            "last_post_date": profile.get_posts().__next__().date.isoformat() if profile.mediacount > 0 else None,
            "posts": []
        }

        # Raccogliere informazioni sui post
        for post in profile.get_posts():
            post_info = {
                "caption": post.caption,
                "likes": post.likes,
                "comments": post.comments,
                "date": post.date.isoformat(),
                "image_url": post.url
            }
            profile_info["posts"].append(post_info)

        return profile_info

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"{Fore.RED}L'account '{username}' non esiste.")
    except instaloader.exceptions.ConnectionException:
        print(Fore.RED + "Errore di connessione. Verifica la tua connessione internet.")
    except Exception as e:
        print(Fore.RED + f"Si è verificato un errore: {e}")

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_html(data, filename):
    html_content = "<html>\n<body>\n"
    for key, value in data.items():
        if key == "posts":
            html_content += "<h2>Post:</h2>\n"
            for post in value:
                html_content += f"<p><strong>Data:</strong> {post['date']}<br>"
                html_content += f"<strong>Didascalia:</strong> {post['caption']}<br>"
                html_content += f"<strong>Like:</strong> {post['likes']}<br>"
                html_content += f"<strong>Commenti:</strong> {post['comments']}<br>"
                html_content += f"<strong>Immagine:</strong> <a href='{post['image_url']}'>{post['image_url']}</a></p>\n"
        else:
            html_content += f"<p><strong>{key}:</strong> {value}</p>\n"
    html_content += "<hr>"
    html_content += "<p style='text-align: center;'>Creato con <strong>InstaOSINT</strong> by <strong>SKELETONita</strong></p>"
    html_content += "</body>\n</html>"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_content)

def download_posts(profile_info, username):
    # Crea una cartella per i post
    folder_name = f"{username}_posts"
    os.makedirs(folder_name, exist_ok=True)

    for i, post in enumerate(profile_info["posts"], start=1):
        image_url = post["image_url"]
        image_name = os.path.join(folder_name, f"post_{i}.jpg")
        
        try:
            # Scarica l'immagine
            instaloader.Instaloader().download_post(post, target=folder_name)
            print(f"{Fore.GREEN}Scaricato: {image_name}")
        except Exception as e:
            print(Fore.RED + f"Errore nel scaricare il post: {e}")

def main():
    print(LOGO)
    print(Fore.GREEN + "Benvenuto in InstaOSINT")
    username = input(Fore.YELLOW + "Inserisci il nome utente dell'account Instagram da analizzare: ")
    profile_info = collect_instagram_data(username)
    
    if profile_info:
        print("\n" + Fore.CYAN + "Informazioni raccolte:")
        for key, value in profile_info.items():
            if key != "posts":
                print(f"{Fore.MAGENTA}{key}: {Fore.WHITE}{value}")
        
        # Scelta del formato di salvataggio
        save_choice = input("\nVuoi salvare le informazioni? (JSON/HTML/N) ").strip().lower()
        if save_choice == 'json':
            filename = f"{username}_info.json"
            save_to_json(profile_info, filename)
            print(f"{Fore.GREEN}Informazioni salvate nel file {filename}")
        elif save_choice == 'html':
            filename = f"{username}_info.html"
            save_to_html(profile_info, filename)
            print(f"{Fore.GREEN}Informazioni salvate nel file {filename}")
        elif save_choice == 'n':
            print(Fore.YELLOW + "Informazioni non salvate.")
        else:
            print(Fore.RED + "Scelta non valida. Informazioni non salvate.")

        # Opzione per scaricare i post
        download_choice = input("\nVuoi scaricare i post dell'account? (Y/N) ").strip().lower()
        if download_choice == 'y':
            download_posts(profile_info, username)

if __name__ == "__main__":
    main()
