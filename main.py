from flask import Flask #type: ignore

app = Flask(__name__)

@app.route("/")
def blog():
   return "Čao! Это мой первый блог. <br>Меня зовут Артем, мне 14(В Январе 2027 мне будет 15), я занимаюсь разработкой на Python с Октября 2025 года(Ну то есть год) <br>Это мой первый раз когда я работаю с библиотекой Flask(А также я самостоятельно изучаю SQL)"

app.run(debug=True)
