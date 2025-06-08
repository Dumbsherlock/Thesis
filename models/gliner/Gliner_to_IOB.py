import pandas as pd
import json


dataPred = pd.read_json(path_or_buf="/code//Daten/IOBGliNEREval/IOB_Pred_Data.jsonl", lines=True)

dataTrue = pd.read_json(path_or_buf="/code//Daten/IOBGliNEREval/IOB_True_Data.jsonl", lines=True)


with open('/code//Daten/IOBGliNEREval/IOB_Pred_Data_final.jsonl', 'w', encoding='utf-8') as file:
            for i in range(dataPred.shape[0]):
                # Dump the JSON object as a JSON string and write to file
                entityList = []
                for each in dataPred.iloc[i]["entities"]:
                    entityList.append({"label":each["label"], "start_offset":each["start"], "end_offset":each["end"]})
                file.write(json.dumps({"id":i,"text": dataPred.iloc[i]["text"], "entities": entityList}) + '\n')
              


with open('/code//Daten/IOBGliNEREval/IOB_True_Data_final.jsonl', 'w', encoding='utf-8') as file:
              for i in range(dataTrue.shape[0]):
                # Dump the JSON object as a JSON string and write to file
                entityList = []
                for each in dataTrue.iloc[i]["entities"]:
                    entityList.append({"label":each["label"], "start_offset":each["start"], "end_offset":each["end"]})
                file.write(json.dumps({"id":i, "text": dataTrue.iloc[i]["text"], "entities": entityList}) + '\n')