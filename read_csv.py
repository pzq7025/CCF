import pandas as pd
# import jiagu
import re


def read_file():
    with open(r'C:\Users\14276\Desktop\ccf\Train_Data.csv', encoding='utf-8-sig') as f:
        file_content = pd.read_csv(f)
    ids = file_content[:20]['id']
    text = file_content[:20]['text']
    title = file_content[:20]['title']
    unknown_entities = file_content[:20]['unknownEntities']

    content = []
    for i in range(len(ids)):
        content.append([ids[i], title[i], unknown_entities[i], text[i]])
    return content


def wash_data():
    """
    'id'  'title' 'unknownEntities' 'text'
    :return:
    """
    content = read_file()
    replace_character = ['?', '#', '【', '】', '&nbsp', '▽', '\u3000\u3000', '@']
    for i in content:
        for re_c in replace_character:
            i[3] = i[3].replace(re_c, '')  # i[3]是text
        for x in range(7):
            i[3] = i[3].replace('{IMG:' + str(x) + '}', '')

    for i in content:
        print(i[3])
        result = re.compile(r'[http|https]+://.*\b[\w]+', re.S).findall(i[3])
        print(result)

        # convert = list(enumerate(jiagu.ner(i[3])))
        # entity_x = [[x[0], i[3][x[0]]] for x in convert if x[1] != 'O']
        # print(entity_x)
        # print(chunk)


wash_data()
