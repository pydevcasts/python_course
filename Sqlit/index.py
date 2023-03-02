import sqlite3

con = sqlite3.connect("sqlite.db")
# con.execute("""
# CREATE TABLE person (id, name, family, age);
# """)

# con.execute("""
# INSERT INTO person (id, name, family, age) VALUES (3, "siyamak", "abs", "20");
# """)
# con.commit()

result = con.execute("""
SELECT * FROM person WHERE id = 2;
""")

# for i in result:
#     print(i)
x = result.fetchall()
print(x)