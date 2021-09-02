# vm-id-finder.py

### What this script does?
It takes VM name from `input.csv`, finds it's vm_id and return both in valid `output.csv` file. 
This `output.csv` can be then directly used to prepare v2v-migration-plan. 

[![asciicast](https://asciinema.org/a/NFflf1RDMVFbyYHi5sqaoDyxu.png)](https://asciinema.org/a/NFflf1RDMVFbyYHi5sqaoDyxu)

### Prerequisite:
1. VM names in `input.csv` file
2. ManageIQ appliance URL/IP address
3. Provider name

### Sample `input.csv` file
```
➜ ytale@manageiq$ cat migration.csv                 
v2v-dnd-ytale-window1, abc, 11
v2v-dnd-ytale-fedora1, xyz, 22
vm_not_exist1, provider1, 33
vm_not_exist2, provider2, 44
```
(Note: Only `VM name` field column is required; other fields are optional!)

### Usage
```
python vm-id-finder.py -u appliance-url -c username:password -p vcenter-provider -i input-file
```
(Caution: Script overwrites output in `output.csv` if you have not specified file via `-o` option.)

### Examples
Common usage
```
python vm-id-finder.py -u https://10.111.10.111/ -c admin:smartvm -p vsphere65-nested -i input.csv -o output.csv
```

Use default `user/pass` (`admin/smartvm`) via `-d` option
```
python vm-id-finder.py -u https://10.111.10.111/ -d -p vsphere65-nested -i input.csv
```

### Thanks
ManageIQ API team for crystal clear documentation! ;)

### Todo
Dynamic provider selection

(Improvements are more than welcome!)
