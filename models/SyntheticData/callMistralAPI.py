import os
from mistralai import Mistral
import pandas as pd
import json

def translate_code_to_disease(code):
    listCode1 = []
    listCode2 = []
    
    frequency_path = "/code//Daten/Syndata_EvalAluminum/frequency.csv"
    icd_path = "/code//Daten/Syndata_EvalAluminum/ICD-10-GM-Katalog2023.xlsx"
    
    freq_data = pd.read_csv(frequency_path, nrows=1000)
    icd_data = pd.read_excel(icd_path,engine="openpyxl", usecols="H,K") 

    for i in range(freq_data.shape[0]):	
        code1 = freq_data.iloc[i]["Code1"]
        code2 = freq_data.iloc[i]["Code2"] 
        try:
            disease1 = icd_data[icd_data["Unnamed: 7"] == code1]["Unnamed: 10"].values[0]
            listCode1.append(disease1)
        except:
            listCode1.append("Error")
       
        try:
            disease2 = icd_data[icd_data["Unnamed: 7"] == code2]["Unnamed: 10"].values[0]
            listCode2.append(disease2)
        except:
           listCode2.append("Error")
    
        print(disease1)
        print(disease2)    
    freq_data["Disease1"] = listCode1
    freq_data["Disease2"] = listCode2   
    
    df = pd.DataFrame(freq_data, )
    df.to_csv("/code//Daten/Syndata_EvalAluminum/output_4_Bezeichner.csv", index=False)

    print("CSV file created successfully!")
    
    # print(freq_data.head())
    # print(icd_data.iloc[3:7])
    # print(search_results)



def callMistralAPI():
   
    api_key = os.environ["MISTRAL_API_KEY"]
    model = "mistral-large-latest"
 #   data = pd.read_json(path_or_buf=path, lines=True)
    disease_occurrence_path = "/code//Daten/Syndata_EvalAluminum/frequency.csv"
 

    responseList = []

    for i in range(500):
       # text = data.iloc[j]["text"]
        j = i
        print(j)
       
        client = Mistral(api_key=api_key) 
        chat_response = client.chat.complete(
            model= model,
            messages = [
                            {
                                "role": "user",
                                "content": """Du bist ein Daten generator und annotator für synthetische Untersuchungsbefunde von Patienten aus der Onkologie. Erstelle einen synthetischen Befund für einen Patienten. Der Befund soll Informationen über Vorerkrankungen, Medikamente, Prozeduren, Vordiagnosen, Symptome, Anatomie und Unfälle enthalten, zudem sollen Negationen verwendet werden. Der Befund soll in deutscher Sprache verfasst sein und folgendem format ensprechen:
                                [{"text": Befundtext, "entities":[{"word": "Vorerkrankung", "label": "Vorerkrankung"}, {"word": "Medikament","label": "Medikament"}, {"word": "Symptom","label": "Symptom"}, {"word": "Vordiagnose","label": "Vordiagnose"}, {"word": "Prozedur","label": "Prozedur"}, {"word": "Anatomie","label": "Anatomie"}, {"word": "Unfall","label": "Unfall"}, {"word": "Negation", "label": "Negation"}]}]
                                """
                            },
                            {
                                "role": "assistant",
                                "content": """{"text":"Selbstständige Vorstellung in unserer Notaufnahme mit Einweisung vom Hausarzt und in Begleitung der Tochter. Die Patientin ist in domo bekannt. Therapie bei Mantelzell-Lymphom. Aktuell laut Hausarzt massive Leukopenie, sowie Nierenversagen nach dem 2. Zyklus Chemotherapie Schema R-DHAP. Zuletzt stationär bis zum 26.03.2024. Aufgrund der Sprachbarriere übersetzt die Tochter. Die Patientin habe aktuell keine Beschwerden, die Vorstellung erfolgt aufgrund der schlechten Blutwerte. Keine AP-Beschwerden, keine Dyspnoe. Kein Fieber, kein Infekt in letzter Zeit. Keine Beschwerden bei Miktion oder Defäkation. Durchfall wurde nicht erwähnt.", "entities":[{"word": "Chronische Hypertonie", "label": "Vorerkrankung"}, {"word": "Amlodipin","label": "Medikament"}, {"word": "Husten","label": "Symptom"}, {"word": "Brustschmerzen","label": "Symptom"}, {"word": "Primäres Lungenkarzinom","label": "Vordiagnose"}, {"word": "Biopsie","label": "Prozedur"}, {"word": "Oberer rechter Lungenlappen","label": "Anatomie"}, {"word": "Sturz beim Treppensteigen","label": "Unfall"}, {"word": "Prellung des linken Oberschenkels","label": "Unfall"}, {"word": "Ibuprofen","label": "Medikament"}, {"word": "Gewichtsverlust","label": "Symptom"}, {"word": "Keine","label": "Negation"}, {"word":"nicht,""label":"Negation"}]}""",
                            },
                            {
                                "role": "user",
                                "content": "Führe die vorherige Aufgabe erneut aus.",
                            },
            ]
        )
        response = chat_response.choices[0].message.content
        with open(f"/code//Daten/SynData/API_generated_data/split/testrun{j}.jsonl", "w", encoding="utf-8") as file:
            file.write(json.dumps(response) + "\n")
        
        responseList.append(response)
        
        
  
        
if __name__ == "__main__":
   # callMistralAPI()
    translate_code_to_disease("I10")
    #callMistralAPI()