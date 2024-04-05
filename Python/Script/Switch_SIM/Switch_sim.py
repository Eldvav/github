import tkinter as tk
from tkinter import messagebox


# Définir les configurations de carte SIM
configurations = {
    "SIM ORANGE": {
        "APN1": "orange",
        "PIN1": "0000",
        "USERNAME1": "orange",
        "PASSWORD1": "orange",
        "APN2": "orange",
        "PIN2": "0000",
        "USERNAME2": "orange",
        "PASSWORD2": "orange",
        "IFACE": "wwan0",
        "SIM_SLOT": "1"
    },
    "SIM SFR": {
        "APN1": "sl2sfr",
        "PIN1": "0000",
        "USERNAME1": "sl2sfr",
        "PASSWORD1": "sl2sfr",
        "APN2": "sl2sfr",
        "PIN2": "0000",
        "USERNAME2": "sl2sfr",
        "PASSWORD2": "sl2sfr",
        "IFACE": "wwan0",
        "SIM_SLOT": "1"
    },
    "SIM Free": {
        "APN1": "free",
        "PIN1": "0000",
        "USERNAME1": "free",
        "PASSWORD1": "free",
        "APN2": "free",
        "PIN2": "0000",
        "USERNAME2": "free",
        "PASSWORD2": "free",
        "IFACE": "wwan0",
        "SIM_SLOT": "1"
    },
    "SIM Bouygue": {
        "APN1": "mmsbouygtel.com",
        "PIN1": "0000",
        "USERNAME1": "mmsbouygtel.com",
        "PASSWORD1": "mmsbouygtel.com",
        "APN2": "mmsbouygtel.com",
        "PIN2": "0000",
        "USERNAME2": "mmsbouygtel.com",
        "PASSWORD2": "mmsbouygtel.com",
        "IFACE": "wwan0",
        "SIM_SLOT": "1"
    }
}

# Fonction pour écrire la configuration dans un fichier
def write_config_to_file(config, filename):
    with open(filename, 'w') as f:
        for key, value in config.items():
            f.write(f"{key}=\"{value}\"\n")

# Fonction appelée lors du clic sur le bouton "Sélectionner"
def select_sim():
    selected_sim = sim_var.get()
    selected_config = configurations[selected_sim]
    write_config_to_file(selected_config, config_file_path)
    messagebox.showinfo("Succès", f"Configuration de la carte SIM '{selected_sim}' mise à jour.")

# Création de l'IG
root = tk.Tk()
root.title("Switch carte SIM")
root.geometry("240x180")
root.iconbitmap("C:/Users/dylan.moreau/Desktop/github/Python/Script/Switch_SIM/cartesim.ico")

# Path du fichier de conf
config_file_path = "C:/Users/dylan.moreau/Desktop/github/Python/Script/Switch_SIM/cellular_modem.conf"

# Variable de suivi pour la sélection de la carte SIM
sim_var = tk.StringVar()

# Liste déroulante pour sélectionner la carte SIM
sim_label = tk.Label(root, text="Sélectionnez la carte SIM :")
sim_label.pack()
sim_dropdown = tk.OptionMenu(root, sim_var, *configurations.keys())
sim_dropdown.pack()

# Bouton pour sélectionner la carte SIM
select_button = tk.Button(root, text="Sélectionner", command=select_sim)
select_button.pack()



root.mainloop()
