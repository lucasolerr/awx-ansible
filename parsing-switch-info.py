#!/usr/bin/env python3

import pandas as pd
import os

df = pd.DataFrame(columns=["Hostname", "Vendor", "Product Name", "Serial Number", "MAC Address", "Software Revision", "Up Time", "CPU Util"])

# Spécification du répertoire contenant les fichiers à traiter
directory = 'files'

# Boucle pour parcourir les fichiers dans le répertoire
for filename in os.listdir(directory):
    data = {}
    if filename.endswith(".txt"):
        # Ouverture du fichier en lecture
        
        with open(os.path.join(directory, filename), 'r') as input_file:
            # Lecture du fichier ligne par ligne
            lines = input_file.readlines()
            # Lecture de la première ligne

        # Test sur la deuxième ligne
        if lines[1].startswith("response: Status and Counters - General System Information"):
            # Création d'un dictionnaire pour stocker les informations extraites
            for line in lines:
                # Recherche de la ligne contenant "System Name"
                if "System Name" in line:
                    # Extraction du nom d'hôte et stockage dans le dictionnaire
                    hostname = line.split(":")[1].strip()
                    data["Hostname"] = hostname
                # Recherche de la ligne contenant "Vendor"
                if "Vendor" in line:
                    # Extraction du vendeur et stockage dans le dictionnaire
                    vendor = line.split(":")[1].strip()
                    data["Vendor"] = vendor
                if "Chassis" in line:
                    # Extraction du nom du produit et stockage dans le dictionnaire
                    product_name = line.split(":")[1]
                    product_name = product_name.split("   ")[0].strip()
                    data["Product Name"] = product_name
                # Recherche de la ligne contenant "Serial Number"
                if "Serial Number" in line:
                    # Extraction du numéro de série et stockage dans le dictionnaire
                    serial_number = line.split(":")[-1].strip()
                    data["Serial Number"] = serial_number
                # Recherche de la ligne contenant "Base MAC Addr"
                if "Base MAC Addr" in line:
                    # Extraction de l'adresse MAC et stockage dans le dictionnaire
                    mac_address = line.split(":")[-1]
                    mac_address = mac_address.split("  ")[0].strip()
                    data["MAC Address"] = mac_address
                # Recherche de la ligne contenant "Software revision"
                if "Software revision" in line:
                    # Extraction de la révision logicielle et stockage dans le dictionnaire
                    software_revision = line.split(":")[1]
                    software_revision = software_revision.split("  ")[0].strip()
                    data["Software Revision"] = software_revision
                # Recherche de la ligne contenant "Up Time"
                if "Up Time" in line:
                    # Extraction de la durée de fonctionnement et stockage dans le dictionnaire
                    uptime = line.split(":")[1].strip()
                    uptime = uptime.split("  ")[0].strip()
                    data["Up Time"] = uptime
                # Recherche de la ligne contenant "CPU Util (%)"
                if "CPU Util" in line:
                    # Extraction de l'utilisation CPU et stockage dans le dictionnaire
                    cpu_util = line.split(":")[1].strip()
                    cpu_util = cpu_util.split("  ")[0].strip()
                    cpu_util += '%'
                    data["CPU Util"] = cpu_util
        else:
            # Parcours des lignes du fichier
            for line in lines:
                # Recherche de la ligne contenant "System Name"
                if "response: Hostname" in line:
                    # Extraction du nom d'hôte et stockage dans le dictionnaire
                    hostname = line.split(":")[2].strip()
                    data["Hostname"] = hostname
                # Recherche de la ligne contenant "Vendor"
                if "Vendor" in line:
                    # Extraction du vendeur et stockage dans le dictionnaire
                    vendor = line.split(":")[1].strip()
                    data["Vendor"] = vendor
                if "Product Name" in line:
                    # Extraction du nom du produit et stockage dans le dictionnaire
                    product_name = line.split(":")[1].strip()
                    data["Product Name"] = product_name
                # Recherche de la ligne contenant "Serial Number"
                if "Serial Nbr" in line:
                    # Extraction du numéro de série et stockage dans le dictionnaire
                    serial_number = line.split(":")[1].strip()
                    data["Serial Number"] = serial_number
                # Recherche de la ligne contenant "Base MAC Addr"
                if "Base MAC Addr" in line:
                    # Extraction de l'adresse MAC et stockage dans le dictionnaire
                    mac_address = line.split(":")[1].strip()
                    data["MAC Address"] = mac_address
                # Recherche de la ligne contenant "Software revision"
                if "System Description" in line:
                    # Extraction de la révision logicielle et stockage dans le dictionnaire
                    software_revision = line.split(":")[1].strip()
                    data["Software Revision"] = software_revision
                # Recherche de la ligne contenant "Up Time"
                if "Up Time" in line:
                    # Extraction de la durée de fonctionnement et stockage dans le dictionnaire
                    uptime = line.split(":")[1].strip()
                    data["Up Time"] = uptime
                # Recherche de la ligne contenant "CPU Util (%)"
                if "CPU Util" in line:
                    # Extraction de l'utilisation CPU et stockage dans le dictionnaire
                    cpu_util = line.split(":")[1].strip()
                    data["CPU Util"] = cpu_util
                    cpu_util += '%'
        # Création d'un DataFrame à partir du dictionnaire
        # df = df.append(data, ignore_index=True)
        data = pd.DataFrame(data, index=[0])
        df = pd.concat([df, data])



# Export du DataFrame vers un fichier Excel
df.to_excel('output.xlsx', index=False)
