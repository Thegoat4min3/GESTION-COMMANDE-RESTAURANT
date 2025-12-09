from tkinter import *
from tkinter import messagebox
from reportlab.pdfgen import canvas


# CREATION DE L'INTERFACE ET PERSONNALISATION

window = Tk()
window.title(' RESTAURANT AMINE ')
window.geometry('720x480')
window.iconbitmap('projet8/restaurant.ico')
window.config(bg='#E9EA81')

# CREATION DES FRAME

titre_frame = Frame(window , bg='#E9EA81')
left_frame = Frame(window , bg='#E9EA81' , width=300)
right_frame = Frame(window , bg='#E9EA81', width=300)




# CREATION DE MA BASE DE DONNES ( Mon Dictionnaire )

menus = [
    {
        "nom": "Pizza Margherita",
        "categorie": "Plat",
        "prix": 12.50
    },
    {
        "nom": "Burger Classique",
        "categorie": "Plat",
        "prix": 10.00
    },
    {
        "nom": "Salade César",
        "categorie": "Entrée",
        "prix": 8.50
    },
    {
        "nom": "Tiramisu",
        "categorie": "Dessert",
        "prix": 6.00
    },
    {
        "nom": "Coca-Cola",
        "categorie": "Boisson",
        "prix": 3.00
    }
]

# CREATION DES FONCTIONS  ( MENU )

list_valeur = [0 ,  0 , 0 , 0 , 0]

def bouton_add1() :
    result_Text.delete("1.0" , "1.end")
    
    try :
        valeur = int(nb_entry1.get())
    except ValueError :
        valeur = 1


    valeur_result = valeur * menus[0]['prix']

    list_valeur[0] = valeur_result
    result_Text.insert("1.end", f"{menus[0]['nom']} x {valeur} .......... {valeur_result}\n")
    


def bouton_add2() :
    result_Text.delete("2.0" , "2.end")
    try :
        valeur = int(nb_entry2.get())
    except ValueError :
        valeur = 1

    valeur_result = valeur * menus[1]["prix"]

    list_valeur[1] = valeur_result
    result_Text.insert("2.end", f"{menus[1]['nom']} x {valeur} .......... {valeur_result}\n")


def bouton_add3() :
    result_Text.delete("3.0" , "3.end")
    try :
        valeur = int(nb_entry3.get())
    except ValueError :
        valeur = 1

    valeur_result = valeur * menus[2]["prix"]

    list_valeur[2] = valeur_result
    result_Text.insert("3.end", f"{menus[2]['nom']} x {valeur} .......... {valeur_result}\n")




def bouton_add4() :
    result_Text.delete("4.0" , "4.end")
    try :
        valeur = int(nb_entry4.get())
    except ValueError :
        valeur = 1


    valeur_result = valeur * menus[3]["prix"]

    list_valeur[3] = valeur_result
    result_Text.insert("4.end", f"{menus[3]['nom']} x {valeur} .......... {valeur_result}\n")


def bouton_add5() :
    result_Text.delete("5.0" , "5.end")
    try :
        valeur = int(nb_entry5.get())
    except ValueError :
        valeur = 1

    valeur_result = valeur * menus[4]["prix"]

    list_valeur[4] = valeur_result
    result_Text.insert("5.end", f"{menus[4]['nom']} x {valeur} .......... {valeur_result}\n")



# CREATION DES FONCTIONS ( PANIER )

def reinitialiser() :
    nb_entry1.delete(0 , END)
    nb_entry2.delete(0 , END)
    nb_entry3.delete(0 , END)
    nb_entry4.delete(0 , END)
    nb_entry5.delete(0 , END)
    total_entry.delete(0 , END)
    result_Text.delete("1.0" , END)
    for i in range(len(list_valeur)):
        list_valeur[i] = 0

def total() :
    global somme
    somme = sum(list_valeur)
    total_entry.delete(0 , END)
    total_entry.insert(0 ,somme)

   

def valider_commande():
    somme = sum(list_valeur)  # pas besoin de global
    total_entry.delete(0, END)
    total_entry.insert(0, somme)
    
    c = canvas.Canvas("ticket.pdf")
    c.drawString(50, 800, "Ticket de Commande")
    c.drawString(50, 780, f"Total : {somme} €")
    c.save()
    
    messagebox.showinfo("Commande validée", "Votre commande a été enregistrée !")


# LABEL DU TITRE ( TITRE FRAME )

titre_lbl = Label(titre_frame , text=" RESTAURANT - COMMANDE " ,font=("Arial", 18, "bold"),bg='#E9EA81',fg='#333333' )
titre_lbl.pack()


# LABEL , BOUTON , ENTRY SUR LA LEFT FRAME ( MENU ) 


menu_lbl = Label(left_frame , text="MENU" ,font=("Arial", 18, "bold"),bg='#E9EA81',fg='#333333' )
menu_lbl.grid(row=0, column=0, columnspan=4, pady=10)
 
for numero , menu in enumerate(menus , start=3) :
    nom = menus[numero - 3]["nom"]
    categorie = menus[numero - 3]["categorie"]
    prix = menus[numero - 3]["prix"]

    nom_lbl = Label(left_frame , text=nom , bg='#E9EA81')
    nom_lbl.grid(row=numero, column=1)
    
    categorie_lbl = Label(left_frame , text=categorie , bg='#E9EA81')
    categorie_lbl.grid(row=numero , column = 2)

    prix_lbl = Label(left_frame , text=prix , bg='#E9EA81')
    prix_lbl.grid(row=numero , column = 3)

nb_entry1 = Entry(left_frame , width=5)
nb_entry1.grid(row =3 , column=4)

nb_entry2 = Entry(left_frame , width=5)
nb_entry2.grid(row =4 , column=4)

nb_entry3 = Entry(left_frame , width=5)
nb_entry3.grid(row =5 , column=4)

nb_entry4 = Entry(left_frame , width=5)
nb_entry4.grid(row =6 , column=4)

nb_entry5 = Entry(left_frame , width=5)
nb_entry5.grid(row =7 , column=4)


btn_ajouter1 = Button(left_frame , text='ADD' , command=bouton_add1)
btn_ajouter1.grid(row=3 , column=5 , padx=5 )

btn_ajouter2 = Button(left_frame , text='ADD' , command=bouton_add2)
btn_ajouter2.grid(row=4 , column=5 , padx=5 )

btn_ajouter3= Button(left_frame , text='ADD' , command=bouton_add3)
btn_ajouter3.grid(row=5, column=5 , padx=5 )

btn_ajouter4= Button(left_frame , text='ADD' , command=bouton_add4)
btn_ajouter4.grid(row=6 , column=5 , padx=5 )

btn_ajouter5 = Button(left_frame , text='ADD' , command=bouton_add5)
btn_ajouter5.grid(row=7 , column=5 , padx=5 )



# LABEL , BOUTON ET ENTRY DE LA RIGHT FRAME ( PANIER )


panier_lbl = Label(right_frame , text="PANIER" ,font=("Arial", 18, "bold"),bg='#E9EA81',fg='#333333' )
panier_lbl.grid(row=0, column=0, columnspan=4, pady=10)


result_Text = Text(right_frame, width=40 , height=6)
result_Text.grid(row=1 , column=1 , columnspan=5)

scroll = Scrollbar(right_frame, command=result_Text.yview)
scroll.grid(row=1, column=6, sticky="ns")

result_Text.config(yscrollcommand=scroll.set)


total_lbl = Label(right_frame , text=' Total :')
total_lbl.grid(row=3 , column=2 , pady=100)

total_entry = Entry(right_frame)
total_entry.grid(row=3 , column=3 )

bouton_total = Button(right_frame , text= 'Total' , command=total)
bouton_total.grid(row=5,column=2 , ipadx=10 , ipady=5 )

btn_valider = Button(right_frame, text="Valider", command=valider_commande)
btn_valider.grid(row=5, column=3, pady=10)


bouton_reinitialiser = Button(right_frame , text= 'Reinitialiser' , command=reinitialiser)
bouton_reinitialiser.grid( row=5, column=4 , ipadx=10 , ipady=5 )
 
# AFFICHER LES TROIS  FRAME

titre_frame.pack(side=TOP , fill=X , pady=10)
left_frame.pack(side=LEFT ,  fill=BOTH, expand=True, padx=10, pady=10)
right_frame.pack(side=RIGHT ,  fill=BOTH, expand=True, padx=10, pady=10)

# AFFICHER L'INTERFACE

window.mainloop()