import argparse
import csv
import json
import requests

# useful arguments
ap = argparse.ArgumentParser(description="Tool arguments")
ap.add_argument("-u", "--url", required=True, help="Use ManageIQ hostname")
ap.add_argument("-i", "--input", required=True, help="Use .csv file or path as input")
ap.add_argument("-o", "--output", help="Use .csv file or path as output")
ap.add_argument("-c", "--cred", help="Specify credentials username:password")
ap.add_argument("-d", "--default", help="Use default admin/smartvm credentials", action="store_true")
ap.add_argument("-p", "--provider", required=True, help="Use your vCenter provider name")
args = vars(ap.parse_args())


# output handling
output = "output.csv"
if args["output"] is not None:
    output = args["output"]

# removes slash from url
if args["url"].endswith("/"):
    args["url"] = args["url"][:-1]

# auth check
if args["default"] is True:
    auth = ("admin", "smartvm")
else:
    if args["cred"] is not None:
        auth = (tuple(args["cred"].split(":")))

url = args["url"] + "/api/vms/?expand=resources&attributes=name"
headers = {"Accept": "application/json"}
response = requests.get(url, headers=headers, verify=False, auth=auth)

# receives vm_names and ids
data = json.loads(response.text)

error = []
di = {}
new_csv = ""
print "-----------------------------------------------------------------"
for i in range(0, len(data["resources"]) - 1):
    di.update({data["resources"][i]["name"]: int(data["resources"][i]["id"])})

with open(args["input"]) as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] in di:
            print "{0}, {1}, {2}".format(di[row[0]], args["provider"], row[0])
            new_csv = new_csv + "{0}, {1}, {2}\n".format(row[0], args["provider"], di[row[0]])
        else:
            error.append(row[0])
    f = open(output, "w")
    f.write(new_csv)
    f.close()

# error reporting
print "-----------------------------------------------------------------"
print "Following VMs not exists on '{0}' " \
      "please check them manually!\n{1}".format(args["provider"], error)
print "-----------------------------------------------------------------"

