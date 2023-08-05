<h2 align="center">
  <a href="https://reolink.com"><img src="https://raw.githubusercontent.com/JimStar/reolink_ip/master/logo.png" width="200"></a>
  <br>
  <i>Reolink IP NVR/cameras API package</i>
  <br>
</h2>

<p align="center">
  <a href="https://pypi.org/project/reolink-ip"><img src="https://img.shields.io/pypi/dm/reolink-ip"></a>
  <img src="https://img.shields.io/github/v/release/JimStar/reolink_ip?display_name=tag&include_prereleases&sort=semver" alt="Current version">
</p>

The `reolink_ip` Python package allows you to integrate your [Reolink](https://www.reolink.com/) devices (NVR/cameras) in your application.

### Description

This is a package implementing Reolink IP NVR and camera API. Also it’s providing a way to subscribe to Reolink ONVIF SWN events, so that real-time events can be received on a webhook.

### Prerequisites

- Python 3.9

### Installation

```
pip3 install reolink-ip
```

or manually:
````
git clone https://github.com/JimStar/reolink_ip
cd reolink_ip/
pip3 install .
````

### Usage

````
# Create a host-object (representing either a camera, or NVR with several channels)
host = api.Host('192.168.1.10', 80, 'user', 'mypassword')

# Obtain/cache NVR or camera settings and capabilities, like model name, ports, HDD size, etc:
await host.get_host_data()

# Get the subscribtion port and host-device name:
subscribtion_port =  host.onvif_port
name = host.nvr_name

# Obtain/cache states of features:
await host.get_states()

# Print some state value on the channel with index 0:
print(host.ir_enabled(0))

# Enable the infrared lights on the channel with index 1:
await host.set_ir_lights(1, True)

# Enable the spotlight on the channel with index 1:
await host.set_spotlight(1, True)

# Enable the siren on the channel with index 0:
await host.set_siren(0, True)

# Now subscribe to events, suppose our webhook url is http://192.168.1.11/webhook123
await host.subscribe('http://192.168.1.11/webhook123')

# After some minutes check the renew timer (keep the eventing alive):
if (host.renewTimer <= 100):
    await host.renew()

# Logout and disconnect
await host.disconnect()
````

### Example

This is an example of the usage of the API. In this case we want to retrive and print the Mac Address of the NVR.
````
from reolink_ip.api import Host
import asyncio

async def print_mac_address():
    # initialize the host
    host = Host('192.168.1.109', 80, 'admin', 'admin1234')
    # connect and obtain/cache device settings and capabilities
    await host.get_host_data()
    # check if it is a camera or an NVR
    print("It is an NVR: %s, number of channels: %s", host.is_nvr, host.num_channels)
    # print mac address
    print(host.mac_address)
    # close the device connection
    await host.logout()

if __name__ == "__main__":
    asyncio.run(print_mac_address())
````
