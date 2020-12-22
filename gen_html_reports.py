import requests
import json
import sys
import time
import csv
from datetime import datetime, timedelta

input_dir="../"
results_dir="../results/"
output_dir="../reports/"


f=open(output_dir+"asset_report.html","w+")

html_header='<html>\n'\
		'<head>\n'\
		'<title>Tenable Report</title>\n'\
		'<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />\n'\
		'<meta http-equiv="Pragma" content="no-cache" /><meta http-equiv="Expires" content="0" />\n'

f.write(html_header)
f2=open("style.css","r")
for line in f2:
	f.write(line)
f2.close()
'''
f.write('<script>\n')
f2=open("Chart.min.js","r")
for line in f2:
	f.write(line)
f2.close()


f.write('</script>\n')
'''

# get asset list
f2=open(results_dir+"results.json","r")
asset_list=json.load(f2)
f2.close()
asset_list.sort(key=lambda x: (x.get('repo_name'),int(x.get('crit'))+int(x.get('high')),x.get('ip')), reverse=True)
#print(asset_list)

f.write('</head>\n<body>\n')

f.write('<div class=page_heading>\n')
f.write('<h1>IT/OT Asset Report</h1>')
f.write('</div>')
f.write('<table width=100%></table>')



#
# repo summary
#
f.write('<div class=bar_chart_fl>\n')
repo_summary={}
count=1
for x in asset_list:
	repo_name=x["repo_name"]
	if repo_name in repo_summary:
		count=count+1
		repo_summary.update({repo_name:count})
	else:
		count=1
		repo_summary.update({repo_name:count})
print(repo_summary)
print(len(asset_list))
f.write('<table class=table1 width=250px>')
f.write('<tr><th>Repo</th><th>Asset Count</th>')
count=0
for k,v in repo_summary.items():
	count=count+v
	f.write('<tr>')
	f.write('<td>')
	f.write(k)
	f.write('</td>')
	f.write('<td align=center>')
	f.write(str(v))
	f.write('</td>')
f.write('<tr>')
f.write('<td>Total</td><td align=center>')
f.write(str(count))
f.write('</td>')
f.write('</table>')
f.write('</div>')

f.write('<table width=100%></table>')

#
# Search bar
#
f.write('<div class=bar_chart_fl>\n')
f.write('<p>\n')
f.write('<input type="text" id="search_field" onkeyup="myFunction()" placeholder="Search.." title="Type in a name">')
f.write('</p>\n')
f.write('</div>')

f.write('<table width=100%></table>')

#
# Asset Info
#
f.write('<div class=bar_chart_fl>\n')
f.write('<table class=table1 id=search_table>')
f.write('<tr>')
f.write('<th>IP / Agent ID / Mac Address</th>')
f.write('<th>Name / OS</th>')
f.write('<th>Vulnerabilities</th>')
f.write('<th>Vendor / Family / Firmware</th>')
f.write('<th>Type</th>')
f.write('<th>Repo</th>')
for x in asset_list:
	f.write('<tr>')
	f.write('<td class=hideme valign=top>')
	f.write(str(x["ip"])+"<br>")
	f.write(str(x["uuid"])+"<br>")
	f.write(str(x["mac"])+"<br>")
	f.write(str(x["name"])+"<br>")
	f.write(str(x["os"]))
	f.write(str(x["vendor"])+"<br>")
	f.write(str(x["family"])+"<br>")
	f.write(str(x["firmware"]))
	f.write(str(x["repo_name"]))
	f.write(str(x["type"]))
	f.write('</td>')
	f.write('<td valign=top width=300px>')
	f.write(str(x["ip"])+"<br>")
	f.write(str(x["uuid"])+"<br>")
	f.write(str(x["mac"])+"<br>")
	f.write('</td>')
	f.write('<td align=center valign=top width=500px>')
	f.write(str(x["name"])+"<br>")
	f.write(str(x["os"]))
	f.write('</td>')
	f.write('<td valign=top align=left width=80px>')
	if x["crit"]!="0":
		f.write("<div class=critical>"+str(x["crit"])+"</div>")
	if x["high"]!="0":
		f.write("<div class=high>"+str(x["high"])+"</div>")
	if x["med"]!="0":
		f.write("<div class=medium>"+str(x["med"])+"</div>")
	if x["low"]!="0":
		f.write("<div class=low>"+str(x["low"])+"</div>")
	f.write('</td>')
	f.write('<td align=center valign=top width=200px>')
	f.write(str(x["vendor"])+"<br>")
	f.write(str(x["family"])+"<br>")
	f.write(str(x["firmware"]))
	f.write('</td>')
	f.write('<td valign=top align=center>')
	f.write(str(x["type"]))
	f.write('</td>')
	f.write('<td valign=top align=center>')
	f.write(str(x["repo_name"]))
	f.write('</td>')
f.write('</table>')
f.write('</div>')

fscript=open("search_script.txt","r")
for x in fscript:
	f.write(x)

f.write("</html>")

f.close()
