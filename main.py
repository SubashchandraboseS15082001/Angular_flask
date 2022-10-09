from flask import Flask, request as req, jsonify
from flask_cors import CORS, cross_origin
import os
from werkzeug.utils import secure_filename
import pickle
import numpy as np
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)
cors = CORS(app)
# app.config['CORS_HEADERS'] = 'application/json'
# app.config['UPLOAD_FOLDER'] = r"C:\\Users\\Subashhh\\Desktop"
users = []

@app.post('/signup')
@cross_origin()
def signup():
    try:
        username=req.json['username']
        email=req.json['email']
        password=req.json['password']

        if len(username) < 5:
            return {
                'message': "Username Should be atleast 5 characters",
                'error': 0
            }

        if len(email)==0:
            return {
                'message': "Please enter email id",
                'error': 0
            }

        if "@" not in email:
            return {
                "message": "Invalid email",
                "error": 0
            }

        if ".com" not in email and ".net" not in email:
            return {
                "message": "Invalid email",
                "error": 0
            }     
       
        if len(password) < 5:
            return {
                'message': "Password should be atleast 5 characters",
                'error': 0
            }

        user = {
        'username': username,
        'email': email,
        'password': password
        }

        if len(users)==0:
            users.append(user)
            return {
                'message': 'Account created successfully',
                'error': 1
            }
        

        if email in list(map(lambda x:x['email'],users)):
            return {
                'message':"Email already exists",
                'error':0
            }

        if username in list(map(lambda x:x['username'],users)):
            return {
                'message':"Username already exists",
                'error':0
            }

        
        users.append(user)
        return {
            'message': 'Account created successfully',
            'error': 1
        }
    except Exception as e:
        return {
            'message': "Invalid request",
            'error':0
        }

@app.post('/signin')
@cross_origin()
def signin():
    try:
        email=req.json['email']
        password=req.json['password']
        emails=list(map(lambda x: x["email"], users))

        if len(email) == 0 and len(password) == 0:
            return {
                    "message": "Enter email and password",
                    "error" : 0
                }

        if email in emails:
            if password == users[emails.index(email)]['password']:
                username = users[emails.index(email)]['username']
                return {
                    "message": f"Welcome {username}",
                    "error" : 1
                }
                
            else:
                return {
                    "message": "Invalid Password",
                    "error" : 0
                }
        else:
            return {
                "message": "User not found!",
                "error" : 0
            }

    except Exception as e:
        return {
            'message': "Invalid request",
            'error':0
        }

@app.post("/main")
@cross_origin()
def main():
    try:
        # f = req.files['file']
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        f = req.files['file']
        f.save(secure_filename(f.filename))
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        # file_name = app.config['UPLOAD_FOLDER'] + f.filename
         # dataframe = pd.read_csv(r"C:\\Users\\Subashhh\\Desktop\\transactions.csv"+file)
        # dataframe = pd.read_csv(file_name)
        # print(dataframe)
        fileName = os.path.abspath(f.filename)
 
        print(fileName)
        return {
            "message" : "File Uploaded Successfully",
            "error" : 1
    }
    except:
        return{
            "message" : "Select a file",
            "error" : 0
        }
  
@app.post("/dashboard")
@cross_origin()
def dashboard():
    try:
        television = req.json['television']
        radio = req.json['radio']
        newspaper = req.json['newspaper']
        inputData = {
        'television': television,
        'radio': radio,
        'newspaper': newspaper
        }
        if len(str(television)) == 0 or len(str(radio)) == 0 or len(str(newspaper)) == 0:
            return {
                "message": "Enter all the datas",
                "error" : 0
            }

        model = pickle.load(open("model","rb"))
        
        predicted_val = model.predict(np.array([list(map(float,[television,radio,newspaper]))]))[0]
        predicted_val="{:.1f}".format(predicted_val)
        print(predicted_val)
        with open('Advertising.csv','a') as f:
            f.write(','.join([television,radio,newspaper,predicted_val]))
            f.write("\n")

        return {
            "message": str(inputData),
            "predicted_val": predicted_val,
            "error": 1
        }

    except Exception as e:
        print(e)
        return {
            "message": "Invalid Request",
            "error": 0
        }

if __name__ == "__main__":
    app.run(debug=True)