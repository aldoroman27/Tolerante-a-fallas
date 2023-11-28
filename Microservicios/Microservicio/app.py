from flask import Flask
app = Flask(__name__)

@app.route('/getWeatherForecast')
def getWeatherOnline():
    return 'Hoy será un día soleado dentro del microservicio!'

if __name__ == '__main__':
    app.run(debug=True)
