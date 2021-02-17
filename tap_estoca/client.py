import requests
import singer
import sys


LOGGER = singer.get_logger()


class EstocaClient():

    def __init__(self, config):
        self.config = config
        self.api_url = 'https://plataforma.estoca.com.br/devtools/data_connector/get_data'

       
    
    def get_orders(self,startDate,endDate,stream_schema):

        columns = ",".join(stream_schema['properties'].keys())

        api_params = {
            'startDate': startDate,
            'endDate': endDate,
            'columns': ",".join(columns),
            'api_key': self.config['api_key'],
            'storeID': self.config['storeID']
        }
        
        LOGGER.info("Requesting URL: {0} | startDate: {1} , endDate: {2}".format(
            self.api_url,startDate,endDate))
        LOGGER.info("Requesting Columns: {0}".format(columns))
        req = requests.get(url=self.api_url,params=api_params)
        
        if req.status_code != 200:
            LOGGER.error("Error Code: {0}, {1}".format(
                req.status_code,req.content))
            sys.exit(1)

        resp = req.json()
        
        if 'data' in resp:
            if resp['data'] is None:
                LOGGER.error("Invalid request. Please check the parameters used.")
                sys.exit(1)
        else:
            LOGGER.error("Invalid request. Please check the parameters used.")
            sys.exit(1)
        
        
        api_data = resp['data']
        
        return api_data
