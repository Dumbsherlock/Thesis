from transformers import PreTrainedTokenizerFast
import pandas as pd


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
            
for i in range(data.shape[0]):
    entities = data.iloc[i]["entities"]
    tokens = cleanedTokens[i]
    tagList = []
    pos = 0
    for token in tokens:
        tag = verifyTokenIndex(pos, i)
        pos = pos + len(token)
        tagList.append(tag) #hier muss noch die Position des Tokens im Text übergeben werden enstprechend dem Format der Model Ausgabe
    nerTags.append(tagList)

convertedToIOB = {"tokens": realtokens, "ner_tags": nerTags}
       
print((convertedToIOB["tokens"][0]))
print((convertedToIOB["ner_tags"][0]))


        

    
 





