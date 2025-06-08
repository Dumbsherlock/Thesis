import json
from gliner import GLiNER
from nervaluate import Evaluator
import pandas as pd  

true = []
evaltrue = []
pred = []
evalpred = []

LaptopPath = "/code//Daten/doccano_annotations/cedis/first/cedis_100.jsonl"
LaptopPathAlt = "/code//Daten/doccano_annotations/cedis/first/juan_40.jsonl"
LaptopPathAlt2 = "/code//Daten/doccano_annotations/cedis/second/cedis_151.jsonl"

DesktopPath = "D:/Uni/BA/Doccano/doccano_annotations/cedis/second/cedis_151.jsonl"
  
data = pd.read_json(path_or_buf=DesktopPath, lines=True)
    
model = GLiNER.from_pretrained("knowledgator/gliner-multitask-large-v0.5")


labels = ["Vorerkrankung", "Medikament","Prozedur","Vordiagnose","Symptom","Negation","Anatomie","Unfall"]
allsamples = len(data)
partialSamples = 30

for i in range(data.shape[0]):
  text = data.iloc[i]["text"]
  print(i)

  groundTruths = []
  for entity in data.iloc[i]["entities"]:
    groundTruth = {"label": entity["label"],"start": entity["start_offset"], "end": entity["end_offset"]}
    groundTruths.append(groundTruth)
  textAndTrue = {"text": text, "entities": groundTruths}
  true.append(textAndTrue)
  evalpred.append(groundTruths)

  entities = model.predict_entities(text, labels, multi_label=True)
  predictions = []
  for entity in entities:
    prediction = {"label": entity["label"],"start": entity["start"], "end": entity["end"]}
    predictions.append(prediction)
  textAndPred = {"text": text, "entities": predictions}
  pred.append(textAndPred)
  evaltrue.append(predictions)
#liste von listen von Dictionaries

evaluator = Evaluator(evaltrue, evalpred, tags=["Vorerkrankung","Medikament","Prozedur","Vordiagnose","Symptom","Negation","Anatomie","Unfall"])

# Returns overall metrics and metrics for each tag

results, results_per_tag, result_indices, result_indices_by_tag = evaluator.evaluate()

# with open('/code//Daten/IOBGliNEREval/IOB_Pred_Data.jsonl', 'w', encoding='utf-8') as file:
#             for obj in pred:
#                 # Dump the JSON object as a JSON string and write to file
#                 file.write(json.dumps(obj) + '\n')
              


# with open('/code//Daten/IOBGliNEREval/IOB_True_Data.jsonl', 'w', encoding='utf-8') as file:
#             for obj in true:
#                 # Dump the JSON object as a JSON string and write to file
#                 file.write(json.dumps(obj) + '\n')
               
#for result in results_per_tag:
  #print(result + ":") 
 # print(results_per_tag[result]["partial"]) 
for mode in results:
  print(mode)
  print(results[mode])
for tag in results_per_tag:
  print(tag)
  print(results_per_tag[tag])