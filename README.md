# tenable-ot-it-assets
```
*** This tool is not an officially supported Tenable project ***

Generates a consolidated asset list for IT and OT information
when using Nessus and tenable.ot linked back to tenable.sc.
Tenable.sc stores asset data in a variety of plugins. This queries
all the plugins and produces a single line output per asset.

Generates a csv, json and html output

run with

python3 assets_to_csv.py
python3 gen_html_reports.py

Connectivity to tenable.sc is controlled in the assets_to_csv.py file by the
following line. Adjust accordingly

keys_file="../sc_keys.json"

format for sc_keys.json is

{"server":"your_sc_server_ip","user":"your_user_name","password":"your_password"}

```
