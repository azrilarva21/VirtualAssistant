import sqlite3


def main():
    db=sqlite3.connect("information.db")
    db.row_factory=sqlite3.Row
    db.execute("create table if not exists admin(name text,age int)")
    db.execute("insert into admin (name,age) values (? , ?)",("Hussein",26))
    db.execute("insert into admin (name,age) values (? , ?)",("Jena",1))
    db.commit()
    
    cursor=db.execute("select * from admin")
    for row in cursor:
        print("Name:{}, Age:{}".format(row["name"],row["age"]))


if __name__ == '__main__':main()