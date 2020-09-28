#CSV Comma Separate Values
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

#Reading and writing csv files with Dictionaries
with open("software.csv") as software:
    reader = csv.DictReader(software)
    for row in reader:
        print("{} has the role of: {}".format(row["Name"],row["Role"]))
        print(row["Phone"])

users = [{"name": "Sol Mansi", "username": "solm", "department": "IT infrasctructure"},
    {"name": "Lio Nelson", "username": "lion", "department": "User Experience Research"},
    {"name": "Charlie Grey", "username": "greyc", "department": "Development"}]
keys=["name", "username", "department"]

with open("by_deparment.csv", "w") as by_deparment:
    writer = csv.DictWriter(by_deparment, fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)

#Final Test
#!/usr/bin/env python3
#"/home/student-02-939e70601012/data/employees.csv"
import csv
def read_employees(csv_file_location):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(csv_file_location), dialect = 'empDialect')
    employee_list = []
    for data in employee_file:
        employee_list.append(data)
    return employee_list

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data


def write_report(dictionary, report_file):
      with open(report_file, "w+") as f:
        for k in sorted(dictionary):
             f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close()


#Test
employee_list = read_employees("/home/student-02-939e70601012/data/employees.csv")
dictionary = process_data(employee_list)
report = "/home/student-02-939e70601012/test_report.txt"
write_report(dictionary, report)

#CSV info
Full Name, Username, Department
Audrey Miller, audrey, Development
Arden Garcia, ardeng, Sales
Bailey Thomas, baileyt, Human Resources
Blake Sousa, sousa, IT infrastructure
Cameron Nguyen, nguyen, Marketing
Charlie Grey, greyc, Development
Chris Black, chrisb, User Experience Research
Courtney Silva, silva, IT infrastructure
Darcy Johnsonn, darcy, IT infrastructure
Elliot Lamb, elliotl, Development
Emery Halls, halls, Sales
Flynn McMillan, flynn, Marketing
Harley Klose, harley, Human Resources
Jean May Coy, jeanm, Vendor operations
Kay Stevens, kstev, Sales
Lio Nelson, lion, User Experience Research
Logan Tillas, tillas, Vendor operations
Micah Lopes, micah, Development
Sol Mansi, solm, IT infrastructure
