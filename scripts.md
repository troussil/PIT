# Exécution et arguments

## Exercice 0

Créer le script nommé `test1` et comportant les instructions suivantes :
```bash
echo script test1
pwd
ls -l
```
Donner à ce fichier une autorisation d'exécution avec `chmod u+x test1`.
Déclencher l'exécution avec
- la commande `./test1`,
- la commande `test1`, après avoir ajouté dans la variable d'environnement `PATH` le chemin d'accès au répertoire dans lequel se trouve le script `test1`.

## Exercice 1

Ecrire un script nommé `la` qui affiche tous les fichiers du répertoire fourni en argument.

## Exercice 2

Ecrire le script `saisie` suivant :
```bash
echo "saisie : "
read a b
echo "a=$a"
echo "b=$b"
```
Tester dans les cas suivants :
- `saisie`
- `saisie toto`
- `saisie toto titi`
- `saisie toto titi tata`

# Choix et boucles

## Exercice 3

Ecrire un script nommé `existe` qui admet deux paramètres, un nom de fichier et un nom de répertoire, respectant la description fonctionnelle suivante :  
- s'il n'y a aucun argument, le script doit indiquer sur la sortie standard quel est l'usage attendu du script,
- s'il n'y a qu'un argument représentant un fichier, faire la recherche dans le répertoire courant,
- s'il y a deux arguments, un fichier, suivi d'un répertoire, indiquer si le fichier donné se trouve dans le répertoire donné ou non. 
- s'il y a trop d'arguments ou si le premier (resp. second) n'est pas un fichier (resp. répertoire), écrire un message d'erreur.
Vous utiliserez les structures de contrôle `case` pour le nombre d'arguments, `if` pour s'assurer que les chaines représentent des fichiers ou répertoires, ainsi que les commandes `echo`, `test`, `ls`, `grep`.

## Exercice 4

Ecrire un script nommé `utilisateur` qui recherche plusieurs numéros d'utilisateurs dans le fichier `/etc/passwd` (les numéros d'utilisateur se trouvent dans le troisième champs).
- si aucun paramètre n'est fourni, on affiche la liste des numéros d'utilisateur,
- sinon, pour chaque numéro fourni, on indique si celui-ci se trouve dans le fichier `/etc/passwd` ou non.
Vous serez amenés à utiliser `echo`, `cut`, `grep`, ainsi que les structures de contrôle `if` et `for`.  

## Exercice 5

Ecrire un script nommé `question` qui admet en entrée une question, la pose à l'utilisateur et attend sa réponse.
- si la réponse est `o` (oui), le script retourne `0` avec la commande `exit`.
- si la réponse est `n` (non), le script retourne immédiatement `1`,
- si la réponse est autre, le script repose la question.
Vérifier le code renvoyé par le script avec la commande `echo $?`.

## Exercice 6

Ecrire un script nommé `effaceTout` qui utilise le script `question` pour le dialogue avec l'utilisateur. Il admet en entrée une liste de chemins. Pour tous les chemins correspondant à des fichiers, il demande à l'utilisateur de confirmer leur suppression et le supprime dans le cas d'une réponse positive. Pour tous les chemins correspondant à des répertoires, il demande à l'utilisateur de confirmer la suppression de tout son contenu et déclenche cette opération dans le cas d'une réponse positive.

# Signaux

Un processus peut se protéger contre un [signal](https://fr.wikipedia.org/wiki/Signal_(informatique)) en donnant une instruction à faire à la place de ce qu'il doit faire normalement à la réception du signal en question (en général, se terminer). Pour mettre en oeuvre ce mécanisme à l'exécution d'un script bash, on utilise la commande `trap`.

## Exercice 7

Ecrire un script nommé `pas10pas12` qui se met en attente active (boucle infinie) et affiche "signal 10" (resp. "signal 12") à la réception du signal 10 (resp. 12).
Pour envoyer des signaux à votre script en cours d'exécution, utiliser les commande `ps` et `kill`.

## Exercice 8 (optionnel)

Ecrire un script en attente perpétuelle de signaux. Le signal 10 (resp. 12) aura la valeur 0 (resp. 1) dans la [table ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange#Description). Quand une lettre de l'alphabet (minuscule) est reconnue, celle-ci est affichée sur la sortie standard.
Note : si vous êtes avancés, utilisez des fonctions pour la traduction signaux - caractères.  