# coding=utf-8

import os


if __name__ == '__main__':

    file_name = os.path.join(os.path.dirname(__file__), 'tables.txt')



    with open(file_name, 'r') as f1:
        _list = f1.readlines()

    # print _list




    r = []
    for each in _list:
        s = """ALTER TABLE ** ADD application_id int DEFAULT 1 NULL;\nCREATE INDEX index_application_id ON ** (application_id);\n"""
        each = each.strip()
        s = s.replace('**', each)
        r.append(s)


    out_file_name = os.path.join(os.path.dirname(__file__), 'output.txt')

    with open(out_file_name, 'w') as f2:
        f2.writelines(r)
