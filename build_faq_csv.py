import pandas as pd

questions = pd.read_csv('data/q.csv')
answers = pd.read_csv('data/a.csv')
selectField = 'ZHTW'
outputPath = 'data/raw.csv'

combinedData = []
for index, row in questions.iterrows():
    if '_' not in row.iloc[0]:
        continue
    questionID = row.iloc[0].split('_')[1]
    questionData = row[selectField]

    answerRow = answers.loc[answers.iloc[:, 0].str.split('_').str[1] == questionID]
    if not answerRow.empty:
        answerData = answerRow[selectField].values[0]
        
        combinedData.append({
            'ID': questionID,
            'Product': row.iloc[1],
            'Question': questionData,
            'Answer': answerData
        })

combinedDataframe = pd.DataFrame(combinedData)
combinedDataframe.to_csv(outputPath, index=False, header=['ID', 'Product', 'Question', 'Answer'])
print(combinedDataframe)
