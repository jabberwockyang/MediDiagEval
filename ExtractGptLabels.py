import json

with open('Data/PMC-patients/PMC-Patients-Sample-gpt4-240218.jsonl', 'r') as f:
    lines = f.readlines()
    jsons = [json.loads(line) for line in lines]
newlist = []
for obj in jsons:
    try:
        text = obj['gpt_gene'].replace('```json', '').replace('```', '')
        parsed_dicts = json.loads(text)
        obj['standardDiagnosis'] = parsed_dicts['standardDiagnosis']
        obj['originalText']= parsed_dicts['originalText']
        newlist.append(obj)
    except:
        pass

with open('Data/PMC-patients/PMC-Patients-Sample-gpt4-240218-e.jsonl', 'w') as f:
    for obj in newlist:
        f.write(json.dumps(obj) + '\n')