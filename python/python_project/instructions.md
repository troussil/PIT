# Organiser votre espace de travail
1. Créez un dossier ``PIT_sudoku_<nom>_<prénom>``,
en remplaçant ``<nom>`` et ``<prénom>`` par... votre nom et prénom, respectivement.
Ce sera votre espace de travail pour ce projet.
2. Déplacez le fichier ``sudoku_db.txt`` dans votre espace de travail.
3. Créez deux sous-dossiers ``script`` et ``src``.
4. Dans le sous-dossier ``script``, créez un fichier ``compress.sh`` contenant l'instruction en bash
permettant de compresser l'intégralité de votre espace de travail **à l'exception** du fichier ``sudoku_db.txt``
dans une archive ``PIT_sudoku_<nom>_<prénom>.tar.gz``.
Ce script sera exécuté à partir du dossier parent de votre espace de travail ``PIT_sudoku_<nom>_<prénom>``.
5. Rendez ce script exécutable.
6. Déplacez les fichiers ``grid.py``, ``solver.py``, ``test_grid.py``, ``test_solver.py``
et ``solve_all_sudokus.py`` fournis dans la même archive que ces consignes dans le sous-dossier ``src``.
7. Vérifiez que les fichiers ``test_grid.py``, ``test_solver.py``
et ``solve_all_sudokus.py`` soient tous exécutables.
8. Dans le sous-dossier ``script``, créez un fichier ``install.sh`` contenant l'instruction en bash
permettant d'ajouter à la fin du fichier ``~/.bashrc`` une ligne modifiant la variable d'environnement PATH
afin de lancer les programmes en python de ce projet depuis n'importe quel autre dossier.
Ce script sera exécuté à partir de votre espace de travail ``PIT_sudoku_<nom>_<prénom>``.

# Créer un modèle pour manipuler une grille de Sudoku
1. Complétez le fichier ``grid.py`` en vous laissant guider par les docstrings.
2. Testez votre implémentation de ``SudokuGrid`` en appelant le script ``test_grid.py``.

# Créer un programme exécutable
1. Dans le sous-dossier ``src``, rédigez un programme en python appelé ``play_sudoku.py``
permettant de jouer au Sudoku en utilisant votre implémentation de ``SudokuGrid``.
+ Ce script devra accepter un argument de la ligne de commande donnant le nom du fichier et le numéro de ligne
à partir desquels initialiser la grille.
+ Si cet argument n'est pas donné, le script demandera à l'utilisateur de saisir manuellement une grille.
+ Il alternera ensuite les étapes suivantes:
	1. Affichage de l'état actuel de la grille;
	2. Saisie utilisateur de la position et de la valeur à écrire;
	3. Vérification de la validité de la saisie;
	4. Inscription dans la grille de la valeur donnée à la position donnée si valide.
2. Faites du fichier ``play_sudoku.py`` un programme exécutable.
3. Bonus / Optionnel:
Pour les plus acharnés d'entre vous, créez une classe ``SudokuGUI`` dans un nouveau fichier ``src/gui.py``
implémentant une interface graphique pour jouer au Sudoku,
en utilisant votre implémentation de ``SudokuGrid`` comme représentation interne.
Nous vous conseillons d'utiliser le paquet ``tkinter`` (backend GTK) ou bien le paquet ``PyQt5`` (backend Qt),
qu'il faudra probablement installer vous-même...
Créez ensuite un programme ``src/play_sudoku_gui.py`` (qu'il faudra aussi rendre exécutable)
mettant en œuvre cette interface graphique.

# Créer un solver pour résoudre automatiquement (et efficacement) des Sudokus
1. Complétez le fichier ``solver.py`` en vous laissant guider par les docstrings.
2. Testez votre implémentation de ``SudokuSolver`` en appelant le script ``test_solver.py``.
3. Testez les performances de votre implémentation de ``SudokuSolver``
en appelant le script ``solve_all_sudokus.py``.
