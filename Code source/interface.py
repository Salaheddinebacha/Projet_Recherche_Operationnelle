import tkinter as tk
from welsh_powel import execute_welsh_powel
from kruskal import execute_kruskal
from dijkstra import dijkstra
from bellman_ford import bellman_ford
from moindre_cout import execute_moindre_cout
from nord_ouest import execute_nord_ouest
from stepping_stone import execute_stepping_stone
from ford_fulkerson import ford_fulkerson
from potentiel_metra import execute_potentiel_metra
from PIL import Image, ImageTk
import sys
import os

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


def open_about_window():
    about_window = tk.Toplevel(root)
    about_window.title("A propos")
    
    # Obtenir la taille de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculer 80% de la largeur et de la hauteur
    width = int(screen_width * 0.8)
    height = int(screen_height * 0.8)

    # Appliquer ces dimensions à la fenêtre
    about_window.geometry(f"{width}x{height}")
    about_window.configure(bg="white")

    # Charger et afficher l'image
    img_path = resource_path("logo-1.png")  # Utilisez resource_path
    img = Image.open(img_path)  # Chargez l'image depuis le chemin embarqué
    img = img.resize((950, 300))  # Redimensionner l'image si nécessaire
    photo = ImageTk.PhotoImage(img)

    label_image = tk.Label(about_window, image=photo, bg="white")
    label_image.image = photo  # Conserver une référence à l'image
    label_image.pack(pady=20)
    
    # Texte à afficher
    label_text = tk.Label(about_window, text="Ce projet est réalisé par Salaheddine Bacha.\nIl est encadré par Madame El Mkhalet Mouna. \nCM : Recherche opérationnelle.", font=("Helvetica", 18, "bold"), bg="#A9A9A9", fg="black")
    label_text.pack(pady=20)

    
# Fonction pour ouvrir la fenêtre des algorithmes
def open_algorithm_window():
    algorithm_window = tk.Toplevel(root)
    algorithm_window.title("Select Algorithm")
    algorithm_window.geometry("1000x400")
    algorithm_window.configure(bg="#A9A9A9")

    def close_window():
        algorithm_window.destroy()

    sortie_button = tk.Button(algorithm_window, text="Sortie", command=close_window, width=20, height=3, bg="#8B6F4B", fg="white")
    sortie_button.pack(pady=10, side=tk.BOTTOM)

    def execute_algorithm(algorithm_name):
        input_window = tk.Toplevel(algorithm_window)
        input_window.title(f"Input for {algorithm_name}")
        def on_submit():
            if algorithm_name == "Welsh Powel":
                n = int(entry_n.get())
                execute_welsh_powel(n, result_label)
            elif algorithm_name == "Kruskal":
                n = int(entry_n.get())
                execute_kruskal(n, result_label)
            elif algorithm_name == "Dijkstra":
                n = int(entry_n.get())
                start_node = entry_start.get()
                dijkstra(n, start_node, result_label)
            elif algorithm_name == "Bellman-Ford":
                n = int(entry_n.get())
                start_node = entry_start.get()
                end_node = entry_end.get()
                bellman_ford(n, start_node, end_node, result_label)
            elif algorithm_name == "Moindre Cout":
                rows = int(entry_n.get())
                cols = int(entry_m.get())
                execute_moindre_cout(rows, cols, result_label)
            elif algorithm_name == "Nord Ouest":
                rows = int(entry_n.get())
                cols = int(entry_m.get())
                execute_nord_ouest(rows, cols, result_label)
            elif algorithm_name == "Stepping Stone":
                rows = int(entry_n.get())
                cols = int(entry_m.get())
                execute_stepping_stone(rows, cols, result_label)
            elif algorithm_name == "Ford Fulkerson":
                n = int(entry_n.get())
                start_node = entry_start.get()
                end_node = entry_end.get()
                ford_fulkerson(n, start_node, end_node, result_label)
            elif algorithm_name == "Potentiel de Metra":
                n = int(entry_n.get())
                start_node = entry_start.get()
                end_node = entry_end.get()
                execute_potentiel_metra(n, start_node, end_node, result_label)
            input_window.destroy()

        if algorithm_name in ["Welsh Powel", "Kruskal"]:
            label_n = tk.Label(input_window, text="Entrez le nombre de sommets:", bg="#A9A9A9", fg="black")
            label_n.pack(pady=10)
            entry_n = tk.Entry(input_window)
            entry_n.pack(pady=10)
        elif algorithm_name in ["Dijkstra"]:
            label_n = tk.Label(input_window, text="Entrez le nombre de sommets:", bg="#A9A9A9", fg="black")
            label_n.pack(pady=10)
            entry_n = tk.Entry(input_window)
            entry_n.pack(pady=10)
            label_start = tk.Label(input_window, text="Entrez le sommet de départ:", bg="#A9A9A9", fg="black")
            label_start.pack(pady=10)
            entry_start = tk.Entry(input_window)
            entry_start.pack(pady=10)
        elif algorithm_name in ["Bellman-Ford", "Ford Fulkerson"]:
            label_n = tk.Label(input_window, text="Entrez le nombre de sommets:", bg="#A9A9A9", fg="black")
            label_n.pack(pady=10)
            entry_n = tk.Entry(input_window)
            entry_n.pack(pady=10)
            label_start = tk.Label(input_window, text="Entrez le sommet de départ:", bg="#A9A9A9", fg="black")
            label_start.pack(pady=10)
            entry_start = tk.Entry(input_window)
            entry_start.pack(pady=10)
            label_end = tk.Label(input_window, text="Entrez le sommet d'arrivée:", bg="#A9A9A9", fg="black")
            label_end.pack(pady=10)
            entry_end = tk.Entry(input_window)
            entry_end.pack(pady=10)
        elif algorithm_name in ["Moindre Cout", "Nord Ouest", "Stepping Stone"]:
            label_n = tk.Label(input_window, text="Entrez le nombre de lignes:", bg="#A9A9A9", fg="black")
            label_n.pack(pady=10)
            entry_n = tk.Entry(input_window)
            entry_n.pack(pady=10)
            label_m = tk.Label(input_window, text="Entrez le nombre de colonnes:", bg="#A9A9A9", fg="black")
            label_m.pack(pady=10)
            entry_m = tk.Entry(input_window)
            entry_m.pack(pady=10)
        elif algorithm_name == "Potentiel de Metra":
            label_n = tk.Label(input_window, text="Entrez le nombre de sommets:", bg="#A9A9A9", fg="black")
            label_n.pack(pady=10)
            entry_n = tk.Entry(input_window)
            entry_n.pack(pady=10)
            label_start = tk.Label(input_window, text="Entrez le sommet de départ (A-Z):", bg="#A9A9A9", fg="black")
            label_start.pack(pady=10)
            entry_start = tk.Entry(input_window)
            entry_start.pack(pady=10)
            label_end = tk.Label(input_window, text="Entrez le sommet d'arrivée (A-Z):", bg="#A9A9A9", fg="black")
            label_end.pack(pady=10)
            entry_end = tk.Entry(input_window)
            entry_end.pack(pady=10)

        submit_button = tk.Button(input_window, text="Submit", command=on_submit, bg="#8B6F4B", fg="white", font=("Helvetica", 8, "bold"))
        submit_button.pack(pady=10)

    algorithms = ["Welsh Powel", "Kruskal", "Dijkstra", "Bellman-Ford", "Moindre Cout", "Nord Ouest", "Stepping Stone", "Ford Fulkerson", "Potentiel de Metra"]
    
    button_frame = tk.Frame(algorithm_window, bg="#A9A9A9")
    button_frame.pack(pady=20, fill=tk.X, padx=10)
    
    for i, algorithm in enumerate(algorithms):
        button = tk.Button(button_frame, text=algorithm, command=lambda alg=algorithm: execute_algorithm(alg), width=20, height=3, bg="#333333", font=("Helvetica", 12, "bold") ,fg="white")
        button.grid(row=i//3, column=i%3, padx=10, pady=10, sticky="nsew")
        
    for i in range(3):
        button_frame.grid_columnconfigure(i, weight=1)
    for i in range(len(algorithms)//3 + 1):
        button_frame.grid_rowconfigure(i, weight=1)

def quit_application():
    root.destroy()

root = tk.Tk()
root.title("Algorithm Executor")
root.geometry("1000x500")  
root.configure(bg="#A9A9A9")

frame = tk.Frame(root, bg="#A9A9A9", bd=10)
frame.pack(fill=tk.BOTH, expand=True)
tk.Label(frame, text="Bienvenue dans l'Interface GUI\n\n\n Appuyez sur Entrée pour continuer", font=("Helvetica", 16, "bold"), bg="#A9A9A9", fg="black").pack(pady=20)

entry_button = tk.Button(root, text="Entrer", font=("Helvetica", 16, "bold"), command=open_algorithm_window, width=20, height=3, bg="#8B6F4B", fg="white")
entry_button.place(relx=0.5, rely=0.4, anchor="center")

about_button = tk.Button(root, text="A propos", font=("Helvetica", 16, "bold"), command=open_about_window, width=20, height=3, bg="#8B6F4B", fg="white")
about_button.place(relx=0.5, rely=0.6, anchor="center")

sortie_button = tk.Button(root, text="Sortie", font=("Helvetica", 16, "bold"), command=quit_application, width=20, height=3, bg="#8B6F4B", fg="white")
sortie_button.place(relx=0.5, rely=0.8, anchor="center")

result_label = tk.Label(root, text="", bg="#A9A9A9", fg="black")
result_label.pack(pady=20)

root.mainloop()
