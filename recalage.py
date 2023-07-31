from ast import For
from cProfile import label
from itertools import count
import re
from subprocess import list2cmdline
import tkinter as tk
from tkinter import NO, Grid, Variable, ttk
from turtle import distance, position
from xml.etree.ElementTree import tostringlist
import matplotlib.pyplot as plt
import numpy as np
import pylab as plt
import pandas as pd



df=pd.DataFrame(columns=[0,1,2,3,4])
df2=pd.DataFrame(columns=[0,1,2,3,4])

my_w = tk.Tk()
my_w.title("Outil recalage")
global data 
global data2






#boucle for pour copier coller dans toutes les colonnes#
 


#une boucle for
#for i in (le clique):
    #e1.grid(row = 0, column= i, columnspan = 4)


    
 # copy selected text to clipboard 

def paste_select():
    e1.tag_add("sel", "1.0","end") # all text selected
    e1.tag_config("sel",background="green",foreground="red")
    global data 
    
    
    
    data = e1.get("1.0", tk.END).strip()
    

    print("Function Paste2 is called")
    lines = data.split('\n')
    
    for i, line in enumerate(lines):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df.loc[i, 0] = float(item)

    
    e1.delete('sel.first', 'sel.last')
    e2.delete('1.0', tk.END)
    e2.insert(tk.END, df[0].to_string(header=False, index=False,na_rep=''))
    
def Paste2():
    e1.tag_add("sel", "1.0","end") # all text selected
    e1.tag_config("sel",background="green",foreground="red")
    global data 
    
    
    
    data = e1.get("1.0", tk.END).strip()
    
    print("function appelez")
    lines2 = data.split('\n')
    for i, line in enumerate(lines2):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df.loc[i, 1] = float(item)
    e1.delete('sel.first', 'sel.last')
    e3.delete('1.0', tk.END)
    e3.insert(tk.END, df[1].to_string(header=False, index=False,na_rep=''))
    
def Paste3():
    e1.tag_add("sel", "1.0","end") # all text selected
    e1.tag_config("sel",background="green",foreground="red")
    global data 
    
    
    
    data = e1.get("1.0", tk.END).strip()
    
    lines3 = data.split('\n')
    for i, line in enumerate(lines3):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df.loc[i, 2] = float(item)
    e1.delete('sel.first', 'sel.last')
    e4.delete('1.0', tk.END)
    e4.insert(tk.END, df[2].to_string(header=False, index=False ,na_rep=''))

def Paste4():
    e1.tag_add("sel", "1.0","end") # all text selected
    e1.tag_config("sel",background="green",foreground="red")
    global data 
    
    
    
    data = e1.get("1.0", tk.END).strip()
    
    lines4 = data.split('\n')
    for i, line in enumerate(lines4):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df.loc[i, 3] = float(item)
    e1.delete('sel.first', 'sel.last')
    e5.delete('1.0', tk.END)
    e5.insert(tk.END, df[3].to_string(header=False, index=False, na_rep=''))

def Paste5():
    e1.tag_add("sel", "1.0","end") # all text selected
    e1.tag_config("sel",background="green",foreground="red")
    global data 
    
    
    
    data = e1.get("1.0", tk.END).strip()
    
    lines5 = data.split('\n')
    for i, line in enumerate(lines5):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df.loc[i, 4] = float(item)
    e1.delete('sel.first', 'sel.last')
    e6.delete('1.0', tk.END)
    e6.insert(tk.END, df[4].to_string(header=False, index=False,na_rep=''))


def create_button_widget(parent, row, col, text, command, padx=10, pady=10):  
    button = tk.Button(parent, 
                       text=text, 
                       command=command, 
                       font=('Verdana', 10, 'bold'),
                       width=10,
                       height=1,
                       bg='darkgray',  # Couleur de fond gris foncé
                       fg='white',  # Couleur de texte blanc
                       bd=1, 
                       relief='ridge',
                       activebackground='gray',  # Couleur de fond lorsqu'on clique sur le bouton
                       activeforeground='lightgray')  # Couleur du texte lorsqu'on clique sur le bouton
    button.grid(row=row, column=col, padx=padx, pady=pady)
    button.bind("<Enter>", lambda event, button=button: button.config(bg='palegreen'))  # Changement de couleur au survol
    button.bind("<Leave>", lambda event, button=button: button.config(bg='darkgray'))  # Retour à la couleur d'origine quand le curseur quitte le bouton
    return button



def create_text_widget(parent, row, col, text, pady=0):
    widget = tk.Text(parent, 
                     font=('Verdana', 12),  # Modifiez la police et la taille
                     height=5, 
                     width=50, 
                     bg='lightsteelblue',  # Changez la couleur de fond pour un bleu plus doux
                     fg='darkslategray',  # Changez la couleur du texte pour un gris foncé
                     bd=1, 
                     relief='ridge')  # Utilisez une bordure en relief
    widget.insert(tk.END, text)
    widget.grid(row=row, column=col, columnspan=3, pady=pady)
      
  

    # Effet de survol
    widget.bind("<Enter>", lambda event, widget=widget: widget.config(bg='powderblue'))  # Changement de couleur au survol
    widget.bind("<Leave>", lambda event, widget=widget: widget.config(bg='lightsteelblue'))  # Retour à la couleur d'origine quand le curseur quitte le widget
    return widget


# Personnalisez la police du LabelFrame pour le rendre plus voyant
style = ttk.Style()
style.configure('Custom.TLabelframe.Label', font=('Verdana', 18, 'bold'))

my_w1 = ttk.LabelFrame(my_w, text="Jeu de données 1", style='Custom.TLabelframe')
my_w1.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')

b4 = create_button_widget(my_w1, 1, 1, 'D_soud-ref', lambda: paste_select())
b6 = create_button_widget(my_w1, 1, 2, 'Longueur', lambda: Paste2())
b7 = create_button_widget(my_w1, 1, 3, 'PA', lambda: Paste3())
b8 = create_button_widget(my_w1, 1, 4, 'Largeur', lambda: Paste4())
b9 = create_button_widget(my_w1, 1, 5, 'N°Indication', lambda: Paste5())

e1 = create_text_widget(my_w1, 0, 1, '', pady=10)
# Créer les boutons



# Créer les widgets de texte
distance_soudure_reference ="D_soud-R(m)"
e2 = create_text_widget(my_w1, 2, 1, distance_soudure_reference, pady=10)

longueur="Longueur(mm)"
e3 = create_text_widget(my_w1, 2, 2, longueur, pady=5)

position="PA(°)"
e4 = create_text_widget(my_w1, 2, 3, position, pady=10)

largeur="Largeur(mm)"
e5 = create_text_widget(my_w1, 2, 4, largeur, pady=5)

Indication="N°Indication"
e6 = create_text_widget(my_w1, 2, 5, Indication, pady=5)









    
    
    
 # copy selected text to clipboard 

def paste_select2():
    e8.tag_add("sel", "1.0","end") # all text selected
    e8.tag_config("sel",background="green",foreground="red")

    global data2 
    global df2

    
    
    data2=e8.get("1.0", tk.END).strip()
    

    liste21=data2.split('\n')
    for i, line in enumerate(liste21):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        for j, item in enumerate(elements):
            df2.loc[i, 0] = float(item)
    e8.delete('sel.first', 'sel.last')
    e10.delete('1.0', tk.END)
    e10.insert(tk.END, df2[0].to_string(header=False, index=False, na_rep=''))

def Paste22():
    e8.tag_add("sel", "1.0","end") # all text selected
    e8.tag_config("sel",background="green",foreground="red")

    global data2 
    global df2

    data2=e8.get("1.0", tk.END).strip()
    liste22=data2.split()
    for i, line in enumerate(liste22):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df2.loc[i, 1] = float(item)
    e8.delete('sel.first', 'sel.last')
    e11.delete('1.0', tk.END)
    e11.insert(tk.END, df2[1].to_string(header=False, index=False,na_rep=''))
def Paste32():
    e8.tag_add("sel", "1.0","end") # all text selected
    e8.tag_config("sel",background="green",foreground="red")

    global data2 
    global df2

    data2=e8.get("1.0", tk.END).strip()
    liste32=data2.split()
    for i, line in enumerate(liste32):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df2.loc[i, 2] = float(item)
    e8.delete('sel.first', 'sel.last')
    e12.delete('1.0', tk.END)
    e12.insert(tk.END, df2[2].to_string(header=False, index=False,na_rep=''))

def Paste42():
    e8.tag_add("sel", "1.0","end") # all text selected
    e8.tag_config("sel",background="green",foreground="red")

    global data2 
    global df2

    data2=e8.get("1.0", tk.END).strip()
    liste42=data2.split()
    for i, line in enumerate(liste42):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df2.loc[i, 3] = float(item)
    e8.delete('sel.first', 'sel.last')
    e13.delete('1.0', tk.END)
    e13.insert(tk.END, df2[3].to_string(header=False, index=False,na_rep=''))

def Paste52():
    e8.tag_add("sel", "1.0","end") # all text selected
    e8.tag_config("sel",background="green",foreground="red")

    global data2 
    global df2

    data2=e8.get("1.0", tk.END).strip()
    liste52=data2.split()
    for i, line in enumerate(liste52):
        # Divisez chaque ligne en éléments en utilisant un ou plusieurs espaces comme séparateurs
        elements = re.split(r' {1,}', line.strip())
        for j, item in enumerate(elements):
            item = item.replace(',', '.')
            df2.loc[i, 4] = float(item)
    e8.delete('sel.first', 'sel.last')
    e14.delete('1.0', tk.END)
    e14.insert(tk.END, df2[4].to_string(header=False, index=False, na_rep=''))




def create_text_widget(parent, row, col, text, pady=0):
    widget = tk.Text(parent, 
                     font=('Verdana', 12),  # Modifiez la police et la taille
                     height=5, 
                     width=50, 
                     bg='lightsteelblue',  # Changez la couleur de fond pour un bleu plus doux
                     fg='darkslategray',  # Changez la couleur du texte pour un gris foncé
                     bd=1, 
                     relief='ridge')  # Utilisez une bordure en relief
    widget.insert(tk.END, text)
    widget.grid(row=row, column=col, columnspan=3, pady=pady)
      
  

    # Effet de survol
    widget.bind("<Enter>", lambda event, widget=widget: widget.config(bg='powderblue'))  # Changement de couleur au survol
    widget.bind("<Leave>", lambda event, widget=widget: widget.config(bg='lightsteelblue'))  # Retour à la couleur d'origine quand le curseur quitte le widget
    return widget

# créer les widgets de texte


def create_button_widget(parent, row, col, text, command, padx=10, pady=10):  
    button = tk.Button(parent, 
                       text=text, 
                       command=command, 
                       font=('Verdana', 10, 'bold'),
                       width=10,
                       height=1,
                       bg='darkgray',  # Couleur de fond gris foncé
                       fg='white',  # Couleur de texte blanc
                       bd=1, 
                       relief='ridge',
                       activebackground='gray',  # Couleur de fond lorsqu'on clique sur le bouton
                       activeforeground='lightgray')  # Couleur du texte lorsqu'on clique sur le bouton
    button.grid(row=row, column=col, padx=padx, pady=pady)
    button.bind("<Enter>", lambda event, button=button: button.config(bg='palegreen'))  # Changement de couleur au survol
    button.bind("<Leave>", lambda event, button=button: button.config(bg='darkgray'))  # Retour à la couleur d'origine quand le curseur quitte le bouton
    return button


# créer les boutons
my_w2 = ttk.LabelFrame(my_w, text="Jeu de données 2", style='Custom.TLabelframe')
my_w2.grid(row=1, column=0, padx=10, pady=10, sticky='nsew')

c4 = create_button_widget(my_w2, 1, 1, 'D_soud-ref', lambda: paste_select2())
c6 = create_button_widget(my_w2, 1, 2, 'Longueur', lambda: Paste22())
c7 = create_button_widget(my_w2, 1, 3, 'PA', lambda: Paste32())
c8 = create_button_widget(my_w2, 1, 4, 'Largeur', lambda: Paste42())
c9 = create_button_widget(my_w2, 1, 5, 'N°Indication', lambda: Paste52())

e8 = create_text_widget(my_w2, 0, 1, '', pady=10)
e10 = create_text_widget(my_w2, 2, 1, distance_soudure_reference)
e11 = create_text_widget(my_w2, 2, 2, longueur, pady=10)
e12 = create_text_widget(my_w2, 2, 3, position, pady=10)
e13 = create_text_widget(my_w2, 2, 4, largeur, pady=5)
e14 = create_text_widget(my_w2, 2, 5, Indication, pady=5)

def create_visualisation_button(parent, row, col, text, command, padx=10, pady=10):
    button = tk.Button(parent, 
                       text=text, 
                       command=command, 
                       font=('Verdana', 10, 'bold'),
                       bg='dimgray',  # Couleur de fond plus foncée
                       fg='white',
                       bd=1, 
                       relief='ridge', 
                       activebackground='black',  # Couleur de fond lorsqu'on clique sur le bouton
                       activeforeground='lightgray')
    button.grid(row=row, column=col, padx=padx, pady=pady, sticky='ew')  # Utilisez 'sticky' pour étirer le bouton sur toute la largeur de la grille

    button.bind("<Enter>", lambda event, button=button: button.config(bg='darkgray'))
    button.bind("<Leave>", lambda event, button=button: button.config(bg='dimgray'))
    return button

my_w3 = ttk.LabelFrame(my_w, text="visualisation", style='Custom.TLabelframe')
my_w3.grid(row=3, column=0, padx=10, pady=10, sticky='nsew')

# Créer le bouton de visualisation
b5 = create_visualisation_button(my_w3, 3, 4, 'visualisation graphique', lambda: visulatisation())



labelChoix = tk.Label(my_w3, text = "diamètre à insérer !")
labelChoix.grid(row=3,column=2,padx=2,pady=2)

Diametre =tk.Entry(my_w3,background='white')
Diametre.grid(row=3, column=3,padx=2,pady=2)


def visulatisation():
    
    x1= Diametre.get()
    Diametre_tube=float(x1)*25.4*3.14/360

    plt.figure("", figsize=(12,10), dpi=150)
    plt.legend(loc=1)
                #graduation de l'axe des abscisses#
    plt.ylim(0,360,10)
    plt.xlabel("Longueur du tube (m)")
    plt.ylabel("POSITION ANGULAIRE (°)")
    

    global select
    global select2
    
    select2=listeCombo2.get()
    select=listeCombo.get()


    if(select=="en haut à gauche"):              #point5 côté sup gauche#    #point5 côté sup droit#
        #en haut à gauche
        
        for i in range(len(df)):
            x=[df[0][i],df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000]
                #1                #2                                  #3                                #4                                                        #5
                #1          #2           #3                             #4                                  #5
            y=[df[2][i],df[2][i],df[2][i]-(df[3][i]/Diametre_tube),df[2][i]-(df[3][i]/Diametre_tube),df[2][i]-(df[3][i]/Diametre_tube)+(df[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in y):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(y)
                over_y = np.array([yi for yi in y if yi > 360])
                over_x = np.array([xi for xi, yi in zip(x, y) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(x, y)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in y]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')
            
        # Tracer le rectangle
            plt.plot(x, y, color='b')
            if i == 0:
                plt.scatter(df[0][i],df[2][i],label='Jeu de données 1', color='blue')
            else:
                plt.scatter(df[0][i],df[2][i], color='blue')
            plt.legend()
            plt.text(df[0][i], df[2][i], str(df[4][i]), fontsize=8)
            
          
        
        #centre milieu
    #EN BAT A GAUCHE
    if(select=="en bas à gauche"): 
        for i in range(len(df)):
            z=[df[0][i],df[0][i],df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000]
            s=[df[2][i],df[2][i]+(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube)-(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube)-(df[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in s):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(s)
                over_y = np.array([yi for yi in s if yi > 360])
                over_x = np.array([xi for xi, yi in zip(z, s) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(z, s)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in s]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')
            plt.plot(z,s,'b')
            if i == 0:
                plt.scatter(df[0][i],df[2][i],label='Jeu de données 1', color='blue')
            else:
                plt.scatter(df[0][i],df[2][i], color='blue')
            plt.legend()
            plt.text(df[0][i], df[2][i], str(df[4][i]), fontsize=8)
            
        
    # centre
    if(select=="centre"):
        for i in range(len(df)):
            a=[df[0][i]-df[1][i]/2/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000, df[0][i]-df[1][i]/2/1000+df[1][i]/1000-df[1][i]/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000-df[1][i]/1000]
            b=[df[2][i]+df[3][i]/Diametre_tube/2,df[2][i]+df[3][i]/Diametre_tube/2,df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube, df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube, df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube+df[3][i]/Diametre_tube]
            if any(yi > 360 for yi in b):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(b)
                over_y = np.array([yi for yi in b if yi > 360])
                over_x = np.array([xi for xi, yi in zip(a, b) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(a, b)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in b]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')
            plt.plot(a,b, 'b',label="jeu de donnée1")
            if i == 0:
                plt.scatter(df[0][i],df[2][i],label='Jeu de données 1', color='blue')
            else:
                plt.scatter(df[0][i],df[2][i], color='blue')
            plt.legend()
            plt.text(df[0][i], df[2][i], str(df[4][i]), fontsize=8)
           
        
#--------------------------------------------------------------------------------------------------------#
    if(select2=="en haut à gauche"):
        for i in range(len(df2)):
            x2=[df2[0][i],df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000]
                #1                #2                                  #3                                #4                                                        #5
                #1          #2           #3                             #4                                  #5
            y2=[df2[2][i],df2[2][i],df2[2][i]-(df2[3][i]/Diametre_tube),df2[2][i]-(df2[3][i]/Diametre_tube),df2[2][i]-(df2[3][i]/Diametre_tube)+(df2[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in y2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(y2)
                over_y = np.array([yi for yi in y2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(x2, y2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(x2, y2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in y2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')    #centre milieu
            plt.plot(x2,y2,'r')
            if i == 0:
                plt.scatter(df2[0][i],df2[2][i],label='Jeu de données 2', color='red')
            else:
                plt.scatter(df2[0][i],df2[2][i], color='red')
            plt.legend()
            plt.text(df2[0][i], df2[2][i], str(df2[4][i]), fontsize=8)
             
        
    #EN BAT A GAUCHE
    if(select2=="en bas à gauche"):
        for i in range(len(df2)):
           z2=[df2[0][i],df2[0][i],df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000]
           s2=[df2[2][i],df2[2][i]+(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube)-(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube)-(df2[3][i]/Diametre_tube)]
           if any(yi > 360 for yi in s2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(s2)
                over_y = np.array([yi for yi in s2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(z2, s2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(z2, s2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in s2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')    #centre milieu
            
           plt.plot(z2,s2,'r')
           if i == 0:
                plt.scatter(df2[0][i],df2[2][i],label='Jeu de données 2', color='red')
           else:
                plt.scatter(df2[0][i],df2[2][i], color='red')
           plt.legend()
           plt.text(df2[0][i], df2[2][i], str(df2[4][i]), fontsize=8)
          

    # centre
    if(select2=="centre"):
        for i in range(len(df2)):
            a2=[df2[0][i]-df2[1][i]/2/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000, df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000-df2[1][i]/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000-df2[1][i]/1000]
            b2=[df2[2][i]+df2[3][i]/Diametre_tube/2,df2[2][i]+df2[3][i]/Diametre_tube/2,df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube, df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube, df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube+df2[3][i]/Diametre_tube]
            if any(yi > 360 for yi in b2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(b2)
                over_y = np.array([yi for yi in b2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(a2, b2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(a2, b2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in b2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')
             
            plt.plot(a2,b2, 'r')
            if i == 0:
                plt.scatter(df2[0][i],df2[2][i],label='Jeu de données 2', color='red')
            else:
                plt.scatter(df2[0][i],df2[2][i], color='red')
            plt.legend()
            plt.text(df2[0][i], df2[2][i], str(df2[4][i]), fontsize=8)
            

  
    plt.title("Projet recalage",
    fontsize=12,family='monospace',fontweight='bold',
    style='italic',color='m', backgroundcolor='y',
    horizontalalignment='center')
                #Il faudra faire une boucle  for sur chaque point comme ça sa se répètera à chaque fois#
              
    plt.show()


def action(event):
  x1= Diametre.get()
  Diametre_tube=float(x1)*25.4*3.14/360
  if(select=="en haut à gauche"):
         for i in range(len(df)):
            x=[df[0][i],df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000]
                #1                #2                                  #3                                #4                                                        #5
                #1          #2           #3                             #4                                  #5
            y=[df[2][i],df[2][i],df[2][i]-(df[3][i]/Diametre_tube),df[2][i]-(df[3][i]/Diametre_tube),df[2][i]-(df[3][i]/Diametre_tube)+(df[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in y):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(y)
                over_y = np.array([yi for yi in y if yi > 360])
                over_x = np.array([xi for xi, yi in zip(x, y) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(x, y)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in y]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')

        # Tracer le rectangle
            plt.plot(x, y, color='blue')
           
        
  if(select=="en bas à gauche"):
         for i in range(len(df)):
            z=[df[0][i],df[0][i],df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000,df[0][i]+df[1][i]/1000-df[1][i]/1000]
            s=[df[2][i],df[2][i]+(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube)-(df[3][i]/Diametre_tube),df[2][i]+(df[3][i]/Diametre_tube)-(df[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in s):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(s)
                over_y = np.array([yi for yi in y if yi > 360])
                over_x = np.array([xi for xi, yi in zip(z, s) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(z, s)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in s]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')
            plt.plot(z,s,'r') 
            plt.scatter(df[0][i],df[2][i])
  if(select=="centre"):
        for i in range(len(df)):
            a=[df[0][i]-df[1][i]/2/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000, df[0][i]-df[1][i]/2/1000+df[1][i]/1000-df[1][i]/1000,df[0][i]-df[1][i]/2/1000+df[1][i]/1000-df[1][i]/1000]
            b=[df[2][i]+df[3][i]/Diametre_tube/2,df[2][i]+df[3][i]/Diametre_tube/2,df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube, df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube, df[2][i]+df[3][i]/Diametre_tube/2-df[3][i]/Diametre_tube+df[3][i]/Diametre_tube]
            if any(yi > 360 for yi in b):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(b)
                over_y = np.array([yi for yi in b if yi > 360])
                over_x = np.array([xi for xi, yi in zip(a, b) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(a, b)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in b]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='blue')
            plt.plot(a,b, 'y')
       

listeProduits=[ "en haut à gauche","en bas à gauche","centre"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo = ttk.Combobox(my_w1, values=listeProduits)

listeCombo.current(0)

listeCombo.grid(row=0,column=5,padx=2,pady=5)
listeCombo.bind("<<ComboboxSelected>>",action)
def action2(event):
  x1= Diametre.get()
  Diametre_tube=float(x1)*25.4*3.14/360
  if(select2=="en haut à gauche"):
        for i in range(len(df2)):
            x2=[df2[0][i],df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000]
                #1                #2                                  #3                                #4                                                        #5
                #1          #2           #3                             #4                                  #5
            y2=[df2[2][i],df2[2][i],df2[2][i]-(df2[3][i]/Diametre_tube),df2[2][i]-(df2[3][i]/Diametre_tube),df2[2][i]-(df2[3][i]/Diametre_tube)+(df2[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in y2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(y2)
                over_y = np.array([yi for yi in y2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(x2, y2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(x2, y2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in y2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')    #centre milieu
            plt.plot(x2,y2,'r')
            
  if(select2=="en bas à gauche"):
        for i in range(len(df2)):
            z2=[df2[0][i],df2[0][i],df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000,df2[0][i]+df2[1][i]/1000-df2[1][i]/1000]
            s2=[df2[2][i],df2[2][i]+(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube)-(df2[3][i]/Diametre_tube),df2[2][i]+(df2[3][i]/Diametre_tube)-(df2[3][i]/Diametre_tube)]
            if any(yi > 360 for yi in s2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(s2)
                over_y = np.array([yi for yi in s2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(z2, s2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(z2, s2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in s2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')    #centre milieu
            
            plt.plot(z2,s2,'r')

  if(select2=="centre"):
        for i in range(len(df2)):
            a2=[df2[0][i]-df2[1][i]/2/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000, df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000-df2[1][i]/1000,df2[0][i]-df2[1][i]/2/1000+df2[1][i]/1000-df2[1][i]/1000]
            b2=[df2[2][i]+df2[3][i]/Diametre_tube/2,df2[2][i]+df2[3][i]/Diametre_tube/2,df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube, df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube, df2[2][i]+df2[3][i]/Diametre_tube/2-df2[3][i]/Diametre_tube+df2[3][i]/Diametre_tube]
            if any(yi > 360 for yi in b2):
            # Trouver les coordonnées qui dépassent
                bottom_y = min(b2)
                over_y = np.array([yi for yi in b2 if yi > 360])
                over_x = np.array([xi for xi, yi in zip(a2, b2) if yi > 360])

                # Transposer les coordonnées qui dépassent de manière à partir de 0 sur l'axe des ordonnées
                over_y_transposed = over_y - bottom_y
                bottom_y_transposed = 0

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                x_transposed = [xi for xi, yi in zip(a2, b2)]
                y_transposed = [(yi - bottom_y) if yi > 360 else 0 for yi in b2]

                # Tracer la partie qui dépasse sur la même colonne que le reste du rectangle
                plt.fill_between(x_transposed, y_transposed, color='red')
            
            plt.plot(a2,b2, 'r')
       

listeProduits2=["en haut à gauche","en bas à gauche","centre"]

# 3) - Création de la Combobox via la méthode ttk.Combobox()
listeCombo2 = ttk.Combobox(my_w2, values=listeProduits2)

listeCombo2.current(0)

listeCombo2.grid(row=0,column=5,padx=2,pady=5)
listeCombo2.bind("<<ComboboxSelected>>", action2)

my_w.mainloop()