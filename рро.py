import mysql.connector

conn = mysql.connector.connect(user="root", password="pass", host="127.0.0.1", database="vagina")
cursor = conn.cursor(buffered=True)
# name  = input("Enter your name")
# cursor.execute("Select *from vagina")
# rows = cursor.fetchall()
# for j in rows:
#     if name == j[0]:
#         print(name)
#         print(j)

name1 = input("Enter your name: ")
surname = input("Enter your surname: ")
ages = int(input("Enter your ages: "))
person_new = ("INSERT INTO vagina(first_name, surname, age) values (%(first_name)s, %(second_name)s, %(age)s )")
data_person = {
    'first_name': name1,
    'second_name': surname,
    'age': ages,
}
cursor.execute(person_new, data_person)

conn.commit()
