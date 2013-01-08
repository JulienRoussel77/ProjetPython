#encoding:latin1
from numpy import *
from random import *
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.cbook as cbook
from PIL import Image
import sys
from time import *
largeur = 512
hauteur = 512
pasEspace = 20		
		
class Noeud:
	def __init__(self, pere, dx, dz):
		if pere != None:
			self.x = pere.x + dx
			self.z = pere.z + dz
		else:
			self.x = dx
			self.z = dz
		self.pere = pere
		self.gauche = None
		self.droit = None
		self.haut = None
		self.ombre = False;
		
class Feuille(Noeud) :
	def __init__(self, pere, dx, dz):
		Noeud.__init__(self, pere, dx, dz)
		self.truc = 0
	def affiche(self, fig, ax):				
		square = plt.Circle((pasEspace*self.x,pasEspace*self.z), pasEspace/2, color='r', fill = False)
		fig.gca().add_artist(square)
	
class Branche(Noeud) :
	def __init(self, pere, dx, dz):
		Noeud.__init__(self, pere, dx, dz)
		self.truc = 0
	def feuilleGauche(self):
		self.gauche = Feuille(self, -1, 0)
	def feuilleDroit(self):
		self.droit = Feuille(self, 1, 0)
	def feuilleHaut(self):
		self.haut = Feuille(self, 0, 1)
	def brancheGauche(self):
		self.gauche = Branche(self, -1, 0)
	def brancheDroit(self):
		self.droit = Branche(self, 1, 0)
	def brancheHaut(self):
		self.haut = Branche(self, 0, 1)
	def affiche(self, fig, ax):				
		square = plt.Circle((pasEspace*self.x,pasEspace*self.z), pasEspace/2, color='r', fill = True)
		fig.gca().add_artist(square)
		if (self.gauche != None): self.gauche.affiche(fig, ax)
		if (self.droit != None): self.droit.affiche(fig, ax)
		if (self.haut != None): self.haut.affiche(fig, ax)
		
class Arbre:
	# """Un noeud est defini par sa racine."""
	def __init__(self, x0, z0):				#Compexité : O(1)
		self.racine = Branche(None, x0, z0)
		self.x = x0
		self.z = z0
	def affiche(self):
		fig = plt.gcf()
		ax = plt.gca()
		ax.cla()
		ax.set_xlim((0,largeur))
		ax.set_ylim((0,hauteur))
		self.racine.affiche(fig, ax)
		# fig.savefig("Arbre")
		plt.show()
	# def jouer(self):
		
		
#stocker la hauteur des feuilles les plus hautes dans un tableau
a1 = Arbre(5,1)
a1.racine.brancheHaut()
a1.racine.feuilleDroit()
a1.affiche()