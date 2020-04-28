from collections import defaultdict
# при обращении к отсутствующему ключу его создает
# и инициализирует фабрику по умолчанию List()
def_dic = defaultdict(list)
def_dic['dogs'].append('Woodie')
def_dic['dogs'].append('Matros')
print(def_dic['dogs']) # ['Woodie', 'Matros']
