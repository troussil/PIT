# Passeport Informatique Télécoms (PIT), 2020

Voir aussi https://moodle.insa-lyon.fr/,
Mes cours,
Télécommunications,
Télécommunications,
TC-3,
TC-3-I-PIT.


## Faire connaissance

4h

### Informatique

La Société Informatique de France a proposé la définition suivante de l'informatique :

> L’informatique est la science et la technique de la représentation de l’information d’origine artificielle ou naturelle, ainsi que des processus algorithmiques de collecte, stockage, analyse, transformation, communication et exploitation de cette information, exprimés dans des langages formels ou des langues naturelles et effectués par des machines ou des êtres humains, seuls ou collectivement.

L’informatique n’est donc pas juste la science des ordinateurs, c'est une science et une technique qui peut s’appliquer à des supports matériels très différents, 
dont [l’ordinateur](https://www.lemonde.fr/blog/binaire/2014/04/01/que-diriez-vous-dordinateur/), mais pas seulement. 

Comme entrée en matière, vous êtes invité à lire ce [billet](https://www.lemonde.fr/blog/binaire/2015/08/27/linformatique-privee-dordinateur/) ainsi que les textes qui lui sont liés.

### Ordinateur

L'ordinateur reste néanmoins la machine type de l'informatique. Vous allez certainement utiliser une telle machine pendant des heures, des jours, voire des années. Cela mérite bien de savoir, au moins sommairement, de quoi est fait un ordinateur.  

Après avoir visionné cette vidéo [sur ce qu'à un ordinateur dans le ventre](https://www.lemonde.fr/blog/binaire/2017/05/31/podcast-le-ventre-de-mon-ordi/) 
et vous être renseigné, éventuellement, sur les termes employés, vous devriez savoir ce que sont des périphériques (interne/externe, entrée/sortie), des controleurs, des ports, des disques dur, des barettes de RAM, une carte graphique, une carte mère, un micro-processeur.  

### Système d'exploitation

Le *système d’exploitation* se situe à l'interface entre deux mondes : le logiciel et le matériel, composé essentiellement de mémoire, de processeur(s), de périphériques. Le rôle du système d'exploitation est d'assurer que ces éléments matériels, requis par les logiciels en cours d'exécution, soient utilisés de manière partagée, équilibrée et sûre.

Cette vidéo explique le [rôle du système d'exploitation](https://www.lemonde.fr/blog/binaire/2017/06/14/podcast-systeme-dexploitation/), notamment dans la gestion virtualisée de la mémoire, le contrôle de l'exécution via l'ordonnanceur et la médiation par les appels systèmes. 

### Codage des informations

Vous savez certainement que toutes les informations que l'ordinateur manipule sont codées en binaire, c'est-à-dire en suites de 0 et 1 : 
- les [entiers naturels et relatifs](https://fr.wikipedia.org/wiki/Syst%C3%A8me_binaire) bien sûr,
- les nombres décimaux dits [à virgule flottante](https://fr.wikipedia.org/wiki/Virgule_flottante), 
- les caractères ([ASCII](https://fr.wikipedia.org/wiki/American_Standard_Code_for_Information_Interchange#Description), [unicode](https://fr.wikipedia.org/wiki/Unicode)),
- les données multimédias (son, image, vidéo, page web...),
- ainsi que les instructions et programmes...

Lire ce billet introduisant le [codage binaire](https://interstices.info/nom-de-code-binaire/) est un minimum.

Mais pourquoi le binaire ? C'est d'abord un compromis entre nombre de symboles et nombre de chiffres pour représenter un nombre possible. En décimal, il nous faut 4 chiffres pour réprésenter 1024, c'est pas mal. Mais nous avons dix symboles possibles 0, 1, ... 9 pour chaque chiffre. C'est beaucoup et difficile à matérialiser avec une bonne résistance au bruit. En unaire, on n'a au contraire qu'un seul symbole. C'est facile à matérialiser (une pierre, une diode allumée, etc.), mais il nous faut 1024 chiffres pour représenter 1024 ! En binaire, on a deux symboles, généralement notées 0 et 1. C'est encore facile à matérialiser (tension inférieure ou supérieure à un seuil, courant électrique qui passe ou ne passe pas, etc.) et il ne faut que log2(1024) = 10 chiffres pour représenter 1024, ce qui est encore raisonnable.

### Fichier et système de fichiers

Le terme *système de fichiers* désigne à la fois [l'organisation des informations mémorisées sur les périphériques de stockage de l'ordinateur](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers) et la vue logique hiérarchique présentée à l'utilisateur. Les informations sont stockées dans des paquets appelées *fichiers*, écrits dans un certain *format*, c'est-à-dire selon une certaine manière d'encoder les informations en binaire. Ces fichiers peuvent être aussi bien du texte, une page Web, un morceau de musique, une photo de vacance, un script, un logiciel, etc. Un *répertoire* regroupe des fichiers ou d'autres répertoires, ce qui aboutit à une hiérarchie de fichiers. C'est le [chemin d'accès](https://en.wikipedia.org/wiki/Path_(computing)) qui permet de localiser un fichier de la hiérarchie. 

Vous maîtrisez ce qu'est un fichier, un répertoire (= dossier), un chemin d'accès, un lien symbolique, le répertoire courant ? Si oui, passez à la suite. 
Si non, jouez à [Find your path](http://demo710.univ-lyon1.fr/FYP/) pour vous familiariser avec la représentation des chemins dans les environnements de type unix. Si vous avez joué déjà 20 minutes et que vous ne voyez pas le rapport avec ce qui précède, contactez l'enseignant. 

### Interpréteur de commandes

La [console](https://doc.ubuntu-fr.org/console) est une interface textuelle qui permet à un utilisateur de demander à l'ordinateur de réaliser certaines tâches, uniquement à l'aide d'un écran et d'un clavier. Sur un serveur sans interface graphique la console est généralement directement accessible au démarrage. Sur une machine grand public, on utilise un [émulateur de terminal](https://doc.ubuntu-fr.org/terminal), c'est-à-dire un programme qui émule une console dans une interface graphique.

L'utilisateur n'a qu'à écrire par le clavier la *commande* qu'il souhaite que le système d'exploitation exécute. Quand une ligne de commande est écrite, elle est passée à l'interpréteur de lignes de commande (=*shell*), qui la décortique et se charge de la faire exécuter en interaction avec le système d'exploitation. Il existe de nombreux interpréteurs de lignes de commandes, qui fonctionnent tous plus ou moins de la même façon. Nous considérerons que ce sera *Bourne-Again Shell* (Bash) dans le reste du document. C'est le shell associé par défaut à un compte d'utilisateur dans Ubuntu. Si vous utilisez un autre système d'exploitation, voyez comment utiliser un émulateur de terminal, ainsi que Bash, ou vous adapter à un autre shell. Cette [page](https://github.com/TCastus/TChelp/blob/master/Travailler_a_distance/1-Terminal.md) peut vous aider. 

### Pour aller plus loin

Selon un [rapport de l'académie des sciences](https://www.academie-sciences.fr/pdf/rapport/rads_0513.pdf), l'informatique s'articule autour de quatre piliers fondamentaux :
- information,
- algorithme,
- langage,
- machine.

Au cours du premier semestre, vous approfondirez les piliers algorithme, langage, machine, respectivement en ALG, ELP et ARC. Le pilier information sera graduellement renforcé au cours de la formation transversalement aux domaines informatique, réseaux et systèmes de communications.  

## Passer aux commandes

4h

Une commande est une instruction qu'un utilisateur envoie au système d'exploitation de l'ordinateur pour lui faire exécuter une tâche. Il peut s'agir de manipuler des fichiers, d'accéder à des répertoires, de modifier des droits d'accès, etc. Il existe un grand nombre de commandes et les actions précises de chacune d'elles sont de plus conditionnées par un ensemble plus ou moins grand d'options et de paramètres.

- niveau débutant: [commandes basiques](https://doc.ubuntu-fr.org/tutoriel/console_ligne_de_commande)
- niveau intermédiaire: [commandes à connaitre](https://doc.ubuntu-fr.org/commande_shell) (uniquement les sections 1, 2 et 3 à ce stade).
- niveau avancé (non demandé): [maitriser l'art de la ligne de commande](https://github.com/jlevy/the-art-of-command-line)

Il reste des commandes très importantes en ces temps où le travaille à distance n'est pas rare :
- ssh
- scp

Vous pensez avoir bien travaillé ? Malheureusement, utiliser Bash ne se résume pas à taper des commandes mais impliquent aussi :

- des [redirections et enchainements](https://doc.ubuntu-fr.org/projets/ecole/scripting/initiation_au_shell) (sections 2, 3 et 5),
- des [variables d'environnement](https://doc.ubuntu-fr.org/variables_d_environnement),
- des [processus](https://www.tuteurs.ens.fr/unix/processus.html).

exercices, quizz

## Editeur de texte

de 30 min à 4h

## Programmation shell

4h

- [Ecrire un script shell](https://doc.ubuntu-fr.org/tutoriel/script_shell)

? https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/42867-introduction-aux-scripts-shell

exercices, quizz

## Programmation python

8h

exercices, quizz

## Git, Github

4h

- [Git](https://github.com/TCastus/TChelp/blob/master/Git_GitHub/1-Git.md)
- [Github](https://github.com/TCastus/TChelp/blob/master/Git_GitHub/2-GitHub.md)