import sys
import time

from flask import Flask, request
from flask_restful import Resource, Api
from datetime import timedelta


app = Flask(__name__)
api = Api(app)


class SystemUptime(Resource):
    def get(self):
        # Get the uptime in seconds since system boot from /proc/uptime
        # and turn it into a human-readable form using the really handy
        # timedelta function

        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            uptime_string = str(timedelta(seconds = uptime_seconds))

        return { 'uptime' : uptime_string }


api.add_resource(SystemUptime, '/uptime')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10004
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
