from flask import Flask, request, jsonify

app = Flask(__name__)

customers = [{"name": "John","age":25,"city": "New York"},
                {"name": "Peter","age":30,"city": "Chicago"},
             {"name": "Jane","age":22,"city": "Los Angeles"}]
  
@app.route('/',methods=['GET'])
def GetInfo():
    return jsonify({"message": "Welcome to the Home Page"})

@app.route('/customers',methods=['GET','POST'])
def GetCustomers():
    return jsonify(customers)

if __name__ == '__main__':
    app.run(debug=True)