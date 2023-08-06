import itertools, json, random

def result_chart_js(exam_logs_json, color_json = None) :
    '''
    

    color_json = {
    "tag1" : "#2e5355"
    "tag2" : "#c348f1"
    }
    :param student_json:
    :param test_json:
    :param color_json:
    :return: chart.js json
    '''
    exam_logs_json = json.loads(exam_logs_json)

    all_tag = [q['tags'] for e in exam_logs_json['exam_logs'] for q in e['exam']['questions']]
    all_tag = list(itertools.chain(*all_tag))

    all_tag = [x['name'] for x in all_tag]
    all_tag = list(set(all_tag))
    all_tag = sorted(all_tag)

    prob_nums = [len(e['answers']) for e in exam_logs_json['exam_logs']]

    #accs = [[cor for ans, cor in zip(t_ans['answer'], test['problems']) if ans == cor['correctanswer']] for t_ans, test in zip(student_json['test'], test_json)]

    accs = [[cor for i, cor in enumerate(e['exam']['questions']) if e['answers'][i]['id'] == cor['response']['answer']['id']] for e in exam_logs_json['exam_logs']]
    for acc in accs :
        for p in acc :
            tag_list = []
            for t in p['tags'] :
                tag_list.append(t['name'])

            p['tags'] = tag_list


    print(accs)

    tag_cor = {}
    for t in all_tag :
        acc_scores = [sum([1 / len(p['tags']) for p in acc if t in p['tags']]) * 100.0 / prob_nums[i] for i, acc in enumerate(accs)]

        tag_cor[t] = acc_scores

    print(tag_cor)

    chart_dic = {}
    chart_dic['type'] = "bar"

    data_dic = {}
    data_dic['labels'] = [t['exam']['name'] for t in exam_logs_json['exam_logs']]
    if color_json == None :
        data_dic['datasets'] = [{'label':t, 'data':s, 'backgroundColor':'#'+hex(random.randrange(16777215))[2:]} for t, s in tag_cor.items()]
    else :
        data_dic['datasets'] = [{'label':t, 'data':s, 'backgroundColor':color_json[t]} for t, s in tag_cor.items()]

    chart_dic['data'] = data_dic

    option_dic= {}
    option_dic['scales'] = {'xAxes':[{'stacked':'true'}], 'yAxes':[{'stacked':'true'}]}
    chart_dic['options'] = option_dic

    chart_json = json.dumps(chart_dic)

    return chart_json



if __name__ == "__main__" :
    c_json = result_chart_js('{'
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
                                '"name": "컴퓨팅사고능력"'
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

    print(c_json)