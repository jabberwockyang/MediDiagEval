from openai import OpenAI
import os
import json
import time
import random
from datetime import datetime

# GPT4
client1 = OpenAI(
  api_key=  "sk-BYG0Lsn3kbcFC6fu6f30Ce3dF9134963819320B17d719d64",
  base_url = "https://api.kwwai.top/v1"
)
# GPT3.5
client2 = OpenAI(
  api_key= "sk-GohLWOCbtuOf2I9o000dFf77F0C04a62A09f9358BbBdD986",
  base_url = "https://api.kwwai.top/v1"
)

def gptAnnotate(infile, outfile):
    
    if os.path.exists(outfile):
        with open(outfile,'r') as f2:
            done_data = f2.readlines()
            done_data = [json.loads(line) for line in done_data]
            done_request = [obj['patient_id'] for obj in done_data]
    else:
        done_request = []

    with open(infile, 'r') as f:
        json_list = json.load(f)
    
    leftJsonObj = [obj for obj in json_list if obj['patient_id'] not in done_request]
    random.shuffle(leftJsonObj)
    for obj in leftJsonObj:
        completion = client1.chat.completions.create(
        model='gpt-4-32k-0613',
        messages=[
            {"role": "user", "content": obj['prompt']}])
        obj['gpt_gene'] = completion.choices[0].message.content
        time.sleep(2)
        with open(outfile, 'a') as file:
            file.write(json.dumps(obj, ensure_ascii=False) + '\n')


now = datetime.now()
outfile = f'Data/PMC-patients/PMC-Patients-Sample-gpt4-{now.strftime("%Y%m%d-%H%M%S")}.jsonl'
infile = 'Data/PMC-patients/PMC-Patients-Sample2.json'
gptAnnotate(infile, outfile)


