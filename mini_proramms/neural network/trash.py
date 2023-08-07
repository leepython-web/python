friendlyHP = 100
friendlyAttackPower = 0
friendlyProtection = 0
friendlyFraction = 0
enemyHP = 100
enemyAttackPower = 0
enemyProtection = 0
enemyFraction = 0
berserkRage = 0


def friendlyFractionInput():
    global friendlyFraction
    friendlyFraction = input('''Выбери одну из фракций:
    1. Тьма
    2. Свет
    3. Нейтралитет
    ''')
    match friendlyFraction:
        case ('1'):
            friendlyFraction = -1
            print('Тьма. Отличный выбор!')
        case ('2'):
            friendlyFraction = 1
            print('Свет. Отличный выбор!')
        case ('3'):
            friendlyFraction = 0
            print('Нейтралитет. Отличный выбор!')
        case _:
            print('Соберись и попробуй снова.')
            return friendlyFractionInput()

def enemyFractionInput():
    global enemyFraction
    enemyFraction = input('''Выбери фракцию в которой состоит противник:
    1. Тьма
    2. Свет
    3. Нейтралитет
    ''')
    match enemyFraction:
        case ('1'):
            enemyFraction = -1
            print('Тьма. Отличный выбор!')
        case ('2'):
            enemyFraction = 1
            print('Свет. Отличный выбор!')
        case ('3'):
            enemyFraction = 0
            print('Нейтралитет. Отличный выбор!')
        case _:
            print('Соберись и попробуй снова.')
            return enemyFractionInput()

def parametrsHPF(num):
    print(f'Cоюзник: {friendlyHP - num} HP')
def parametrsHPE(num):
    print(f'Соперник: {enemyHP - num} HP')

friendlyAttackPower = input('Приветсвую, Воин. Введи значение своей базовой атаки: \n')
friendlyProtection = input('Введи значение своей защиты: \n')
friendlyFractionInput()

enemyAttackPower = input('Введи значение базовой атаки оппонента: \n')
enemyProtection = input('Введи значение защиты соперника: \n')
enemyFractionInput()

'''damageTaken = (attackPower + berserkRage + 0.5 * fraction) * protection/100'''

def fight():
    global friendlyaAttackPower, friendlyBerserkRage, friendlyFraction, friendlyProtection, enemyProtection,enemyaAttackPower, enemyBerserkRage, enemyFraction

    win = None
    print('Да начнется битва!')
    print('Увидев отдыхающего Врага, союзный Герой выпрыгнул из кустов и совершил атаку.')
    while not win:
        parametrsHPF(0)
        parametrsHPE(0)
        damageTakenF = (friendlyaAttackPower + friendlyBerserkRage + 0.5 * friendlyFraction) * friendlyProtection / 100
        damageTakenE = (enemyaAttackPower + enemyBerserkRage + 0.5 * enemyFraction) * enemyProtection / 100
        parametrsHPF(damageTakenF)
        parametrsHPE(damageTakenE)

fight()
