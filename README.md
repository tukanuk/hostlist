# hostList Readme

Uses the Dynatrace API to build a list of host files that are being monitored.

Outputs to `host_logs[datetime].csv` and `process_group_logs[datetime].csv`


## Usage

`usage: hostlist.py [-h] [-q] url token`

Get a list of hosts

```positional arguments:
  url                  tennant url with format
                       https://[tennant_key].live.dynatrace.com
  token                Your API Token generated with Access

optional arguments:
  -h, --help           show this help message and exit
  -q, --quiet          no output printed to terminal
```