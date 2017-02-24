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
    remote_mgmt = redfish.connect(
        url, login, password, verify_cert=False, enforceSSL=False)
except Exception as e:
    log(e)
    raise

log("Redfish API version: {}".format(remote_mgmt.get_api_version()))

chassises = remote_mgmt.Chassis
for chassis in chassises.chassis_dict.items():
    log("Data for Chassis {}".format(chassis[0]))
    log(chassis[1].data)

    try:
        power = chassis[1].power
    except:
        power = None
    if power is not None:
        log("Power data for Chassis {}".format(chassis[0]))
        log(power.data)
    else:
        log("No power data for chassis {}".format(chassis[0]))

    try:
        thermal = chassis[1].thermal
    except:
        thermal = None
    if thermal is not None:
        log("Thermal data for Chassis {}".format(chassis[0]))
        log(thermal.data)
    else:
        log("No thermal data for chassis {}".format(chassis[0]))

systems = remote_mgmt.Systems.systems_dict.items()
for system in systems:
    log("Data for system {}".format(system[0]))
    log(system[1].data)

    interfaces = system[1].ethernet_interfaces_collection
    if interfaces is not None:
        for interface in interfaces.ethernet_interfaces_dict.items():
            log("Data for system {} interface {}".format(system[0],
                                                         interface[0]))
            log(interface[1].data)
    else:
        log("No interface for system {}".format(system[0]))

    processors = system[1].processors_collection
    if processors is not None:
        for processor in processors.processors_dict.items():
            log("Data for system {} processor {}".format(system[0],
                                                         processor[0]))
            log(processor[1].data)
    else:
        log("No processor for system {}".format(system[0]))

    storages = system[1].simple_storage_collection
    if storages is not None:
        for storage in storages.simple_storage_dict.items():
            log("Data for system {} storage {}".format(system[0], storage[0]))
            log(storage[1].data)
    else:
        log("No storage for system {}".format(system[0]))
