import database_manager as dm


db_path = "../longley.db"  # Replace with your actual database path
conn =dm.create_connection(db_path)

if conn:
    rows = dm.select_all(conn)
    dm.print_rows(rows)
    dm.close_connection(conn)