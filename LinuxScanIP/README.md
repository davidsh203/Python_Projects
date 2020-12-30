# LinuxScanIP
## Scan your used ip addresses of your organization 

* This tool build to display all used ip addresses in your home or your organization
* The tool find inet and netmask address and send ping to all of ip's and print them if there are used
* All of used ip's will be written in log text file

## Required

* Linux OS (tried in ubuntu 20.04)
* Net-tools installed for "ifconfig" command

## Code Explanation

### Imports
* colorama - Print colorised text in terminal
* os - To run OS command 

### Get Inet Line
Run "ifconfig" command to find the line that inlcudes inet and netmask address  
Function Definition:
```python
def get_inet_line():
```

### Get Inet Address

Use `get_inet_line()` function to search inet address between the word `inet` and `netmask`  
Function Definition:
```python
def get_inet_address():
```
return inet address (for example `10.0.0.1`)

### Get Netmask Address
Use `get_inet_line()` function to search netmask address between the word `netmask` and `broadcast`  
Function Definition:
```python
def get_netmask_address():
```
return netmask address (for example `255.255.255.0`)

### Ping Address
Check ping result for ip address (`ip` parameter)  
Function Definition:
```python
def ping_address(ip):
```
return `True` or `False` depending on the result

### Short Inet Address
To ping for all ip addresses we need to know how octets be changed depending on the netmask address  
We need to change inet address in order to remove not relevant octets and add other octets

`inet` - represents original inet address  
`numToShort` - represents the number of octets to remove from the end of the original inet address
```python
def short_inet(inet, numToShort):
```
return relevant inet

## Created by

* [Tzahibhm](https://github.com/tzahibhm )
* [Davidsh203](https://github.com/davidsh203 )