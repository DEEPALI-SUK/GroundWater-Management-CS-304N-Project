from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/predictObject' , methods=['POST'])
def predictObject():
    msg = ''
    if request.method == 'POST':
        details = request.form
        ph = details['ph']
        hardness = details['hardness']
        solid = details['solids']
        chloramines = details['chloramines']
        sulfate = details['sulfate']
        conductivity = details['conductivity']
        organic_carbon = details['organic_carbon']
        trihalomethanes = details['trihalomethanes']
        turbidity = details['turbidity']

        print("form entry received")
        msg='data taken'
    return render_template('index.html', msg=msg)

app.run(debug=True)
