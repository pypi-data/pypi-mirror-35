import sys
import os
import datetime as dt
from contextlib import redirect_stdout
from collections import ChainMap
from ecmwfapi import ECMWFDataServer


class ECMWFio:
    def __init__(self):
        self.terminal = sys.stdout

    def write(self, message):
        self.terminal.write(message)
        if message.find('No data, but EXPECT was provided') >= 0:
            raise Exception('ECMWF: EXPECT was provided')

    def flush(self):
        pass


class ERAretrieval:
    defaultera = {
        'stream': 'oper',
        'step': '0',
        'type': 'an',
        'levtype': 'ml',
        'param': '129/130/133/152',
        'format': 'netcdf'}

    defaultera5 = ChainMap({
        'dataset': 'era5',
        'class': 'ea',
        'levelist': '1/to/137',
        'time': '00/01/02/03/04/05/06/07/08/09/10/11/12/13/14/15/16/17/18/19/20/21/22/23',
        'grid': '0.3/0.3'}, defaultera)

    defaulteraint = ChainMap({
        'dataset': 'interim',
        'class': 'ei',
        'levelist': '1/to/60',
        'time': '00/06/12/18',
        'grid': '0.75/0.75'}, defaultera)

    server = ECMWFDataServer()

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def retrieve(self, fname):
        kwargs = ChainMap({'target': fname}, self.kwargs)
        self.server.retrieve(dict(kwargs))


def daterange(d1, d2):
    return (d1 + dt.timedelta(days=i) for i in range((d2 - d1).days))


def retrieve_single_day(date, retrieve_params, file):
    print('###########################')
    print('get ERA data for', date)
    print('###########################')
    try:
        with redirect_stdout(ECMWFio()):
            args = dict(ChainMap(retrieve_params, {'date': '{}'.format(date)}))
            ret = ERAretrieval(**args)
            ret.retrieve(file)
    except Exception as e:
        print('There was an ECMWF Data Server exception')
        print(type(e))
        print(e)
        quit()


def retrieve_days(startdate, enddate, folder, product='ERA5'):
    if product not in ['ERA5', 'ERA-Int']:
        raise LookupError(f'''{product} not in supported types.
        Supported types are ERA5 and ERA-Int''')
    product_dict = {
        'ERA5': ERAretrieval.defaultera5,
        'ERA-Int': ERAretrieval.defaulteraint
    }
    for today in daterange(startdate, enddate):
        path = os.path.join(folder, f'{today.year}', f'{today.month:02}')
        filename = f'{product}_ml_{today.year}{today.month:02}{today.day:02}.nc'
        file = os.path.join(path, filename)
        if not os.path.exists(path):
            os.makedirs(path)
        if os.path.exists(file):
            if os.path.getsize(file) == 0:
                os.remove(file)
            else:
                continue
        retrieve_single_day(today, product_dict[product], file)


if __name__ == "__main__":
    retrieve_days(dt.date(2016, 9, 12), dt.date(2016, 9, 14), '/media/ecmwf/ERA5/')
