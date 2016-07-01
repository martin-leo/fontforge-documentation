'''
# Conversion d'un glyphe en JSON

Cet exemple permet de convertir un glyphe en JSON (imprimé dans le terminal).

La dernière ligne de ce script enregistre l'outil "convertir en JSON" de la fenêtre glyphe et permet de l'applique au glyphe actif.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

# Listage des éléments (Contours, Points) d'un glyphe

def lister_contours(glyphe):
  '''Retourne la liste des contours du glyphe donné
  Glyphe -> Liste d'objets Contour'''
  # liste des contours
  liste_des_contours = []
  # s'il n'y a pas de layer actif
  if not glyphe.activeLayer:
    return
  # sinon on prend la référence
  layer = glyphe.layers[glyphe.activeLayer]
  # pour chaque contour dans le layer
  for contour in layer:
    # on ajoute à la liste
    liste_des_contours.append(contour)
  # on la retourne
  return liste_des_contours

# Conversion en JSON

def glyphe_vers_json(glyphe):
  '''Retourne une version JSON d'un glyphe donné
  Glyphe -> JSON'''
  # ouverture du JSON
  json = '{'
  # propriété glyphname
  json += '"glyphname":"' + glyphe.glyphname + '",'
  # propriété contours (liste)
  json += '"contours":['
  # on peuple avec les contours en json
  for contour in lister_contours(glyphe):
    json += contour_vers_json(contour) + ","
  # on enlève la dernière virgule inutile !
  json = json[:-1]
  # on ferme la liste
  json += ']'
  # et le JSON
  json += '}'
  # que l'on retourne
  return json

def contour_vers_json(contour):
  '''Retourne une version JSON d'un contour donné
  Contour -> JSON'''
  # ouverture du JSON
  json = '{'
  # propriété points (liste)
  json += '"points":['
  for point in contour:
    json += point_vers_json(point) + ","
  # on enlève la dernière virgule inutile !
  json = json[:-1]
  # on clôt la liste
  json += ']'
  # et le JSON
  json += '}'
  # que l'on retourne
  return json

def point_vers_json(point):
  '''Retourne une version JSON d'un point donné
  Contour -> JSON'''
  # ouverture du JSON
  json = '{'
  # propriété x
  json += '"x":"' + str(point.x) + '",'
  # propriété y
  json += '"y":"' + str(point.y) + '",'
  # propriété on_curve
  json += '"on_curve":' + str(point.on_curve)
  # on ferme le JSON
  json += '}'
  # que l'on retourne
  return json

# fonction proxy
def btn_glyphe_vers_json(data,glyphe):
  '''Imprime la version JSON du glyphe donné dans la console
  data, Glyphe -> JSON'''
  # on imprime dans le terminal le resultat
  # de la conversion en JSON du glyphe
  # contenu dans la fenêtre glyphe
  print(glyphe_vers_json(glyphe))

# Enregistrement de l'outil "convertir en JSON" dans le sous-menu "fontforge-documentation" du menu "outil" de la fenêtre glyphe, et le lie à la fonction "btn_glyphe_vers_json"
fontforge.registerMenuItem(btn_glyphe_vers_json,None,None,("Glyph"),None,"fontforge-documentation","convertir en JSON")
