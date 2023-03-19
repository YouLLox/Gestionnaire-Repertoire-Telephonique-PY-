#########################################################
##                                                     ##
## Projet : Création d'un répertoire téléphonique      ##
## Programme Directory                                 ##
## Auteurs : YouLLox et une autre personne (Anonyme)   ##
## Spécialité NSI, classe de 1ère                      ##
## Version : V1.0 du 16/12/2022                        ##
##                                                     ##
#########################################################

# $$$$$$$\ $$\                             $$\
# $$  __$$\\__|                            $$ |
# $$ |  $$ $$\ $$$$$$\  $$$$$$\  $$$$$$$\$$$$$$\   $$$$$$\  $$$$$$\ $$\   $$\
# $$ |  $$ $$ $$  __$$\$$  __$$\$$  _____\_$$  _| $$  __$$\$$  __$$\$$ |  $$ |
# $$ |  $$ $$ $$ |  \__$$$$$$$$ $$ /       $$ |   $$ /  $$ $$ |  \__$$ |  $$ |
# $$ |  $$ $$ $$ |     $$   ____$$ |       $$ |$$\$$ |  $$ $$ |     $$ |  $$ |
# $$$$$$$  $$ $$ |     \$$$$$$$\\$$$$$$$\  \$$$$  \$$$$$$  $$ |     \$$$$$$$ |
# \_______/\__\__|      \_______|\_______|  \____/ \______/\__|      \____$$ |
#                                                                   $$\   $$ |
#                                                                   \$$$$$$  |
#                                                                    \______/

# Importation d'un package pour changer la couleur des "print"
from simple_chalk import *  #  Importation d'un package pour colorer les print
from time import sleep  # Importation d'un package pour mettre un temps d'attente

with open("directory", "a") as f:  # Création et ouverture du fichier
  print(chalk.green(
    "Le répertoire a bien été crée !"))  # Envoi un message de confirmation
  f.close()  # Ferme le fichier texte "directory"
with open("pro", "w") as t:
  t.write("normal")
  t.close()

###########################################################
################## MENU DE NAVIGATION ####################
#########################################################

list_number = ["1", "2", "3", "4", "5", "6", "7", "8", "9",
               "0"]  # Création d'une liste repertoriant tous les chiffres
list_lettre = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]

list_lettre_up = [
  "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
  "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]

print(
  chalk.blue(
    "Bienvenue sur le menu de navigation de votre répertoire téléphonique !\n\nAvant d'intéragir avec notre système, n'oubliez pas de lire attentivement les instructions et les conditions générales d'utilisation !\n\nConditions générales d'utilisation : https://sites.google.com/view/directory-cassaigne/accueil"
  ))  # Poste un message "bleu" de présentation du système ainsi que les cgu


def cgu_q():  # Création d'une fonction dont le nom est "cgu_q"
  """
    Permet d'accepter ou non les conditions générales d'utilisation.
    """
  cgu = "Non"  # Création d'une variable cgu et affectation de "Non" à celle-ci
  sleep(2)  # Attend 2 secondes pour poursuivre
  while cgu != "Oui":  # Boucle obligeant l'acceptation des cgu
    cgu = input(
      "Acceptez-vous nos conditions générales d'utilisation ? Veuillez répondre par \"Oui\" ou \"Non\" !\n Votre réponse : "
    )  # Demande à l'utilisateur si il accepte les cgu
    if cgu != "Oui":  # Condition si l'utilisateur répond autre chose que "Oui" à la question
      print(
        chalk.red(
          "Pour utiliser le répertoire téléphonique, vous devez accepter nos conditions générales d'utilisation !"
        )
      )  # Poste un message "rouge" informant l'utilisateur qu'il est obligé d'accepter les cgu
    else:  # Si l'utilisateur répond "Oui"...
      print(
        chalk.green(
          "Merci d'avoir accepté nos conditions générales d'utilisation.\n Bienvenue parmi nous !"
        )
      )  # Poste un message "vert" remerciant l'utilisateur d'avoir accepté les cgu
  print(chalk.yellow("\n\nChargement des donnés...")
        )  # Affiche un message "jaune" simulant un chargement de donnés
  sleep(3)  # Attend 3 secondes pour continuer


def password(
):  # Création d'un fonction permettant la configuration d'un mot de passe pour sécuriser le système
  """
    Permet la configuration d'un mot de passe afin de sécuriser l'espace de gestion.
    """
  print(
    chalk.yellow(
      "Afin de sécuriser votre espace, nous vous suggerons de configurer un mot de passe !\n\n"
    ))  # Poste un message "jaune" proposant la configuration d'un mot de passe
  password_q = input(
    # Demande à l'utilisateur si il souhaite mettre en place un mot de passe pour sécuriser son espace
    "Souhaitez-vous ajouter un mot de passe à votre espace ? Veuillez répondre par \"Oui\" ou \"Non\" !\n Votre réponse : "
  )
  if password_q != "Oui":  # Condition "si l'utilisateur répond autre chose que "Oui""
    with open(
        "database", "w"
    ) as d:  # Ouvre le fichier database en mode écriture (écrase le fichier)
      d.write("undefined")  # Ecrit "undefined" dans le fichier database
  if password_q == "Oui":  # Condition "si l'utilisateur répond "Oui"
    caracters = "undefined"  # Création et affectation de "undefined" à "caracters"
    while caracters != "Ok !":  # Boucle obligeant la valeur "Ok !" à la variable "caracters"
      pseudo = input(
        chalk.blueBright("Veuillez entrer un identifiant : ")
      )  # Demande à l'utilisateur l'identifiant avec lequel il souhaite se connecter
      caracters = "undefined"  # Affecte "undefined" à la variable "caracters"
      pseudo = pseudo.lower(
      )  # Converti tous les caractères de pseudo en minuscules
      if (len(pseudo) >= 5) and ((' ' in pseudo) == False) and (
          pseudo != "null"
      ):  # Condition "si le pseudo contient 5 caractères, aucun espace et qu'il n'est pas null"
        caracters = "Ok !"  # Affecte "Ok !" à "caracters"
        with open(
            "database", "w"
        ) as d:  # Ouvre le fichier "database" sur position d'écritre (ecrase les infos précédentes)
          # Ecrit dans "database" le pseudo renseigné
          d.write(pseudo)
      else:  # Si le pseudo ne contient pas 5 caracères et/ou un espece et/ou est null
        print(
          chalk.red(
            "🚨 - Votre pseudo doit contenir minimum 5 caractères, aucun espace !"
          ))  # Envoi un message d'erreur
      if caracters == "Ok !":  # Vérifie si tous les paramètres son respectés
        # Création et affectation de "undefined" à la variable "caracters"
        caracters = "undefined"
        while caracters != "Ok !":  # Boucle obligeant le respect de tous les paramètres
          caracters = "undefined"  # Affectation de "undefined" à la variable "caracters"
          password = input(
            chalk.blueBright("Veuillez entrer un mot de passe : ")
          )  # Demande à l'utilisateur le mot de passe qu'il souhaite configurer
          number = "undefined"  # Création et affectation de "undefined" à la  variable "number"
          for elmt in password:  # Boucle récupérant tous les elements de la liste chaîne de caractères "password"
            if elmt in list_number:  # Condition 'Si l'element en question est dans la liste "list_number"'
              number = "Ok !"  # Affectation de "Ok !" à la variable "number"
          # Condition 'Si le mot de passe contient 5 caractères, aucun espace, au moins 1 numéro et n'est pas égal à "null"''
          if (len(password) >= 5) and ((' ' in password) == False) and (
              number == "Ok !") and (password != "null"):
            caracters = "Ok !"  # Affectation de "Ok !" à la variable
            # Ouvre le fichier "database" sur position d'écriture (ne supprime pas ce qu'il y a dans le fichier)
            with open("database", "a") as d:
              # Ecrit dans le fichier "database" le mot de passe
              d.write(" " + password)
          else:  # Condition "Si le mot de passe ne contient pas 5 caractères et/ou un espace et/ou aucun chiffre"
            print(
              chalk.red(
                "🚨 - Votre mot de passe doit contenir minimum 5 caractères, aucun espace et au moins 1 chiffre !"
              ))  #  Envoi un message d'erreur


def menu():  #  Création de la fonction "menu"
  """
    Permet l'affichage du menu principal.
    """
  menu_q = "undefined"  #  Création et affectation de "undefined" à la variable "menu_q"
  menu_q = input(
    chalk.gray(
      "\n\nBienvenue sur le menu principal !\n\n Pour naviguer, intéragissez avec les numéros ci-dessous.\n\n0 - 🛑・Se déconnecter\n1 - ✅・Créer un nouveau contact\n  ↳ ⭐・Contact Professionnel\n  ↳ 🧔・Contact Personnel\n2 - 🗑️・Supprimer un contact\n3 - 🔍・Rechercher un contact\n4 - ⚙️・Paramètres\n5 - 🗝️・Panel Admin\n Votre réponse : "
    )
  )  #  Envoi le menu principal et permet d'intéragir via les différents numéros

  if menu_q == "0":  #  Condition 'Si "menu_q" est égal à "0"'
    menu_zero()  #  Joue la fonction "menu_zero()"
  elif menu_q == "1":  #  Condition 'Si "menu_q" est égal à "1"'
    menu_one()  #  Joue la fonction "menu_one()"
  elif menu_q == "2":  #  Condition 'Si "menu_q" est égal à "2"'
    menu_two()  #  Joue la fonction "menu_two()"
  elif menu_q == "3":  #  Condition 'Si "menu_q" est égal à "3"'
    menu_three()  #  Joue la fonction "menu_three()"
  elif menu_q == "4":  #  Condition 'Si "menu_q" est égal à "4"'
    menu_four()  #  Joue la fonction "menu_four()"
  elif menu_q == "5":  #  Condition 'Si "menu_q" est égal à "5"'
    menu_admin()  #  Joue la fonction "menu_admin()"
  else:  # Condition 'Si "menu_q" est ni égal à 0, 1, 2, 3, 4, 5'
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  #  Envoie un message d'erreur
    menu()  #  Joue la fonction "menu()"


def menu_admin():  #  Création de la fonction "menu_admin"
  """
    Permet d'afficher le menu d'administration du système.
    """
  admin_password = input(
    chalk.red("🔒 - Veuillez entrer le mot de passe : "
              ))  #  Demande le mot de passe pour accéder au panel admin
  mdp_admin = "I love NSI"  # Création et affectation de "I love NSI" à la variable "mdp_admin"
  if admin_password == mdp_admin:  #  Condition 'Si "admin_password" est égal à "mdp_admin"'
    print(chalk.green(
      "🔓 - Mot de passe correct !"))  #  Envoi un message de confirmation
    sleep(2)  #  Attend 2 secondes puis joue la suite du code
    menu_admin_access()  #  Joue la fonction "menu_admin_access()"
  else:  #  Condition 'Si la valeur rensiegnée n'est pas égale au mot de passe
    sleep(2)  #  Attend 2 secondes puis joue la suite du code
    print(
      chalk.red("🔒 - Le mot de passe est incorrect, vérouillage du système !")
    )  #  Envoi un message disant que le mot de passe renseigné est incorrect
    sleep(3)  # Attend 3 secondes puis joue la suite du code
    while True:  #  Boucle infinie (# Ici beaucoup de chats sont mort ;) )
      print(chalk.red("🚨 Alerte ! Intrusion détectée ! 🚨")
            )  #  Envoi un message alertant d'une potentielle intrusion


def menu_admin_access():  #  Création de fonction
  """
    Permet d'afficher le panel d'administration.
    """
  menu_admin = input(
    chalk.gray(
      "Bienvenue sur le panel d'administration !\n\n Pour naviguer, intéragissez avec le numéros ci-dessous.\n\n0 - 🍃・Quitter le panel\n1 - ⭐・Activer ou désactiver le premium\n Votre réponse : "
    ))  #  Demande de choisir un numéro parmis ceux proposés
  if menu_admin == "0":  #  Condition 'Si "menu_admin" est égla à "0"'
    menu()  #  Joue la fonctione "menu()"
  elif menu_admin == "1":  #  Condition 'Si "menu_admin" est égal à "1"'
    menu_admin_one()  #  Joue la fonction "menu_admin_one()"
  else:  # Condition 'Si "menu_admin" n'est pas égal a 0 ou 1'
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_admin_access()  #  Joue la fonction "menu_admin_access()"


def menu_admin_one():  #  Création de fonction
  """
    Permet d'afficher le panel de gestion des premiums.
    """
  prime = input(
    chalk.gray(
      "Bienvenue sur le panel de gestion des premiums !\n\n Pour naviguer, intéragissez avec le numéros ci-dessous.\n\n0 - 🔙・Retour\n1 - ⭐・Activer le premium\n2 - 🧸・Désactiver le premium\n Votre réponse : "
    ))  #  Demande de choisir un numéro parmis ceux proposés
  if prime == "0":  #  Condition 'Si "prime" est églal à "0"'
    menu_admin_access()  #  Joue la variable "menu_admin_access()"
  elif prime == "1":  #  Condition 'Si "prime" est égal à "1"'
    menu_prim_activ()  #  Joue la fonction "menu_prim_activ()"
  elif prime == "2":  # Condition 'Si "prime" est égal à "2"'
    menu_prim_unactiv()  #  Joue la fonction "menu_prim_unactiv()"
  else:  #  Condition 'Si "prime" n'est pas égal à 0, 1 ou 2
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_admin_one()  # Joue la fonction "menu_admin_one()"


def menu_prim_activ():  #  Création de fonction
  """
  Permet d'activer le premium.
  """
  with open(
      "pro", "w"
  ) as f:  #  Ouvre le fichier "pro" en position écriture (écrase ce qu'il y avait)
    f.write("premium")  #  Ecrit dans le fichier "pro"
    print(chalk.green("✅ - Le premium a bien été activé !")
          )  #  Envoi un message de confirmation
    returne = "undefined"  #  Création et affectation de "undefined" à la variable "returne"
  while returne != "":  #  Boucle reposant la question tant que l'utilisateur n'a pas appuyé sur "Enter"
    returne = input(
      chalk.blue(
        "\n\nAppuyez sur \"Enter\" pour retourner au panel de gestion des premiums !"
      ))  #  Envoi une question permettant de revenir au menu précédent
    if returne == "":  #  Condition 'Si returne est égal à ""
      menu_admin_one()  # Joue la fonction "menu_admin_one()"


def menu_prim_unactiv():  #  Création de fonction
  """
  Permet de désactiver le premium.
  """
  with open(
      "pro", "w"
  ) as f:  #  Ouvrir le fichier "pro" en position d'écriture (écrase ce qu'il y avait)
    f.write("normal")  #  Ecrit "normal" dans le fichier "pro"
    print(chalk.red("✅ - Le premium a bien été désactivé !")
          )  #  Envoi un message de confirmation
    returne = "undefined"  #  Création de la variable "returne" avec affectation de "undefined"
  while returne != "":  #  Boucle repose la question tant "returne" est égal à ""
    returne = input(
      chalk.blue(
        "\n\nAppuyez sur \"Enter\" pour retourner au panel de gestion des premiums !"
      ))  #  Propose de revenir au menu précédent en appuyant sur "Enter"
    if returne == "":  #  Condition 'Si "returne" est égal à ""
      menu_admin_one()  #  Joue la fonction "menu_admin_one()"


def menu_four():  # Création de fonction
  """
    Permet d'afficher le menu des paramètres
    """
  menu_settings = input(
    chalk.gray(
      "Bienvenue sur le menu de paramétrage !\n\n Pour naviguer, intéragissez avec le numéros ci-dessous.\n\n0 - 🔙・Retour\n1 - 🔐・Changer vos identifiants\n Votre réponse : "
    ))  # Propose d'intéragir avec le menu à l'aide des différents numéros
  if menu_settings == "0":  # Condition 'Si "menu_settings" est égal à "0"
    menu()  #  Joue la fonction "menu()"
  elif menu_settings == "1":  #  Condition 'Si "menu_settings" est égal à "1"
    menu_settings_one()  #  Joue la fonction "menu_settings_one()"
  else:  #  Condition 'Si "menu_settings" est ni égal à 0 et ni à 1
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_four()  #  Joue la fonction "menu_four()"


def menu_settings_one():  #  Création de fonction
  """
    Permet de modifier son identifiant
    """
  caracters = "undefined"  # Création et affectation de "undefined" à "caracters"
  while caracters != "Ok !":  # Boucle obligeant la valeur "Ok !" à la variable "caracters"
    pseudo = input(
      chalk.blueBright("Veuillez entrer un identifiant : ")
    )  # Demande à l'utilisateur l'identifiant avec lequel il souhaite se connecter
    caracters = "undefined"  # Affecte "undefined" à la variable "caracters"
    pseudo = pseudo.lower(
    )  # Converti tous les caractères de pseudo en minuscules
    if (len(pseudo) >= 5) and ((' ' in pseudo) == False) and (
        pseudo != "null"
    ):  # Condition "si le pseudo contient 5 caractères, aucun espace et qu'il n'est pas null"
      caracters = "Ok !"  # Affecte "Ok !" à "caracters"
      with open(
          "database", "w"
      ) as d:  # Ouvre le fichier "database" sur position d'écritre (ecrase les infos précédentes)
        d.write(pseudo)  # Ecrit dans "database" le pseudo renseigné
    else:  #  Condition 'Si le pseudo ne possède pas 5 caracères et/ou un espace et/ou aucun chiffre
      print(
        chalk.red(
          "🚨 - Votre pseudo doit contenir minimum 5 caractères, aucun espace !"
        ))  #  Envoi un message d'erreur
    if caracters == "Ok !":  # Condition 'Si "caracters" est égal à "Ok !"
      caracters = "undefined"  # Affectation de "undefined" à la variable "caracters"
      while caracters != "Ok !":  #  Boucle obligeant le respect des différents paramètres
        caracters = "undefined"  #  Affectation de "undefined" à la variable "caracters"
        password = input(chalk.blueBright("Veuillez entrer un mot de passe : ")
                         )  #  Demande à l'utilisateur le nouveau mot de passe
        number = "undefined"  #  Création et affectation de "undefined" à la variable "number"
        for elmt in password:  #  Vérifie tous les elements de password
          if elmt in list_number:  #  Condition "Si elmt contient au moins un nombre"
            number = "Ok !"  #  Affectation de "Ok !" à la variable "number"
        if (len(password) >= 5) and (
          (' ' in password) == False
        ) and (number == "Ok !") and (
            password != "null"
        ):  #  Condition 'Si le mot de passe contient 5 caractères ou plus, aucun espace, un chiffre minimum et n'est pas égal à "null"
          caracters = "Ok !"  #  Affectation de "Ok !" à la variable "caracters"
          with open(
              "database", "a"
          ) as d:  #  Ouvre le fichier database en position d'écriture (n'éfface pas ce qu'il y avait)
            d.write(
              " " + password
            )  #  Ecrit le mot de passe renseigné dans le fichier database
        returne = "undefined"  #  Création et affectation de "undefined" à la variable "returne"
        while returne != "":  #  Boucle reposant la question tant que la réponse n'est pas égale à ""
          returne = input(
            chalk.blue(
              "\n\nAppuyez sur \"Enter\" pour retourner au menu de paramétrage !"
            ))  #  Pose une question permettant de retourner au menu précédent
          if returne == "":  #  Condition 'Si returne est égal à ""'
            menu_four()  #  Joue la fonction menu_four()
        else:  #  Condition 'Si le mot de passe ne contient pas 5 caractères et/ou un espace et/ou aucun chiffre
          print(
            chalk.red(
              "🚨 - Votre mot de passe doit contenir minimum 5 caractères, aucun espace et au moins 1 chiffre !"
            ))  #  Envoi un messge d'erreur


def menu_three():  #  Création de fonction
  """
    Permet d'afficher le menu de recherche de contact.
    """
  menu_search = input(
    chalk.gray(
      "Bienvenue sur le menu de recherche de contact !\n\n Pour naviguer, intéragissez avec le numéros ci-dessous.\n\n0 - 🔙・Retour\n1 - 🔍・Rechercher un contact\n Votre réponse : "
    )
  )  #  Affiche un menu de navigation et pose une question afin de pouvoir intéragir avec les numéros
  if menu_search == "0":  #  Condition 'Si menu_search est égal à "0"
    menu()  #  Joue la fonction "menu()"
  elif menu_search == "1":  #  Condition 'Si menu_search est égal à "1"
    menu_search_one()  #  Joue la fonction menu_search_one()
  else:  #  Condition 'Si menu_search est ni égal à 0 et ni à 1
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_three()  #  Joue la fonction menu_three()


def menu_search_one():  #  Création de
  """
    Permet de rechercher un contact.
    """
  name = input(
    chalk.blueBright("Veuillez entrer le nom ou le numéro du contact : ")
  )  #  Demande le nom ou le numéro du contact à rechercher
  with open("directory",
            "r") as f:  #  Ouvre le fichier directory en position de lecture
    lines = f.readlines(
    )  #  Divise le fichier par ligne et classe chaque ligne dans une liste
    total = 0  #  Création et affectation de 0 à la variable total
    for elmt in lines:  #  Recupère et traite chaque elements de la liste lines
      if name in elmt:  #  Condition 'Si le nom donné est présent dans les contacts'
        print(
          chalk.green(
            "✅ - Le contact a bien été trouvé, chargement des donnés...")
        )  #  Envoi un message de chargement
        total += 1  #  Ajoute 1 à la variable total
        sleep(2)  #  Attend 2 secondes puis passes à la suite du code
        if "💼" in elmt:  #  Condition 'Si 💼 est présent dans elmt
          star = elmt.split(
          )  #  Sépare tous les elements en fonction de leurs espaces puis met chaque element dans une liste
          star.remove(
            star[0])  #  retire l'element dont l'index est 0 dans la liste star
          star = ' '.join(
            star
          )  #  Transforme la liste star en chaîne de caractères et mettant un espace entre chaque element
          print(
            chalk.grey("Contact : " + star + "\nProfessionnel : "),
            chalk.greenBright("Oui")
          )  #  Affiche le contact recherché si il existe et spécifie si il est professionnel
        else:  #  Condition 'Si le nom reneigné n'existe pas dans l'element'
          print(
            chalk.grey("Contact : " + elmt + "Professionnel : "),
            chalk.red("Non")
          )  #  Affiche le contact recherché si il existe et spécifie si il est professionnel
        returne = "undefined"  #  Création et affectation de "undefined" à la variable "returne"
        while returne != "":  #  Boucle repose la question tant que returne n'est pas égal à ""
          returne = input(
            chalk.blue(
              "\n\nAppuyez sur \"Enter\" pour retourner au menu de recherche !"
            )
          )  #  Demande si l'utilisateur veut retourner en arrière, il doit confirmer en appuyant sur enter
          if returne == "":  #  Condition 'Si returne est égal à ""
            menu_three()  #  Joue la fonction menu_three()
    if total == 0:  #  Condition 'Si total est égal à 0'
      returne = "undefined"  #  Affectation de "undefined" à la variable returne
      print(
        chalk.red("🚨 - Aucun contact n'est trouvable sous ce nom ou numéro !")
      )  # Envoi un message d'erreur
      while returne != "":  #  Boucle obligeant l'utilisateur à répondre par un enter pour poursuivre
        returne = input(
          chalk.blue(
            "\n\nAppuyez sur \"Enter\" pour retourner au menu de recherche !")
        )  #  Demande d'appuyer sur enter pour retourner au menu précédent
        if returne == "":  #  Condition 'Si returne est égal à ""
          menu_three()  #  Joue la fonction menu_three()


def menu_two():  #  Création de fonction
  """
    Permet d'afficher le menu de suppression de contact.
    """
  menu_delete = input(
    chalk.gray(
      "Bienvenue sur le menu de suppression de contact !\n\n Pour naviguer, intéragissez avec le numéros ci-dessous.\n\n0 - 🔙・Retour\n1 - 🗑️・Supprimer un contact\n Votre réponse : "
    )
  )  #  Propose à l'utilisateur de naviguer dans le menu en intéragissant avec les différents numéros
  if menu_delete == "0":  #  Condition 'Si menu_delete est égal à "0"
    menu()  #  Joue la fonction menu()
  elif menu_delete == "1":  #  Condition  'Si menu_delete est égal à "1"'
    menu_delete_one()  #  Joue la fonction menu_delete_one()
  else:  #  Condition 'Si menu_delete est ni égal à 0 ni à 1'
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_two(
    )  #  Renvoie l'utilisateur au menu de suppression de cotact (joue la fonction menu_two())


def menu_delete_one():  #  Création de fonction
  """
    Permet de supprimer un contact par son nom ou son numéro.
    """
  name = input(
    chalk.blueBright("Veuillez entrer le nom ou le numéro du contact : ")
  )  #  Pose une question demandant le contact à supprimer
  with open("directory",
            "r") as f:  #  Ouvre le fichier directory en position de lecture
    lines = f.readlines(
    )  #  Divise le fichier par ligne et classe chaque ligne dans une liste
    total = 0  #  Création et affectation de 0 à la variable total
    with open("directory",
              "w") as t:  #  Ouvre le fichier directory en position d'écriture.
      t.write("")  #  Le contenu du fichier est écrasé
    for elmt in lines:  #  Recupère et traite chaque elements de la liste lines
      if name in elmt:  #  Condition 'Si le nom donné est présent dans les contacts
        print(chalk.green("✅ - Le contact a bien été supprimé du répertoire !")
              )  #  Envoie un message de confirmation
        total += 1
      else:
        with open(
            "directory", "a"
        ) as fw:  #  Ouvre le fichier directory en position d'écriture ajout
          fw.write(elmt)
    if total == 0:
      print(
        chalk.red("🚨 - Aucun contact n'est trouvable sous ce nom ou numéro !")
      )  #  Envoie un message d'erreur
    returne = "undefined"  #  Affectation de "undefined" à la variable returne
    while returne != "":  #  Boucle reposant la question tant que la réponse n'est pas égale à ""
      returne = input(
        chalk.blue(
          "\n\nAppuyez sur \"Enter\" pour retourner au menu de suppression de contact !"
        ))  #  Demande d'appuyer sur enter pour retourner au menu précédent
      if returne == "":  #  Condition 'Si returne est égal à ""
        menu_two(
        )  #  Renvoie l'utilisateur au menu de suppression de contact (joue la fonction menu_two())


def menu_zero():  #  Création de fonction
  """
    Permet de se déconnecter de son espace de gestion.
    """
  print(
    chalk.blue(
      "Bienvenue sur le menu de navigation de votre répertoire téléphonique !\n\n"
    ))  # Poste un message bleu de "présentation"
  connect = "undefined"  #  Affectation de "undefined" à la variable connect
  while connect != "":
    connect = input(
      chalk.blue("Appuyez sur \"Enter\" pour vous identifier !")
    )  #  Demande d'appuyer sur enter pour s'identifier et donc aller au menu suivant
  with open("database",
            "r") as d:  #  Ouvre le fichier database en position de lecture
    listdata = d.read()
    if listdata != "undefined":
      listdata = listdata.split()
      passw = listdata[0] + listdata[1]
      passw_q = "undefined"
      while passw != passw_q:
        pseudo_q = input(
          chalk.blueBright("Veuillez entrer votre identifiant : ")
        )  ###  Demande un identifiant et le stocke dans la variable pseudo_q
        password_q = input(
          chalk.blueBright("Veuillez entrer votre mot de passe : ")
        )  ###  Demande un mot de passe et le stocke dans la variable password_q
        passw_q = pseudo_q + password_q
        if passw != passw_q:  ###  'Si le pseudo et le mot de passe entrés par l'utilisateur sont différents de ceux entrés lors de l'identification'
          print(
            chalk.red("🚨 - L'identifiant ou le mot de passe est incorrect !\n")
          )  #  Envoie un message d'erreur
      menu()  #  Renvoie l'utilisateur au menu principal
    else:
      menu()


def menu_one():  #  Création de fonction
  """
    Permet d'afficher le menu de création de contact.
    """
  menu_create = input(
    chalk.gray(
      "Bienvenue sur le menu de création !\n\n Pour naviguer, intéragissez avec les numéros ci-dessous.\n\n0 - 🔙・Retour\n1 - ⭐・Contact Professionnel\n2 - 🧔・Contact Personnel\n Votre réponse : "
    )
  )  #  Envoie le menu de création de contact et permet à l'utilisateur d'intéragir via les différents numéros

  if menu_create == "2":  #  Condition 'Si "menu_create" est égal à "2"'
    menu_create_two()  #  Joue la fonction "menu_create_two()"
  elif menu_create == "1":  #  Condition 'Si "menu_create" est égal à "1"'
    menu_create_two_pro()  #  Joue la fonction "menu_create_two_pro()"
  elif menu_create == "0":  #  Condition 'Si "menu_create" est égal à "0"'
    menu()  #  Joue la fonction "menu()" et renvoie l'utilisateur au menu
  else:  #  Condition 'Si "menu_create" est ni égal à 2, ni à 1, ni à 0'
    print(chalk.red("🚨 - Veuillez choisir un des numéros du menu")
          )  # Envoi un message d'erreur
    menu_one(
    )  #  Retourne au menu de création de contact (joue la fonction menu_one())


def menu_create_two():  #  Création de fonction
  """
    Permet de créer un contact personnel.
    """
  with open("directory",
            "r") as f:  #  Ouvre le fichier directory en position de lecture
    verify = f.read(
    )  #  Permet de lire le contenu du fichier et le stocke dans la variable verify
    verif = "undefined"
    while verif != "Ok !":
      name = input(chalk.blueBright("Veuillez entrer le nom du contact : ")
                   )  #  Pose une question demandant le nom du contact à créer
      if name in verify:  #  Condition 'Si le nom renseigné existe déjà dans le fichier verify'
        print(chalk.red("🚨 - Ce contact est déjà existant ! ")
              )  #  Envoie un message d'erreur
      else:  #  Condition 'Si le nom reneigné n'existe pas dans le fichier verify'
        verif = "Ok !"
    verif = "undefined"
    while verif != "Ok !":
      number = input(
        chalk.blueBright("Veuillez entrer le numéro de téléphone : ")
      )  #  Pose une question demandant le numéro de téléphone du contact à créer
      if number in verify:  #  Condition 'Si le numéro renseigné existe déjà dans verify'
        print(chalk.red("🚨 - Ce numéro est déjà attribué à un contact !")
              )  #  Envoie un message d'erreur
      else:  #  Condition 'Si le nom reneigné n'existe pas dans le fichier verify'
        error = 0
        for elmt in number:
          if elmt in list_lettre:
            error += 1
        if error == 0:
          verif = "Ok !"
        else:
          print(
            chalk.red(
              "🚨 - Un numéro de téléphone ne peut pas contenir de lettre !"))
    with open(
        "directory",
        "a") as r:  #  Ouvre le fichier directory en position d'écriture ajout
      r.write(
        name + " " + number + " \n"
      )  #  Ecrit le nom et le numéro de contact entrés par l'utilisateur dans le fichier directory
      print(chalk.green("✅ - Le contact a bien été crée !")
            )  #  Envoie un message de confirmation
    returne = "undefined"
    while returne != "":
      returne = input(
        chalk.blue(
          "\n\nAppuyez sur \"Enter\" pour retourner au menu de création de contact !"  #  Demande d'appuyer sur enter pour retourner au menu précédent
        ))
      if returne == "":
        menu_one(
        )  #  Retourne au menu de création de contact (joue la fonction menu_one())


def menu_create_two_pro():  #  Création de fonction
  """
    Permet créer un contact professionnel.  
    """
  with open("pro", "r") as t:  #  Ouvre le fichier pro en position de lecture
    content = t.read(
    )  #  Permet de lire le contenu du fichier et le stocke dans la variable content
    if "premium" in content:  #  Condition 'Si il y a "premium" dans le fichier content'
      with open(
          "directory",
          "r") as f:  #  Ouvre le fichier directory en position de lecture
        name = f.read(
        )  #  Permet de lire le contenu du fichier et le stocke dans la variable name
        verif = "undefined"
        while verif != "Ok !":
          name_pro = input(
            chalk.blueBright("Veuillez entrer le nom du contact : ")
          )  #  Pose une question demandant le nom du contact à créer
          if name_pro in name:  #  Condition 'Si le nom renseigné existe déjà dans name'
            print(chalk.red("🚨 - Ce contact est déjà existant ! ")
                  )  #  Envoie un message d'erreur
          else:
            verif = "Ok !"
        verif = "undefined"
        while verif != "Ok !":
          number_pro = input(
            chalk.blueBright("Veuillez entrer le numéro du contact : ")
          )  #  Pose une question demandant le numéro de téléphone du contact à créer
          if number_pro in name:  #  Condition 'Si le numéro renseigné existe déjà dans name'
            print(chalk.red("🚨 - Ce numéro est déjà attribué à contact !")
                  )  #  Envoie un message d'erreur
          else:  #  Condition 'Si le numéro renseigné n'existe pas dans name'
            error = 0
            for elmt in number_pro:
              if elmt in list_lettre:
                error += 1
            if error == 0:
              verif = "Ok !"
            else:
              print(
                chalk.red(
                  "🚨 - Un numéro de téléphone ne peut pas contenir de lettre !"
                ))
        with open(
            "directory", "a"
        ) as r:  #  Ouvre le fichier directory en position d'écriture ajout
          r.write(
            "💼" + " " + name_pro + " " + number_pro + " \n"
          )  #  Ecrit le nom et le numéro de contact entrés par l'utilisateur dans le fichier directory, rajoute une valisette devant pour montrer que c'est un contact professionnel
          print(chalk.green("✅ - Le contact a bien été crée !")
                )  #  Envoie un message de confirmation
        returne = "undefined"
        while returne != "":
          returne = input(
            chalk.blue(
              "\n\nAppuyez sur \"Enter\" pour retourner au menu de création de contact !"
            ))  #  Demande d'appuyer sur enter pour retourner au menu précédent
          if returne == "":
            menu_one(
            )  #  Retourne au menu de création de contact, joue la fonction menu_one()
    else:  #  Condition 'Si il n'y a pas "premium" dans le fichier content '
      print(
        chalk.red(
          "🚨 - Vous devez être premium pour utiliser cette fonctionnalité !")
      )  #  Envoie un message d'erreur
      menu_one(
      )  #  Retourne au menu de création de contact, joue la fonction menu_one()


cgu_q()
password()
menu()
