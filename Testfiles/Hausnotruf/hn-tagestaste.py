import ntplib
from time import ctime

###pip install ntplib


def print_time():
    ntpClient = ntplib.ntpClient()
    response = ntpClient.request('pool.ntp.org')

    print(ctime(response.tx_time))

if __name__ == "__main__":
        print_time()