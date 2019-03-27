from geosupport import Geosupport
from geosupport import GeosupportError
import re

g = Geosupport()

def geocode(inputs):
    inputs_copy = inputs
    uid = inputs.pop('uid')
    try:
        geo = g['1'](**inputs, mode = 'extended')
        return get_output(uid, geo)
    except GeosupportError as e:
        return error_handling(e, uid, inputs)
               
def error_handling(e, uid, inputs):
    return {'status': 'failure',
            'output': { 
                        'uid':uid,
                        **inputs,
                        'error_message':str(e),
                        'alternative_names': e.result.get('List of Street Names', '')
                        }
            }

def get_output(uid, geo):
    output = {
        # Spatial info
        'lat' : geo.get('Latitude', ''),
        'lon' : geo.get('Longitude', ''),
        
        # Address specific info
        'bbl' : geo.get('BOROUGH BLOCK LOT (BBL)', {})\
                    .get('BOROUGH BLOCK LOT (BBL)', ''),
        'house_number' : geo.get('House Number - Display Format', ''),
        'street_name' : geo.get('First Street Name Normalized', ''),
        'vacant_lot': geo.get('Vacant Lot Flag', ''),
        'boro_name' : geo.get('First Borough Name', ''),
        'bin': geo.get('Building Identification Number (BIN) of Input Address or NAP', ''), 

        # Diagnostics info
        'GRC' : geo.get('Geosupport Return Code (GRC)', ''),
        'msg' : geo.get('Message', 'msg err'),
        'GRC2' : geo.get('Geosupport Return Code 2 (GRC 2)', ''),
        'msg2' : geo.get('Message 2', 'msg2 err')
        }

    return {'status': 'success',
            'output': {'uid': uid,
                        **output}
            }