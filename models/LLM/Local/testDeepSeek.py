import ollama

desiredModel = "deepseek-r1:7b"
question = """
Beispiel:
Herr Max Mustermann, geboren am 15.04.1975, wurde am 28.01.2025 aufgenommen. Er hat bereits eine chronischer Hypertonie, die mit Amlodipin (5 mg täglich) behandelt wird. Zudem nimmt Ibuprofen gegen Rückenbeschwerden. Am 25.01.2025 erfolgte eine Biopsie eines Tumors in der Lunge, deren Ergebnisse noch ausstehen. Es liegt eine Vordiagnose auf ein primäres Lungenkarzinom vor, basierend auf CT und MRT. Der Patient klagt über Brustschmerzen und Husten. Es gibt keine Hinweise auf Metastasen oder lymphatischer Involvierung. Der Tumor befindet sich im oberen rechten Lungenlappen. Vor drei Wochen verletze er sich beim Treppensteigen und zog er sich eine Prellung des linken Oberschenkels zu, die ohne Komplikationen heilt.

Beispiel Antwort:
1.Vorerkrankung: Chronische Hypertonie|True| da es eine 2.Krankheit ist
3.Medikament: Amlodipin, Ibuprofen |True| da es bekannte Medikamente sind
4.Prozedur: Biopsie des Tumors |True| da es eine Behanldugn eines Tumors ist
5.Vordiagnose: Primäres Lungenkarzinom |True| da es als Vordiagnose genannt wird
7.Symptom: Brustschmerzen, Husten, Gewichtsverlust |True| Symptome
8.Negation: Keine Metastasen, keine lymphatische Involvierung |True| Verneinung der Aussagen 
7.Anatomie: Oberer rechter Lungenlappen |True| beschreibt Organ
8.Unfall: Sturz beim Treppensteigen, Prellung des linken Oberschenkels |True| Beispiel eines Haushaltunfalls

Eine Entity ist eine Vorerkrankung, Medikament, Prozedur, Vordiagnose, Symptom, Negation, Anatomie, Unfall.

Basierend auf dem oben genannten Beispiel, identifiziere alle Enities und erkläre warum bzw. warum etwas keine der oben genannten Entites ist, und gebe sie im format einer Python list mit Start und end index zurück:

Herr Johann Beispiel, geboren am 22.06.1968, wurde am 05.02.2025 aufgenommen. Er leidet an Diabetes Typ 2, der mit Metformin (850 mg zweimal täglich) behandelt wird. Zudem nimmt er Paracetamol wegen gelegentlicher Gelenkschmerzen. Am 02.02.2025 wurde eine Gewebeentnahme aus einem Knoten in der Leber durchgeführt, deren Ergebnisse noch ausstehen. Basierend auf CT- und MRT-Befunden besteht der Verdacht auf ein hepatozelluläres Karzinom. Der Patient klagt über Müdigkeit und Appetitlosigkeit. Es gibt keine Hinweise auf Fernmetastasen oder Lymphknotenbefall. Der Tumor befindet sich im rechten Leberlappen. Vor einem Monat stürzte er auf Glatteis und erlitt eine Verstauchung des rechten Handgelenks, die komplikationslos verheilt.
"""

response = ollama.chat(model=desiredModel, messages = [
   {
    "role": "user",
    "content": question
    }
])

Ollamaresponse = response["message"]["content"]

print(Ollamaresponse)