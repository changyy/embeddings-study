import os
import sys
import pandas as pd

from openai_helper import get_embedding

inputCSVPath = 'data/raw.csv'
if not os.path.exists(inputCSVPath):
    print(f'找不到 {inputCSVPath}，請先準備好 {inputCSVPath}，其欄位為 `ID,Product,Question,Answer`')
    sys.exit(1)

outputCSVPath = 'data/all_with_embeddings.csv'
combinedDataFrame = pd.read_csv(inputCSVPath)

embeddings = []
for question in combinedDataFrame['Question']:
    embedding = get_embedding(question)
    embeddings.append(embedding)
    #print(embedding)
    #break

combinedDataFrame['embedding'] = embeddings

combinedDataFrame.to_csv(outputCSVPath, index=False)
