import csv
import random
import string
from datetime import datetime
import psycopg2

try:
    db = psycopg2.connect(user='postgres',
                          password='1223345ktFDKL',
                          host='127.0.0.1.',
                          database='deputies',
                          port=5432)
except:
    print('RM2 DATABASE CONNECTION IS FAILED\n')

def translate(name):
    name = name.replace(' ', '_').lower()
    transtable = (
        (u"Щ", u"Sch"),
        (u"Щ", u"SCH"),
        (u"Ё", u"Yo"),
        (u"Е", u"Е"),
        (u"Ё", u"YO"),
        (u"Ж", u"Zh"),
        (u"Ж", u"ZH"),
        (u"Ц", u"Ts"),
        (u"Ц", u"TS"),
        (u"Ч", u"Ch"),
        (u"Ч", u"CH"),
        (u"Ш", u"Sh"),
        (u"Ш", u"SH"),
        (u"Ы", u"Yi"),
        (u"Ы", u"YI"),
        (u"Ю", u"Yu"),
        (u"Ю", u"YU"),
        (u"Я", u"Ya"),
        (u"Я", u"YA"),
        (u"А", u"A"),
        (u"Б", u"B"),
        (u"В", u"V"),
        (u"Г", u"G"),
        (u"Д", u"D"),
        (u"Е", u"E"),
        (u"З", u"Z"),
        (u"И", u"I"),
        (u"Й", u"J"),
        (u"К", u"K"),
        (u"Л", u"L"),
        (u"М", u"M"),
        (u"Н", u"N"),
        (u"О", u"O"),
        (u"П", u"P"),
        (u"Р", u"R"),
        (u"С", u"S"),
        (u"Т", u"T"),
        (u"У", u"U"),
        (u"Ф", u"F"),
        (u"Х", u"H"),
        (u"Э", u"E"),
        (u"Ъ", u"`"),
        (u"Ь", u"'"),
        (u"щ", u"sch"),
        (u"ё", u"yo"),
        (u"ж", u"zh"),
        (u"ц", u"ts"),
        (u"ч", u"ch"),
        (u"ш", u"sh"),
        (u"ы", u"yi"),
        (u"ю", u"yu"),
        (u"я", u"ya"),
        (u"а", u"a"),
        (u"б", u"b"),
        (u"в", u"v"),
        (u"ь", u""),
        (u"г", u"g"),
        (u"д", u"d"),
        (u"е", u"e"),
        (u"є", u"e"),
        (u"з", u"z"),
        (u"и", u"i"),
        (u"й", u"j"),
        (u"к", u"k"),
        (u"л", u"l"),
        (u"м", u"m"),
        (u"н", u"n"),
        (u"о", u"o"),
        (u"п", u"p"),
        (u"р", u"r"),
        (u"с", u"s"),
        (u"т", u"t"),
        (u"у", u"u"),
        (u"ф", u"f"),
        (u"х", u"h"),
        (u"э", u"e"),
    )
    for symb_in, symb_out in transtable:
        name = name.replace(symb_in, symb_out)
    return str(name).replace("'", '')

def password_randomizer(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def insert_data_automatizer(database_name, values, data):
    cur = db.cursor()
    cur.execute('INSERT INTO {0} {1} VALUES {2}'.format(str(database_name), str(values), str(data)))
    db.commit()

# try:
#     insert_data_automatizer('convocation', '( id, title, title_roman, years )', "( '8', '8', 'IIX', '2014-2015' )")
# except:
#     pass

with open("mps_8.csv") as f:
    counter = 0
    empty_emails = []
    reader = csv.reader(f)
    next(f, None)
    for row in reader:
        print('deputies ready -', counter)
        normalized_data = list(row)
        separated_names = tuple(row)[0].split(' ')
        # print(len(normalized_data))

        if normalized_data[6] == '':
            empty_emails.append(normalized_data[0])
            normalized_data[6] = str(counter)
        normalized_data = tuple(normalized_data)
        insert_data_automatizer('auth_user',
                                '( password, is_superuser, username, first_name, last_name, middle_name, email, phone, date_joined, is_staff, is_active, gender, photo, short_info, socials, convocation_id)',
                                "('" + password_randomizer() + "','" + '0' + "','" + translate(normalized_data[0])+"','"+ str(separated_names[1]).replace("'", "") + "','" + separated_names[2].replace("'", "") + "','" + separated_names[0].replace("'", "") + "','" + str(normalized_data[6]) + "','" + normalized_data[10] + "','" + str(datetime.now()) + "','" + '0' + "','" + '0' + "','" + normalized_data[7] + "','" + normalized_data[11] + "','" + str(normalized_data[22]).replace("'", '') + "','" + normalized_data[23] + "','" + normalized_data[3] + "')")
        counter += 1
    print(empty_emails)
with open("parties_8.csv") as f:
    counter = 0
    reader = csv.reader(f)
    next(f, None)
    for row in reader:
        print('parties-ready', counter)
        # print(row)
        normalized_data = tuple(row)
        print(normalized_data)
        insert_data_automatizer('party', '( rada_id, title )', "('" + normalized_data[0] + "','" + str(normalized_data[1]).replace("'", '') +"')")
        counter += 1
