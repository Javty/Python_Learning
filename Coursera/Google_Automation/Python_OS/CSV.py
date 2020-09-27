#CSV Comma Separete Values
#Read CSV files
import csv
f = open("csv_file.txt")
f_csv = csv.reader(f)
for row in f_csv:
    name, phone, role = row
    print("Name: {}, Phone: {}, Role: {}".format(name,phone,role))
f.close()

#Write CSV files

hosts = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
with open("hosts.csv", "w") as hosts_csv:
    writer = csv.writer(hosts_csv)
    writer.writerows(hosts)
