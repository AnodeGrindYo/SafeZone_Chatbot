# Titre du Projet : Assistance Chatbot pour les Victimes de Harcèlement Sexuel en Milieu Professionnel

## Introduction
- Application web responsive dédiée aux entreprises, visant à apporter un soutien immédiat et anonyme aux victimes de harcèlement sexuel via un chatbot intelligent.

## Choix Stratégiques
- **Appli Web** : Accessibilité universelle sans nécessité d'installation, accessible sur tout appareil connecté, ce qui encourage l'utilisation et garantit une aide accessible en tout temps.
- **Chatbot basé sur LLM** : Fournit des interactions naturelles, compréhensibles et empathiques, cruciales pour les sujets sensibles comme le harcèlement sexuel.


## Technologies Clés
- **Frontend** : Bootstrap pour une conception responsive.
- **Backend** : FastAPI pour une API performante et fiable.
- **Chatbot Engine** : LLaMA-2-CPP (portage C++ de LLaMA-2) pour une interaction utilisateur avancée.

## Architecture
- Conception modulaire avec une classe `Chat` dédiée pour encapsuler l'interaction avec LLaMA-2-CPP.
- Backend développé en FastAPI, garantissant performances et facilité de développement.
- Utilisation de scripts Bash pour l'automatisation de l'installation et de la configuration du serveur.

## Avantages de LLaMA-2-CPP
- **Optimisation pour Dialogue** : Modèles affinés spécifiquement pour les cas d'utilisation de dialogue.
- **Efficacité et Performance** : Plus rapide et efficace par rapport aux modèles de taille plus grande.
- **Open Source** : Flexibilité et accessibilité pour la recherche et l'exploitation commerciale.

## Déploiement Local
- Utilisation de WSL Debian pour exécuter le serveur localement.
- Exposition du serveur sur Internet via ngrok pour un accès facile et sécurisé.
- Scripts Bash pour une installation, compilation et configuration simplifiée de LLaMA-2-CPP.

## Documentation et Réplicabilité
- Instructions complètes fournies dans le fichier `README.md` pour l'installation et la mise en ligne sur un serveur Debian via nginx.
- Scripts Bash pour automatiser l'installation des dépendances, la compilation et la configuration de LLaMA-2-CPP, et le lancement du serveur.

## Performances et évolutivité
- FastAPI offre une performance élevée et une scalabilité.
- LLaMA-2-CPP permet des interactions rapides et précises avec les utilisateurs.
- Possibilité d'étendre le chatbot avec des fonctionnalités supplémentaires et d'intégrer d'autres technologies au besoin.

## Sécurité et Confidentialité
- Respect des normes de sécurité et de confidentialité dans le traitement des données sensibles.
- Conception attentive pour garantir la sécurité des utilisateurs et la protection de leurs informations.

## Impact social
- Fournit un soutien crucial aux victimes de harcèlement sexuel en milieu professionnel.
- Encourager une culture d'entreprise sécuritaire et soutenir la sensibilisation et la prévention du harcèlement.

## Avantages pour les Entreprises
- **Réponse Immédiate** : Le chatbot offre une réponse immédiate aux employés, fournissant un support initial en cas de harcèlement.
- **Anonymat** : Permet aux victimes de parler librement, ce qui peut encourager la déclaration d'incidents.
- **Éducation** : Fournit des informations précieuses sur la manière de traiter le harcèlement sexuel, éduquant à la fois les employés et les employeurs.
- **Économies de Coûts** : Réduit la charge sur les ressources humaines en fournissant des réponses automatisées tout en gardant une interaction humaine grâce à l'intelligence du LLM.
- **Amélioration de la Culture d'Entreprise** : Contribuer à une culture d'entreprise sécuritaire et respectueuse en apportant de l'aide et de l'éducation autour du harcèlement sexuel.
- **Conformité Légale** : Aide les entreprises à respecter les obligations légales en matière de prévention et de traitement du harcèlement sexuel.


## Conclusion
- Projet innovant qui allie technologies modernes et impact social positif.
- Solution robuste et fiable qui répond à un problème sociétal critique avec une approche technologique avancée.