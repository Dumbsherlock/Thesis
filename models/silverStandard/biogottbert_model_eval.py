
from transformers import PreTrainedTokenizerFast
import pandas as pd
from nervaluate import Evaluator


path = "/code//Daten/doccano_annotations/cedis/second/cedis_151.jsonl"
fast_tokenizer = PreTrainedTokenizerFast(tokenizer_file="/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base/tokenizer.json")

data = pd.read_json(path_or_buf=path, lines=True)
# def tokenCleanUp(tokens):
#     cleanedTokens = []
#     for ent in tokens:
#         ent = ent.replace("ÃŁ", "ß")
#         ent = ent.replace("Ã¶", "ö")
#         ent = ent.replace("Ã¼", "ü")
#         ent = ent.replace("Ã¤", "ä")
#         ent = ent.replace("ÃŸ", "ß")
#         ent = ent.replace("Ãĸ", "Ö")
#         ent = ent.replace("Ãľ", "Ü")
#         ent = ent.replace("ÃĦ", "Ä")
#         ent = ent.replace("Â°", "°")
#         ent = ent.replace("Ã©", "e")
#         ent = ent.replace("Â½", "½")
#         ent = ent.replace("âĤ¬", "€")
#         cleanedTokens.append(ent)
#     return cleanedTokens

# all = []
# for i in range(data.shape[0]):
#     unit = data.iloc[i]
#     labels = []
#     for ent in unit["entities"]:
#         tokens = fast_tokenizer.tokenize(unit["text"][ent["start_offset"]:ent["end_offset"]])
#         cleanedTokens = tokenCleanUp(tokens)
#         entity = []
#         pos = ent["start_offset"]
#         for i in range(len(cleanedTokens)):
#             if(i == 0):
#                 entity.append({ "label": "B-" + ent["label"],"word":tokens[i], "start_offset":pos, "end_offset":pos + len(cleanedTokens[i])-1})
#                 pos = pos + len(cleanedTokens[i]) -1
#             else:
#                 entity.append({ "label": "I-" + ent["label"],"word":tokens[i], "start_offset":pos, "end_offset":pos + len(cleanedTokens[i])})
#                 pos = pos + len(cleanedTokens[i])

#         labels.append(entity)
#     all.append({ "text": unit["text"]  ,"entites":labels})

#activate .venv to use this model

model_path = "/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base"
model_path2 = "/code//Code/scripts/tmp/test-ner/Scia-Bio-Disease/SCAI-BIO/bio-gottbert-base"
model_path3 = "/code//Code/scripts/tmp/test-ner/Scia-Bio-CountedDataset/SCAI-BIO/bio-gottbert-base" 
model_path4 = "/code//Code/scripts/tmp/test-ner/Scia-Bio-V2CountedDataset/SCAI-BIO/bio-gottbert-base"
model_path5 = "/code//Code/scripts/tmp/test-ner/cedis/SCAI-BIO/bio-gottbert-base"
model_path6 = "/code//Code/scripts/tmp/test-ner/V3Counted1000samples/SCAI-BIO/bio-gottbert-base"

from transformers import pipeline
# classifier = pipeline("ner", model="/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base")
token_classifier = pipeline("token-classification", model=model_path5 , aggregation_strategy="simple", device=0)

# for i in range(data.shape[0]):
#     result = token_classifier(data.iloc[i]["text"])
#     print(i)
#     print("lenght: ")
#     print( len(result))
#     if(len(result) > 1):

#         print(result)
true = []
evalpred = []
pred = []
evaltrue = []
        
for i in range(30):
  text = data.iloc[i]["text"]
  print(i)

  groundTruths = []
  for entity in data.iloc[i]["entities"]:
    groundTruth = {"label": entity["label"],"start": entity["start_offset"], "end": entity["end_offset"]}
    groundTruths.append(groundTruth)
  textAndTrue = {"text": text, "entities": groundTruths}
  true.append(textAndTrue)
  evalpred.append(groundTruths)

  entities = token_classifier(text)
  print(entities)
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



            

            

