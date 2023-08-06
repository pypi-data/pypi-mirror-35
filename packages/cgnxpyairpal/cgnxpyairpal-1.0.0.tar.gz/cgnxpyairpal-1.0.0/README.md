# cgnxpyairpal
Python Client/SDK for Airpal

## Synopsis

cgnxpyairpal: Python Client/SDK to allow headless queries and response retrieval for Airpal.

## Code Example

View the included example.py

## Motivation

Airpal (http://airbnb.io/airpal/) is a great WebUI/Front end for PrestoDB (https://prestodb.io/)

One really nice thing Airpal does is create a method of User Access Control/logging/etc to the PrestoDB interface.

Native PrestoDB clients will likely be more efficient, but this stack allows organizations to provide batch/scripting 
access to the PrestoDB Via Airpal, while maintaining the nice UAC/etc that Airpal provides.

## Requirements

* Working Airpal server
* Python modules:
    * Requests - http://docs.python-requests.org/en/master/
    * SSEClient - https://pypi.python.org/pypi/sseclient
    * Pandas (for example script only) - http://pandas.pydata.org/

## License

MIT

## Version
Version | Changes
------- | --------
**1.0.0**| Initial Release
