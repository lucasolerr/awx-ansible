import csv
import requests

# URL de base pour l'API REST d'AWX
base_url = "http://localhost:7080/api/v2/inventories/{id_of_your_inventory}/"

# Identifiant et mot de passe pour l'authentification avec l'API REST d'AWX
auth = ("your_username", "your_password")

# En-tête pour l'authentification
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

# Nom du fichier CSV contenant les nouveaux hôtes
csv_file = "hosts.csv"

# Lecture des données du fichier CSV
with open(csv_file, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Récupération des informations sur l'hôte à partir de la ligne courante
        host_name = row["host_name"]
        host_ip = row["host_ip"]
        # Construction de la requête pour ajouter un nouvel hôte à AWX
        data = {
            "name": host_name,
            "description": "",
            "enabled": True,
            "variables": "ansible_host: " + host_ip + "\nansible_user: {your_ansible_user}"
        }
        url = base_url + "hosts/"
        # Envoi de la requête pour ajouter le nouvel hôte
        response = requests.post(url, auth=auth, headers=headers, json=data)
        # Vérification de la réponse pour déterminer si l'ajout de l'hôte a réussi
        if response.status_code == 201:
            print(f"Hôte {host_name} ajouté avec succès")
        else:
            print(f"Échec de l'ajout de l'hôte {host_name}: {response.text}")
