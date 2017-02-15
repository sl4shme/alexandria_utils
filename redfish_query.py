import sys
import redfish
import datetime

def log(text):
    with open(sys.argv[4], 'a') as f:
        f.write(str(text) + "\n\n")

url = "https://{}/rest/v1/".format(sys.argv[1])
login = sys.argv[2]
password = sys.argv[3]

with open(sys.argv[4], 'w') as f:
    f.write("Querying: " + url + " - " + login + " - " + password + "\n")
    f.write(str(datetime.datetime.now()) + "\n")

try:
    remote_mgmt = redfish.connect(url, login, password, verify_cert=False, enforceSSL=False)
except Exception as e:
    log(e)
    raise

log("Redfish API version: {}".format(remote_mgmt.get_api_version()))


chassises = remote_mgmt.Chassis
for chassis in chassises.chassis_dict.items():
    log("Data for Chassis {}".format(chassis[0]))
    log(chassis[1].data)

systems = remote_mgmt.Systems.systems_dict.values()
for i, system in enumerate(systems):
    log("Data for system number {}".format(i))
    log(system.data)
    interfaces = system.ethernet_interfaces_collection
    if interfaces is not None:
        for j, interface in enumerate(interfaces.ethernet_interfaces_dict.values()):
            log("Data for system {} interface number {}".format(i, j))
            log(interface.data)
    else:
        log("No interfaces for system {}".format(i))

