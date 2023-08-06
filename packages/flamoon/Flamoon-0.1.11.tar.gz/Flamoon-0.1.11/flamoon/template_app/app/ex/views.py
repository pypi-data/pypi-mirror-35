# ex/views.py

# Формирует страницы для запрошенных урлов 

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import render_template

from . import (
    # blueprint
    ex,

    # data
    page_titles
)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

@ex.route('/')
def ex_page():
    return render_template('ex.html', data={
        'title_page': page_titles['ex_page']
    })

