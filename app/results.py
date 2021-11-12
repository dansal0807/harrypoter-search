from flask_table import Table, Col

class Results(Table):
    id = Col('Id', show=False)
    name = Col('Nome')
    gender = Col('Gênero')
    house = Col('Casa de Hogwarts')
    actor = Col('Ator')
