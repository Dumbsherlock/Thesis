# #activate .venv to use this model
# from transformers import pipeline
# classifier = pipeline("token-classification", model="/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base", aggregation_strategy="simple")

# text = "Selbstständige fußläufige Vorstellung in unserer Notaufnahme mit Einweisung vom Hausarzt und in Begleitung der Tochter. Die Patientin ist in domo bekannt. Therapie bei Mantelzell-Lymphom. Aktuell laut Hausarzt massive Leukopenie, sowie Nierenversagen nach dem 2. Zyklus Chemotherapie Schema R-DHAP. Zuletzt stationär bis zum 26.03.2024."
# result = classifier(text)
# print(result)
# for entity in result:
#     print(f"{entity['entity']} - {entity['score']} - {entity['index']} - {entity['word']}")
import pandas as pd
import json 
def countMentions():
    path = '/code//Daten/SilverStandardDaten/V3CountedPartialData.jsonl'
    data = pd.read_json(path_or_buf=path, lines=True)
    VoerkrankungCount = 0
    MedikamentCount = 0
    SymptomCount = 0
    AnatomyCount = 0
    ProcedureCount = 0
    Unfallcount = 0

    for i in range (data.shape[0]):
        y = data.iloc[i]
        mentionsList = []
        usefulFlag = False
        for each in y["entities"]:
            if(each["label"] == "Vorerkrankung" ):
                VoerkrankungCount = VoerkrankungCount + 1     
            elif(each["label"] == "Medikament" ):
                MedikamentCount = MedikamentCount + 1
                
            elif(each["label"] == "Symptom" ): 
                SymptomCount = SymptomCount + 1
            
            elif(each["label"] == "Anatomie" ):
                AnatomyCount = AnatomyCount + 1

            elif(each["label"] == "Prozedur" ):
                ProcedureCount = ProcedureCount + 1
                #should be Vordiagnose?
                
            elif(each["label"] == "Prozedur"  ):
                ProcedureCount = ProcedureCount + 1
        
            elif(each["label"] == "Prozedur" ):
                ProcedureCount = ProcedureCount + 1
            
            elif(each["label"] == "Unfall"    ):
                Unfallcount = Unfallcount + 1
                #should be Vordiagnose?
                
            elif(each["label"] == "Anatomie" ):
                AnatomyCount = AnatomyCount + 1
                
    print("Vorerkrankung: " + str(VoerkrankungCount))
    print("Medikament: " + str(MedikamentCount))
    print("Symptom: " + str(SymptomCount))  
    print("Anatomy: " + str(AnatomyCount))
    print("Procedure: " + str(ProcedureCount))
    print("Unfall: " + str(Unfallcount))

def countMentionsIOB():
    path = '/code//Daten/SilverStandardDaten/processed/V3/test.json'
    data = pd.read_json(path_or_buf=path, lines=True)
    VoerkrankungCount = 0   
    MedikamentCount = 0
    SymptomCount = 0
    AnatomyCount = 0
    ProcedureCount = 0
    Unfallcount = 0
    for i in range (data.shape[0]):
        y = data.iloc[i]
        mentionsList = []
        usefulFlag = False
        for each in y["ner_tags"]:
            if(each == "B-Vorerkrankung" ):
                VoerkrankungCount = VoerkrankungCount + 1     
            elif(each == "B-Medikament" ):
                MedikamentCount = MedikamentCount + 1
                
            elif(each == "B-Symptom" ): 
                SymptomCount = SymptomCount + 1
            
            elif(each == "B-Anatomie" ):
                AnatomyCount = AnatomyCount + 1

            elif(each == "B-Prozedur" ):
                ProcedureCount = ProcedureCount + 1
                #should be Vordiagnose?
                
            elif(each == "B-Prozedur"  ):
                ProcedureCount = ProcedureCount + 1
        
            elif(each == "B-Prozedur" ):
                ProcedureCount = ProcedureCount + 1
            
            elif(each == "B-Unfall"    ):
                Unfallcount = Unfallcount + 1
                #should be Vordiagnose?
                
            elif(each == "B-Anatomie" ):
                AnatomyCount = AnatomyCount + 1
    print("Vorerkrankung: " + str(VoerkrankungCount))
    print("Medikament: " + str(MedikamentCount))
    print("Symptom: " + str(SymptomCount))
    print("Anatomy: " + str(AnatomyCount))
    print("Procedure: " + str(ProcedureCount))
    print("Unfall: " + str(Unfallcount))
    
    
countMentionsIOB()
        
