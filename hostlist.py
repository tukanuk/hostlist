#!/usr/bin/env python3



import json
import requests
import csv
import argparse
import time


# Required API permissions
# Access problem and event feed, metrics, and topology 

# API docs
# GET all hosts >> https://www.dynatrace.com/support/help/shortlink/api-hosts-get-all

# see url on line 53 for specific tag filtering. Case sensitive!

def main():
    parser = argparse.ArgumentParser(description="Get a list of hosts")

    
    parser.add_argument("url", 
                        help="tennant url with format https://[tennant_key].live.dynatrace.com")
    parser.add_argument("token", type=str,
                        help="Your API Token generated with Access",)
    parser.add_argument("-q", "--quiet",
                        help="no output printed to terminal",
                        action="store_true")

    args = parser.parse_args()
    
    tennant = args.url

    api_token = args.token

    environment_id = ""
    
    #The time string #YEARMONTHDAY-Hours-Minutes-Seconds
    #making it at the start, so both files have same timestamp for sure. 
    timestr = time.strftime("%Y%m%d_%H%M%S")


    
    payload = {'Api-token': api_token}

    # if args.hosts:
    get_host_list(tennant=args.url, saas=True, quiet=args.quiet, payload=payload, timestr=timestr, environment_id=environment_id)    


def get_host_list(tennant, saas, quiet, payload, timestr, environment_id=""):

# set the host endpoint
    host_endpoint = tennant + "/api/v1/entity/infrastructure/hosts?tag=AllSQL&includeDetails=false"

    # make the host request

    response = requests.get(host_endpoint, params=payload)

    if response.status_code != 200:
        raise Exception('Error on GET /hosts/ code: {}'.format(response.status_code))


    # collect the hosts

    hosts = json.loads(response.text)
    host_list = []
    # host_list = hosts_response['']['entityId']
    if not quiet:

        print('`\nHosts')
        print("=====")

    # a list of hosts
    host_list = [host['entityId'] for host in hosts]
    host_list_norm = [host['displayName'] for host in hosts]

    # query the logs
    f_name = "host_list_" + timestr + ".csv"
    with open(f_name,'w', newline='') as csvfile:
        linewriter = csv.writer(csvfile, delimiter=',')
        linewriter.writerow(["Host"])
        # for host in host_list:
        for host in host_list_norm:
            if not quiet:
                print("\n{}".format(host))
            linewriter.writerow([host]) 

    print("\n", f_name, " Created")

if __name__ == "__main__":
    main()


    


