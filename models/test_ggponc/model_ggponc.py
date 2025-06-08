
import spacy
nlp = spacy.load('/code/.venvGG/Lib/site-packages/de_ggponc_medbertde/de_ggponc_medbertde-1.0.0')
d = nlp("allein nach Versagen einer Behandlung mit Oxaliplatin und Irinotecan")
for e in d.spans['entities']:
  print(e, e.label_)
