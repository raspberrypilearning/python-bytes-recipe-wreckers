emoji = '🍽️😋'.replace('😋', '🤢')

protein = 'ТОФУ'.replace('ФУ', 'ПАД')         # ➝ ТОПАД
veg_1 = 'МОРКВА'.replace('МОРК', '')          # ➝ ВА
carb = 'РИС'.replace('Р', 'В')              # ➝ ВИС
veg_2 = 'ГОРОШОК'
garnish = 'М’ЯТА'
side = 'ВАРЕНІ ЯЙЦЯ'

print(
    f'{emoji} Почни з ложки {carb.lower()}',
    f'Зверху додай нарізані {veg_1.lower()} і {veg_2.lower()}',
    f'Додай смаженого {protein.title()}',
    f'Прикрась {garnish.lower()}',
    f'Подавай з гарніром із {side.lower()}',
    sep='\n'
)
