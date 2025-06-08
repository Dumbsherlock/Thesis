import pandas as pd
import json

def find_substring_boundaries(text, substring):
    # List to store boundaries
    text_lower = text.lower()
    substring_lower = substring.lower()
    
    boundaries = []
    
    # Find start positions of all occurrences
    start = text_lower.find(substring_lower)
    while start != -1:
        end = start + len(substring_lower)
        boundaries.append((start, end))
        # Continue searching from the next position
        start = text_lower.find(substring_lower, start + 1)
    
    return boundaries

def find_substring_boundary(text, substring):
    # List to store boundaries
    text_lower = text.lower()
    substring_lower = substring.lower()
    
    boundary = []
    
    # Find start positions of all occurrences
    start = text_lower.find(substring_lower)
    end = start + len(substring_lower)
    if(start == -1):
        return boundary 
    boundary.append((start, end)) 
    
    return boundary


data2 = pd.read_json(f'/code//Daten/LLMEval/Local/ThirdTry/evalList.jsonl', lines=True)
convertedAnnotations = []

for i in range(151):
    try:
        data = data2.iloc[i]
        text = data["text"]
        labels = data["collection"]
        truth = data["truth"]
        labelAnno = []
        for each in labels:
            occcurence = find_substring_boundaries(text , (each["word"]))
            if len(occcurence) > 0:
                for v in range( len(occcurence)):
                    labelAnno.append({  "text":each["word"], "start_offset": occcurence[v][0], "end_offset": occcurence[v][1], "label":each["label"]})
            else:
                labelAnno.append({  "text":each["word"], "start_offset": 0, "end_offset": 0, "label":each["label"]})
        convertedAnnotations.append({"id":i, "text":text, "entities":labelAnno, "truth":truth } )
        print(len(convertedAnnotations))
    except:
        print("Error in sample: ", i)
        continue

with open(f'/code//Daten/LLMEval/Local/ThirdTry/AnnotatedEvalSamples/evalAnno.jsonl', 'w', encoding='utf-8') as file:
    for each in convertedAnnotations:
       file.write(json.dumps({"id":each["id"],"text": each["text"], "entities": each["entities"], "truth":each["truth"]}) + '\n')