from javascript import require, On, Once, AsyncTask, once, off
import random
from time import sleep
mineflayer = require('mineflayer')
pathfinder = require('mineflayer-pathfinder')
GoalFollow = pathfinder.goals.GoalFollow
GoalBlock = pathfinder.goals.GoalBlock

"""Имя бота"""
displayName = 'podik'

"""Данные о сервере и о боте"""
bot = mineflayer.createBot({

    'host': '123',
    'master': 'mrshopa5',
    'username': displayName,
    'version': '1.20.1',
})


"""Настройки полета бота на элитрах"""
bot.elytrafly = ({
    'speed': 0.05,
    'velocityUpRate': 0.1,
    'velocityDownRate': 0.01,
    'proportionalSpeed': True
})

"""Плагин на авто еду, с помощью этого плагина бот сможет самостоятельно есть когда ему понадобится"""
autoeat = require('mineflayer-auto-eat').plugin
bot.loadPlugin(autoeat)

"""Плагин на одевание брони, бот будет одевать броню полностью самостоятельно"""
armorManager = require("mineflayer-armor-manager")
bot.loadPlugin(armorManager)


"""Плагин на веб инвентарь, вам стоит лишь написать "localhost:3000" в вашу строку в браузере """
inventoryViewer = require('mineflayer-web-inventory')
inventoryViewer(bot)





"""Плагин на возможность бота искать нужные блоки"""
blockFinderPlugin = require('mineflayer-blockfinder')(mineflayer)
bot.loadPlugin(pathfinder.pathfinder)

"""Настройка движений бота"""
mcData = require('minecraft-data')(bot.version)
movements = pathfinder.Movements(bot, mcData)





"""Бот начнет лететь на указанные вами координаты, в разработке"""
@On(bot, 'chat')
def chat(this, user, message, *args):
    if '#элитры' in message:
        bot.elytrafly.start()





"""Бот будет искать руду которую вы указали (#алмаз, #железо, #обломок) в радиусе 128 блоков
Так же бот умеет добывать столько дерева сколько вы захотите (не более 40 и пока что только ель) """
@On(bot, 'chat')
def chat(this, user, message, *args):
    # бот будет добывать алмазы
    if '#алмаз' in message:
        block = bot.findBlock({
            'matching': mcData.blocksByName.diamond_ore.id,
            'maxDistance': 128, #здесь вы можете радиус поиска

        })
        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position)
            bot.chat('Нашел')
            bot.equip(bot.registry.itemsByName.netherite_pickaxe.id, 'hand')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(40)
            bot.chat('#алмаз') #бот подождет 40 секунд и снова пойдет искать следующий алмаз

    # бот будет добывать железо
    elif '#железо' in message:

        block = bot.findBlock({
            'matching': mcData.blocksByName.iron_ore.id,
            'maxDistance': 128, #здесь вы можете радиус поиска
        })
        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position)
            bot.chat('Нашел')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(20)
            bot.chat('#железо') #бот подождет 40 секунд и снова пойдет искать следующее железо


    # бот будет добывать обломки
    elif '#обломок' in message:
        block = bot.findBlock({
            'matching': mcData.blocksByName.ancient_debris.id,
            'maxDistance': 128, #здесь вы можете радиус поиска
        })

        if not block:
            bot.chat('Блок не найден!')

        else:
            print(block.position)
            bot.chat('Нашел')
            bot.pathfinder.setMovements(movements)
            goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
            bot.pathfinder.setGoal(goal1, True)
            sleep(40)
            bot.chat('#обломок') #бот подождет 40 секунд и снова пойдет искать следующий обломок незерита

    #бот будет добывать дерево
    elif '#дерево ' in message:
        list = message.split(' ')
        number = list[1]
        print(list)
        for i in range(int(number)):
            block = bot.findBlock({
                'matching': mcData.blocksByName.spruce_log.id,
                'maxDistance': 128, #здесь вы можете радиус поиска
            })

            if not block:
                bot.chat('Блок не найден!')
                break

            else:
                print(block.position)
                bot.pathfinder.setMovements(movements)
                goal1 = GoalBlock(block.position.x, block.position.y, block.position.z)
                bot.pathfinder.setGoal(goal1, True)
            sleep(0.5)

        print("Закончил")  #бот напишет вам в консоль, когда закончит





"""По комманде '#следуй за мной', бот будет следовать за вами, но не стоит далеко от него убегать.
По комманде '#хватит преследовать', бот перестанет вас преследовать"""
@On(bot, 'chat')
def sled(this, user, message, *args):
    if user != displayName:
        if '#следуй за мной' in message:
            bot.chat('Хорошо, следую за вами!')

            player = bot.players[user]
            target = player.entity

            bot.pathfinder.setMovements(movements)
            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, True)

        elif '#хватит преследовать' in message:
            bot.chat('Вот мы и прибыли')
            player = bot.players[user]
            target = player.entity

            bot.pathfinder.setMovements(movements)
            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, False)



"""По комманде '#дом', бот будет идти на заданные ему ниже координаты"""
@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if message == '#дом':
            x = -431  # здесь вы можете указать координаты x
            y = 150  # здесь вы можете указать координаты y
            z = -6023  # здесь вы можете указать координаты z
            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))



"""По комманде '#сундук', бот найдет ближайший к нему сундук и скинет в него свои вещи (В РАЗРАБОТКЕ)"""
@On(bot, 'chat')
def chat(this, user, message, slot, *args):
    if user and (user != displayName):
        if message == '#сундук':

            block = bot.findBlock({
                'matching': mcData.blocksByName.chest.id,
                'maxDistance': 128
            })

            print(block.position)

            pos0 = block.position

            if not block:
                bot.chat('Блок не найден!')

            else:
                bot.chat('Иду к сундуку!')
                bot.lookAt(pos0)

                bot.pathfinder.setMovements(movements)

                goal3 = GoalBlock(pos0.x, pos0.y, pos0.z)

                bot.pathfinder.setGoal(goal3, True)
                bot.lookAt(pos0)

                sleep(1)
                bot.openContainer(block)
                item = (bot.registry.itemsByName.diamond.id)






"""По комманде '#слот', бот будет показывать вам слоты поочередно"""
@On(bot, 'chat')
def chat(this, user, message, slot, *args):
    if user and (user != displayName):
        if message == '#слот':
            bot.activateItem(False)
            bot.setQuickBarSlot(0)
            bot.chat('Вот первый слот')
            sleep(2)
            bot.setQuickBarSlot(1)
            bot.chat('Вот второй слот')
            sleep(2)
            bot.setQuickBarSlot(2)
            bot.chat('Вот третий слот')
            sleep(2)
            bot.setQuickBarSlot(3)
            bot.chat('Вот четвёртый слот')
            sleep(2)
            bot.setQuickBarSlot(4)
            bot.chat('Вот пятый слот')
            sleep(2)
            bot.setQuickBarSlot(5)
            bot.chat('Вот шестой слот')
            sleep(2)
            bot.setQuickBarSlot(6)
            bot.chat('Вот седьмой слот')
            sleep(2)
            bot.setQuickBarSlot(7)
            bot.chat('Вот восьмой слот')
            sleep(2)
            bot.setQuickBarSlot(8)
            bot.chat('Вот и девятый слот')





"""По комманде (число от 1 - 36), бот будет скидывать вам предмет из этого слота
(к сожалению из за приколов движка java нумерация слотов меняется в зависимости от ситуации)"""
@On(bot, 'chat')
def tossNext1(this, user, message, slot, *args):
    if user and (user != displayName):
        b = [str(a) for a in range(0, 36)]
        a = b.copy()
        if message in a:
            if bot.inventory.items()[int(message) - 1] == None:
                bot.chat('Пусто')
                return
            else:
                friend = bot.nearestEntity()
                bot.lookAt(friend.position)
                pos = friend.position

                bot.pathfinder.setMovements(movements)
                bot.pathfinder.setGoal(pathfinder.goals.GoalNear(pos.x, pos.y, pos.z))
                bot.chat("Держи")
                print(bot.inventory.items()[int(message) - 1])

                item = bot.inventory.items()[int(message) - 1]
                bot.tossStack(item, tossNext1)
            if not friend:
                bot.chat("Братишка, ты где?")
                return

"""По комманде '#где ты', бот скинет его точные координаты"""
@On(bot, 'chat')
def say_position(this, username, message, *args):
    if message == '#где ты':
        p = bot.entity.position
        bot.chat(f"Мои кординаты: {p.toString()}")


"""По комманде '#еда' вы сможете узнать кол-во голода у бота"""
@On(bot, 'chat')
def eda(this, user, message, *args):
    if user != displayName:
        if '#еда' in message:
            bot.chat(f'Моя еда - {bot.food}')





"""По комманде '#сражайся со мной', бот будет сражаться с вами (всего 75 ударов)"""
@On(bot, "chat")
def attack(this, user, message, entity, *args):
    mcData = require('minecraft-data')(bot.version)
    movements = pathfinder.Movements(bot, mcData)
    if user != displayName:
        if '#сражайся со мной' in message:
            bot.chat('Тебе конец, щегол')
            bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')
            player = bot.players[user]
            target = player.entity

            player = bot.players[user]  # еслу указать никнейм то он будет бить того игрока с тем никнеймом

            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, True)

            for i in range(75): #здесь можно указать и число больше, но я не рекомендую вам этого делать т.к он может просто вылететь
                sleep(0.001)
                bot.setControlState('jump', True)
                sleep(0.1)
                bot.setControlState('jump', False)
                bot.attack(target)

                bot.equip(bot.registry.itemsByName.netherite_sword.id, 'hand')






"""Если у бота очков голода меньше 17, она начинает есть"""
@On(bot, 'eat')
def eat(this, eat):
    if bot.eat < 17: #здесь вместо 17 вы можете изменить на любое другое число до 20
        bot.equip(bot.registry.itemsByName.golden_apple.id, 'hand')
        bot.activateItem()




"""Бот при заходе на сервер будет писать нужную вам комманду (в основном это /login <password> или 
/register <password> <password>"""
@On(bot, 'login')
def login(this):
    bot.chat('/login 123321') #здесь вы можете настроить комманду при заходе бота на сервер




"""Бот будет говорить, что начался дождь, и что дождь закончился"""
@On(bot, "rain")
def rain(this):
    if bot.isRaining:
        bot.chat("Дождь пошел кажись")
    else:
        bot.chat('О, а вот уже и дождь закончился!')



"""По комманде '#тотем', бот будет брать тотем в левую руку"""
@On(bot, 'chat')
def chat(this, user, message, *args):
    if message == '#тотем':
        bot.equip(bot.registry.itemsByName.totem_of_undying.id, 'off-hand')

"""По комманде '#скинь' бот будет скидывать вам предмет, который вы сможете указать ниже"""
@On(bot, 'chat')
def chat(this, user, message, *args):
    if message == '#скинь':
        item = bot.registry.itemsByName[bot.registry.itemsByName.totem_of_undying.id] #вместо totem_of_undying вы можете указать свой предмет
        if (item) in (bot.inventory.items()):
            bot.chat('Одну секунду')
            player = bot.players[user]
            target = player.entity
            bot.pathfinder.setMovements(movements)
            goal = GoalFollow(target, 1)
            bot.pathfinder.setGoal(goal, True)
        else:
            bot.chat("Такого предмета у меня нет")




@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if '#иди на' in message:
            message = message[8:]
            message = message.split(' ')
            a = []
            for i in message:
                a.append(int(i))
            x, y, z = a

            bot.pathfinder.setGoal(pathfinder.goals.GoalNear(x, y, z))


@On(bot, 'chat')
def chat(this, user, message, *args):
    if user and (user != displayName):
        if message == '#git':
            bot.chat("https://github.com/MrShopa5/BotMineflayer")


while True:
    pass
