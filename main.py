import random
from flask import Flask #type: ignore

app = Flask(__name__)

@app.route("/")
def my_fav_game():
    game = ["GTA V", "PAYDAY 2", "Terraria", "WorldBox", "Minecraft"]
    facts = ["Больше всего я наиграл:", "Моя любимая игра:", "Самая дорогая для меня игра:", "Самая недорогая для меня игра:", "Самая крутая музыка:"]
    
    result = random.choice(facts) + " " + random.choice(game)

    return result

app.run(debug=True)