from flask import Flask, render_template, request

app = Flask(__name__)

# Пример данных о машинах (в будущем можно подключить базу данных)
cars = [
    {
        "brand": "Toyota", "model": "Camry", "price": 1100000, "year": 2018,
        "image": "/static/images/Toyota Camry.jpg"
    },
    {
        "brand": "BMW", "model": "X5", "price": 2300000, "year": 2016,
        "image": "/static/images/BMW X5.jpg"
    },
    {
        "brand": "Kia", "model": "Rio", "price": 850000, "year": 2020,
        "image": "/static/images/Kia Rio.jpg"
    },
    {
        "brand": "Toyota", "model": "Corolla", "price": 950000, "year": 2017,
        "image": "/static/images/Toyota Corolla.jpg"
    }
]

@app.route('/')
def index():
    return render_template('index.html', cars=cars)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


