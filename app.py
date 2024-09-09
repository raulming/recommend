from flask import Flask, jsonify,render_template,request
import joblib
import pandas as pd
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend',methods=['POST'])
def recommend():
    print(request.form)
    print(request)
    # gender = request.form['gender']
    age = int(request.form['age'])
    height = float(request.form['height'])
    weight = float(request.form['weight'])
    
    # 这里添加你的尺寸推荐算法
    # 例如，根据身高和体重计算衣服尺寸
#     size = calculate_size(gender, age, height, weight)
    # if request.is_json:
    #     data = request.json
    # else:
    #     data = request.form.to_dict()
    
    # print(data)
      
    prediction = clf.predict([[ weight, height,age]])
    size = prediction[0]

    print(size)
    
    return render_template('recommend.html', size=size)




@app.route('/predict', methods=['POST'])
def predict():
     json_ = request.json
     query_df = pd.DataFrame(json_)
     query = pd.get_dummies(query_df)
     prediction = clf.predict(query)
     return jsonify({'prediction': list(prediction)})
if __name__ == '__main__':
     clf = joblib.load('DecisionTreeClassifier.pkl')
     app.run(port=8080)