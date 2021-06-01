import pandas as pd   
import plotly.graph_objects as go 

file_data = pd.read_csv('data/data.csv')
studentId = 'TRL-xyz'

def analysis(i):
    print(i)
    return i
students = []
value = fileData['student_id']
for std in value:
    if not std in students:
        students.append(std)
print(students)

for student in students:
    dataForStudent = fileData.loc[fileData['student_id'] == student]
    data = dataForStudent.groupby("level")["attempt"].mean()
    Levels = ['Level 1', 'Level 2', 'Level 3', 'Level 4']
    title = f'Progress Report for student id {student} .'
    graph = go.Figure(go.Bar(x=data, y=Levels, orientation='h',))
    graph.update_layout(title=title,)
    graph.show()