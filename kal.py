from flask import Flask, request
import requests
app = Flask(__name__)
@app.route('/payment',methods=['post','get','put'])
def test():
    pass



if __name__ == "__main__":
    app.run(host='localhost',port=4444,debug=True)

