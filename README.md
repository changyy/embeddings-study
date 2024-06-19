# embeddings-study

Embeddings with OpenAI API

# Steup

```
% python3 -m venv venv
% source venv/bin/activate
(venv) % python3 -V
Python 3.12.2
(venv) % sw_vers 
ProductName:		macOS
ProductVersion:		14.5
BuildVersion:		23F79
(venv) % pip install pandas faiss-cpu numpy openai
```

```
% python3 -m venv venv
% source venv/bin/activate
(venv) % python3 -V
Python 3.12.2
(venv) % sw_vers 
ProductName:		macOS
ProductVersion:		14.5
BuildVersion:		23F79
(venv) % pip install -r requirements.txt 
```

# Input Data

```
% cat .env 
OPENAI_API_KEY=sk-proj-XXXXXXXXXXXXXXXXXXXXXX

% tree data 
data
├── all_with_embeddings.csv
└── raw.csv

1 directory, 2 files

% head -n 1 data/raw.csv 
ID,Product,Question,Answer

% head -n 2 data/all_with_embeddings.csv 
ID,Product,Question,Answer,embedding
1,MyProduct,如何安裝?,1. 配件中...,"[0.02327146753668785, -0.020045360550284386, -0.05237892270088196, ..., -0.001935890642926097]"
```

# Usage

```
% bash script_query.sh 
usage: query.py [-h] query
query.py: error: the following arguments are required: query
```

```
% bash script_query.sh 我不會用
    ID  ...                                          embedding
12  13  ...  [0.019805965945124626, -0.016489805653691292, ...
95  96  ...  [-0.0029852555599063635, -0.00715451268479228,...
60  61  ...  [0.04740266129374504, -0.00805624108761549, -0...
74  75  ...  [0.02464713156223297, -0.011430890299379826, 0...
63  64  ...  [0.02185901068150997, -0.00896691344678402, 0....

[5 rows x 5 columns]
```
