import pandas as pd
class gameCreate:
    def __init__(self, csv_file):
        self.csv = csv_file
        self.csv = csv_file
        df = pd.read_csv(self.csv)
        headers = df.iloc[0]
        self.df = pd.DataFrame(df.values[1:], columns = headers)
        total_question_ct = ["q1", "q2", "q3", "q4"]
        global x
        all_questions = []
        for x in total_question_ct:
            for i in range(10):
                x = df.iloc[i,0]
                all_questions.append(x)
        print(all_questions)
        
    def round_create(self, question):
        question_answers = question + "_answer"
        question_answers = self.df.iloc[0, self.df.columns != 'Question_Name']
        question_answers_list = question + "_answer_list"
        question_answers_list = list(question_answers)
        question_answers_count = question + "_answers_count"
        question_answers_count = self.df.iloc[0,11]
        q1_count = 10
        print(q1_count)
        total_ans_count = ["Question", 1,2,3,4,5,6,7,8,9,10,11,12]
        question_answers_list.insert(0,question)
        q1_dict = {total_ans_count[i]:question_answers_list[i] for i in range(0,question_answers_count+1)}
        print(q1_dict)

