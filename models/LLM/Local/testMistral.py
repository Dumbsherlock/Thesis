import ollama
import pandas as pd
import json

path = "/code//Daten/doccano_annotations/cedis/second/cedis_151.jsonl"
data = pd.read_json(path_or_buf=path, lines=True)

texts = "\"Selbstständige fußläufige Vorstellung in unserer Notaufnahme mit Einweisung vom Hausarzt und in Begleitung der Tochter. Die Patientin ist in domo bekannt. Therapie bei Mantelzell-Lymphom. Aktuell laut Hausarzt massive Leukopenie, sowie Nierenversagen nach dem 2. Zyklus Chemotherapie Schema R-DHAP. Zuletzt stationär bis zum 26.03.2024.\n\n\n\n\n\n\n\nAufgrund der Sprachbarriere übersetzt die Tochter. Die Patientin habe aktuell keine Beschwerden, die Vorstellung erfolgt aufgrund der schlechten Blutwerte. Keine AP-Beschwerden, keine Dyspnoe.  \n\n\n\n\n\n\n\nKein Fieber, kein Infekt in letzter Zeit. Keine Beschwerden bei Miktion oder Defäkation, kein Durchfall.\n."

desiredModel = "hf.co/lmstudio-community/Mistral-Nemo-Instruct-2407-GGUF:Q4_K_M"
for i in range(data.shape[0]):
    j = i +134
    text = data.iloc[j]["text"]
        
    question = f"""
    Eine Entity ist eine \"Vorerkrankung\", \"Medikament\", \"Prozedur\", \"Vordiagnose\", \"Symptom\", \"Negation\", \"Anatomie\",\"Unfall\". Abstrakte wissenschaftliche Konzepte können Entities sein, wenn sie mit einem Namen verbunden sind. Daten, Zeiten, Adjektive und Verben sind keine Entitäten.
    
    Beispiel: 
    Herr Max Mustermann, geboren am 15.04.1975, wurde am 28.01.2025 aufgenommen. Er hat bereits eine chronische Hypertonie, die mit Amlodipin (5 mg täglich) behandelt wird. Zudem nimmt Ibuprofen gegen Rückenbeschwerden. Am 25.01.2025 erfolgte eine Biopsie eines Tumors in der Lunge, deren Ergebnisse noch ausstehen. Es liegt eine Vordiagnose auf ein primäres Lungenkarzinom vor, basierend auf CT und MRT. Der Patient klagt über Brustschmerzen und Husten. Es gibt keine Hinweise auf Metastasen oder lymphatischer Involvierung. Der Tumor befindet sich im oberen rechten Lungenlappen. Vor drei Wochen verletze er sich beim Treppensteigen und zog er sich eine Prellung des linken Oberschenkels zu, die ohne Komplikationen heilt.
    Beispiel Antwort:
    1.Vorerkrankung: Chronische Hypertonie|True| da diese Erkrankung schon vor der Aufnahne bestand
    2.Medikament: Amlodipin |True| da es der Name eines Medikaments ist 
    3.Medikment: Ibuprofen |True| da es der Name eines Medikaments ist
    4.Prozedur: Biopsie |True| da es eine Behandlung eines Tumors ist
    5.Vordiagnose: Primäres Lungenkarzinom |True| da diese Diagnose vor der Aufnahme getätigt wurde
    6.Symptom: Brustschmerzen |True| ist Symptom einer Erkrankung
    7.Symptom: Husten |True| ist Symptom einer Erkrankung
    8.Symptom: Gewichtsverlust |True| ist Symptom einer Erkrankung
    9.Negation: Keine |True| Verneinung der Aussage 
    10.Anatomie: Oberer rechter Lungenlappen |True| beschreibt ein Organ oder Körperteil
    11.Unfall: Sturz beim Treppensteigen |True| Beispiel eines Haushaltunfalls
    12.Unfall: Prellung des linken Oberschenkels |True| Beispiel eines Haushaltunfalls
 

    Ermittele anhand des obigen Absatzes eine Liste möglicher Entities und erkläre, warum es sich entweder um eine Entity handelt oder nicht. Gebe alle gefundenen Entities auch in einer Python Liste wie folgt zurück, füge keine Kommentare hinzu: 
    {{'collection':  [{{'word': 'Chronische Hypertonie', 'label': 'Vorerkrankung'}}, {{'word': 'Amlodipin','label': 'Medikament'}}, {{'word': 'Husten','label': 'Symptom'}}, {{'word': 'Brustschmerzen','label': 'Symptom'}}, {{'word': 'Primäres Lungenkarzinom','label': 'Vordiagnose'}}, {{'word': 'Biopsie','label': 'Prozedur'}}, {{'word': 'Oberer rechter Lungenlappen','label': 'Anatomie'}}, {{'word': 'Sturz beim Treppensteigen','label': 'Unfall'}}, {{'word': 'Prellung des linken Oberschenkels','label': 'Unfall'}}, {{'word': 'Ibuprofen','label': 'Medikament'}}, {{'word': 'Gewichtsverlust','label': 'Symptom'}}, {{'word': 'Keine','label': 'Negation'}}]}}
    
    text: {text}
    """
#Annotation für die Entities genauer machen -> falls LLM ein word anottiert welches gar nichr existiert, dann wird es nicht annotiert ->  model scheont besser zu sein als es ist-


    response = ollama.chat(model=desiredModel, messages = [
    {
        "role": "user",
        "content": question
        }
    ])

    Ollamaresponse = response["message"]["content"]
    print(Ollamaresponse)
    with open(f'/code//Daten/LLMEval/Local/ThirdTry/eval{j}.jsonl', 'w', encoding='utf-8') as file:
    
                file.write(json.dumps({"id":j,"response": Ollamaresponse, "groundTruth": data.iloc[j]["entities"], "text":text}) + '\n')
