'''
# Retourner les points de contrôle lié à un point donné

Cet exemple permet de lister les points de contrôle liés à un point donné. La dernière ligne de ce script enregistre l'outil "lister les points de contrôle du point" de la fenêtre glyphe et permet de l'applique au premier point de la liste des points du glyphe actif.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

# lister les points d'un glyphe

def lister_points(glyphe):
  '''Retourne la liste des points du glyphe actif.
  Glyphe -> Liste d'objets Points'''
  # liste des points sélectionnés
  liste_des_points = []
  # s'il n'y a pas de layer actif
  if not glyphe.activeLayer:
      return
  # sinon on prend la référence
  layer = glyphe.layers[glyphe.activeLayer]
  # pour chaque contour dans le layer
  for contour in layer:
    # pour chaque point dans le contour
    for point in contour:
      # on l'ajoute à la liste
      liste_des_points.append(point)
  # que l'on retourne
  return liste_des_points

 ## lister les points de contrôle associés à un point donné

def points_de_controle_du_point(point):
  '''Retourne un tuple correspondant aux points de contrôle liés au point
  Point -> tuple
  La première valeur de Tuple correspond au point précédent,
  la seconde au point suivant.
  Ces valeurs sont égales à False si le point n'a pas
  de point de contrôle le précédant ou le suivant,
  Et corresponde à un objet point le cas contraire.'''
  point_precedent = False
  point_suivant = False
  # si pas de glyphe actif
  if not fontforge.activeGlyph():
    return
  # sinon on prend la référence
  glyphe = fontforge.activeGlyph()
  points_du_glyphe = lister_points(glyphe)
  # Dans un premier temps on retrouve notre point dans la liste actuelle
  for i in range(0, len(points_du_glyphe)):
    # si on retrouve notre point
    if points_du_glyphe[i] == point:
      # point précédent
      if i > 0:
        if not points_du_glyphe[i-1].on_curve:
          point_precedent = points_du_glyphe[i-1]
      # point précédent
      if i < len(points_du_glyphe)-1:
        if not points_du_glyphe[i+1].on_curve:
          point_suivant = points_du_glyphe[i+1]
  return((point_precedent,point_suivant))

# fonction proxy
def btn_points_de_controle_du_point(data,glyphe):
  # on imprime dans le terminal
  # la liste des points de contrôle
  # du premier point de la liste des points sélectionnés
  print points_de_controle_du_point(lister_points(glyphe)[0])

# Enregistrement de l'outil "lister les points de contrôle du point" dans le sous-menu "fontforge-documentation" du menu "outil" de la fenêtre glyphe, et lien vers la fonction "btn_points_de_controle_du_point"
fontforge.registerMenuItem(btn_points_de_controle_du_point,None,None,("Glyph"),None,"fontforge-documentation","lister les points de controle du point")
