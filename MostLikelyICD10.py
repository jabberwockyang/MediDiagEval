import BioGptEmbedding
import pandas as pd
import numpy as np
import json

# 加载ICD-10标准编码嵌入
def load_standard_embeddings(embeddingFile):
    # 假设CSV的前两列分别为代码和名称，后面是嵌入
    df = pd.read_csv(embeddingFile)
    codes = df.iloc[:, 0].values  # ICD-10代码
    name = df.iloc[:, 1].values  # ICD-10名称
    embeddings = df.iloc[:, 2:].values  # 嵌入向量
    return codes, name, embeddings

# 计算余弦相似度
def calculate_cosine_similarity_batch(embeddings1, embeddings2):
    '''
    # 
    input:
    - embeddings1: M × 1024 matrix（M non-standard diagnoses, 1024 embedding size）
    - embeddings2: N × 1024 matrix（N standard codes, 1024 embedding size）
    output:
    - similarity_matrix: M × N matrix（M non-standard diagnoses, N standard codes）
    '''
    embeddings1_normalized = embeddings1 / np.linalg.norm(embeddings1, axis=1, keepdims=True)
    embeddings2_normalized = embeddings2 / np.linalg.norm(embeddings2, axis=1, keepdims=True)
    similarity_matrix = np.dot(embeddings1_normalized, embeddings2_normalized.T)
    return similarity_matrix

# 找到最接近的ICD-10代码
def find_closest_code_forBatch(non_standard_embeddings, standard_embeddings):
    '''
    input:
    - non_standard_embeddings: M × 1024 matrix（M non-standard diagnoses, 1024 embedding size）
    - standard_embeddings: N × 1024 matrix（N standard codes, 1024 embedding size）
    output:
    - closest_indices: M × 1 array（M non-standard diagnoses, index of the closest standard code）
    
    '''
    similarity_matrix = calculate_cosine_similarity_batch(non_standard_embeddings, standard_embeddings)
    closest_indices = np.argmax(similarity_matrix, axis=1)
    return closest_indices

def GetEmbedFindClosest(non_standard_diagnoses, embeddingFile):

    # 生成非标准诊断的嵌入 
    # non_standard_embeddings M × 1024 matrix（M non-standard diagnoses, 1024 embedding size）
    non_standard_embeddings = BioGptEmbedding.generate_embeddings(non_standard_diagnoses, batch_size=200)

    # 加载ICD-10标准编码嵌入
    # standard_embeddings  N × 1024 matrix（N standard codes, 1024 embedding size）
    standard_codes, standard_name, standard_embeddings = load_standard_embeddings(embeddingFile)

    # matrix calculation
    closest_indices = find_closest_code_forBatch(non_standard_embeddings, standard_embeddings)
    closest_icd_codes = standard_codes[closest_indices]
    closest_icd_names = standard_name[closest_indices]
    return closest_icd_codes, closest_icd_names

if __name__ == '__main__':
    # 从JSONL文件中加载非标准诊断
    with open('Data/PMC-patients/PMC-Patients-Sample-gpt4-240218-e.jsonl', 'r') as f:
        lines = f.readlines()
        jsons = [json.loads(line) for line in lines]
    
    non_standard_diagnoses = [obj['standardDiagnosis'] for obj in jsons]
    embeddingFile = 'Data/ICD10/icd10cm_codes_2022_embedded.csv'

    closest_icd_codes, closest_icd_names = GetEmbedFindClosest(non_standard_diagnoses, embeddingFile)

    # 将结果写入JSONL文件
    for i, obj in enumerate(jsons):
        obj['closestIcdCode'] = closest_icd_codes[i]
        obj['closestIcdName'] = closest_icd_names[i]
        print(obj['standardDiagnosis'], '->', closest_icd_codes[i], closest_icd_names[i])

    with open('Data/PMC-patients/PMC-Patients-Sample-gpt4-240218-e-l.jsonl', 'w') as f:
        for obj in jsons:
            f.write(json.dumps(obj) + '\n')