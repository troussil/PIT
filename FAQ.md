# FAQ

## `bash_exercices`

- Je veux commencer les exercices sur bash mais je ne comprends pas où aller.

> Après avoir téléchargé et décompresssé [l'archive](bash/bash_exercises.tar.bz2), vous avez un nouveau répertoire appelé `bash_exercices`. Dans le terminal, vous devez faire en sorte que ce répertoire soit le répertoire courant, soit en utilisant la commande `cd`, soit en sélectionnant `ouvrir dans un terminal` à partir de l'explorateur de fichier, si celui-ci le permet. Tous les chemins d'accès écrits dans le fichier `instructions.md` sont des chemins *relatifs* au répertoire `bash_exercices`. Par exemple, quand il est question du répertoire `corge/grault/wyzzy/`, cela signifie que `bash_exercices` contient le répertoire `corge` qui contient `grault` qui contient `wyzzy`.

- Comment afficher les 5 premières lignes du fichier `corge/longerfile.txt` ?

> Regardez les commandes `head` et `tail`.

- Dans la section *Variable*, je ne comprends pas la question 5.  

> Cette question vous demande de modifier la variable `PATH` afin de rendre le script `runanywhere.sh` utilisable comme commande depuis n'importe quel répertoire. Cela nécessite quelques explications. Quand on tape une commande, bash se charge de trouver un fichier exécutable correspondant à cette commande et de l'exécuter. Par exemple, quand vous tapez `ls`, le fichier `ls`, généralement situé dans `/bin`, va être exécuté. Pour rechercher les fichiers exécutables, bash ne regarde que dans quelques répertoires listés dans la variable d'environnement `PATH`. Si vous affichez le contenu de cette variable par `echo $PATH`, vous allez certainement voir, entre autres, le répertoire `/bin`. Les répertoires sont séparés par des `:`. Maintenant que vous avez un script `runanywhere.sh` que vous avez rendu exécutable vous pouvez en faire véritablement une nouvelle commande en ajoutant le répertoire contenant ce script à la variable `PATH`. En général, on écrit `PATH=$PATH:cheminVersLeRepertoire` car on veut *ajouter* ce répertoire à la liste existante et ne surtout pas perdre la liste existante.

- Comment je peux faire exécuter une commande à partir d'un résultat de `find` ?

> Dans la section *Archivage*, on vous demande de regroupez vos fichiers `.log` dans un nouveau répertoire et vous avez la bonne idée d'utiliser `find` pour obtenir la liste des fichiers `.log`. Par exemple `find . -name *.log`. Mais la commande `mv` ne lit rien sur l'entrée standard et attend la liste des fichiers à déplacer comme arguments. Heureusement `find` a une option `exec` qui résoud ce problème. Il suffit de faire suivre l'option `exec` par la commande que l'on souhaite voir exécuter, en ajoutant néanmoins deux symboles spéciaux : `{}` qui représente les fichiers trouvés par `find` et un symbole de terminaison, qui peut être soit `\;`, soit `+` (sachant que `+` doit être immédiatement précédé par `{}`). Si le symbole de terminaison est `\;`, la commande sera exécutée *successivement* pour *chacun* des fichiers trouvés, si c'est `+`, la commande sera exécutée *une seule fois* avec la *liste* des fichiers trouvés.

## Autres commandes et astuces 

- Je n'arrive pas à utiliser `scp` ; j'ai pourtant vérifé la bonne utilisation de toutes les options...

> SSH est un protocole permettant d'établir une communication sécurisée sur un réseau entre sa machine locale et une machine distante. Les machines ont deux rôles différents : la machine locale est le *client*, tandis que la machine distante est le *serveur*. Ce protocole est utilisé pour différents cas d'usage, par différentes commandes. La commande `ssh` permet d'accéder au shell de la machine distante et faire comme si on travaillait directement dessus. La commande `scp` permet de transférer des fichiers (ou répertoires) d'une machine à l'autre. Ce sont donc deux cas d'usage à bien distinguer. Pour taper la commande `scp`, vous devez être dans le shell de la machine locale et non dans le shell de la machine distante, comme vous pouvez l'être après avoir utilisé la commande `ssh`. Si vous venez de taper la commande `ssh`, il faut clore la connexion avant de taper la commande `scp`.

- Quotes simples, doubles, inversées... je ne m'y retrouve pas. 

> La quote simple (ou apostrophe) sert à délimiter une chaîne de caractère en désactivant toute interprétation, même si cette chaîne contient des commandes ou des variables shell. Par exemple :
```
$ variable="secret"
$ echo 'Mon mot de passe est $variable.'
Mon mot de passe est $variable.
```
> La quote double (ou guillemet) sert à délimiter une chaîne de caractère dans laquelle les noms de variable sont interprétés. Ceci est utile pour générer des messages dynamiques au sein d'un script. Par exemple :
```
$ variable="secret"
$ echo "Mon mot de passe est $variable."
Mon mot de passe est secret.
```
> La quote inversée (back-quote en anglais) sert à délimiter une chaîne de caractère dans laquelle les noms de variable *et les commandes* sont interprétés. Pour ajouter le répertoire courant à la variable `PATH`, vous pouvez par exemple écrire :
```
PATH=$PATH:`pwd`
```

## scripts bash

- Mon script ne fait pas du tout ce qu'il devrait faire / Mon script ne fait rien. Le code de mon script me parait pourtant correct...

> Attention à ne pas nommer votre script par le nom d'une commande qui existe déjà. Par exemple, `test` est un nom malheureux pour l'un de vos scripts, car il existe déjà une commande ` test`. Imaginons que vous écrivez un super script tout à fait correct mais que vous nommez `test`. Vous le rendez exécutable et oubliez ou non d'ajouter le répertoire dans lequel il se trouve au `PATH`. Vous tapez `test` et il ne se passe rien. Vous pouvez constater avec `echo $?` que la valeur de retour est `1`, ce qui indique une erreur, car la commande `test` attend habituellement un argument.

## Python

- Comment exécuter un script ?

> Vous écrivez votre programme dans un fichier, nommé par exemple `script.py`, puis tapez la commande suivante : `python3 script.py`. Par ailleurs, pour transformer votre fichier en véritable fichier exécutable, il faut lui accorder le droit d'exécution, avec par exemple la commande `chmod u+x script.py` et lui ajouter, en première ligne, le *shebang*, qui indique l'outil permettant l'interprétation du script, par exemple `#!/usr/bin/env python3`. Après avoir fait cela, vous pourrez taper plus simplement `./script.py` ou même `script.py`, si le répertoire courant est listé dans la variable d'environnement `PATH`. 

- Comment exécuter une fonction ?

> Imaginons que `func.py` contienne :
```
def sayHello():
    print("hello")
```
> Le plus simple, c'est de lancer le script puis d'entrer dans le mode interactif. Cela est possible avec l'option `-i`. Par exemple, `python3 -i func.py`. A l'issue de l'exécution du script, le prompt python, symbolisé par `>>>`, apparait et vous pouvez écrire et faire évaluer des expressions python. Si vous tapez `sayHello()`, vous verrez s'afficher `hello`. Une autre façon de faire consiste à entrer dans le mode interactif avec la commande `python3`, puis à importer les instructions et définitions contenues dans le fichier `func.py`, vu maintenant comme un *module*. Il suffit d'écrire pour cela `import func` (le nom du fichier sans l'extension `.py` donne le nom du module). Le contenu de `func.py` est alors interprété et la fonction `sayHello` devient connue. Si vous tapez `func.sayHello()`, vous verrez s'afficher `hello`. Remarquez qu'il existe d'autres directives d'import pour être autorisé à écrire plus simplement `sayHello`, par exemple `from func import sayHello`.

- Des traces s'affichent quand j'importe un module, comment les désactiver ?

> Imaginons que `func.py` contienne :
```
def sayHello():
    return "hello"
    
if sayHello() == "hello":
    print("test OK")
else:
    print("test failed")
```
> Si vous importez le module `func.py`, le résultat du test s'affichera à l'écran. Mais il est probable que vous ne vouliez pas de cet affichage, que vous ne vouliez que de la fonction `sayHello`. Or, il est possible de n'activer cet affichage que lorsque le module est exécuté comme un script en réécrivant le test ainsi :
```
if __name__ == "__main__":
    if sayHello() == "hello":
        print("test OK")
    else:
        print("test failed")
```
> En effet, quand un module est exécuté comme un script, la variable `__name__` censée contenir le nom du module contiendra la valeur `"__main__"`. 

- J'ai un message d'erreur mentionnant `NoneType`. Que se passe-t-il ?

> Python est un langage typé, mais implicitement. Si vous tapez `x = 5`, puis `type(x)`, vous obtiendrez `<class 'int'>`, indiquant que `x` est une variable de type `int`. Il y a un type spécial vide appelé `NoneType`. Si vous avez défini une fonction `func` qui ne retourne aucune valeur (vous n'avez pas utilisé le mot-clé `return`) et que vous tapez `x = func()`, puis `type(x)`, alors vous obtiendrez `<class 'NoneType'>`. Cela peut arriver si vous confondez *effet* - ce que fait la fonction, par exemple afficher quelque chose vers la sortie standard - et *valeur de retour* - ce qui est renvoyé par la fonction après qu'elle ait été appelée.  

> Pas bien :
```python
import math

def cube(x): 
  print(x*x*x)

def volSphere(radius): 
  print(4/3*math.pi*cube(radius))
```
```
>>> volSphere(3)
27
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "essai.py", line 7, in volSphere
    print(4/3*math.pi*cube(radius))
TypeError: unsupported operand type(s) for *: 'float' and 'NoneType'
```
> Bien :
```python
import math

def cube(x): 
  return x*x*x

def volSphere(radius): 
  return 4/3*math.pi*cube(radius)
```
```
>>> volSphere(3)
113.09733552923254
```

- Quel est le rôle de l'opérateur `*` (star ou splat) devant les arguments (lors de l'appel à une fonction) ou les paramètres (lors de la définition d'une fonction) ?

> Vous pouvez définir une fonction avec une liste de paramètres, éventuellement de type différent. Si lors de l'appel, vous avez une liste ou un tuple contenant l'ensemble des valeurs requises, il est possible d'utiliser l'opérateur `*` pour faire la correspondance entre les valeurs contenues dans la liste ou le tuple et les paramètres attendus sans avoir à extraire soi-même chacune des valeurs. Voici un exemple :
```python
def normL1(x, y, z):
  return abs(x)+abs(y)+abs(z)
```
```
>>> normL1(1,2,3)
6
>>> pt = [1,2,3]
>>> normL1(*pt)
6
>>> pt = (1,2,3)
>>> normL1(*pt)
6
```

> Par ailleurs, comme il peut être parfois commode de voir la liste de paramètres comme un seul objet composé, il est aussi possible d'utiliser l'opérateur `*` lors de la définition de la fonction. Voici une version beaucoup plus élégante de la fonction précédente : 
```python
def normL1(*pt):
  return sum([abs(c) for c in pt])
```
```
>>> normL1(1,2,3)
6
>>> pt = [1,2,3]
>>> normL1(*pt)
6
```

> Le même mécanisme permet de mettre en correspondance des paramètres nommés et le contenu d'un dictionnaire. Il suffit pour cela de doubler l'opérateur. En voici un exemple :
```python
def volAndMassEllipsoid(**d):
  vol = 4/3*math.pi*d["a"]*d["b"]*d["c"]
  mass = d["mu"]*vol
  return vol, mass
```
```
>>> volAndMassEllipsoid(a=1,b=1,c=2,mu=0.5)
(8.377580409572781, 4.1887902047863905)
>>> data = {"a":1,"b":1,"c":2,"mu":0.5}
>>> volAndMassEllipsoid( **data )
(8.377580409572781, 4.1887902047863905)
```
