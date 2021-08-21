import sys
import pandas
dfs = pandas.read_html('歷年成績.html')
df = df[0]
df = df[df.排名.isnull()]
df['pass'] = False
df['pass'][df.成績>59] = True
df['pass'][df.備註 == '抵免'] = True
df.to_csv('out_put_score.csv',encoding='utf-8-sig')

score_history = pd.read_csv('out_put_score.csv')
score_history = score_history.drop('Unnamed: 0',axis=1)

need_score = pd.read_csv('data/必修學分.csv',encoding = "big5")
need_score['pass'] = False
for history_index, history_row in score_history.iterrows():
    for need_index,need_row in need_score.iterrows():
        if (history_row.科目名稱 == need_row.科目 and history_row['pass'] == True):
            need_score['pass'][need_index] = True
print("未修過必修課程為:")
print(need_score[need_score['pass'] == False])

choose_imformation = pd.read_csv('data/imformation.csv')
choose_innovation = pd.read_csv('data/innovation.csv')
choose_other = pd.read_csv('data/other.csv')
choose_technology = pd.read_csv('data/technology.csv')
choose_imformation = choose_imformation.drop('Unnamed: 0',axis=1)
choose_innovation = choose_innovation.drop('Unnamed: 0',axis=1)
choose_other = choose_other.drop('Unnamed: 0',axis=1)
choose_technology = choose_technology.drop('Unnamed: 0',axis=1)
def check_if_learn(df):
    status = False
    for history_index, history_row in score_history.iterrows():
        for choose_index,choose_row in df.iterrows():
            if (history_row.科目名稱 == choose_row.科目 and history_row['pass'] == True):
                status = True
    return status
print("imformation:" + str(check_if_learn(choose_imformation)))
print("technology:" + str(check_if_learn(choose_technology)))
print("innovation:" + str(check_if_learn(choose_innovation)))

def caculate_total_score(arr):
    total = 0
    for df in arr:
        for history_index, history_row in score_history.iterrows():
            for choose_index,choose_row in df.iterrows():
                if (history_row.科目名稱 == choose_row.科目 and history_row['pass'] == True):
                    total += 3
    return total
arr = [choose_imformation,choose_innovation,choose_technology,choose_other]
print("選修尚缺學分:" + str(18 - caculate_total_score(arr)))