from web_game.main.sql_processing import DatabaseConnection

db = DatabaseConnection()


def add_a_cnt(cnt_name: str, capital_name: str, description: str):
    request = """INSERT INTO Countries_list (CountryName, CapitalCity , Description )
                 VALUES (?, ?, ?);"""
    db.execute_request(request, (cnt_name.lower(), capital_name.lower(), description.lower(),))


def delete_cnt(cnt_id: int):
    request = """DELETE FROM Countries_list WHERE OperationID = ?;"""
    db.execute_request(request, (cnt_id,))


def get_cnt_for_table():
    result = db.execute_request("""SELECT * FROM Countries_list;""")
    return result


print(get_cnt_for_table())

