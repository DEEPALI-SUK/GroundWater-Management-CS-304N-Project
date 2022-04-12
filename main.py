from flask import Flask, render_template, request, redirect, url_for, session
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

__model = None

def get_estimated_potability(ph,hardness,solid,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity):
    x = np.array([[ph,hardness,solid,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity],])
    print(x)
    y=pd.DataFrame(x,columns=['c1','c2','c3','c4','c5','c6','c7','c8','c9'])
    x=y.to_numpy()
    print(y)
    print(x)
    return __model.predict(x)[0]


def load_saved_artifacts():
    print("loading saved artifacts...start")
    global __model
    if __model is None:
        with open('./model/ground_water_management_model.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

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
        potability=get_estimated_potability(ph,hardness,solid,chloramines,sulfate,conductivity,organic_carbon,trihalomethanes,turbidity)
        if (potability):
            msg='Water is safe for drinking purpose!'
        else:
            msg='Water is not safe for drinking purpose!'
    return render_template('index.html', msg=msg)

if __name__ == '__main__':
    load_saved_artifacts()
    app.run(debug=True)
