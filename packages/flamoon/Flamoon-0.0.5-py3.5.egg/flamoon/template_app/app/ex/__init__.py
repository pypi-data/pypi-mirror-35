# ex package

# инициализирует и получает необходимые данные для работы пакета

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from flask import Blueprint

from .data import page_titles

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

ex = Blueprint(
    name='ex',
    import_name=__name__, 
    static_folder='statics_ex',
    template_folder='templates'
)

# :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

from . import views