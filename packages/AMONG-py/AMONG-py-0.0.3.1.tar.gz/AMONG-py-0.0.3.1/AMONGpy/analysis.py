import csv, json, itertools

def get_recommended_project(exam_logs_json) :
    '''
    Student json
    {
    "name" : "이름",
    "id" : "아이디",
    "test" : [
    {"answer" : [5, 4]},
    {"answer" : [2, 4]}
    ]
    }

    Test json
    [
    {"name" : "시험 이름",
    "number" : 10,
    "problems" : [
    {
    "tags" : ["tag1", "tag2"],
    "correctanswer" : 3
    },
    {
    "tags" : ["tag1", "tag2"],
    "correctanswer" : 2
    }]},
    {"name" : "시험 이름",
    "number" : 15,
    "problems" : [
    {
    "tags" : ["tag1", "tag2"],
    "correctanswer" : 2
    }
    ]}]
    :param student_json:
    :param test_json:
    :return:
    {
    "name":"프로젝트 이름",
    "tool":"사용교구(예. 아두이노, 앱인벤터, ...)"
    "difficuly":0~20
    }
    '''

    f = open('AMONGpy/projectKeyword.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)

    project_list = []
    for idx, line in enumerate(rdr):
        if idx >= 1:
            project_list.append({"분류":line[0], "프로젝트명":line[1], "난이도":line[2], "키워드":line[3]})

    print(project_list)

    exam_logs_json = json.loads(exam_logs_json)

    scores = [len([a for a, q in zip(e['answers'], e['exam']['questions']) if a['id'] == q['response']['answer']['id']]) / len(e['exam']['questions']) * 20.0 for e in exam_logs_json['exam_logs']]
    print(scores)

    all_tag = [q['tags'] for e in exam_logs_json['exam_logs'] for q in e['exam']['questions']]
    all_tag = list(itertools.chain(*all_tag))

    all_tag = [x['name'] for x in all_tag]
    all_tag = list(set(all_tag))
    all_tag = sorted(all_tag)

    accs = [[q for a, q in zip(e['answers'], e['exam']['questions']) if a['id'] == q['response']['answer']['id']]
            for e in exam_logs_json['exam_logs']]

    for acc in accs :
        for p in acc :
            tag_list = []
            for t in p['tags'] :
                tag_list.append(t['name'])

            p['tags'] = tag_list

    tag_cor = []
    for t in all_tag:
        acc_scores = [sum([1.0 / len(p['tags']) for p in acc if t in p['tags']]) for i, acc in enumerate(accs)]

        tag_cor.append((t, acc_scores))

    tag_cor = sorted(tag_cor, key=lambda x : x[1])

    print(tag_cor)

    project_list = sorted(project_list, key=lambda x : abs(int(x["난이도"]) - scores[-1]))
    print(project_list)


    distlist = []
    for i, p in enumerate(project_list) :
        for j, t in enumerate(tag_cor) :
            if p["키워드"] == t[0] :
                distlist.append((p, i + j * 1.5))

    distlist = sorted(distlist, key=lambda x : x[1])
    print(distlist)

    if len(distlist) == 0 :
        print('There was any matched tag with the test and recommandable projects')
        return None

    most_recommended_project = distlist[0][0]
    return json.dumps({"name":most_recommended_project["프로젝트명"], "tool":most_recommended_project["분류"], "difficulty":most_recommended_project["난이도"]})


if __name__ == "__main__" :
    p = get_recommended_project('{'
    '"id": 7,'
    '"exam_logs": ['
        '{'
            '"id": 5,'
            '"answers": ['
                '{'
                    '"id": 3,'
                    '"text": "우진이가 잘했다"'
                '},'
                '{'
                    '"id": 6,'
                    '"text": "승의가 잘못했다"'
                '}'
            '],'
            '"exam": {'
                '"id": 4,'
                '"questions": ['
                    '{'
                        '"id": 5,'
                        '"response": {'
                            '"id": 5,'
                            '"choices": ['
                                '{'
                                    '"id": 2,'
                                    '"text": "상준이가 잘했다"'
                                '},'
                                '{'
                                    '"id": 3,'
                                    '"text": "우진이가 잘했다"'
                                '},'
                                '{'
                                    '"id": 4,'
                                    '"text": "고러엄"'
                                '},'
                                '{'
                                    '"id": 5,'
                                    '"text": "안녕"'
                                '}'
                            '],'
                            '"answer": {'
                                '"id": 3,'
                                '"text": "우진이가 잘했다"'
                            '},'
                            '"polymorphic_ctype": 16,'
                            '"resourcetype": "UniqueAnswerResponse"'
                        '},'
                        '"context_block": {'
                            '"id": 1,'
                            '"blocks": []'
                        '},'
                        '"tags": ['
                            '{'
                                '"id": 2,'
                                '"name": "아두이노"'
                            '},'
                            '{'
                                '"id": 3,'
                                '"name": "자료수집"'
                            '}'
                        '],'
                        '"name": "1번문제"'
                    '},'
                    '{'
                        '"id": 6,'
                        '"response": {'
                            '"id": 6,'
                            '"choices": ['
                                '{'
                                    '"id": 6,'
                                    '"text": "승의가 잘못했다"'
                                '},'
                                '{'
                                    '"id": 7,'
                                    '"text": "승의가 잘했다"'
                                '}'
                            '],'
                            '"answer": {'
                                '"id": 7,'
                                '"text": "승의가 잘했다"'
                            '},'
                            '"polymorphic_ctype": 16,'
                            '"resourcetype": "UniqueAnswerResponse"'
                        '},'
                        '"context_block": {'
                            '"id": 2,'
                            '"blocks": ['
                                '{'
                                    '"id": 7,'
                                    '"text": "과연 상준이가 잘했을까? 우진이가 잘했을까?",'
                                    '"polymorphic_ctype": 15,'
                                    '"resourcetype": "TextBlock"'
                                '},'
                                '{'
                                    '"id": 8,'
                                    '"text": "과연 누가 잘했을까? 보기에서 잘 골라보자",'
                                    '"polymorphic_ctype": 15,'
                                    '"resourcetype": "TextBlock"'
                                '}'
                            ']'
                        '},'
                        '"tags": ['
                            '{'
                                '"id": 2,'
                                '"name": "아두이노"'
                            '}'
                        '],'
                        '"name": "두번째 문제"'
                    '}'
                '],'
                '"name": "첫번째 시험"'
            '}'
        '}'
    '],'
    '"name": "홍승의"'
'}')

    print(p)