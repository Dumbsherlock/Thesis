import os
from mistralai import Mistral
import pandas as pd
import json


api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

path = "/code//Daten/Syndata/ConvertedData.jsonl"
data = pd.read_json(path_or_buf=path, lines=True)

for i in range(data.shape[0]):
    j = i + 33
    text = data.iloc[j]["text"]
    question = f"""
        Eine Entity ist eine \"Krankheit\". Abstrakte wissenschaftliche Konzepte können Entities sein, wenn sie mit einem Namen verbunden sind. Daten, Zeiten, Adjektive und Verben sind keine Entities.
        
        Beispiel: 
        "Name: Frau Müller Alter: 49 Jahre Geschlecht: weiblich Hauptdiagnose: Mitralklappeninsuffizienz Nebendiagnose: Nichtrheumatische Trikuspidalklappeninsuffizienz Allgemeinbefund:Die Patientin wirkt körperlich gepflegt und altersentsprechend. Sie ist wach und orientiert. Die Atemfrequenz beträgt 18 Atemzüge pro Minute. Der Blutdruck liegt bei 130/85 mmHg. Die Patientin hat keine sichtbaren Symptome einer Atemnot.Herzbefund:Bei der Auskultation des Herzens hört man ein beidseitiges Systolikum, das am besten im Apexbereich und in der Pulmonalklappe zu hören ist. Darüber hinaus sind galoppierende Rhythmen hörbar. Die Herzfrequenz liegt bei 78 Schlägen pro Minute. Der Puls ist regelmäßig.Lungenbefund:Die Lungen sind frei von pathologischen Auffälligkeiten. Es sind keine Atemgeräusche oder Rasselgeräusche zu hören. Die Atembewegungen sind regelmäßig und gleichmäßig.Abdominalbefund:Im Abdomen sind keine Auffälligkeiten tastbar. Die Leber ist nicht vergrößert. Der Darm ist weich und nicht verschoben. Konzentrationsbefund: Die Aufmerksamkeit, Konzentration und Orientierung der Patientin ist unauffällig. Sie kann Fragen korrekt beantworten und zeigt keine kognitiven Beeinträchtigungen. Zusammenfassung: Frau Müller, 49 Jahre alt, weiblich, hat eine Mitralklappeninsuffizienz als Hauptdiagnose sowie eine Nichtrheumatische Trikuspidalklappeninsuffizienz als Nebendiagnose. Bei der körperlichen Untersuchung hört man ein beidseitiges Systolikum im Apexbereich und in der Pulmonalklappe. Darüber hinaus sind galoppierende Rhythmen hörbar. Die Patientin hat keine weiteren pathologischen Auffälligkeiten."

        Beispiel Antwort:
        1.Krankheit: Mitralklappeninsuffizienz |True| da es sich um einen Herzklappenfehler handelt
        2.Krankheit: Nichtrheumatische Trikuspidalklappeninsuffizienz |True| da es eine Undichtigkeit der Trikuspidalklappe des Herzens beschreibt

    

        Ermittele anhand des obigen Absatzes eine Liste möglicher Entities und erkläre, warum es sich entweder um eine Entity handelt oder nicht. Gebe alle gefundenen Entities auch in einer Python Liste wie folgt zurück: 
        {{'collection':  [{{'word': 'Mitralklappeninsuffizienz', 'label': 'Krankheit'}}, {{'word': 'Nichtrheumatische Trikuspidalklappeninsuffizienz','label': 'Krankheit'}}, ]}}
        
        text: {text}
        """


    client = Mistral(api_key=api_key)

    chat_response = client.chat.complete(
        model= model,
        messages = [
            {
                "role": "user",
                "content": question,
            },
        ]
    )
    response = chat_response.choices[0].message.content
    print(response)
    with open(f'/code//Daten/LLMEval/API/eval{j}.jsonl', 'w', encoding='utf-8') as file:
    
            file.write(json.dumps({"id":j,"response": response, "groundTruth": data.iloc[j]["entities"], "text":text}) + '\n')