from flask import Flask # клас Flask дозволить нам створити екземпляр веб-додатку

app = Flask(__name__) # екземпляр і __name__ для того щоб flask коректно розпізнавав шляхи до файлів

@app.route('/')
def hello():
    return 'Hello, World!'

# у моєму випадку не виконується так як flask займається запуском серверу а не мій код 
if __name__ == '__main__':
    app.run()


# flask run
