#!/usr/bin/env python3

import os
import paramiko

# Création d'une nouvelle instance SSHClient
client = paramiko.SSHClient()

# Ajout de la clé SSH de la machine distante au "known_hosts"
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connexion à la machine distante
client.connect(hostname='10.50.33.21', username='user-ansible', password='password')

# Ouverture d'un SFTP session
sftp = client.open_sftp()

# Chemin du fichier local à exporter
local_directory = './'

# Chemin de destination sur la machine distante
remote_directory = './logs'

# Boucle pour parcourir les fichiers dans le répertoire
for filename in os.listdir(local_directory):
    if filename.endswith(".logs"):
        # Chemin du fichier local à exporter
        local_file = os.path.join(local_directory, filename)

        # Chemin de destination sur la machine distante
        remote_file = os.path.join(remote_directory, filename)

        # Transfert du fichier
        sftp.put(local_file, remote_file)

# Fermeture de la session SFTP
sftp.close()

# Fermeture de la connexion SSH
client.close()
