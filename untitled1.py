from flask import Flask, render_template,request,jsonify
import pickle
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('info.html')

@app.route('/predict', methods =['POST'])
def index1():
    name = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl','rb'))
    sal = round(mymodel.predict([[exp]])[0],2)
    return '<h1>Hi {}, Your Predicted Salary is {}</h1>'.format(name,sal)

@app.route('/api',methods=['POST'])
def index2():
    data=request.get_json()
    name = data['name']
    exp = float(data['exp'])
    mymodel = pickle.load(open('model1.pkl','rb'))
    sal = round(mymodel.predict([[exp]])[0],2)
    return jsonify({'name':name,'salary':sal})
if __name__ == "__main__":
    app.run(debug = True)