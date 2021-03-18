from BFS import BFS
from DFS import DFS
from Astar import ASTART
from IDFS import IDFS
from Graphe import graphe, adjacency_list
from collections import deque

# On importe Tkinter
from tkinter import *


class Interface:
    # ################################################ BFS ###############################################################
    #
    # print('Pour le recherche en BFS...')
    # nodeStartBfs = input('Quel est votre noeud de départ? ')
    # nodeFinaleBfs = input('Quel est votre noeud de finale? ')
    #
    # bfs = BFS(graphe)
    # bfsList = bfs.rechercherBFS(graphe, nodeStartBfs, nodeFinaleBfs)
    #
    # # On crée une fenêtre, racine de notre interface
    # fenetreBfs = Tk()
    #
    # # On crée un label (ligne de texte) souhaitant la bienvenue
    # # Note : le premier paramètre passé au constructeur de Label est notre
    # # interface racine
    #
    # champ_label = Label(fenetreBfs, text=('bfs :' + str(bfsList)))
    #
    # # On affiche le label dans la fenêtre
    # champ_label.pack()
    #
    # # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    # fenetreBfs.mainloop()
    # #
    # ################################################## DFS ###############################################################
    #
    # print('Pour le recherche en DFS...')
    # nodeStartDfs = input('quel est votre noeud de départ? ')
    # nodeFinaleDfs = input('quel est votre noeud de finale?')
    #
    # dfs = DFS(graphe)
    # dfsList = dfs.rechercherDFS(graphe, nodeStartDfs, nodeFinaleDfs)
    # # print(dfsList)
    #
    # # On crée une fenêtre, racine de notre interface
    # fenetreDfs = Tk()
    #
    # # On crée un label (ligne de texte) souhaitant la bienvenue
    # # Note : le premier paramètre passé au constructeur de Label est notre
    # # interface racine
    #
    # champ_label = Label(fenetreDfs, text=('dfs'+ str(dfsList)))
    #
    # # On affiche le label dans la fenêtre
    # champ_label.pack()
    #
    # # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    # fenetreDfs.mainloop()
    #
    # print('Merciiiiiiiii')

    # ############################################### A* ##################################################################
    #
    # print('Pour le recherche en A*...')
    # nodeStartASTAR = input('quel est votre noeud de départ? ')
    # nodeFinaleASTAR = input('quel est votre noeud de finale?')
    #
    # astart = ASTART(adjacency_list)
    # astartList = astart.rechercherASTAR(adjacency_list, nodeStartASTAR, nodeFinaleASTAR)
    #
    # # print(dfsList)
    #
    # # On crée une fenêtre, racine de notre interface
    # fenetreAstart = Tk()
    #
    # # On crée un label (ligne de texte) souhaitant la bienvenue
    # # Note : le premier paramètre passé au constructeur de Label est notre
    # # interface racine
    #
    # champ_label = Label(fenetreAstart, text=('Astart '+ str(astartList)))
    #
    # # On affiche le label dans la fenêtre
    # champ_label.pack()
    #
    # # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    # fenetreAstart.mainloop()
    #
    # print('Merciiiiiiiii')


    ############################################### IDDFS ##################################################################

    print('Pour le recherche en IDFS...')
    nodeStartIDFS = input('quel est votre noeud de départ? ')
    nodeFinaleIDFS = input('quel est votre noeud de finale?')

    idfs = IDFS(graphe)
    idfsList = idfs.rechercherIDFS(nodeStartIDFS, nodeFinaleIDFS, graphe, 4)

    # print(dfsList)

    # On crée une fenêtre, racine de notre interface
    fenetreIdfs = Tk()

    # On crée un label (ligne de texte) souhaitant la bienvenue
    # Note : le premier paramètre passé au constructeur de Label est notre
    # interface racine

    champ_label = Label(fenetreIdfs, text=('IDFS '+ str(idfsList)))

    # On affiche le label dans la fenêtre
    champ_label.pack()

    # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
    fenetreIdfs.mainloop()

    print('Merciiiiiiiii')