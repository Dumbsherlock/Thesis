import pandas as pd
import json

ListOfJsons = []

for i in range(1407):
    data = pd.read_json(f'/code//Daten/LLMEval/API/SecondTry/eval{i}.jsonl', lines=True)
    response = data.iloc[0]["response"]
    truth = json.dumps(data.iloc[0]["groundTruth"]).replace("\'","\"")
    text = data.iloc[0]["text"].replace("\n","\\n").replace("\"","\'")
    print(i)
    

    word = "["
    end = "]"

    index = response.find(word)
    index2 = response.find(end)
    response = response[index:index2+len(end)].replace("\'","\"").replace("\n","")
    textWithBothLabels =f"{{\"collection\": {response},\"text\": \"{text}\" , \"truth\": {truth}}}"
    #ListOfJsons.append(textWithBothLabels)
 

    with open(f'/code//Daten/LLMEval/API/SecondTry/Processed/evalProcessed{i}.jsonl', 'w', encoding='utf-8') as file:
        file.write(textWithBothLabels + '\n')

               # file.write(json.dumps({"id":j,"response": Ollamaresponse, "groundTruth": data.iloc[j]["entities"], "text":text}) + '\n')
              
#data2 = pd.read_json(f'/code//Daten/LLMEval/evalList.jsonl', lines=True)
#print(   data2.iloc[0]["collection"][0]["label"])