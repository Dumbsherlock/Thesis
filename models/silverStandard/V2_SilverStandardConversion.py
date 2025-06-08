import json
import pandas as pd  
path = "/code/SilverStandard/BEL-silver-standard/BEL-silver-standard/WikiMed-DE/WikiMed-DE.json"

data = pd.read_json(path_or_buf=path )
nerList = []

VoerkrankungCount = 0
MedikamentCount= 0
SymptomCount = 0 
AnatomyCount    = 0
ProcedureCount = 0
Unfallcount = 0

for i in range (data.shape[0]):
    x = data.iloc[i]
    mentionsList = []
    usefulFlag = False
    for y in x["mentions"]:
        if(y["semantic_type"] == "Disease or Syndrome" and y["start_index"] >= 0 and VoerkrankungCount < 10000):
             mentionsList.append( {  "word":y["mention"], "label":"Vorerkrankung", "start_offset":y["start_index"], "end_offset":y["end_index"]})
             usefulFlag = True
             VoerkrankungCount = VoerkrankungCount + 1
             
        elif(y["semantic_type"] == "Clinical Drug" and y["start_index"] >= 0 and MedikamentCount < 10000):
             mentionsList.append( {  "word":y["mention"], "label":"Medikament", "start_offset":y["start_index"], "end_offset":y["end_index"]})
             usefulFlag = True
             MedikamentCount = MedikamentCount + 1
        elif(y["semantic_type"] == "Sign or Symptom" and y["start_index"] >= 0 and SymptomCount < 10000): 
            mentionsList.append( { "word":y["mention"], "label":"Symptom", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            SymptomCount = SymptomCount + 1
        elif(y["semantic_type"] == "Anatomical Structure" and y["start_index"] >= 0 and AnatomyCount < 10000):
            mentionsList.append( { "word":y["mention"], "label":"Anatomie", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            AnatomyCount = AnatomyCount + 1
        elif(y["semantic_type"] == "Diagnostic Procedure" and y["start_index"] >= 0 and ProcedureCount < 10000):
        #should be Vordiagnose?
            mentionsList.append( { "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            ProcedureCount = ProcedureCount + 1
        elif(y["semantic_type"] == "Laboratory Procedure"  and y["start_index"] >= 0 and ProcedureCount < 10000):
            mentionsList.append( { "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            ProcedureCount = ProcedureCount + 1
        elif(y["semantic_type"] == "Therapeutic or Preventive Procedure" and y["start_index"] >= 0 and ProcedureCount < 10000):
            mentionsList.append( {  "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            ProcedureCount = ProcedureCount + 1
        elif(y["semantic_type"] == "Injury or Poisoning"    and y["start_index"] >= 0 and Unfallcount < 10000):
            mentionsList.append( {  "word":y["mention"], "label":"Unfall", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            Unfallcount = Unfallcount + 1
        elif(y["semantic_type"] == "Body Part, Organ, or Organ Component" and y["start_index"] >= 0 and AnatomyCount < 10000):
            mentionsList.append( {  "word":y["mention"], "label":"Anatomie", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
            AnatomyCount = AnatomyCount + 1
    if (usefulFlag):
        nerList.append({"id":i , "text":x["text"], "entities":mentionsList})
    
    
print(len(nerList))

# for ent in nerList[33]["entities"]:
#    for entit in ent:
#         print(entit)
# for ent in nerList[222]["entities"]:
#    for entit in ent:
#         print(entit)
# for ent in nerList[134]["entities"]:
#     for entit in ent:
#         print(entit)
counter = 0
with open('/code//Daten/SilverStandardDaten/V4CountedPartialData.jsonl', 'w', encoding='utf-8') as file:
            for obj in nerList:
                # Dump the JSON object as a JSON string and write to file
                file.write(json.dumps(obj) + '\n')
                counter = counter + 1
                # if (counter == 1000000):
                #     break


# with open('/code//Daten/SilverStandardDaten/data2.json', 'w', encoding='utf-8') as f:
#     for each in nerList:
#         json.dump(each, f, ensure_ascii=False, indent=4)

