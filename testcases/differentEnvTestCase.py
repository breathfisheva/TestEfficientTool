

from utils.traverseFolder import traverse_folder
from utils.compareImage import *

def get_alpha_str(s):  #因为图片名字里会包含测试账号，所以会导致不同的环境下的文件夹的png文件名不一样，所以把测试账号这一部分去掉
    result = ''.join([x for x in s if x.isalpha()])
    return result

if __name__ == '__main__':
    #get file list
    file_list = []
    qa_file_list = traverse_folder('../QA')
    uat_file_list = traverse_folder('../UAT')

    #compare files
    for fileqa in qa_file_list:
        for fileuat in uat_file_list:
            if get_alpha_str(fileqa) == get_alpha_str(fileuat):
                fileqa = '../QA/' + fileqa
                fileuat = '../UAT/' + fileuat
                compare_image(fileqa, fileuat)