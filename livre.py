#gestion simple dune bibliotheque
titre=input("titre du livre : ")
exemplaires = int(input("nombre dexemplaires : "))

print("livre :",titre)
print("exemplaires dispo :",exemplaires)

#emprunt dun livres
exemplaires=exemplaires-1
print("apres emprunt :",exemplaires ,"exemplaire(s) dispo(s)")