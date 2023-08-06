# -*- coding: utf-8 -*-
# app.py

# 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

import os, shutil, subprocess
from .config import configs

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

class App:
    def __init__(self):
        self.template_folder = configs['template']
        self.scripts = configs['scripts']

    def init(self):
        where = os.getcwd()
        src = self.template_folder

        for src_folder, list_folder, files in os.walk(src):
            if os.path.basename(src_folder) == '__pycache__':
                shutil.rmtree(src_folder)

        try:
            for item in os.listdir(src):
                if item != '__pycache__':
                    s = os.path.join(src, item)
                    d = os.path.join(where, item)
                    if os.path.isdir(s):
                        shutil.copytree(s, d)
                    else:
                        shutil.copy2(s, d)
            os.system('echo "\n[ \033[92mTrue\033[0m ] - работа выполнена\n"')
        
        except FileExistsError:
            os.system('echo "\n[ \033[31mFalse\033[0m ] - вы уже инициализировали данные\n"')
          
        
        print()


# alias
app = App()