import bluetooth
from bluetooth.ble import DiscoveryService
def list_devices():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    print("searching Devices Bluetooth")
    print("found %d devices" % len(nearby_devices))
    for addr, name in nearby_devices:
        print("  %s - %s" % (addr, name))

def list_devices_ble():
    service = DiscoveryService()
    devices = service.discover(2)

    for address, name in devices.items():
        print("searching devices BLE")
        print("name: {}, address: {}".format(name, address))

if __name__=="__main__":
    list_devices()
    list_devices_ble()
