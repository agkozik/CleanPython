# Ввести в Python Console
import datetime
# dir(), чтобы интерактивно исследовать модули и классы Python, находясь внутри сеанса интерпретатора.

# чтобы получить только имена, которые включают слово «date»:
[_ for _ in dir(datetime) if 'date' in _.lower()]

# help() позволяет просматривать документацию прямо из вашего интерпретатора (для выхода нажмите клавишу q).

help(datetime)
help(datetime.date)
help(datetime.date.fromtimestamp)
help(dir)