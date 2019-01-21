from flask import *
import time
import record
import products
import json

app = Flask(__name__)
app.config['DEBUG'] = True
HOST = "127.0.0.1"
PORT = 5000

history = {}   # used to the order from a table
records = []   # keep tracks of all the records
rec_stack = [] # used to get the last record

starting_server_time = (time.asctime(time.localtime(time.time()))).split(" ")
# the ID will contains the date when the server has started and a number of the last order
# since the start of the server separated by a "#"
last_ID = "_".join(starting_server_time) + "___0"


def generate_id():
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
    if request.method == "POST":
        raw_data = request.get_json()
        print(raw_data)
        info = {
            "date": time.asctime(time.localtime(time.time())),
            "request": raw_data["bill_info"]
        }

        new_record = record.Record(generate_id(), table_name, raw_data["bill_info"], "Pending", raw_data["total_value"])
        print(new_record)

        records.append(new_record)
        rec_stack.append(new_record)

        if table_name not in history.keys():
            history[table_name] = []
        history[table_name].append(info)
        print(history[table_name])
        return "ok "
    else:
        return "The method is not available"


@app.route('/table/<string:table_name>/status', methods=['GET', 'POST'])
def get_table_status(table_name):
    if request.method == "POST":
        for rec in records:
            if rec.table_name == table_name:
                return rec.status
        return "Table name is not in records!"
    else:
        return "The method is not available"


@app.route('/table/<string:table_name>/getOrder')
def get_order(table_name):
    product_list = []

    if table_name in history.keys():
        if len(history[table_name]):
            product_list = history[table_name][-1]["request"]
        if len(product_list):
            print(jsonify(products=product_list))
            return jsonify(products=product_list)

    return "None"


@app.route('/history')
def get_history():
    return jsonify(history)


@app.route('/records')
def get_records():
    return jsonify(records_list=[rec.get_record_for_history_json() for rec in records])


@app.route('/lastrecord')
def get_last_record():
    if len(rec_stack):
        rec = rec_stack[0].get_record_for_history_json()
        rec_stack.pop(0)
        return rec
    return "None"


@app.route('/status/accepted/<string:id>')
def set_status_accepted_record(id):
    log_rec = "Status -> ID: %s \n" % id

    for rec in records:
        print(rec)
        if rec.ID == id:
            if rec.status == "Pending":
                rec.status = "Accepted"
                rec.update_date()
                log_rec += "Request validated!"
                rec_stack.append(rec)
    print(log_rec)
    return log_rec


@app.route('/status/canceled/<string:id>')
def set_status_canceled_record(id):
    log_rec = "Status -> ID: %s \n" % id
    for rec in records:
        if rec.ID == id:
            if rec.status == "Pending":
                rec.status = "Canceled"
                log_rec += "Request validated!"
                rec_stack.append(rec)
    print(log_rec)
    return log_rec


@app.route('/status/<string:id>',  methods=['GET', 'POST'])
def set_status(id):
    if request.method == "POST":
        job_done = False
        log_rec = "ID: %s \n" % id
        data = request.get_json()
        print(data)
        if data is not None:
            if len(data) > 0:
                data = data["new_status"]
                if data == "Canceled" or data == "Accepted":
                    for rec in records:
                        if rec.ID == id:
                            rec.status = data
                            job_done = True
                            log_rec += "Request validated!"
                    if not job_done:
                        log_rec += "The id is not in records!\n"
                else: log_rec += "Invalid format!\n"
        else:
            log_rec += "No data!\n"
        print(log_rec)
        if job_done:
            return jsonify(valid = "Yes", log = "The request was processed")
        else:
            return jsonify(valid = "No", log = "No good")
    else:
        return jsonify(valid="No", log="Not a post method")


@app.route('/thankyou')
def thank_you():
    return render_template("thankyou.html")


if __name__ == '__main__':
    app.run(host=HOST, port=PORT)
