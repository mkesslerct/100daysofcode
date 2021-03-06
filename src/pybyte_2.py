from datetime import datetime
import os
import urllib.request
from pprint import pprint

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:
import re

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
    """
    fecha_string = re.findall(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)
    fecha = datetime.strptime(fecha_string[0], '%Y-%m-%dT%H:%M:%S')
    return(fecha)


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    lista = []
    for l in loglines:
        if re.search('Shutdown initiated', l):
            lista.append(convert_to_datetime(l))
    if len(lista) > 1:
        return lista[-1] - lista[0]
    else: 
        return 0




def main():
    #pprint(loglines)
    print(convert_to_datetime('INFO 2014-07-03T23:27:51 supybot Shutdown initiated.\n'))
    print(time_between_shutdowns(loglines))
    
if __name__ == "__main__":
    main()