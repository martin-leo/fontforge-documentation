'''
# Lister les contours du glyphe actif

La fonction lister_contours permet de lister les Contours (groupes de points) d'un glyphe donné. La dernière ligne de ce script enregistre l'outil "lister les contours" de la fenêtre glyphe et permet de l'applique au glyphe actif.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

def lister_contours(glyphe):
  '''Retourne une liste de contours pour un glyphe donné.
  Glyphe -> Liste d'objets Contours'''
  # liste des contours
  liste_des_contours = []
  # si pas de layer actif
  if not glyphe.activeLayer:
    return
  # sinon on prend la référence
  layer = glyphe.layers[glyphe.activeLayer]
  # pour chaque contour dans le layer
  for contour in layer:
    # on ajoute à la liste
    liste_des_contours.append(contour)
  # que l'on retourne
  return liste_des_contours

# fonction proxy
def btn_lister_contours(data, glyphe):
  # on imprime dans le terminal
  # la liste des contours
  print lister_contours(glyphe)

# Enregistrement de l'outil "lister les contours" dans le sous-menu "fontforge-documentation" du menu "outil" de la fenêtre glyphe, et lien vers la fonction "btn_lister_contours"
fontforge.registerMenuItem(btn_lister_contours,None,None,("Glyph"),None,"fontforge-documentation","lister les contours")
