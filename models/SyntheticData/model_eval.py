import pandas as pd
from nervaluate import Evaluator


data_path = "/code//Daten/doccano_annotations/cedis/second/cedis_151.jsonl"
model_path = "/code//Code/scripts/tmp/test-ner/Syndata/SCAI-BIO/bio-gottbert-base"
model_path2 = "/code//Code/scripts/tmp/test-ner/Syndata500samples/SCAI-BIO/bio-gottbert-base"
model_path3 = "/code//Code/scripts/tmp/test-ner/Syndata1000samples/SCAI-BIO/bio-gottbert-base"
model_path4 = "/code//Code/scripts/tmp/test-ner/Syndata_with_disease/SCAI-BIO/bio-gottbert-base"
data = pd.read_json(path_or_buf=data_path, lines=True)

#activate .venv to use this model

from transformers import pipeline
# classifier = pipeline("ner", model="/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base")
token_classifier = pipeline("token-classification", model=model_path3 , aggregation_strategy="simple", device=0)
true = []
evalpred = []
pred = []
evaltrue = []
        
for i in range(data.shape[0]):
  text = data.iloc[i]["text"]
  print(i) if (i % 30 == 1) else None

  groundTruths = []
  for entity in data.iloc[i]["entities"]:
    groundTruth = {"label": entity["label"],"start": entity["start_offset"], "end": entity["end_offset"]}
    groundTruths.append(groundTruth)
  textAndTrue = {"text": text, "entities": groundTruths}
  true.append(textAndTrue)
  evalpred.append(groundTruths)

  entities = token_classifier(text)
  predictions = []
  for entity in entities:
    prediction = {"label": entity["entity_group"],"start": entity["start"], "end": entity["end"]}
    predictions.append(prediction)
  textAndPred = {"text": text, "entities": predictions}
  pred.append(textAndPred)
  evaltrue.append(predictions)
#liste von listen von Dictionaries

evaluator = Evaluator(evaltrue, evalpred, tags=["Vorerkrankung","Medikament","Prozedur","Symptom","Anatomie","Unfall", "Negation", "Vordiagnose"])

results, results_per_tag, result_indices, result_indices_by_tag = evaluator.evaluate()

for mode in results:
  print(mode)
  print(results[mode])
for tag in results_per_tag:
  print(tag)
  print(results_per_tag[tag])

# for entity in result:
#     print(f"{entity['entity']} - {entity['score']} - {entity['index']} - {entity['word']}")


# for label in labels:
#     for ent in label:
#         print(ent)

# print("\n")
# for i in data.iloc[0]["entities"]:
#         print(i)



            

            

