from nervaluate import Evaluator 
import pandas as pd

data = pd.read_json(path_or_buf="/code//Daten/LLMEval/Local/ThirdTry/AnnotatedEvalSamples/evalAnno.jsonl", lines=True)

predicitons = []
truths = []

for i in range(data.shape[0]):
    entitiesPred = []
    entitiesTruth = []
    for each in data.iloc[i]["entities"]:
        print(each["start_offset"])
        entitiesPred.append({"start":each["start_offset"], "end":each["end_offset"], "label": each["label"] })
    predicitons.append(entitiesPred)
    
    for each in data.iloc[i]["truth"]:
        entitiesTruth.append({"start":each["start_offset"], "end":each["end_offset"], "label": each["label"] })
    truths.append(entitiesTruth)

evaluator = Evaluator(predicitons, truths, tags=["Vorerkrankung", "Medikament","Prozedur","Vordiagnose","Symptom","Negation","Anatomie","Unfall"])

results, results_per_tag, result_indices, result_indices_by_tag = evaluator.evaluate()
for mode in results:
  print(mode)
  print(results[mode])
for tag in results_per_tag:
  print(tag)
  print(results_per_tag[tag])