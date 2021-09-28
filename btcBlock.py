# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 09:30:41 2021

@author: Filippo Loddo
"""

import requests
from datetime import datetime
import time

# Set the retrieval interval in seconds
RETRIEVE_INTERVAL = 5
# Get data from the API
DATASOURCE = "https://chain.api.btc.com/v3/block/latest/tx"

# Function to retrieve block data, updates the latest timestamp
def get_blocks(latest_block_time):
    try:
        r = requests.get(DATASOURCE)
        data = r.json()
    except:
        print('Could not retrieve API data')
        return latest_block_time
    # Get the blocks list
    data_list = (data['data']['list'])
    if not data_list:
        print('list empty', data_list)
        return latest_block_time
    # Initialize block record and addresses list
    block_info = {}
    # Add data from every block:
    for block in data_list:
        addresses = []
        block_info['block_height'] = block['block_height']
        ts = block['block_time']
        # Create new record only if there is new data
        if ts > latest_block_time:
            block_info['block_time'] = datetime.utcfromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
            block_info['fee'] = block['fee']
            block_info['inputs_value'] = block['inputs_value']
            block_info['outputs_value'] = block['outputs_value']
            outputs = block['outputs']
            # Get all addresses
            for output in outputs:
                address = output['addresses'][0]
                # add only valid addresses
                if address:
                    addresses.append(address)
            block_info['addresses'] = addresses

            print(block_info)
        else:
            print('no new block found')
            return ts
    return ts


# Retrieve data every N seconds
if __name__ == "__main__":
    latest_time = 0
    forever = True
    while forever:
        latest_time=get_blocks(latest_time)
        time.sleep(RETRIEVE_INTERVAL)
