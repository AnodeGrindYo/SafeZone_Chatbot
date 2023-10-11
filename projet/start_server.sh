#!/bin/bash

# Fonction pour vérifier si workshop_env est actif
function check_venv() {
    # Vérifie si un environnement virtuel est actif
    if [[ -z "$VIRTUAL_ENV" ]]; then
        echo "Aucun environnement virtuel actif. Activation de workshop_env..."
        source ../workshop_env/bin/activate
    else
        # Vérifie si l'environnement virtuel actif est workshop_env
        if [[ "$VIRTUAL_ENV" != *"/workshop_env"* ]]; then
            echo "L'environnement virtuel actif n'est pas workshop_env. Activation de workshop_env..."
            deactivate
            source ../workshop_env/bin/activate
        else
            echo "L'environnement virtuel workshop_env est déjà actif."
        fi
    fi
}

# vérifier/activer workshop_env
check_venv

# démarrage du serveur
python -m uvicorn main:app --reload