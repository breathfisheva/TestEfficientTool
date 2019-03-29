import os

qa_path = './QA'
def traverse_folder(folderpath):
    file_list = os.listdir(folderpath)
    return file_list

if __name__ == '__main__':
    print(traverse_folder(qa_path))