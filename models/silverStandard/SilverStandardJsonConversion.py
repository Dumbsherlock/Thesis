import json
import pandas as pd  
path = "/code/SilverStandard/BEL-silver-standard/BEL-silver-standard/WikiMed-DE/val_data.json"

data = pd.read_json(path_or_buf=path )
nerList = []


for i in range (data.shape[0]):
    x = data.iloc[i]
    mentionsList = []
    usefulFlag = False
    for y in x["mentions"]:
        if(y["semantic_type"] == "Disease or Syndrome" and y["start_index"] >= 0):
             mentionsList.append( {  "word":y["mention"], "label":"Vorerkrankung", "start_offset":y["start_index"], "end_offset":y["end_index"]})
             usefulFlag = True
        elif(y["semantic_type"] == "Clinical Drug" and y["start_index"] >= 0):
             mentionsList.append( {  "word":y["mention"], "label":"Medikament", "start_offset":y["start_index"], "end_offset":y["end_index"]})
             usefulFlag = True
        elif(y["semantic_type"] == "Sign or Symptom" and y["start_index"] >= 0): 
            mentionsList.append( { "word":y["mention"], "label":"Symptom", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Anatomical Structure" and y["start_index"] >= 0):
            mentionsList.append( { "word":y["mention"], "label":"Anatomie", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Diagnostic Procedure" and y["start_index"] >= 0):
        #should be Vordiagnose?
            mentionsList.append( { "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Laboratory Procedure"  and y["start_index"] >= 0):
            mentionsList.append( { "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Therapeutic or Preventive Procedure" and y["start_index"] >= 0):
            mentionsList.append( {  "word":y["mention"], "label":"Prozedur", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Injury or Poisoning"    and y["start_index"] >= 0):
            mentionsList.append( {  "word":y["mention"], "label":"Unfall", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Body Part, Organ, or Organ Component" and y["start_index"] >= 0):
            mentionsList.append( {  "word":y["mention"], "label":"Anatomie", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        elif(y["semantic_type"] == "Anatomical Structure" and y["start_index"] >= 0):
            mentionsList.append( {  "word":y["mention"], "label":"Anatomie", "start_offset":y["start_index"], "end_offset":y["end_index"]})
            usefulFlag = True
        
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
with open('/code//Daten/SilverStandardDaten/PartialData.jsonl', 'w', encoding='utf-8') as file:
            for obj in nerList:
                # Dump the JSON object as a JSON string and write to file
                file.write(json.dumps(obj) + '\n')
                counter = counter + 1
                if (counter == 900):
                    break


# with open('/code//Daten/SilverStandardDaten/data2.json', 'w', encoding='utf-8') as f:
#     for each in nerList:
#         json.dump(each, f, ensure_ascii=False, indent=4)

