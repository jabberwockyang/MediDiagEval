import BioGptEmbedding
import pandas as pd
from tqdm import tqdm
import os


if os.path.exists('Data/ICD10/icd10cm_codes_2022_embedded.csv'):
    embedded_df = pd.read_csv('Data/ICD10/icd10cm_codes_2022_embedded.csv')
    start = embedded_df.shape[0]
else:
    start = 0

# chunk the dataframe into 10 rows each
df = pd.read_csv('Data/ICD10/icd10cm_codes_2022.csv', dtype=str)
chunksize = 500
chunks = [df.iloc[i:i+chunksize] for  i in range(start, df.shape[0], chunksize)]

for i, chunk in enumerate(tqdm(chunks)):
    embeddings = BioGptEmbedding.generate_embeddings(chunk['name'].tolist(),batch_size=200)
    
    embeddings_df = pd.DataFrame(embeddings)
    embeddings_df.columns = [f'V{i+1}' for i in range(embeddings_df.shape[1])]
    result_df = pd.concat([chunk.reset_index(drop=True), embeddings_df], axis=1)

    with open('Data/ICD10/icd10cm_codes_2022_embedded.csv', 'a') as f:
        result_df.to_csv(f, header=f.tell()==0, index=False)