# FAQ

## `bash_exercices` et autres commandes 

- Je veux commencer les exercices sur bash mais je ne comprends pas où aller.

> Après avoir téléchargé et décompresssé [l'archive](bash/bash_exercises.tar.bz2), vous avez un nouveau répertoire appelé `bash_exercices`. Dans le terminal, vous devez faire en sorte que ce répertoire soit le répertoire courant, soit en utilisant la commande `cd`, soit en sélectionnant `ouvrir dans un terminal` à partir de l'explorateur de fichier, si celui-ci le permet. Tous les chemins d'accès écrits dans le fichier `instructions.md` sont des chemins *relatifs* au répertoire `bash_exercices`. Par exemple, quand il est question du répertoire `corge/grault/wyzzy/`, cela signifie que `bash_exercices` contient le répertoire `corge` qui contient `grault` qui contient `wyzzy`.

- Comment afficher les 5 premières lignes du fichier `corge/longerfile.txt` ?

> Regardez les commandes `head` et `tail`.

- Dans la section *Variable*, je ne comprends pas la question 5.  

> Cette question vous demande de modifier la variable `PATH` afin de rendre le script `runanywhere.sh` utilisable comme commande depuis n'importe quel répertoire. Cela nécessite quelques explications. Quand on tape une commande, bash se charge de trouver un fichier exécutable correspondant à cette commande et de l'exécuter. Par exemple, quand vous tapez `ls`, le fichier `ls`, généralement situé dans `/bin`, va être exécuté. Pour rechercher les fichiers exécutables, bash ne regarde que dans quelques répertoires listés dans la variable d'environnement `PATH`. Si vous affichez le contenu de cette variable par `echo $PATH`, vous allez certainement voir, entre autres, le répertoire `/bin`. Les répertoires sont séparés par des `:`. Maintenant que vous avez un script `runanywhere.sh` que vous avez rendu exécutable vous pouvez en faire véritablement une nouvelle commande en ajoutant le répertoire contenant ce script à la variable `PATH`. En général, on écrit `PATH=$PATH:cheminVersLeRepertoire` car on veut *ajouter* ce répertoire à la liste existante et ne surtout pas perdre la liste existante.

- Comment je peux faire exécuter une commande à partir d'un résultat de `find` ?

> Dans la section *Archivage*, on vous demande de regroupez vos fichiers `.log` dans un nouveau répertoire et vous avez la bonne idée d'utiliser `find` pour obtenir la liste des fichiers `.log`. Par exemple `find . -name *.log`. Mais la commande `mv` ne lit rien sur l'entrée standard et attend la liste des fichiers à déplacer comme arguments. Heureusement `find` a une option `exec` qui résoud ce problème. Il suffit de faire suivre l'option `exec` par la commande que l'on souhaite voir exécuter, en ajoutant néanmoins deux symboles spéciaux : `{}` qui représente les fichiers trouvés par `find` et un symbole de terminaison, qui peut être soit `\;`, soit `+` (sachant que `+` doit être immédiatement précédé par `{}`). Si le symbole de terminaison est `\;`, la commande sera exécutée *successivement* pour *chacun* des fichiers trouvés, si c'est `+`, la commande sera exécutée *une seule fois* avec la *liste* des fichiers trouvés.

- Je n'arrive pas à utiliser `scp` ; j'ai pourtant vérifé la bonne utilisation de toutes les options...

> SSH est un protocole permettant d'établir une communication sécurisée sur un réseau entre sa machine locale et une machine distante. Les machines ont deux rôles différents : la machine locale est le *client*, tandis que la machine distante est le *serveur*. Ce protocole est utilisé pour différents cas d'usage, par différentes commandes. La commande `ssh` permet d'accéder au shell de la machine distante et faire comme si on travaillait directement dessus. La commande `scp` permet de transférer des fichiers (ou répertoires) d'une machine à l'autre. Ce sont donc deux cas d'usage à bien distinguer. Pour taper la commande `scp`, vous devez être dans le shell de la machine locale et non dans le shell de la machine distante, comme vous pouvez l'être après avoir utilisé la commande `ssh`. Si vous venez de taper la commande `ssh`, il faut clore la connexion avant de taper la commande `scp`. 