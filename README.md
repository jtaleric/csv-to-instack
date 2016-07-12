# csv-to-instack
Convert a CSV of your Overcloud nodes into the instackenv.json format.

## Usage
```
python csv-to-instack.py --csv=target-csv-file
```

## Example CSV
Always provide the header row. The code ignores the first row, since it assumes it is the header

```
macaddress,ipmi url,ipmi user,ipmi password,ipmi tool
d4:be:d9:b3:8f:0d,compute001-drac.redhat.com,root,calvin,pxe_ipmitool
d4:be:d9:b3:8f:10,compute002-drac.redhat.com,root,calvin,pxe_ipmitool
d4:be:d9:b3:8f:11,compute003-drac.redhat.com,root,calvin,pxe_ipmitool
```

**macaddress** - Mac Address of NIC that will PXE.

**ipmi url** - URL to the drac/ilo/etc.

**ipmi user** - Username to login to the drac/ilo/etc.

**ipmi password** - Password to login to the drac/ilo/etc.

**ipmi tool** - Which tool to use, when in doubt, use pxe_ipmitool.

## Example output
```
{
    "nodes": [
        {
            "arch": "x86_64", 
            "cpu": "2", 
            "disk": "20", 
            "mac": [
                "d4:be:d9:b3:8f:0d"
            ], 
            "memory": "1024", 
            "pm_addr": "compute001-drac.redhat.com", 
            "pm_password": "calvin", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "root"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "2", 
            "disk": "20", 
            "mac": [
                "d4:be:d9:b3:8f:10"
            ], 
            "memory": "1024", 
            "pm_addr": "compute002-drac.redhat.com", 
            "pm_password": "calvin", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "root"
        }, 
        {
            "arch": "x86_64", 
            "cpu": "2", 
            "disk": "20", 
            "mac": [
                "d4:be:d9:b3:8f:11"
            ], 
            "memory": "1024", 
            "pm_addr": "compute003-drac.redhat.com", 
            "pm_password": "calvin", 
            "pm_type": "pxe_ipmitool", 
            "pm_user": "root"
        }
    ]
}
```
