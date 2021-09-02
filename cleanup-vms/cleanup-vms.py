import argparse
import datetime
import dateutil.parser as dt
import openstack
import pytz

from prettytable import PrettyTable


def parse_cmd_line():
    parser = argparse.ArgumentParser(argument_default=None)
    parser.add_argument(
        "--list",
        dest="list",
        action="store_false",
        default=True,
        help="List VM name and age of all OpenStack instances",
    )
    parser.add_argument(
        "--max-hours",
        help="Option to provide Max hours since the VM was created",
    )
    parser.add_argument(
        "--dryrun",
        dest="dryrun",
        action="store_false",
        default=True,
        help="Run string match and max-hours on OpenStack instances and dryrun before actual cleanup",
    )
    parser.add_argument(
        "--cleanup",
        dest="cleanup",
        action="store_false",
        default=True,
        help="Cleanup VMs that are older max-hours and matches to the string criteria",
    )
    args = parser.parse_args()
    return args


def _connection():
    return openstack.connect(cloud="openstack")


def _get_vms_obj():
    obj = []
    conn = _connection()
    # openstack.enable_logging(debug=True) // enble logging
    try:
        for instance in conn.list_servers():
            obj.append(instance)
    except openstack.exceptions.ResourceNotFound as e:
        pass
    return obj


def _get_vms_age(creation_time):
    current_time = datetime.datetime.now(tz=pytz.UTC)
    vm_creation_time = dt.parse(creation_time)
    age_delta = (current_time - vm_creation_time).total_seconds() // 3600
    return age_delta


def _get_vms():
    vms_data = []
    instances = _get_vms_obj()
    try:
        for instance in instances:
            age_delta = _get_vms_age(instance.created_at)
            vms_data.append([instance.name, age_delta])
    except openstack.exceptions.ResourceNotFound as e:
        pass
    return vms_data


def list_all():
    table = PrettyTable()
    table.field_names = ["VM Name", "Age (Hours)"]
    vms_data = _get_vms()
    table.add_rows(vms_data)
    print(table)


def max_hours(max_hours):
    vms_data = []
    table = PrettyTable()
    table.field_names = ["VM Name", "Age (Less than {} (Hours)".format(max_hours)]
    for vms in _get_vms():
        # check if VM age is greater than maximum hours
        if vms[1] <= max_hours:
            vms_data.append(vms)
    table.add_rows(vms_data)
    print(table)


def cleanup_vms(text_pattern, max_hours, dryrun):
    delete_list = []
    table = PrettyTable()
    table.field_names = ["VM Name", "Age (Less than {} (Hours)".format(max_hours)]
    for vms in _get_vms():
        # check if VM age is greater than maximum hours
        if (text_pattern in vms[0]) and (vms[1] <= max_hours):
            delete_list.append([vms[0], vms[1]])
    if dryrun:
        table.add_rows(delete_list)
        print(table)
    else:
        for instance_data in delete_list:
            for instance_name in instance_data:
                for server in _get_vms_obj():
                    if server.name == instance_name:
                        if _connection().delete_server(server.name):
                            print(
                                "VM deleted sucessfully => {}".format(
                                    server.name
                                )
                            )
                        else:
                            print(
                                "VM deletion failed => {}".format(server.name)
                            )


if __name__ == "__main__":
    args = parse_cmd_line()
    if (not args.list) and (not args.max_hours):
        list_all()
    if args.max_hours:
        if not args.cleanup:
            cleanup_vms(
                text_pattern="adsaea12asd", # edit text_pattern
                max_hours=int(args.max_hours),
                dryrun=False,
            )
        elif not args.list:
            max_hours(int(args.max_hours))
        elif not args.dryrun:
            cleanup_vms(
                text_pattern="adsaea12asd", # edit text_pattern
                max_hours=int(args.max_hours),
                dryrun=True,
            )
        else:
            print("Error: You have to specify --list with max-hours option!")
    if (not args.cleanup) and (not args.max_hours) and (args.list):
        print("Error: You have to specify --max-hours with cleanup option!")
