# coding=utf-8

from __future__ import unicode_literals

import os
import sys
import zipfile
import shutil


PROJECT_ROOT = os.path.realpath(os.path.dirname(__file__))



def dfs_get_zip_file(input_path,result):
    files = os.listdir(input_path)
    for file in files:
        if os.path.isdir(input_path+'/'+file):
            dfs_get_zip_file(input_path+'/'+file,result)
        else:
            result.append(input_path+'/'+file)


def zip_path(input_path,output_path,output_name):
    f = zipfile.ZipFile(output_path+'/'+output_name,'w',zipfile.ZIP_DEFLATED)
    filelists = []
    dfs_get_zip_file(input_path,filelists)
    for file in filelists:
        f.write(file)
    f.close()
    return output_path+"/"+output_name


def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))



def run(output_dir):

    input_path = output_dir
    output_path = PROJECT_ROOT
    output_name = '%s.zip' % output_dir
    zipped_path = os.path.join(PROJECT_ROOT, output_name)
    # print zipped_path
    # input_path = os.path.join(PROJECT_ROOT, output_dir)

    if os.path.exists(zipped_path):
        os.remove(zipped_path)

    # zip_path(input_path,output_path,output_name)

    # zipf = zipfile.ZipFile(output_name, 'w', zipfile.ZIP_DEFLATED)

    # zipdir(output_dir, zipf)

    dir_path = os.path.join(PROJECT_ROOT, output_dir)
    shutil.make_archive(dir_path, 'zip', dir_path)


if __name__ == "__main__":
    output_dir = 'zip_output'
    run(output_dir)
