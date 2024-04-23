README en français
Générateur de Sudoku avec Flask

Ce projet est une application web Flask qui génère des grilles de Sudoku personnalisées en format PDF. L'utilisateur peut entrer le nombre de cases à supprimer et obtenir un PDF contenant quatre grilles de Sudoku. Les grilles générées sont valides et suivent les règles du Sudoku.
Fonctionnalités

    Génération de grilles de Sudoku valides
    Création de fichiers PDF avec quatre grilles de Sudoku
    Interface web simple pour définir le nombre de cases à supprimer

Prérequis

Pour exécuter ce projet localement, vous devez avoir Python et Flask installés. Voici les instructions pour installer Flask et autres dépendances.

bash

# Créer et activer un environnement virtuel
python -m venv .venv
source .venv/bin/activate  # Sur MacOS/Linux
.venv\Scripts\activate  # Sur Windows

# Installer Flask et les dépendances
pip install flask reportlab

Utilisation

    Clonez ce dépôt GitHub.
    Accédez au répertoire du projet.
    Activez votre environnement virtuel si nécessaire.
    Lancez l'application Flask.

bash

flask run

    Ouvrez un navigateur web et accédez à http://127.0.0.1:5000/.
    Entrez le nombre de cases à supprimer et cliquez sur "Générer".
    Téléchargez le fichier PDF contenant les grilles de Sudoku générées.



Inglish
Sudoku Generator with Flask

This project is a Flask web application that generates custom Sudoku grids in PDF format. The user can enter the number of cells to be removed and receive a PDF containing four Sudoku grids. The generated grids are valid and follow the rules of Sudoku.
Features

    Generation of valid Sudoku grids
    Creation of PDF files with four Sudoku grids
    Simple web interface to set the number of cells to remove

Prerequisites

To run this project locally, you need to have Python and Flask installed. Here are the instructions for installing Flask and other dependencies.

bash

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # On MacOS/Linux
.venv\Scripts\activate  # On Windows

# Install Flask and dependencies
pip install flask reportlab

Usage

    Clone this GitHub repository.
    Navigate to the project directory.
    Activate your virtual environment if needed.
    Start the Flask application.

bash

flask run

    Open a web browser and go to http://127.0.0.1:5000/.
    Enter the number of cells to remove and click "Generate".
    Download the PDF file containing the generated Sudoku grids.
