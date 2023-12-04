import hashlib
a = 0
while a < 4:
    pwd = input("Entrez votre mot de passe : ")
    
    if len(pwd) < 8:
        print("Mot de passe trop court")
    else:
        a += 1
    
    if any(char in pwd for char in "!@#$%^&*"):
        a += 1
    else:
        print("Aucun caractère spécial trouvé")

    if any(char.isupper() for char in pwd):
        a += 1
    else:
        print("Au moins une lettre majuscule est requise")

    if any(char.islower() for char in pwd):
        a += 1
    else:
        print("Au moins une lettre minuscule est requise")

    if any(char.isalpha() or char.isdigit() for char in pwd):
        a += 1
    else:
        print("Le mot de passe ne peut contenir que des lettres et des chiffres")
    print("Mot de passe est bien Safe")
    h = hashlib.sha256(pwd.encode('UTF-8'))
    print("voici le hash", h.hexdigest())