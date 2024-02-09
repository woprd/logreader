"""
A class that reads a text file in Common Log Format and converts to different formats
"""
import json
import pandas as pd 

class CLFReader:

    @staticmethod
    def parse_log(log):
        """
        receives a single line of CLF file and returns tuple of items
        """
        ip_address, residual = log.split(" ", 1)
        rfc_id, residual = residual.split(" ", 1)
        user_id, residual = residual.split(" ", 1)
        date_time_tz, residual = residual.split("] ", 1)
        date_time_tz = date_time_tz.strip('[')
        request_line, residual = residual.split('\" ', 1)
        status_code, residual = residual.split(" ", 1)
        response_size, residual = residual.split(" ", 1)
        referrer, residual = residual.split(' \"', 1)
        referrer = referrer.strip('\"')
        user_agent = residual[:-1]
        return (ip_address, rfc_id, user_id, date_time_tz, request_line, 
            status_code, response_size, referrer, user_agent)

    def __init__(self, filename):
        with open(filename) as f:
            logs = f.read().splitlines()
            self.logs = [self.parse_log(log) for log in logs]
        # convert to dataframe
        self.to_dataframe()

    def to_dataframe(self):
        self.df = pd.DataFrame(self.logs)
        self.df.columns = ["ip_address", "rfc_id", "user_id", "date_time_tz", "request_line",
                          "status_code", "response_size", "referrer", "user_agent"]
        datetime_format = "%d/%b/%Y:%H:%M:%S %z"
        date_time_objs = pd.to_datetime(self.df.date_time_tz, format=datetime_format)
        self.df.set_index(date_time_objs, inplace=True)
        del self.df["date_time_tz"]

        


class MongoDBReader:

    def __init__(self, filename):
        with open(filename) as f:
            logs = f.read().splitlines()

        self.logs = []
        for log in logs: 
            try:
                self.logs.append(json.loads(log))
            except Exception:
                print("line containin invalid json")

        new_logs = []
        for log in self.logs:
            datetime = log['t']['$date']
            severity = log['s']
            component = log['c']
            id = log['id']
            context = log['ctx']
            try:
                message = log['msg']
            except Exception: 
                attr = None  
            try:
                attr = log['attr'] # this is optional and higly variable 
            except Exception: 
                attr = None  
            try:
                tags = log['tags'] # this is optional and higly variable 
            except Exception: 
                tags = None  

            # TODO handle other tags, if present

            new_logs.append((datetime, severity, component, id, context, message, attr, tags))

        self.logs = new_logs
        self.to_dataframe()

    def to_dataframe(self):
        self.df = pd.DataFrame(self.logs)
        self.df.columns = [
            "datetime", "severity", "component", "id", "context", "message", "attr", "tags"
        ]
        date_time_objs = pd.to_datetime(self.df.datetime)
        self.df.set_index(date_time_objs, inplace=True)
        del self.df["datetime"]

    





        



