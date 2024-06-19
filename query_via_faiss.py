import os
import sys
import argparse
import pandas as pd
import faiss
import numpy as np

from openai_helper import get_embedding

parser = argparse.ArgumentParser(description='命令列參數解析範例')
parser.add_argument('query', type=str, help='需要查詢的內容')
args = parser.parse_args()

if not args.query.strip():
    parser.print_help()
    sys.exit(1)

inputCSVPath = 'data/all_with_embeddings.csv'
if not os.path.exists(inputCSVPath):
    print(f'找不到 {inputCSVPath}，請先執行 `bash script_generate_embeddings.sh`')
    sys.exit(1)

df = pd.read_csv(inputCSVPath)

# 假设你的 CSV 文件有两列：'id' 和 'embedding'
# 将嵌入向量转为 numpy 数组
embeddings = np.stack(df['embedding'].apply(eval).values)

# 创建 Faiss 索引
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# 查询向量
query = args.query.strip()
query_vector = np.array(get_embedding(query)).reshape(1, -1)

# 进行搜索
k = 5  # 返回最近的 5 个结果
distances, indices = index.search(query_vector, k)

# 获取搜索结果
results = df.iloc[indices[0]]

print(results)
