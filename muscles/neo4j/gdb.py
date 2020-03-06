from neo4j import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "changeme"))

from py2neo import Graph
grapher = Graph("bolt://localhost:7687", auth=("neo4j", "changeme"))


def get_gdb():
    session = driver.session()
    return session

# resp = get_gdb()
# print (f"Resp = {resp}")


# x = grapher.run("MATCH (a:CELL) RETURN a.cell_ref, a.rural").to_data_frame()
# print(f"To_data_frame() :\n{x}")
