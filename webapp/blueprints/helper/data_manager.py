from neo4j import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://hobby-jemomenbpiokgbkeepnkiodl.dbs.graphenedb.com:24787", auth=basic_auth("magicspanarchian", "b.DJuNReIhBxtM.LebI9GHhqFV6o47e"))


def print_friends_of(tx, name):
    for record in tx.run("MATCH (a:Person)-[:KNOWS]->(f) "\
                         "WHERE a.name = {name} "\
                         "RETURN f.name", name=name):
        print("record : "+record["f.name"])

with driver.session() as session:
    session.read_transaction(print_friends_of, "Alice")