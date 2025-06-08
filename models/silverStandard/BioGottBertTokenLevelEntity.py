
from transformers import PreTrainedTokenizerFast
import pandas as pd
import re


path = "/code//Daten/doccano_annotations/cedis/second/cedis_151.jsonl"
fast_tokenizer = PreTrainedTokenizerFast(tokenizer_file="/code//Code/scripts/tmp/test-ner/SCAI-BIO/bio-gottbert-base/tokenizer.json")

data = pd.read_json(path_or_buf=path, lines=True)
realtokens = []
cleanedTokens = []
nerTags = []

for i in range(data.shape[0]):
    text = data.iloc[i]["text"]
    tokens = fast_tokenizer.tokenize(text)
    realtokens.append(tokens)
    tempTokenList = []
    for ent in tokens:
        ent = ent.replace("ÃŁ", "ß")
        ent = ent.replace("Ã¶", "ö")
        ent = ent.replace("Ã¼", "ü")
        ent = ent.replace("Ã¤", "ä")
        ent = ent.replace("ÃŸ", "ß")
        ent = ent.replace("Ãĸ", "Ö")
        ent = ent.replace("Ãľ", "Ü")
        ent = ent.replace("ÃĦ", "Ä")
        ent = ent.replace("Â°", "°")
        ent = ent.replace("Ã©", "e")
        ent = ent.replace("Â½", "½")
        ent = ent.replace("âĤ¬", "€")
        tempTokenList.append(ent)
    cleanedTokens.append(tempTokenList)

def verifyTokenIndex (index, indexList):
        for ent in data.iloc[indexList]["entities"]:
            if(ent["start_offset"] == index):
                return "B-" + ent["label"]
            elif ((index < ent["end_offset"]) and (index > ent["start_offset"])):
                return "I-" + ent["label"]
        return "O"
def returnVerifiedEntity (index, indexList):
        for ent in data.iloc[indexList]["entities"]:
            if ((index < ent["end_offset"]) and (index >= ent["start_offset"])):
                return ent

B_pattern = "B-"
I_pattern = "I-"            

for i in range(1):
    entities = data.iloc[i]["entities"]
    tokens = cleanedTokens[i]
    tagList = []
    pos = 0
    
    for token in tokens:
        print(pos)
        tag = verifyTokenIndex(pos, i)
        entity = returnVerifiedEntity(pos, i)
        if(re.match(B_pattern ,tag) != None):
           tagList.append({"token": token ,"start": entity["start_offset"], "end": pos + len(token)-1, "label": tag})
           pos = pos + len(token) -1
        elif(re.match(I_pattern, tag) != None):
            tagList.append({"token": token ,"start": pos, "end": pos + len(token), "label": tag})
            pos = pos + len(token)
        else:
            pos = pos + len(token)
        #tagList.append(tag) #hier muss noch die Position des Tokens im Text übergeben werden enstprechend dem Format der Model Ausgabe
    nerTags.append(tagList)

for each in nerTags:
    for i in each:
        print(i)
for each in data.iloc[0]["entities"]:
    print(each) 
convertedToIOB = {"tokens": realtokens, "ner_tags": nerTags}