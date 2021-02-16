import requests
import singer
import sys


LOGGER = singer.get_logger()


class EstocaClient():

    def __init__(self, config):
        self.config = config
        self.api_url = 'https://plataforma.estoca.com.br/devtools/data_connector/get_data'

       
    
    def get_orders(self,startDate,endDate):

        columns = [
            "id",
            "created_at",
            "customer_full_address",
            "customer_name",
            "delivery_full_address",
            "delivery_name",
            "erp_marketplace_id",
            "external_id",
            "handoff_finished_at",
            "handoff_idle_time",
            "has_extra_packaging",
            "holded_at",
            "human_id",
            "invoice_access_key",
            "invoice_number",
            "invoice_serie",
            "is_manual_order",
            "is_quarantine",
            "is_same_day_delivery",
            "marketplace_name",
            "operator_name",
            "order_price",
            "packing_finished_at",
            "packing_idle_time",
            "packing_packer_name",
            "packing_started_at",
            "packing_total_time",
            "picking_finished_at",
            "picking_idle_time",
            "picking_picker_name",
            "picking_started_at",
            "picking_total_time",
            "quarantine_comment",
            "service_name",
            "status",
            "store_id",
            "store_name",
            "total_items",
            "total_skus",
            "transporter",
            "updated_at",
            "warehouse_name"
        ]

        api_params = {
            'startDate': startDate,
            'endDate': endDate,
            'columns': ",".join(columns),
            'api_key': self.config['api_key'],
            'storeID': self.config['storeID']
        }
        
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
