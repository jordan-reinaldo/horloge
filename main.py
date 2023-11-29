import time
import keyboard  # installation biblio python

heure_actuelle = (13, 10, 55)
heure_reveil = (13, 11, 00)

def alarme(heure_reveil, heure_actuelle):
    if heure_actuelle == heure_reveil:
        print("C'est l'heure du réveil")

def format_12h(h, m, s):
    am_pm = "AM" if h < 12 else "PM"
    h = h % 12
    h = 12 if h == 0 else h
    return f"{h:02d}:{m:02d}:{s:02d} {am_pm}"

def afficher_heure(heure_actuelle):
    h, m, s = heure_actuelle
    en_pause = False

    while True:
        if keyboard.is_pressed('space'):
            en_pause = not en_pause

        if not en_pause:
            alarme(heure_reveil, (h, m, s))
            heure = f"{h:02d}:{m:02d}:{s:02d}"
            print(heure, end="\r")
            s += 1

            if s == 60:
                s = 0
                m += 1
                if m == 60:
                    m = 0
                    h += 1
                    if h == 24:
                        h = 0

        time.sleep(1)  # Attendre une seconde

# test
afficher_heure(heure_actuelle) 