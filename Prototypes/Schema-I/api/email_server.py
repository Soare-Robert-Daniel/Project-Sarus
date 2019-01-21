from flask import *
from tools import check_email
from database import insert as insert_db

app = Flask(__name__)

@app.route('/email', methods=['POST', 'GET'])
def email():
    if request.method == 'POST':
        data = request.get_json()
        if check_email(data['email']):
            insert_db(data['email'])        
            return jsonify(result = 0) # Everything is good!
        return jsonify(result = 1)     # The email format is no valid
    return jsonify(result = -1)        # the type request is not valid

if __name__ == '__main__':
   app.run(host = '0.0.0.0', port = 6000)