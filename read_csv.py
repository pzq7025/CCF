import pandas as pd
import jiagu


def read_file():
    with open(r'C:\Users\14276\Desktop\ccf\Train_Data.csv', encoding='utf-8-sig') as f:
        file_content = pd.read_csv(f)
    ids = file_content[:10]['id']
    text = file_content[:10]['text']
    title = file_content[:10]['title']
    unknown_entities = file_content[:10]['unknownEntities']

    content = []
    for i in range(len(ids)):
        content.append([ids[i], title[i], unknown_entities[i], text[i]])
    return content


def wash_data():
    content = read_file()
    for i in content:
        i[3] = i[3].replace('?', '').replace('#', '').replace('【', '').replace('】', '').replace('&nbsp', '')
        for x in range(7):
            i[3] = i[3].replace('{IMG:' + str(x) + '}', '')
    for i in content:
        chunk = jiagu.cut(i[3])
        print(chunk)


wash_data()
