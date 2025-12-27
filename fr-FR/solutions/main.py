emoji = '🍽️😋'.replace('😋', '🤢')

proteine = 'TOFU'.replace('FU', 'RTUE') # ➝ TORTUE
legume_1 = 'CAROTTE'.replace('CAR', 'B') # ➝ BOTTE
glucide = 'RIZ'.replace('RIZ, 'AT') # ➝ RAT
legume_2 = 'POIS'
garniture = 'MENTHE'
accompagnement = 'ŒUFS CUITS DUR'

print(
    f'{emoji} Commencez par une dose de {glucide.lower()}',
    f'Recouvrez par des dés de {legume_1.lower()} et {legume_2.lower()}',
    f'Ajoutez des {protéine.title()} grillées',
    f'Garnissez avec {garniture.lower()}',
    f'Servez avec un accompagnement de {accompagnement.lower()}',
    sep='\n'
)
