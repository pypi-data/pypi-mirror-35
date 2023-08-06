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

    def init(self):
        where = os.getcwd()
        src = self.template_folder

        try:
            for item in os.listdir(src):
                s = os.path.join(src, item)
                d = os.path.join(where, item)
                if os.path.isdir(s):
                    shutil.copytree(s, d)
                else:
                    shutil.copy2(s, d)
            os.system('echo "\n[ \033[92mTrue\033[0m ] - работа выполнена\n"')
        
        except FileExistsError:
            os.system('echo "\n[ \033[31mFalse\033[0m ] - вы уже инициализировали данные\n"')
        
        subprocess.call('export FLASK_APP=manage.py', shell=True)
        # subprocess.call('flask db init', shell=True)
        print()


# alias
app = App()