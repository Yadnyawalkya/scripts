### Script to cleanup old OpenStack instances

#### Warning
Handle with care, this can delete your instances if not properly configured!

#### Prerequisite
* Make sure you gedited hard-coded `text_pattern` from the script (search for `# edit text_pattern`).
* You should have `clouds.yaml` file in the same dir as `cleanup-vms.py` for seemless authentiation.
```
.
├── cleanup-vms.py
├── clouds.yaml
└── README.md
```

To download `clouds.yaml` file from OpenStack Platform web portal, navigate to `Project > API Access` and search for `Download clouds.yaml File` button. Anyway, sample file is provided with the script.

#### Usage:

```
$ python cleanup-vms.py --list
+---------------------------------+---------+
|             VM Name             |   Age   |
+---------------------------------+---------+
|               vm1               |   8.0   |
|               vm2               |   25.0  |
|    ytale-adsaea12asd-cleanup3   |   38.0  |
|    ytale-adsaea12asd-cleanup1   |   39.0  |
|               vm3               |  376.0  |
|        ytale-24x7-fedora        | 11398.0 |
|               vm4               | 13168.0 |
+---------------------------------+---------+

$ python cleanup-vms.py --max-hours 40 --list
+----------------------------+---------------------+
|          VM Name           | Age (Less than 40h) |
+----------------------------+---------------------+
|             vm1            |         8.0         |
|             vm2            |         25.0        |
| ytale-adsaea12asd-cleanup3 |         38.0        |
| ytale-adsaea12asd-cleanup1 |         39.0        |
+----------------------------+---------------------+

$ python cleanup-vms.py --max-hours 40 --dryrun
+----------------------------+---------------------+
|          VM Name           | Age (Less than 40h) |
+----------------------------+---------------------+
| ytale-adsaea12asd-cleanup3 |         38.0        |
| ytale-adsaea12asd-cleanup1 |         38.0        |
+----------------------------+---------------------+

$ python cleanup-vms.py --max-hours 40 --cleanup
VM deleted => ytale-adsaea12asd-cleanup3
VM deleted => ytale-adsaea12asd-cleanup1
```
