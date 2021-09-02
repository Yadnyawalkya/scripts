# This script will pull upstream repository names, compare w/ downstream srpm
# list, and gives out the match!
# Prerequisite: Generate product srpm list and provide it as input file
# (This is only possible when the product release team uses the exact upstream
# repo name in downstream srpm. For example: in Red Hat Satellite,
# foreman_discovery is an upstream repo name that is packaged as
# tfm-rubygem-foreman_discovery in downstream Satellite, so it surely works!)

import re, requests

api_data = []
org_list = ["theforeman", "pulp", "Katello", "candlepin"]
downstream_srpm_list = []
downstream_component_list = []
upstream_repo_list = []

downstream_dict = {}
upstream_dict = {}

for org in org_list:
    for page in range(1, 4):
        # GH API per_page limit is max 100
        _json_data = requests.get(
            "https://api.github.com/orgs/{0}/repos?page={1}&per_page=100".format(
                org, page
            )
        ).json()
        api_data.append(_json_data)

try:
    for dataset in api_data:
        for el in dataset:
            upstream_without_dash = el["name"].replace("-", "").replace("_", "")
            upstream_dict[upstream_without_dash] = el["name"]
            upstream_repo_list.append(el["name"])
except TypeError:
    print(
        "IP got blocked due to GH rare limiting, need to wait for 1h or use token-based auth instead!"
    )

file = open("product_srpmlist.txt")
for srpm in file.read().split("\n"):
    _srpm_name = re.split(r"\-\d.*", srpm)[0]
    downstream_srpm_list.append(_srpm_name)
    _without_dash = _srpm_name.replace("-", "").replace("_", "")
    downstream_dict[_without_dash] = _srpm_name

for upstream_repo_name in upstream_dict.keys():
    for downstream_srpm_name in downstream_dict.keys():
        if upstream_repo_name in downstream_srpm_name:
            downstream_component_list.append(downstream_dict[downstream_srpm_name])

print(len(downstream_component_list))
print(sorted(set(downstream_component_list)))
