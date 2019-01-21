from flask import *
import time
import record
import products
import json

app = Flask(__name__)
app.config['DEBUG'] = True
HOST = "127.0.0.1"
PORT = 5000

records = []   # keep tracks of all the records
rec_stack = [] # used to get the last record

starting_server_time = (time.asctime(time.localtime(time.time()))).split(" ")
# the ID will contains the date when the server has started and a number of the last order
# since the start of the server separated by a "#"
last_ID = "_".join(starting_server_time) + "___0"


def generate_ID():
    # the new ID will contains the date when the server has started and the number of the current order
    # since the start of the server separated by a "#"
    global last_ID
    print(last_ID)
    creation_date, last_order_nr = last_ID.split("___")
    new_order_nr = int(last_order_nr) + 1
    last_ID = creation_date + "___" + str(new_order_nr)
    return last_ID


@app.route('/')
def home():
    return render_template("table_generator.html", ip = "IP: %s" % HOST, port =  "PORT: %s" % PORT)


@app.route('/table/<string:table_name>/')
def get_table(table_name):
    return render_template("test.html", products=products.products_list)


@app.route('/table/<string:table_name>/sendOrder', methods=['GET', 'POST'])
def take_order(table_name):
    """
        Register the new order
    """
    if request.method == "POST":
        # Get the data from the request
        raw_data = request.get_json()
        print(raw_data)

        # Extract the items and make a record for this request
        new_record = record.Record(generate_ID(), table_name, raw_data["bill_info"], "Pending", raw_data["total_value"])
        print(new_record)

        # Save the record
        records.append(new_record)
        rec_stack.append(new_record)

        # Everything is fine
        return "ok " + new_record.ID
    else:
        return "The method is not available"


@app.route('/table/<string:table_name>/<string:ID>/status', methods=['GET', 'POST'])
def get_table_status(table_name, ID):
    """
        Get the order's status from record identified by the ID
        Table name is optional.
    """
    if request.method == "POST":
        for rec in records:
            if rec.ID == ID:
                return rec.status
        return "Record do not exist!"
    else:
        return "The method is not available"


@app.route('/table/<string:ID>/getOrder')
def get_order(ID):
    """
        Get the order's items from record identified by the ID
    """
    for rec in records:
        if rec.ID == ID:
            return jsonify(products=rec.request_data)
    return "None"


@app.route('/records')
def get_records():
    """
         Get all the records
    """
    return jsonify(records_list=[rec.get_record_for_history_json() for rec in records])


@app.route('/lastrecord')
def get_last_record():
    """
        Pull a record from the stack
    """
    if len(rec_stack):
        rec = rec_stack[0].get_record_info_json()
        rec_stack.pop(0)
        return rec
    return "None"


@app.route('/status/accepted/<string:ID>')
def set_status_accepted_record(ID):
    """
        Set status "Accepted" to a record identified by ID
    """
    return set_status(ID, "Accepted")


@app.route('/status/canceled/<ID>')
def set_status_canceled_record(ID):
    """
          Set status "Canceled" to a record identified by ID
    """
    return set_status(ID, "Canceled")


def set_status(ID, status):
    """
        Set status to a record identified by ID
    """
    log_rec = "Request was not validated!"
    for rec in records:
        if rec.ID == ID:
            if rec.status == "Pending":
                rec.status = status
                log_rec = "Request validated!"
                rec_stack.append(rec)  # Push the record again in the stack
    print("Status -> ID: %s \n" % ID + log_rec)
    return log_rec


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
