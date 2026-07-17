from database import Database


def main():

    db = Database()

    db.create_tables()

    print("================================")
    print("AI Investment Assistant")
    print("数据库初始化成功")
    print("================================")

    db.close()


if __name__ == "__main__":
    main()
