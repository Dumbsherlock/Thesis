from nervaluate import Evaluator 
import pandas as pd

dataPred = pd.read_json(path_or_buf="/code//Daten/IOBGliNEREval/processed/pred/train.jsonl", lines=True)

dataTruth = pd.read_json(path_or_buf="/code//Daten/IOBGliNEREval/processed/true/train.jsonl", lines=True)

predicitons = []
truths = []

for i in range(dataPred.shape[0]):
    entities = dataPred.iloc[i]["ner_tags"]
    predicitons.append(entities)
    entities = dataTruth.iloc[i]["ner_tags"]
    truths.append(entities)

evaluator = Evaluator(predicitons, truths, tags=["Vorerkrankung", "Medikament","Prozedur","Vordiagnose","Symptom","Negation","Anatomie","Unfall"], loader="list")

results, results_per_tag, result_indices, result_indices_by_tag = evaluator.evaluate()
for mode in results:
  print(mode)
  print(results[mode])
for tag in results_per_tag:
  print(tag)
  print(results_per_tag[tag])
  