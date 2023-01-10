from app import connection, cursor, fake
from reference_lists import games, consoles
import random

query = '''INSERT INTO products (brand, name, buy_price, sell_price, product_type,
 game_type, in_stock, provider_name)
 VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s
 )
'''

random.shuffle(games)
product_type = 'video_game'
in_stock = 'no'

# games
for _ in range(5000):
    game = random.choice(games)
    brand = game['brand']
    name = game['name']
    buy_price = random.randint(1000, 1750)
    sell_price = buy_price + random.randint(100, 500)
    buy_price *= 1000
    sell_price *= 1000
    game_type = game['gtype']
    provider_name = game['brand']

    bind = (brand, name, buy_price, sell_price, product_type, game_type, in_stock, provider_name)
    cursor.execute(query, bind)

random.shuffle(consoles)
product_type = 'game_console'

# consoles
for _ in range(500):
    console = random.choice(consoles)
    brand = console['brand']
    name = console['name']
    buy_price = console['price']
    rand = random.randint(100, 1000) * 1000
    sell_price = buy_price + rand
    game_type = '-'
    provider_name = console['brand']

    bind = (brand, name, buy_price, sell_price, product_type, game_type, in_stock, provider_name)
    cursor.execute(query, bind)

connection.commit()
