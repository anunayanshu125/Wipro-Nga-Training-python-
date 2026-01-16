import csv
with open("student.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Name","Age","Gender"])
    writer.writerow(["Rose",23,'female'])
    writer.writerow(["Bob",22,'male'])
    writer.writerow(["Jim",23,'male'])
    writer.writerow(['Mary',21,'female'])