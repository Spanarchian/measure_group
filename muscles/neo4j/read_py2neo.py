
from py2neo import Graph
grapher = Graph("bolt://localhost:7687", auth=("neo4j", "changeme"))

x = grapher.run("MATCH (a :Person) RETURN a.name, a.city, a.age").to_data_frame()
print(f"To_data_frame() :\n{x}")
