from pkg_resources import resource_filename
import json

with open(resource_filename(__name__, '1.json')) as f:
    mccs1 = json.loads(f.read())

with open(resource_filename(__name__, '2.json')) as f:
    mccs2 = json.loads(f.read())

for mcc1 in mccs1:
   for mcc2 in mccs2:
        if mcc1['mcc'] == mcc2['mcc'] and mcc1['mnc'] == mcc2['mnc']:
            mcc1.update(country_code = int(mcc2['country_code']), iso = mcc2['iso'])

mccs = mccs1

with open(resource_filename(__name__, 'merged.json'), 'w') as f:
    f.write(json.dumps(mccs))

print(len(list(filter(lambda x: x['active'] is True, mccs))))
