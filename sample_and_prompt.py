import json
import random

#jsonlist = json.loads(open('Data/PMC-patients/PMC-Patients.json').read())
jsonlist = json.loads(open('Data/PMC-patients/PMC-Patients-Sample.json').read())


# random.seed(666)
# SmapledJsonList = random.sample(jsonlist, 200)

SmapledJsonList = jsonlist
def GetPrompt(jsonObj):
    historyText = jsonObj['patient']
    sample_input = "omitted here"
    sample_output = json.dumps({"originalText":"blood cultures returned positive for Gram-positive bacilli, subsequently identified as B cereus","standardDiagnosis": "Bacillus cereus Bacteremia"})
    prompt = f"according to the history given bellow, please extract the diagnosis of the patient from the orginal text and give a standard diagnosis name. \n\nfor example: patient's history:'''{sample_input}''' \n\noutput: {sample_output} \n\n here is a patient's history:'''{historyText}''' \n\n output:"
    jsonObj['prompt'] = prompt
    return jsonObj

SmapledJsonList = [GetPrompt(jsonObj) for jsonObj in SmapledJsonList]
with open('Data/PMC-patients/PMC-Patients-Sample.json', 'w') as f:
    f.write(json.dumps(SmapledJsonList, indent=4, ensure_ascii=False))