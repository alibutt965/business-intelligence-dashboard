from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = []  # Temporary data store

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if request.method == 'POST':
        month = request.form['month']
        profit = float(request.form['profit'])
        loss = float(request.form['loss'])
        net = profit - loss
        data.append({'month': month, 'profit': profit, 'loss': loss, 'net': net})
    return render_template('dashboard.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)


