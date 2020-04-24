from string import Template
# безопасно для ввода данных пользователем, от инъекций
name = "user"
id = 874646848

t = Template('Hello, $name! Your id = $id')
st = t.substitute(name=name, id=id)
print(st)