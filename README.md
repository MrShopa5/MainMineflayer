# ВНИМАНИЕ!
Это только бета - версия. Присутствуют баги, а так же некоторые функции, такие функции как: "#сундук", "#скинь"(не путать с коммандой с номерами слотов) еще не доделаны и требуют доработки. В планах огромная работа с дополненим разных функций и починкой и доработкой старых
# Podik - bot
Да, это новый бот для майнкрафта, написанный на платформе Mineflayer через мост python - javascript. Он создан для облегчения ваше жизни в вашем мире minecraft. Подик умеет копать нужные вам ресурсы, следовать за вами, автоматически есть и многое другое!
Работает с версии 1.16.5  и выше (до 1.20.2)

# Авторы
mrshopa5 - mrshopa(discord)

# Требования
У вас должен быть скачен python - https://www.python.org/
а так же вы должны установить мост - "pip3 install javascript"

# Заход на сервер
Вам стоит лишь найти почти в начале кода эти строки и настроить под себя по инструкции
bot =  mineflayer.createBot({

    'host':'localhost', - ip сервера
    'port':'12345', - если у вас айпи постороннего сервера, а не вашего личного, то порт вам не нужен
    'username': 'name', - имя вашего бота
    'version': 'version', - версия на которой будет работать бот
})

# Функциональность
Боту достаточно будет в чат прописать ниже описанные комманды, что бы привести его в действие
1. #следуй за мной - бот будет следовать за вами сколько вы хотите
2. #хватит преследовать - бот перестанет следовать за вами
3. #турель - бот встанет и начет бить вас (всего 70 ударов). Очень хорошо подходит для тренировки аима
4. #сражайся со мной - бот будет делать то же самое, что и в #турель , но уже будет ходить за вами и прыгать тем самым бить вас критами
5. #алмаз - бот сначало найдет алмаз в расстоянии 128 блоков, а после пойдет до него самыми безопасными способами
6. #железо - тоже самое, что и в #алмаз, но только с железом
7. #обломок - тоже самое, что и в #алмаз, но только с древним обломком
8. #иди на x, y, z - бот пойдет на те координаты, которые вы задали вместо x, y, z
9. #слот - бот покажет вам все слоты в хот баре
10. число от 1 до 37 - бот вам скинет предмет из того слота, номер которого вы написали. Обратите внимание, что номер слотов меняются в зависимости от кол - ва предметов в инвентаре бота
11. #где ты - бот вам скажет свои координаты
12. #тотем - бот возьмет тотем в левую руку
13. #quit - бот выйдет с сервера
14. если вы в вашем браузере напишите: localhost:3000, то перед вами откроется веб-версия инвентаря вашего бота
