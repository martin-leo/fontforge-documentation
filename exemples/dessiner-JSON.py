import fontforge
import json

json_data = '{"glyphname":"A","contours":[{"points":[{"x":"254.0","y":"788.0","on_curve":1},{"x":"29.0","y":"0.0","on_curve":1},{"x":"107.0","y":"0.0","on_curve":1},{"x":"163.0","y":"200.0","on_curve":1},{"x":"448.0","y":"200.0","on_curve":1},{"x":"504.0","y":"0.0","on_curve":1},{"x":"582.0","y":"0.0","on_curve":1},{"x":"357.0","y":"788.0","on_curve":1}]},{"points":[{"x":"305.0","y":"709.0","on_curve":1},{"x":"429.0","y":"265.0","on_curve":1},{"x":"181.0","y":"265.0","on_curve":1}]}]}'

def dessiner_glyphe(donnees, input_glyphe):
  '''Dessine dans un glyphe donné les points correspondant aux données en entrées.
  Objet, Glyphe -> Void
  '''
  # on sélectionne la police
  police = fontforge.activeFont()
  # on créer une plume pour dessiner
  glyphe = police[input_glyphe];
  plume = glyphe.glyphPen()
  # pour chaque contour
  for contour in donnees['contours']:
    # on déplace la plume au niveau du premier point
    plume.moveTo((float(contour['points'][0]['x']),float(contour['points'][0]['y'])));
    # pour les points suivants
    for point in contour['points'][1:]:
      # on trace des lignes
      plume.lineTo((float(point['x']),float(point['y'])));
    # on finit par clore le tracé
    plume.closePath();
  # on supprime la plume pour forcer le rafraîchissement
  plume = None;

# on parse le JSON
data = json.loads(json_data)

# on dessine le JSON dans le glyphe B
dessiner_glyphe(data, "B")
