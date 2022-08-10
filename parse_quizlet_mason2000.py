# -*- coding: utf-8 -*-
import argparse
from datetime import datetime
import os
import pandas as pd
import random
import time
import sys

pd.set_option('display.max_columns', 10)
pd.set_option('display.width', 1000)

parser = argparse.ArgumentParser()
parser.add_argument('--file_base_path',
                    help='the base path of your files are located')

args = parser.parse_args()
file_base_path = args.file_base_path


# file_base_path = '/Users/johnson.huang/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000'

# read file - main file
def get_your_book(file_base_path, file_name='quizlet_mason2000.csv'):
    print(f'file_base_path: {file_base_path}')
    print(f'file_name: {file_name}')

    with open(f'{file_base_path}/{file_name}') as f:
        lines = f.readlines()
    en_lst = list()
    zh_lst = list()
    for line in lines:
        tmp = line.split(' - ')
        en = tmp[0].strip()
        zh = tmp[-1].replace('\n', '').strip()
        en_lst.append(en)
        zh_lst.append(zh)
    df = pd.DataFrame({'en': en_lst, 'zh': zh_lst})
    return df


# read file - your records
def get_your_history_records(file_base_path, file_name='ans_record_file.csv'):
    ans_record_file = f'{file_base_path}/{file_name}'
    print('start to read history records')
    try:
        df_ans_record_file = pd.read_csv(ans_record_file)
        print('read history records done')
    except FileNotFoundError:
        print('First entry, no history records.')
        df_ans_record_file = pd.DataFrame(
            {
                'en': df['en'].tolist(),
                'review_times': [0] * df.shape[0],
                'correct_times': [0] * df.shape[0],
                'avg_correct_rate': [0] * df.shape[0],
                'avg_elapsed_time': [0] * df.shape[0],
                'total_elapsed_time': [0] * df.shape[0],
            }
        )
        df_ans_record_file.to_csv(ans_record_file, index=False)
        print('create history records done')
    return df_ans_record_file


def get_rand_lst(get_n_int: int, input_lst: list):
    rand_lst = random.choices(input_lst, k=get_n_int)
    return rand_lst


def print_progress_bar(value, max_val):
    n_bar = 100
    j = value / max_val
    sys.stdout.write('\r')
    bar = '█' * int(n_bar * j)
    bar = bar + '-' * int(n_bar * (1 - j))

    sys.stdout.write(f"[{bar:{n_bar}s}] {int(100 * j)}% ")
    sys.stdout.flush()


def line_prepender(filename, line):
    # if file does not exist
    if not os.path.exists(filename):
        with open(filename, 'w'): pass
    # seek the top position to append
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)


if __name__ == '__main__':
    print(f'pwd: {os.getcwd()}')
    # read files
    book_file_name = 'quizlet_mason2000.csv'
    df = get_your_book(file_base_path, file_name='quizlet_mason2000.csv')
    # df = get_your_book(file_base_path=file_base_path, file_name=book_file_name)
    ans_record_file_name = 'ans_record_file.csv'
    df_ans_record_file = get_your_history_records(file_base_path=file_base_path, file_name=ans_record_file_name)

    # Number of questions to review
    print('Number of questions to review:')
    ques_num = int(input())
    print(f'There will be {ques_num} questions.')

    # =============================
    #
    # quiz
    #
    # =============================
    choice_num = 4
    # mode - en / zh
    given = 'en'
    all = ['en', 'zh']
    # mode - range
    input_ans = int(input(f"""mode to review:
            1) arbitrary
            2) range
            """))
    print(f'input mode: input_ans, type(input_ans)')
    if input_ans == 1:
        range_start, range_end = 0, df.shape[0]
    else:
        range_start = int(input(f"""range start from no.:"""))
        range_end = int(input(f"""range end to no.:"""))
    #print(f'range_start: {range_start}, {type(range_start)}; range_end: {range_end}, {type(range_end)}')
    rand_list = get_rand_lst(get_n_int=ques_num, input_lst=list(range(range_start, range_end)))
    # rand_list = [3] * 2  # FIXME: for test
    error_book_content = list()
    num_n_question = 1
    for rand in rand_list:
        correct_ans = df.loc[(df.index.isin([rand], level=0)), :]
        # print(f'correct_ans: {correct_ans}')

        tmp = df.loc[~(df.index.isin([rand], level=0)), :]
        other_choices = tmp.sample(n=choice_num - 1)
        # print(f'other_choices: {other_choices}')

        other = list(set(all) - {given})[0]
        print_out_ques = correct_ans[given].tolist()
        correct_choice = correct_ans[other].tolist()
        other_choice = other_choices[other].tolist()
        print_out_choices = correct_choice + other_choice
        # print(f'given: {given}; other: {other}')
        # print(f'print_out_ques: {print_out_ques}')
        # print(f'print_out_choices: {print_out_choices}')
        random.shuffle(print_out_choices)
        # print(print_out_choices, 'type:', type(print_out_choices))

        input_1 = print_out_choices[0]
        input_2 = print_out_choices[1]
        input_3 = print_out_choices[2]
        input_4 = print_out_choices[3]

        print(f'question. {num_n_question} / {ques_num}')
        num_n_question += 1
        # FIXME: maybe we need a pause
        start_ts = time.time()
        input_ans = input(f"""{print_out_ques}:
        1) {input_1}
        2) {input_2}
        3) {input_3}
        4) {input_4}
        """)
        end_ts = time.time()
        elapsed_time = round(end_ts - start_ts, 2)
        # print(f'input_1: {input_1}')
        # print(f'input_2: {input_2}')
        # print(f'input_3: {input_3}')
        # print(f'input_4: {input_4}')

        # update df_ans_record_file
        tmp = df_ans_record_file.loc[df_ans_record_file['en'] == print_out_ques[0]]
        val_review_times = tmp['review_times'].tolist()[0]
        val_correct_times = tmp['correct_times'].tolist()[0]
        val_total_elapsed_time = tmp['total_elapsed_time'].tolist()[0]

        val_review_times += 1
        val_total_elapsed_time += elapsed_time
        if eval(f'input_{input_ans}') == correct_choice[0]:  # get string in list
            print('correct')
            val_correct_times += 1
        else:
            print('wrong')
            cnt = 0
            sec_to_sleep = 5
            print(f'take a glance within {sec_to_sleep} (sec)')
            print(f'################################### \n'
                  f'correct_ans: {correct_ans} \n'
                  f'###################################')
            for i in range(0, sec_to_sleep):
                print(print_progress_bar(cnt, sec_to_sleep), end='')  # make it print in the same line
                time.sleep(1)
                cnt += 1
            error_book_content.append(print_out_ques[0])
        print('\n')
        idx = df_ans_record_file.loc[df_ans_record_file['en'] == print_out_ques[0]].index
        df_ans_record_file.at[idx, 'review_times'] = val_review_times
        df_ans_record_file.at[idx, 'correct_times'] = val_correct_times
        df_ans_record_file.at[idx, 'total_elapsed_time'] = val_total_elapsed_time

    df_ans_record_file['avg_correct_rate'] = round(
        df_ans_record_file['correct_times'] / df_ans_record_file['review_times'], 2)
    df_ans_record_file['avg_elapsed_time'] = round(
        df_ans_record_file['total_elapsed_time'] / df_ans_record_file['review_times'], 2)
    # df_ans_record_file = df_ans_record_file.sort_values(by=['avg_correct_rate', 'avg_elapsed_time'], ascending=[True, False])
    df_ans_record_file = df_ans_record_file.sort_values(by=['avg_elapsed_time', 'avg_correct_rate'],
                                                        ascending=[False, True])
    df_ans_record_file.to_csv(f'{file_base_path}/{ans_record_file_name}', index=False)
    print(f'''Your history answer sheet is updated successfully!
          Check here: {file_base_path}/{ans_record_file_name}''')
    print(f'df_ans_record_file.shape: {df_ans_record_file.shape}')
    top_n = 5
    print(f'top {top_n} to review: \n {df_ans_record_file.head(top_n)}')
    top_n_en_lst = df_ans_record_file.head(top_n)['en'].tolist()
    show = df.loc[df['en'].isin(top_n_en_lst)]
    print(f'top {top_n} to review: \n {show}')

    # error book
    error_book_name = 'error_book_en.txt'
    line_prepender(filename=f'{file_base_path}/{error_book_name}', line=',  '.join(str(x) for x in error_book_content))
    current_time = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    line_prepender(filename=f'{file_base_path}/{error_book_name}', line=f'\n===== {current_time} ===== There are [{ques_num}] questions; range [no. {range_start}] ~ [no. {range_end}]')
    print(f'''error book content - {current_time}
{error_book_content}
''')

"""
base_path="/Users/johnson.huang/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000";
python \
${base_path}/parse_quizlet_mason2000.py \
--file_base_path "${base_path}"
"""
