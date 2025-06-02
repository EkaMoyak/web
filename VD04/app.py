from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def show_current_time():
    current_time = datetime.now()

    # Разные форматы времени для демонстрации
    time_data = {
        'full': current_time.strftime("%d.%m.%Y %H:%M:%S"),
        'time': current_time.strftime("%H:%M:%S"),
        'date': current_time.strftime("%d %B %Y"),
        'weekday': current_time.strftime("%A"),
        'iso': current_time.isoformat(),
        'timestamp': int(current_time.timestamp())
    }

    return render_template('index.html', time=time_data)


if __name__ == '__main__':
    app.run(debug=True)