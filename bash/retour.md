#Principales erreurs

- Attention quand vous créez vos archives (nous avons eu des archives vides) et quand vous téléversez vos archives sur Moodle (certains pensaient avoir rendu, alors que ce n'était pas le cas). Enfin, ne transmettez pas des archives au format *RAR*, du fait du caractère fermé du format, préférez un format plus standard comme `zip` ou `tar.gz`.

- Attention au *shebang*. Pour indiquer au système d'exploitation qu’il s'agit d'un script qui sera interprété par bash on écrira `#!/bin/bash` en première ligne. 

- Pour afficher une chaîne de caractère, utilisez `echo` : ne pas écrire `"chaine"`, mais `echo "chaine"`. Attention à la différence entre cote, guillements et cote inversée (cf. la [FAQ](../FAQ.md)). Par ailleurs, il n'est pas nécessaire d'entourer la valeur d'une variable entre guillements. On peut par exemple écrire `read reponse; echo $reponse`, ce n'est pas la peine d'écrire `echo "$reponse"`.  

- Attentions aux chemins. Vous devez imaginer que vous ne savez a priori pas depuis quel répertoire sera exécuté un script. Vous ne devez donc pas écrire `../../etc/passwd` (chemin relatif), mais plutôt `/etc/passwd` (chemin absolu). Au contraire, si vous savez que votre script sera livré dans un répertoire contenant aussi la hiérarchie `foo/bar`, vous n'allez pas écrire `/home/xxx/rep/foo/bar` (absolu), mais `foo/bar` (relatif).

- Lisez le contenu de `man test`. Par exemple, `-e FILE` indique si `FILE` existe ou non et peut donc être tout simplement utilisé pour savoir si un fichier donné existe dans un répertoire donné. 

- La structure `case` permet d'avoir des alternatives exprimées par des *modèles*. Voici deux exemples :

```bash
read reponse
case $reponse in
  [yYoO]*) echo "Ok, on continue";;
  [nN]*) echo "$0 arrete suite a la mauvaise volonte de l'utilisateur ;-)"
         exit 0;;
  *) echo "ERREUR de saisie"
     exit 1;;
esac
```

```bash
case $1 in
  *[!0-9]*) echo "$1 n'est pas un nombre";;
esac
```

- Une boucle qui ne fait rien pour mettre un script en attente active peut s'écrire avec l'ajout de `:` dans le bloc du `while`. Par exemple :
```bash
while [ true ]
  do
  :
  done
```	

- La commande `trap` permet de donner une instruction à faire à la place de la routine exécutée par défaut à la réception d'un type de signal donné. Elle associe, *une fois pour toute*, un type de signal et une instruction à exécuter. Ensuite, à chaque fois que le signal sera reçu, l'exécution de l'instruction associée sera exécutée. 
