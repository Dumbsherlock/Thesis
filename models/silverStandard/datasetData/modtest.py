
from transformers import PreTrainedTokenizerFast
import pandas as pd
from nervaluate import Evaluator

model_path = '/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base'
model_path2 = '/code//Code/scripts/tmp/test-ner/Scia-Bio-Disease/SCAI-BIO/bio-gottbert-base'
model_path3 = '/code//Code/scripts/tmp/test-ner/Scia-Bio-CountedDataset/SCAI-BIO/bio-gottbert-base' 
model_path4 = '/code//Code/scripts/tmp/test-ner/Scia-Bio-V2CountedDataset/SCAI-BIO/bio-gottbert-base'

from transformers import pipeline
# classifier = pipeline('ner', model='/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base')
token_classifier = pipeline('token-classification', model=model_path3 , aggregation_strategy='simple')


print(token_classifier("""
                       'E'Folgende', 'Symptome', 'k\u00f6nnen', 'auftreten:', 'In', 'der', 'Symptomatik', 'ist', 'die', 'Krankheit', 'leicht', 'mit', 'Tuberkulose', 'zu', 'verwechseln.', 'Diagnostik.', 'Die', 'Hauptkriterien', 'der', 'ABPA', 'sind:', 'Nebenkriterien:', 'Das', 'Diagnosemittel', 'der', 'Wahl', 'bleibt', 'die', 'R\u00f6ntgenaufnahme', 'der', 'Lunge', 'und', 'evtl.', 'auch', 'eine', 'hochaufl\u00f6sende', 'Computertomographie', '(CT),', 'bei', 'der', 'gro\u00dffl\u00e4chige', 'Verschattungen', 'durch', 'einen', 'bronchialen', 'Sekretstau', '(mucoid', 'impactions)', 'zu', 'erkennen', 'sind', 'und', 'sich', 'in', 'der', 'Regel', 'auch', 'zentrale', 'Bronchiektasien', 'feststellen', 'lassen.'
                       """))
