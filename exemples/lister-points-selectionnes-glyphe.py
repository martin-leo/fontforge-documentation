'''
# Lister les points sélectionnés du glyphe actif

Cet exemple permet de lister les points sélectionnés (y compris les points de contrôles) d'un glyphe donné. La dernière ligne de ce script enregistre l'outil "lister les points sélectionnés" de la fenêtre glyphe et permet de l'applique au glyphe actif.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

def lister_points_selectionnes(glyphe):
  '''Retourne la liste des points sélectionnés du glyphe actif.
  Glyphe -> Liste d'objets Points'''
  # liste des points sélectionnés
  liste_des_points_selectionnes = []
  # s'il n'y a pas de layer actif
  if not glyphe.activeLayer:
      return
  # sinon on prend la référence
  layer = glyphe.layers[glyphe.activeLayer]
  # pour chaque contour dans le layer
  for contour in layer:
    # pour chaque point dans le contour
    for point in contour:
      # s'il est sélectionné
      if point.selected:
        # on l'ajoute à la liste
        liste_des_points_selectionnes.append(point)
  # que l'on retourne
  return liste_des_points_selectionnes

# fonction proxy
def btn_lister_points_selectionnes(data,glyph):
  # on imprime dans le terminal
  # la liste des points sélectionnés
  print lister_points_selectionnes(glyph)

# Enregistrement de l'outil "lister les points sélectionnés" dans le sous-menu "fontforge-documentation" du menu "outil" de la fenêtre glyphe, et lien vers la fonction "btn_lister_points_selectionnes"
fontforge.registerMenuItem(btn_lister_points_selectionnes,None,None,("Glyph"),None,"fontforge-documentation","lister les points selectionnes")
