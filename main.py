#!/usr/bin/env python3
# Dev by Jean Dubois
# Domaine public
# PyPendu
from tkinter import *
import random
import os
import itertools
import webbrowser

__author__ = "Jean Dubois <jd-dev@laposte.net>"
__version__ = "1:1i20 InDev Snapchot"


def choose_word():
    """ Choisis le mot parmis une liste et créée les labels tkinter correspondants """
    global label_subtitle1, letter_entry, word, word_with_missing_letters, missing_letters, label_subtitle2, button, \
        label_subtitle3

    # Vérification de l'existance du fichier "words.txt" et choix du mot
    if os.path.exists("words.txt"):
        with open("words.txt", "r+") as words_file:
            words_list = words_file.readlines()
            word = random.choice(words_list)
            words_file.close()
    else:
        word = "ERRORNO\n"

    # Création du mot avec les lettres manquantes
    word_with_missing_letters = word[0]
    missing_letters = []
    e = 1
    for _ in itertools.repeat(None, len(word) - 2):  # Répétition avec itertools
        word_with_missing_letters += '_ '
        missing_letters += [word[e]]
        e += 1

    # Création de labels tkinter
    label_subtitle1 = Label(frame1, text=word_with_missing_letters, font=('Tahoma', 10), bg='orange')
    label_subtitle1.pack()
    label_subtitle2 = Label(frame1, text="Entrez une lettre :", font=('Tahoma', 10), bg='orange')
    label_subtitle2.pack()

    # Création d'une entrée input
    letter_entry = Entry(frame1, font=('Tahoma', 10), bg='orange')
    letter_entry.pack()

    label_subtitle3 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    label_subtitle3.pack()

    # Création d'un bouton OK
    button = Button(frame1, text='OK', font=('Tahoma', 10), bg='darkorange', command=lambda: letter_entered())
    button.pack()

    # Empaquetage
    frame1.pack(expand=YES)
    main_window.mainloop()


def letter_entered():
    """ Vérifie si la lettre est dans le mot, gère les érreurs, vérifie si le joueur a gagné, perdu ou rien """
    global letter_entry, founded_letters, missing_letters, word_with_missing_letters, hanged, label_subtitle1, \
        label_subtitle2, word, frame1, label_title, label_subtitle, label_subtitle3, button, label_subtitle4, \
        label_errors, button2, error, is_in_you_win_or_you_lose_option
    if is_in_you_win_or_you_lose_option:
        pass
    else:
        # Récupération de la lettre
        letter = letter_entry.get().upper()
        alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']

        # Vérifications
        if letter in missing_letters:  # Vérification de la présence de la lettre dans les lettres manquantes
            # Suppression de la lettre dans les lettres manquantes et mise à jour du mot avec les lettres manquantes
            founded_letters += letter
            missing_letters.remove(letter)
            e = 1
            word_with_missing_letters = word[0]
            for _ in itertools.repeat(None, len(word) - 2):
                if word[e] in founded_letters:
                    word_with_missing_letters += word[e]
                else:
                    word_with_missing_letters += '_ '
                e += 1
        elif not len(letter) == 1:  # Vérification de la longueur de ce qui a été entré dans l'entrée "letter_entry"
            pass
        elif letter not in alphabet:  # Vérification de la présence de la lettre dans l'alphabet
            pass
        elif letter not in errors and letter not in word[1:(len(word)-1)]:  # Vérification de la présence de la lettre
            # dans les érreurs
            errors.append(letter)
            hanged += 1
            error = True

        # Mise à jour de l'interface graphique
        label_title.pack_forget()
        label_subtitle.pack_forget()
        label_subtitle1.pack_forget()
        label_subtitle2.pack_forget()
        label_subtitle3.pack_forget()
        letter_entry.pack_forget()
        button.pack_forget()
        label_errors.pack_forget()
        label_subtitle4.pack_forget()

        if '_' not in word_with_missing_letters:
            # Gagné !
            is_in_you_win_or_you_lose_option = True
            label_title = Label(frame1, text='PyPendu', font=('Tahoma', 40), bg='orange')
            label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
            label_subtitle1 = Label(frame1, text=word_with_missing_letters, font=('Tahoma', 10), bg='orange')
            label_subtitle2 = Label(frame1, text="Vous avez gagné !", font=('Tahoma', 10), bg='orange')
            label_subtitle3 = Label(frame1, text="", font=('Tahoma', 10), bg='orange')
            button = Button(frame1, text='Quitter', font=('Tahoma', 10), bg='darkorange', command=lambda: quit(0))
            label_subtitle4 = Label(frame1, text="", font=('Tahoma', 10), bg='orange')
            button2 = Button(frame1, text='Recommencer', font=('Tahoma', 10), bg='darkorange',
                             command=lambda: restart())

            label_title.pack()
            label_subtitle.pack()
            label_subtitle1.pack()
            label_subtitle2.pack()
            button.pack()
            label_subtitle4.pack()
            button2.pack()
        elif hanged == 10:
            # Perdu !
            is_in_you_win_or_you_lose_option = True
            label_title = Label(frame1, text='PyPendu', font=('Tahoma', 40), bg='orange')
            label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
            label_subtitle1 = Label(frame1, text=word_with_missing_letters, font=('Tahoma', 10), bg='orange')
            label_subtitle2 = Label(frame1, text="Vous avez perdu... Le mot était {}".format(word), font=('Tahoma', 10),
                                    bg='orange')
            label_subtitle3 = Label(frame1, text="", font=('Tahoma', 10), bg='orange')
            button = Button(frame1, text='Quitter', font=('Tahoma', 10), bg='darkorange', command=lambda: quit(0))
            label_subtitle4 = Label(frame1, text="", font=('Tahoma', 10), bg='orange')
            button2 = Button(frame1, text='Réessayer', font=('Tahoma', 10), bg='darkorange', command=lambda: restart())

            label_title.pack()
            label_subtitle.pack()
            label_subtitle1.pack()
            label_subtitle2.pack()
            button.pack()
            label_subtitle4.pack()
            button2.pack()
        else:
            # Continuer la partie
            label_title = Label(frame1, text='PyPendu', font=('Tahoma', 40), bg='orange')
            label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
            label_subtitle1 = Label(frame1, text=word_with_missing_letters, font=('Tahoma', 10), bg='orange')
            label_subtitle2 = Label(frame1, text="Entrez une lettre :", font=('Tahoma', 10), bg='orange')
            letter_entry = Entry(frame1, font=('Tahoma', 10), bg='orange')
            label_subtitle3 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
            button = Button(frame1, text='OK', font=('Tahoma', 10), bg='darkorange', command=lambda: letter_entered())
            if error:
                label_subtitle4 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
                if len(errors) == 1:
                    label_errors = Label(frame1, text='Erreur : {}'.format(", ".join(errors)), font=('Tahoma', 10),
                                         bg='orange')
                else:
                    label_errors = Label(frame1, text='Erreurs : {}'.format(", ".join(errors)), font=('Tahoma', 10),
                                         bg='orange')

            label_title.pack()
            label_subtitle.pack()
            label_subtitle1.pack()
            label_subtitle2.pack()
            letter_entry.pack()
            label_subtitle3.pack()
            button.pack()
            if error:
                label_subtitle4.pack()
                label_errors.pack()


def restart():
    """ Redémarre la partie """
    global letter_entry, label_subtitle1, label_subtitle2, frame1, label_title, label_subtitle, label_subtitle3,\
        button, label_subtitle4, label_errors, button2, word_with_missing_letters, missing_letters, founded_letters,\
        hanged, errors, error, is_in_you_win_or_you_lose_option
    label_title.pack_forget()
    label_subtitle.pack_forget()
    label_subtitle1.pack_forget()
    label_subtitle2.pack_forget()
    label_subtitle3.pack_forget()
    letter_entry.pack_forget()
    button.pack_forget()
    label_errors.pack_forget()
    label_subtitle4.pack_forget()
    button2.pack_forget()
    word_with_missing_letters = ''
    missing_letters = []
    founded_letters = []
    hanged = 0
    errors = []
    error = False

    label_title = Label(frame1, text='PyPendu', font=('Tahoma', 40), bg='orange')
    label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='orange')

    label_title.pack()
    label_subtitle.pack()

    label_subtitle1 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    label_subtitle2 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    label_subtitle3 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    label_subtitle4 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    label_errors = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
    is_in_you_win_or_you_lose_option = False
    choose_word()


def about():
    """ Ouvre une fenêtre 'à propos' """
    about_window = Tk()
    about_window.title("À propos de PyPendu")
    about_window.geometry("800x200")
    about_window.minsize(800, 200)
    about_window.maxsize(800, 200)
    about_window.iconbitmap('icon.ico')
    about_window.config(background='orange')
    about_title = Label(about_window, text='PyPendu', font=('Tahoma', 40), bg='orange')
    author_subtitle = Label(about_window, text='Créé par {}'.format(__author__), font=('Tahoma', 10), bg='orange')
    version_subtitle = Label(about_window, text='Version {}'.format(__version__), font=('Tahoma', 10), bg='orange')
    open_source_mention = Label(about_window, text="Copyleft, opensource", font=('Tahoma', 10), bg='orange')
    subtitle = Label(about_window, text='', bg='orange')
    wiki_label = Label(about_window, text='Vérifier les mises à jour', font="Tahoma 10 underline", bg='orange',
                       foreground='blue', cursor='hand2')
    about_title.pack()
    author_subtitle.pack()
    version_subtitle.pack()
    open_source_mention.pack()
    subtitle.pack()
    wiki_label.pack()
    wiki_label.bind("<Button-1>",
                    lambda e: webbrowser.open_new(r"https://github.com/jd-develop/PyPendu/releases"))
    about_window.mainloop()


# Initialisation du programme (définition des variables)
missing_letters = []
founded_letters = []
hanged = 0
word = ''
word_with_missing_letters = ''
errors = []
error = False
is_in_you_win_or_you_lose_option = False

# Création de la fenêtre
main_window = Tk()
main_window.title("PyPendu")
main_window.geometry("900x500")
main_window.minsize(900, 500)
main_window.iconbitmap('icon.ico')
main_window.config(background='orange')

# Création d'une frame
frame1 = Frame(main_window, bg='orange')

letter_entry = Entry(frame1)
button = Button(frame1)
button2 = Button(frame1)


# Création de texte à l'interieur de la frame
label_title = Label(frame1, text='PyPendu', font=('Tahoma', 40), bg='orange')
label_subtitle = Label(frame1, text='', font=('Tahoma', 10), bg='orange')

label_title.pack()
label_subtitle.pack()

label_subtitle1 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
label_subtitle2 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
label_subtitle3 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
label_subtitle4 = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
label_errors = Label(frame1, text='', font=('Tahoma', 10), bg='orange')
canvas = Canvas(frame1)

# Ajout d'un menu
menu_bar = Menu(main_window)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Soumettre cette lettre', command=lambda: letter_entered())  # Bouton OK
file_menu.add_command(label='À propos de PyPendu', command=lambda: about())  # à propos du programme
file_menu.add_command(label='Quitter', command=lambda: quit(0))
menu_bar.add_cascade(label='Options', menu=file_menu)
main_window.config(menu=menu_bar)

# Choisir le mot
choose_word()
