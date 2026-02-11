emoji = '🍽️😋'.replace('😋', '🤢')

eiwitten = 'TOFU'.replace('FU', 'NG') # ➝ TONG
groente_1 = 'WORTEL'.replace('RTE', '') # ➝ WOL
koolhydraten = 'RIJST'.replace('IJ', OE') # ➝ ROEST
groente_2 = 'ERWTEN'
garnering = 'MUNT'
bijgerecht = 'GEKOOKTE EIEREN'

print(
    f'{emoji} Begin met een schepje {koolhydraten.lower()}',
    f'Bedek met in blokjes gesneden {groente_1.lower()} en {groente_2.lower()}',
    f'Voeg gegrilde {eiwitten.title()} toe',
    f'Garneer met {garnering.lower()}',
    f'Serveer met een bijgerecht van {bijgerecht.lower()}',
    sep='\n'
)
