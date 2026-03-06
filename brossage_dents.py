# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime 

DB_PATH = "brossage_dents.db"


def init_db(db_path=DB_PATH):
    """Crée la base et la table si elles n'existent pas."""
    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS suivi_brossage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_reponse TEXT NOT NULL,
            brossages INTEGER NOT NULL CHECK (brossages IN (0, 1, 2))
        )
        """
    )
    conn.commit()
    conn.close()


def demander_brossage():
    """Demande à l'utilisateur une valeur valide (0, 1 ou 2)."""
    while True:
        try:
            reponse = raw_input(
                "Combien de fois vous êtes-vous brossé les dents aujourd'hui ? (0, 1 ou 2) : "
            ).strip()
        except NameError:
            # Python 3
            reponse = input(
                "Combien de fois vous êtes-vous brossé les dents aujourd'hui ? (0, 1 ou 2) : "
            ).strip()

        if reponse in {"0", "1", "2"}:
            return int(reponse)

        print("Entrée invalide. Merci de saisir uniquement 0, 1 ou 2.")


def enregistrer_reponse(brossages, db_path=DB_PATH):
    """Enregistre la réponse de l'utilisateur dans la base SQLite."""
    maintenant = datetime.now().isoformat().split('.')[0]
    conn = sqlite3.connect(db_path)
    conn.execute(
        "INSERT INTO suivi_brossage (date_reponse, brossages) VALUES (?, ?)",
        (maintenant, brossages),
    )
    conn.commit()
    conn.close()


def main():
    init_db()
    brossages = demander_brossage()
    enregistrer_reponse(brossages)
    print("Merci ! Votre réponse a bien été enregistrée dans la base de données.")


if __name__ == "__main__":
    main()
