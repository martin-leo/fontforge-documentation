'''
# Lister les points de contrôle d'un glype

Cet exemple permet de lister les points de contrôle du glyphe. La dernière ligne de ce script enregistre l'outil "lister les points de controle du glyphe" de la fenêtre glyphe et permet de l'applique au glyphe actif.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

def lister_points_de_controle(glyphe):
  '''Return the active glyph's control points
  Glyph -> Points List'''
  liste_des_points_de_controle = []
  # si pas de layer actif
  if not glyphe.activeLayer:
      return
  # sinon on prend la référence
  layer = glyphe.layers[glyphe.activeLayer]
  # pour chaque contour dans le layer
  for contour in layer:
      # pour chaque point dans le contour
      for point in contour:
          # on vérifie s'il n'est pas sur la courbe (= point de contrôle)
          if not point.on_curve == 1:
            # on ajoute à la liste
            liste_des_points_de_controle.append(point)
  # que l'on retourne
  return liste_des_points_de_controle

# fonction proxy
def btn_lister_points_de_controle(data,glyphe):
  # on imprime dans le terminal
  # la liste des points de contrôle
  print lister_points_de_controle(glyphe)

fontforge.registerMenuItem(btn_lister_points_de_controle,None,None,("Glyph"),None,"fontforge-documentation","lister les points de controle du glyphe")
