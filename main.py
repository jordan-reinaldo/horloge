import time
import keyboard

heure_actuelle = (13, 10, 55)
heure_reveil = (13, 11, 00)

# Alarme qui compare l'heure actuelle à l'heure que l'on souhaite pour le réveil
def alarme(heure_reveil, heure_actuelle):
    if heure_actuelle == heure_reveil:
        print("C'est l'heure du réveil")

# Permet de passer du format 24h à 12h
def format_12h(h, m, s):
    if h < 12:
        am_pm = "AM"
    else:
        am_pm = "PM"

    #permet d'avoir un affiche correct en format 12 de midi
    h = h % 12
    if h == 0:
        h = 12

    # heure formatée
    return f"{h:02d}:{m:02d}:{s:02d} {am_pm}"

# permet de mettre en pause avec espace
def espace(keyboard_event):
    global en_pause
    if keyboard_event.event_type == keyboard.KEY_DOWN:
        en_pause = not en_pause

# fonction principale, elle permet d'afficher l'heure, mais fait aussi appel à l'alarme, au format etc
def afficher_heure(heure_actuelle):
    global en_pause
    en_pause = False
    keyboard.on_press_key('space', espace)

    format_choisi = input("Choisissez le format d'heure (12 ou 24) : ")
    print("Si vous souhaitez mettre en pause, veuillez utiliser la barre espace")

    h, m, s = heure_actuelle
    while True:
        try:
            # Si on effectue une pause, ce léger délais permet d'éviter que la machine comprenne des doubles clique non souhaités. 
            if en_pause:
                time.sleep(0.1)
                continue

            #  l'alarme est déclenchée si les conditions de la fonction alarme sont respectées
            alarme(heure_reveil, (h, m, s))

            # choix du format en fonction de l'input utilisé par l'utilisateur
            if format_choisi == "12":
                heure = format_12h(h, m, s)
            elif format_choisi == "24":
                heure = f"{h:02d}:{m:02d}:{s:02d}"
            else: 
                print("Format non valide, utilisation du format 24h par défaut")
                heure = f"{h:02d}:{m:02d}:{s:02d}"

            print(heure, end="\r")
            s += 1

            # Gestion du défilement du temps
            if s == 60:
                s = 0
                m += 1
                if m == 60:
                    m = 0
                    h += 1
                    if h == 24:
                        h = 0

            time.sleep(1)
        except KeyboardInterrupt:
            break       

# Lancement de la fonction avec les paramètres heure actuelles que nous avons définit plus haut
afficher_heure(heure_actuelle)