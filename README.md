# Passeport Informatique Télécoms (PIT), 2021

Voir aussi https://moodle.insa-lyon.fr/,
Mes cours,
Télécommunications,
Télécommunications,
TC-3,
TC-3-I-PIT.

## 1. Faire connaissance

2 à 4h

### Informatique

La Société Informatique de France a proposé la définition suivante de l'informatique :

> L’informatique est la science et la technique de la représentation de l’information d’origine artificielle ou naturelle, ainsi que des processus algorithmiques de collecte, stockage, analyse, transformation, communication et exploitation de cette information, exprimés dans des langages formels ou des langues naturelles et effectués par des machines ou des êtres humains, seuls ou collectivement.

L’informatique n’est donc pas juste la science des ordinateurs, c'est une science et une technique qui peut s’appliquer à des supports matériels très différents, 
dont [l’ordinateur](https://www.lemonde.fr/blog/binaire/2014/04/01/que-diriez-vous-dordinateur/), mais pas seulement. 

Comme entrée en matière, vous êtes invité à lire ce [billet](https://www.lemonde.fr/blog/binaire/2015/08/27/linformatique-privee-dordinateur/) ainsi que les textes qui lui sont liés.

### Ordinateur

L'ordinateur reste néanmoins une machine de prédilection en informatique. Vous allez certainement utiliser une telle machine pendant des heures, des jours, voire des années. Cela mérite bien de savoir, au moins sommairement, de quoi est fait un ordinateur.  

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

Mais pourquoi le binaire ? C'est d'abord un compromis entre la quantité de symboles et la quantité de chiffres nécessaires pour représenter un nombre possible. En décimal, il nous faut 4 chiffres pour réprésenter 1024, c'est pas mal. Mais nous avons dix symboles possibles 0, 1, ... 9 pour chaque chiffre. C'est beaucoup et difficile à matérialiser avec une bonne résistance au bruit. En unaire, on n'a au contraire qu'un seul symbole. C'est facile à matérialiser (une pierre, une diode allumée, etc.), mais il nous faut 1024 chiffres pour représenter 1024 ! En binaire, on a deux symboles, généralement notées 0 et 1. C'est encore facile à matérialiser (tension inférieure ou supérieure à un seuil, courant électrique qui passe ou ne passe pas, etc.) et il ne faut que log2(1024) = 10 chiffres pour représenter 1024, ce qui est tout à fait raisonnable compte-tenu de la petitesse et la complexité des circuits électroniques actuellement construits.

### Fichier et système de fichiers

Le terme [système de fichiers](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_fichiers) désigne à la fois l'organisation des informations mémorisées sur les périphériques de stockage de l'ordinateur et la vue logique hiérarchique présentée à l'utilisateur. Les informations sont stockées dans des paquets appelées *fichiers*, écrits dans un certain *format*, c'est-à-dire selon une certaine manière d'encoder les informations en binaire. Ces fichiers peuvent être aussi bien du texte, une page web, un morceau de musique, une photo de vacance, un script, un logiciel, etc. Un *répertoire* regroupe des fichiers ou d'autres répertoires, ce qui aboutit à une hiérarchie de fichiers. C'est le [chemin d'accès](https://en.wikipedia.org/wiki/Path_(computing)) qui permet de localiser un fichier de la hiérarchie. 

Vous maîtrisez ce qu'est un fichier, un répertoire (= dossier), un chemin d'accès, un lien symbolique, le répertoire courant ? Si oui, passez à la suite. 
Si non, jouez à [Find your path](http://demo710.univ-lyon1.fr/FYP/) pour vous familiariser avec la représentation des chemins dans les environnements de type unix. Si vous avez joué déjà 20 minutes et que vous ne voyez pas le rapport avec ce qui précède, contactez l'enseignant. 

### Interpréteur de commandes

La [console](https://doc.ubuntu-fr.org/console) est une interface textuelle qui permet à un utilisateur de demander à l'ordinateur de réaliser certaines tâches, uniquement à l'aide d'un écran et d'un clavier. Sur un serveur sans interface graphique la console est généralement directement accessible au démarrage. Sur une machine grand public, on utilise un [émulateur de terminal](https://doc.ubuntu-fr.org/terminal), c'est-à-dire un programme qui émule une console dans une interface graphique.

L'utilisateur n'a qu'à écrire par le clavier la *commande* qu'il souhaite que le système d'exploitation exécute. Quand une ligne de commande est écrite, elle est passée à l'interpréteur de lignes de commande (=*shell*), qui la décortique et se charge de la faire exécuter en interaction avec le système d'exploitation. Il existe de nombreux interpréteurs de lignes de commandes, qui fonctionnent tous plus ou moins de la même façon. Nous considérerons que ce sera *Bourne-Again Shell* (bash) dans le reste du document. C'est le shell associé par défaut à un compte d'utilisateur dans Ubuntu. Si vous utilisez un autre système d'exploitation, voyez comment utiliser un émulateur de terminal, ainsi que bash, ou vous adapter à un shell similaire. Cette [page de l'astus](https://tcastus.github.io/TChelp/Travailler_a_distance/1-Terminal.html) peut vous aider. 

## 2. Passer aux commandes

4h

Une *commande* est une instruction qu'un utilisateur envoie au système d'exploitation de l'ordinateur pour lui faire exécuter un *programme*. Un *processus* est une instance d'un programme en train de s'exécuter, autrement dit une tâche en cours. A chaque commande donnée, le programme correspondant est exécuté, un nouveau processus est créé. Il peut s'agir de supprimer des fichiers, d'accéder à des répertoires, de modifier des droits d'accès, etc. Il existe un grand nombre de commandes et les actions précises de chacune d'elles sont de plus conditionnées par un ensemble plus ou moins grand de paramètres.

- Commandes : 
  - [commandes basiques](https://doc.ubuntu-fr.org/tutoriel/console_ligne_de_commande),
  - [commandes à connaitre](https://doc.ubuntu-fr.org/commande_shell) (uniquement les sections 1, 2 et 3 à ce stade),
- Fonctionnalités supplémentaires : 
  - [redirections et enchainements](https://doc.ubuntu-fr.org/projets/ecole/scripting/initiation_au_shell) (sections 2, 3 et 5),
  - [variables d'environnement](https://doc.ubuntu-fr.org/variables_d_environnement),
  - gérer les [processus](https://www.tuteurs.ens.fr/unix/processus.html).

Téléchargez et décompressez cette [archive](bash/bash_exercises.tar.bz2), puis traitez les questions listées dans le fichier `instructions.md`.

Vous avez des difficultés ? Faites un tour sur la [FAQ](FAQ.md). 

Faites le quizz de validation bash sur Moodle.

![Relevant XKCD](https://imgs.xkcd.com/comics/tar.png)

Enfin, en ces temps où le travail à distance prend de l'ampleur, nous vous demandons de connaître le protocole de communication [SSH](https://doc.ubuntu-fr.org/ssh) et de maitriser les commandes *ssh* (section 2.1, 2.3) et *scp* (section 2.4). La documentation de l'astus peut vous aider à vous connecter à des machines de l'INSA depuis chez vous. D'abord, ce connecter au [VPN](https://tcastus.github.io/TChelp/Travailler_a_distance/2-VPN.html), puis lancer une session [SSH](https://tcastus.github.io/TChelp/Travailler_a_distance/3-ConnexionDistanteSSH.html).

Faites le quizz de validation ssh sur Moodle.

Bravo, vous êtes maintenant ceinture verte de bash. Vous voulez devenir ceinture noire ? Apprenez à maitriser [l'art de la ligne de commande](https://github.com/jlevy/the-art-of-command-line/blob/master/README-fr.md).

## 3. Editeur de texte

de 1h à 4h

Vous allez bientôt écrire vous-mêmes des programmes. Ces programmes ne seront d'abord rien d'autre que du texte sauvegardé dans un fichier. Pour écrire du texte, vous avez besoin avant tout d'un *éditeur de texte*, un logiciel permettant d'écrire et modifier un texte. De même que vous êtes libres d'utiliser le système d'exploitation qui vous convient, vous êtes libres d'utiliser l'éditeur de texte qui vous convient, sous réserve que vous sachiez les utiliser bien sûr... Néanmoins, nous vous demandons de savoir utiliser, à un niveau débutant au moins, un éditeur particulier : *vi*. Pourquoi lui ? Il fait parti probablement de tous les systèmes d'exploitation de type unix, car il est léger, rapide, économe en ressource, puissant en fonctionnalité. Vous devrez peut-être un jour vous connecter à un serveur unix en mode console et modifier un fichier de configuration. Vous serez alors content de savoir ouvrir le fichier avec vi, passer en mode insertion et sauvegarder vos modifications. Vous vous remercierez d'avoir regarder attentivement les liens suivants : 

- [tutoriel](https://openclassrooms.com/en/courses/43538-reprenez-le-controle-a-laide-de-linux/42693-vim-lediteur-de-texte-du-programmeur),
- [FAQ](http://www.linux-france.org/article/appli/vi/faq/vifaq.html),
- [cheatsheet](https://www.csee.umbc.edu/courses/undergraduate/202/spring07/Resources/RiceViCheatSheet.pdf) (vous en trouverez pleins d'autres sur le web),
- [vi ou vim ?](https://doc.fedora-fr.org/wiki/Diff%C3%A9rences_entre_vi_et_vim). Note : dans Ubuntu, comme dans d'autres systèmes, vim est le seul éditeur de type vi installé par défaut, et donc, vi démarre vim par défaut. Ce n'est pas un problème car tout ce qui est dans vi est disponible dans vim.   

Téléchargez et décompressez cette [archive](vi/vi_exercises.zip), puis traitez les questions listées dans le fichier `vi.pdf`.

Faites le quizz de validation sur Moodle.

Bravo, vous êtes maintenant ceinture jaune de vi. Vous voulez devenir ceinture noire ? Utilisez-le pour écrire tous vos programmes.  

## 4. Programmation bash

4h

Apprenez à [écrire un script bash](https://doc.ubuntu-fr.org/tutoriel/script_shell).

C'est très utile quand on veut automatiser certaines tâches comme convertir le format de chaque image d'un répertoire, remplacer une chaine de caractère par une autre dans tous les fichiers et noms de fichier d'un projet de développement, etc. Ne prenez pas peur, ces [exercices](bash/scripts.md) sont plus simples. Une fois écrits, testés, téléversez une archive de vos scripts sur Moodle. 

## 5-7. Programmation python

de 8h à 12h

Vous allez maintenant apprendre à programmer dans un langage de haut niveau. Il a l'avantage d'être facile à prendre en main par un débutant et d'être puissant dans le sens où quelques lignes assez lisibles permettront au programmeur de faire effectuer un traitement complexe. Il est très utilisé, entre autres domaines, dans le web côté serveur ([Django](https://www.djangoproject.com/), [Flask](https://flask.palletsprojects.com/)), en calcul scientifique ([Numpy](https://numpy.org/), [Matplotlib](https://matplotlib.org/), [Sympy](https://www.sympy.org/), [SageMath](https://www.sagemath.org/)), en machine learning ([Pytorch](https://pytorch.org/)), voire en administration système, remplaçant alors bash. 

- [niveau débutant](https://zestedesavoir.com/tutoriels/799/apprendre-a-programmer-avec-python-3/)
- niveau avancé, documentation officielle :
  - [tutoriel](https://docs.python.org/fr/3/tutorial/index.html)
  - [HOWTOs](https://docs.python.org/fr/3/howto/index.html)
  - [FAQ](https://docs.python.org/fr/3/faq/programming.html)
 
Attention, il y a différentes versions de python qui cohabitent encore ça et là. Python 2 est maintenant obsolète. Veillez à programmer en python 3 et vérifier la version des extraits de code que vous glanez sur le web.

Pour chacun des items suivants, faites les exercices. 

- (5) [Premiers pas](python/1.pdf)
- (6) [Manipuler des objets](python/2.pdf)
- (7) [Créer des objets](python/3.pdf)

Répondez aux questionnaires de validation sur Moodle.

## 8. Git, Github

4h

- [Git](https://tcastus.github.io/TChelp/Git_GitHub/1-Git.html)
- [Github](https://tcastus.github.io/TChelp/Git_GitHub/2-GitHub.html)

Téléchargez cette [archive](python/python_project.tar.bz2). Elle contient des fichiers à compléter pour réaliser un programme python capable de résoudre une grille de Sudoku. L'objectif n'est pas tant de coder complètement un tel programme, mais de développer à plusieurs (au moins deux !) et se familiariser avec git et github.

Vous pouvez aussi contribuer à améliorer ce document (voir la dernière section). 

## Suite de la formation et logiciels utilisés en TC

Selon un [rapport de l'académie des sciences](https://www.academie-sciences.fr/pdf/rapport/rads_0513.pdf), l'informatique s'articule autour de quatre piliers fondamentaux : information, algorithme, langage, machine.

Au cours du premier semestre, vous approfondirez les piliers algorithme, langage, machine, respectivement en ALG, ELP et ARC. Le pilier information sera graduellement renforcé au cours de la formation transversalement aux domaines informatique, réseaux et systèmes de communications.  

Afin que vous puissiez anticiper l'installation ou la prise en main d'un outil, voici une [liste des logiciels](logicielsTC.md) utilisés au cours de la formation (en cours de construction). 

## Jeux

Vous voulez allier l'utile à l'agréable ? Continuez à vous familliariser avec les outils précédents tout en vous amusant ? Alors voici une sélection de jeux :

- plateforme de code [codingame](https://www.codingame.com/) pour résoudre des énigmes de programmation dans le langage que vous choisissez.
- jeux d'aventure / wargame pour maîtriser bash :
  - [bashcrawl](https://gitlab.com/slackermedia/bashcrawl)
  - [terminus](http://web.mit.edu/mprat/Public/web/Terminus/Web/main.html)
  - [clmystery](https://github.com/veltman/clmystery)
  - [bandit](https://overthewire.org/wargames/bandit/)

## Remerciements

Difficile de savoir qui est à l'origine de telle selection de ressources, tel exercice, telle archive, repris et parfois modifiés au fil des ans. Merci à tous les collègues ayant contribué de près ou de loin à ce document et plus généralement à tous les créateurs de contenus vers lesquels les liens conduisent. Nous traçons les contributions uniquement depuis la diffusion publique du document. 

## Contributions depuis la rentrée 2020

Vous avez vu une coquille sur ce document, repéré un lien cassé ou voudriez corriger ça ? Vous aimeriez mentionner une ressource essentielle ? Vous voudriez ajouter une FAQ en fin de document ? Excellente idée ! Très facile ! Ce document est sur github. Vous cliquez sur `Fork` pour avoir une copie de ce projet sur votre compte. Ensuite vous faites `git clone` pour télécharger ce projet sur votre machine. Faites vos modifications, poussez-les sur le serveur avec `git push`, puis proposez-moi d'intégrer vos modifications en faisant une *pull request*. N'oubliez pas d'ajouter votre nom à la liste des contributeurs.

Contributeurs par ordre alphabétique :
- Titouan-joseph Revol
- Tristan Roussillon

