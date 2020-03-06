from neo4j import GraphDatabase

# uri = "bolt://localhost:7687"
# driver = GraphDatabase.driver(uri, auth=("neo4j", "password"))
driver = GraphDatabase.driver("bolt://hobby-jemomenbpiokgbkeepnkiodl.dbs.graphenedb.com:24787", auth=("magicspanarchian", "b.DJuNReIhBxtM.LebI9GHhqFV6o47e"))


def print_friends_of(tx, name):
    print(f"Hi just landed in print_friends_of")
    for record in tx.run("MATCH (a:CELL)-[:CURRENT_STATE]->(:RURAL)  RETURN a.cell_ref"):  
        print(f"Hi just leaving in print_friends_of")
        print(record["a.cell_ref"])

with driver.session() as session:
    session.read_transaction(print_friends_of, "Alice")
