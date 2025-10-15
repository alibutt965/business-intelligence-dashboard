from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

data = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/input', methods=['GET', 'POST'])
def input_page():
    if request.method == 'POST':
        month = request.form['month']
        profit = float(request.form['profit'])
        loss = float(request.form['loss'])
        net = profit - loss
        data.append({'month': month, 'profit': profit, 'loss': loss, 'net': net})
        return redirect(url_for('input_page'))
    return render_template('input.html', data=data)

@app.route('/graphs')
def graphs_page():
    return render_template('graphs.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)

