# Catalogue image downloader
###### tags: `data scraping`

## Installation
Dans le terminal, exécuter chacune des commandes suivantes, suivant l'OS de votre ordinateur.

- Mac
    ```
    pip install virtualenv
    venv env
    source env/bin/activate
    pip install -R requirements.txt
    ```
- Linux
    ```
    sudo apt install python3-tk
    pip install virtualenv
    venv env
    source env/bin/activate
    pip install -R requirements.txt
    ```
- Windows
    ```
    pip install virtualenv
    venv env
    env\Scripts\activate
    pip install -R requirements.txt
    ```

## Exécution
- S'assurer que votre terminal est bien dans le dossier `catalogue-image-downloader`.
- Exécuter le script suivant
  - Mac / Linux
    ```
    source env/bin/activate
    python download_and_rename_images.py
    ```
  - Windows
    ```
    env\Scripts\activate
    python download_and_rename_images.py
    ```
- Sélectionnez le fichier CSV de data scraping
- Et hop, vos images devraient être téléchargées au bon nom (auto-assignable via Focus) dans le même répertoire.