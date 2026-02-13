import mysql.connector

host = "localhost"
user = "root"
password = "Anshu@123"
database = "feb_2026"
try:
    conn = mysql.connector.connect(
        host=host, user=user, password=password, database=database
    )
    cursor = conn.cursor()
    print("connected to the database successfully")

    # inserting into the table

    query1 = "INSERT INTO `feb_2026`.`employee` (`Emp_id`, `Emp_Name`, `Salary`) VALUES (%s,%s,%s)"

    values = (105, "anunay", 5000)
    cursor.execute(query1, values)
    conn.commit()
    print("record inserted successfully")

    #  printing values after inserting

    query2 = "Select * from employee"
    cursor.execute(query2)
    result = cursor.fetchall()
    for row in result:
        print(row)

except mysql.connector.Error as err:
    print("Error:", err)