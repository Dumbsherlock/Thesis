import pandas as pd
import json

#data = pd.read_json(path_or_buf="/code//Daten/SynData/API_generated_data/testrun.jsonl", lines=True)

def process_jsonl_file():
    for i in range(500):
        j = i 
        input_file_path = f'/code//Daten/SynData_EvalAluminum/API_generated_data/training_data_with_Occ/testrun{j}.jsonl'
        output_file_path = f'/code//Daten/SynData_EvalAluminum/API_generated_data/training_data_with_Occ/processed/testrun{j}_edited.jsonl'
        

        # Open the input file for reading and the output file for writing
        with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
            # Iterate over each line in the input file
            for line in infile:
                # Remove the first and last character of the line
                modified_line = line[1:-1].replace('\\"','"').replace("}]}\"","}]}")
                # Write the modified line to the output file
                outfile.write(modified_line + '\n')

        print("Processing complete. Modified JSONL file has been saved.")

            

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

def generate_entity_annotation(text, word, label ):
    annotated_words = []
    boundaries = find_substring_boundaries(text, word)
    if len(boundaries) > 0:
        for each in boundaries:
            annotated_words.append({"word": word, "start_offset": each[0], "end_offset": each[1], "label": label}) 
    else:
         annotated_words.append({"word": word, "start_offset": 0, "end_offset": 0, "label": label}) 
    return annotated_words

def annotate_data():
    data = pd.read_json(path_or_buf="/code//Daten/SynData/API_generated_data/testrun_edited.jsonl", lines=True)
    convertedAnnotations = []

    for i in range(data.shape[0]):
        annotated_entities = []
        text = data.iloc[i]["text"]
        labels = data.iloc[i]["entities"]
        for each in labels:
            annotated_entities.extend(generate_entity_annotation(text, each["word"], each["label"])) 
        convertedAnnotations.append({"id": i, "text": text, "entities": annotated_entities})
        
        
    with open(f'/code//Daten/SynData/API_generated_data/testrun_edited_annotated.jsonl', 'w', encoding='utf-8') as file:
        for each in convertedAnnotations:
            file.write(json.dumps(each) + '\n')

def annotate_split_data():
    convertedAnnotations = []
    for i in range(200):
        j = i + 0    
        try:
            data = pd.read_json(path_or_buf=f"/code//Daten/SynData_EvalAluminum/API_generated_data/training_data_with_Occ/processed/testrun{j}_edited.jsonl", lines=True)
        except:
            print(f"File{j} not found.")
            continue
        annotated_entities = []
        text = data.iloc[0]["text"]
        labels = data.iloc[0]["entities"]
        for each in labels:
            annotated_entities.extend(generate_entity_annotation(text, each["word"], each["label"])) 
        convertedAnnotations.append({"id": j, "text": text, "entities": annotated_entities})
        
    with open(f'/code//Daten/SynData_EvalAluminum/API_generated_data/testrun_edited_training_data_with_Occ_annotated_100samples.jsonl', 'w', encoding='utf-8') as file:
        for each in convertedAnnotations:
            file.write(json.dumps(each) + '\n')

if __name__ == "__main__":
    #process_jsonl_file()
    annotate_split_data()
    
    
    
    
    
    
    
    
    