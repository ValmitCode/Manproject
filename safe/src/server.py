import telebot
import peewee
import schedule
import time
import os
#variables_block
CO2_text=""
VOC_text=""
temp_text=""
CO2=""
VOC=""
temp=""
new_data="460|81-2"
report=""
s=""
maxData="1356"
minData="705"
maxDay="82"
minDay="2"
Colday="7"
colDay="4"
tempmax="25"
tempmin="18"
downDay="3"
flag=False
#FORMALITY:
bot = telebot.TeleBot("934628400:AAGz6WCtvQo0yN36T_0Z1ldyVZadIuaWJSk")
#Main_function
def sending():
    global new_data  
    #f1 = open(r'\data\MAPB_data.txt', "r")
    #new_data[message.chat.id] = list(f1.readlines()[-1])
    #f1.close()
    n=0
    global s
    global CO2
    global VOC
    global temp
    global CO2_text
    global VOC_text
    global temp_text
    global report
    s=new_data
    for i in range (len(s)):
        if(s[i]=="|"):
            n+=1
            i+=1
        elif(s[i]=="-"):
            n+=1
            i+=1
        elif n==0:
            CO2+=s[i]    
        elif n==1:
            VOC+=s[i]
        elif n==2:
            temp=temp+s[i]
    if int(CO2)<600:
        CO2_text="Кількість co2 в нормі. CO2="+CO2+"ppm"
    if int(CO2)>=600 and int(CO2)<=800:
        CO2_text="Кількість co2 в нормі, рекомендований рівень для освітніх установ. CO2="+CO2+" ppm"
    if int(CO2)>800 and int(CO2)<=1000:
        CO2_text="Кількість co2 в нормі, працездатність під загрозою. CO2="+CO2+" ppm"
    if int(CO2)>1000 and int(CO2)<=1400:
        CO2_text="Нижня межа допустимої норми. Можуть з'явитися перші симптоми: втома, головний біль, задуха, дискомфорт, слабкість, знижена увага. Необхідно провітрити приміщення. Працездатність падає. CO2=" +CO2+" ppm"    
    if int(CO2)>1400 and int(CO2)<=2000:
        CO2_text="Рівень co2 вище норми. Симптоми: головний біль, проблеми з носоглоткою, сильна втома, непрацездатність, задуха, дискомфорт. Необхідно зараз же провітрити приміщення. CO2="+CO2+" ppm"
    if int(CO2)>2000 and int(CO2)<=5000:
        CO2_text="Рівень co2 небезпечний для здоров'я. Можлива зміна складу крові. Симптоми: головний біль, проблеми з носоглоткою, сильна втома, непрацездатність, задуха, дискомфорт. Необхідно зараз же провітрити приміщення. CO2="+CO2+" ppm"
    if int(CO2)>5000 and int(CO2)<8192:
        CO2_text="У такому приміщенні без серйозних наслідків можна знаходиться всього лише кілька годин. Симптоми від минулих попереджень можуть посилитися. CO2="+CO2+" ppm"
    if int(CO2)==8192:
        CO2_text="Датчик зашкалює якщо ви відчуваєте духоту то показання надзвичайно небезпечні аж до летального результату. Але якщо не яких симптомів не спостерігається то датчик може помилятися через раптового збільшення VOC. C02="+C02+" ppm"
    if int(VOC)>0 and int(VOC)<100:
        VOC_text="малоймовірні симптоми: головний біль, роздратування в очах, носі і горлі. VOC="+VOC+" ppb"
    #if int(VOC)>100 and int(VOC)<200:
    #if int(VOC)>200 and int(VOC)<300:
    #if int(VOC)>0 and int(VOC)<100:
    temp_text="Температура повітря="+temp
    
    report=CO2_text+'                 '
    return report
    print(CO2)
    print(VOC)
    print(temp)
    
#sending()
#BotMainAlgorithm  
    
@bot.message_handler(commands=['start', 'help'])
def welcome(message):
    bot.send_message(message.chat.id, """Я бот, який контролює чистоту повітря, використовуючи
    пристрiй APC (Air Pollution Controller) та посилає своєчасні звіти про його забруднення в місці, де ви розмістили APC в Telegram.""")
    markup = telebot.types.ReplyKeyboardMarkup(one_time_keyboard = True)
    markup.add("інформація", "моніторинг", "останні дані", "завершити тестування", "статистика", "найближчі пристрої")
    bot.send_message(
    message.chat.id,
    "Оберіть функцію:",
    reply_markup = markup
    )
    info(message)
    #bot.register_next_step_handler(message, function)
@bot.message_handler(regexp="інформація")
def info(message):
    bot.send_message(message.chat.id, """У всіх приміщеннях, де тимчасово або постійно
перебувають люди, головним забруднювачем повітря є вуглекислий газ (СО2).
В нормі цей газ міститься у вуличному повітрі
у концентрації 300-400 ppm (0,03-0,04%), така концентрація є
оптимальною для дихання людини. Однак, з кожним
видихом людина наповнює оточуюче повітря новою порцією СО2 (18-25 л за годину).
Враховуючи, що концентрація
вуглекислого газу у повітрі, що видихається у 100 разів більша ніж у чистому
атмосферному повітрі, приміщення швидко перетворюється
на потенційно небезпечне для здоров’я.
Комфорт людей, які проводять час в приміщеннях, також знижують запахи, дим, випари від обладнання інтер'єрів, і т. Д.
Більшість з цих речовин, які ми сприймаємо нюхом (але навіть ті, які ми не в змозі розрізнити), відноситься до групи летючих органічних речовин.
Леткі органічні сполуки або ж VOC (volatile organic compounds) представляють собою хімічні речовини, які звільняються у вигляді газів з твердих або рідких речовин і легко випаровуються в повітря навіть при кімнатній температурі.
Концентрація цих речовин в помощеніях може бути навіть в 100 разів вище, ніж зовні.
Безліч виробів, які ми використовуємо щодня, або ж впливу яких ми піддаємося щодня, виділяють в повітря летючі органічні речовини.
У той час, як всі VOC схильні до того, щоб бути шкідливими, існує кілька VOC, які можуть бути особливо небезпечні, і, незважаючи на це, виділяються рядом виробів в наших будинках.
Цими VOC є формальдегід, бензол і фенол, які визначаються як небезпечні забруднювачі повітря за класифікацією Агентства з охорони навколишнього середовища США (EPA), US Green Building Council (USGBC) і Європейського союзу (ЄС).
Дослідження стверджують, що значення вище 500 нг / л (нанограмм на літр) летючих органічних речовин може становити небезпеку для здоров'я жителів будинків.
Проте, дані тисяч тестованих будинків показують, що середнє значення становить 1200 нг / л - більше двократного розміру допустимого рівня.
Навіть помірно підвищені рівні цих хімічних речовин в повітрі можуть викликати у людей проблеми зі здоров'ям, особливо у маленьких дітей, літніх людей, вагітних жінок, а також у тих, хто страждає від алергії і астми.""")
@bot.message_handler(regexp="найближчі пристрої")
def ongoing_test(message):
    print("test")
@bot.message_handler(regexp="статистика")
def ongoing_test(message):
    bot.send_message(message.chat.id, """CO2: максимальне = """+ maxData+""" мінімальне = """+ minData+ """ збільшується останні """+ colDay+""" дні.
    VOC: максимальне = """+maxDay+""" мінімальне = """+minDay+""", зменшуєься останні """+Colday+""" днів. 
    температура: максимальне = """+tempmax+""" мінімальне = """+tempmin+""", зменшується останні """+downDay+""" днів.
""")    
@bot.message_handler(regexp="моніторинг")
def ongoing_test(message):
    global report
    global flag
    global new_data
    flag=True
    while(flag==True):
        sending()
        bot.send_message(message.chat.id, report)
        time.sleep(900)
@bot.message_handler(regexp="завершити тестування")
def stop_test(message):
    global flag
    flag=False

@bot.message_handler(regexp="останні дані")
def m_test(message):
    global report
    global new_data
    sending()
    bot.send_message(message.chat.id, report)  

@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.send_message(message.chat.id, "Я не розумію цієї команди.")
bot.polling()    