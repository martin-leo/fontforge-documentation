'''
# Lister les glyphes sélectionnés

Cet exemple permet de lister les glyphes sélectionnés dans l'UI. La dernière ligne de ce script enregistre l'outil "lister les glyphes selectionnes" de la fenêtre glyphe.

Pensez à importer le module fontforge en décommentant la ligne appropriée si besoin.
'''
# import fontforge

def lister_glyphes_selectionnes():
  '''Retourne une liste des glyphes sélectionné dans la police active.
  Void -> Liste d'objets Glyphe'''
  try:
    # liste des glyphes sélectionnés
    liste_des_glyphes_selectionnes = []
    # police active
    police_active = fontforge.activeFont()
    # pour chaque glyphe de la police
    for glyphe in police_active.glyphs():
      # on vérifie s'il est sélectionné
      if police_active.selection[glyphe]:
        # si oui on l'ajoute à la liste des glyphes sélectionnés
        liste_des_glyphes_selectionnes.append(glyphe)
    # on retourne la liste des glyphes sélectionnés
    return liste_des_glyphes_selectionnes
  except:
    print("lister_glyphes_selectionnes() a rencontré une erreur", sys.exc_info()[0])

# fonction proxy
def btn_lister_glyphes_selectionnes(data,font):
  # on imprime dans le terminal
  # la liste des glyphes sélectionnés
  print lister_glyphes_selectionnes()

# Enregistrement de l'outil "lister les glyphes selectionnes" dans le sous-menu "fontforge-documentation" du menu "outil" de la fenêtre glyphe, et lien vers la fonction "btn_lister_glyphes_selectionnes"
fontforge.registerMenuItem(btn_lister_glyphes_selectionnes,None,None,("Glyph"),None,"fontforge-documentation","lister les glyphes selectionnes")
