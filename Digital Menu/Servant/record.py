import time
from flask import jsonify

# For every request from the client will be created a record which will contains all the information about the order,
# the time of creating and a uniq ID


class Record:

    def __init__(self, ID, table_name, request_data, status = "Pending", value = 0):
        self.request_data = request_data
        self.date = time.asctime(time.localtime(time.time()))
        self.ID = ID
        self.table_name = table_name
        self.value = value
        self.status = status

    def __str__(self):
        return "ID: %s, Date: %s, Table: %s, Status: %s,Value: %.2f,Request Data: %s" % (
            self.ID, self.date, self.table_name, self.status,self.value, self.request_data)

    def update_date(self):
        self.date = time.asctime(time.localtime(time.time()))

    def get_record_info(self):
        return [self.ID, self.date, self.table_name, self.status]

    def get_record_info_json(self):
        return jsonify(id = self.ID, date = self.date, table_name = self.table_name, status = self.status, total_value = str(self.value))

    def get_record_data(self):
        return self.request_data
