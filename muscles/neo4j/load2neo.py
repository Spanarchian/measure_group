# from gdb import get_gdb as session

from neo4j import GraphDatabase, basic_auth
# driver = GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", "changeme"))
driver = GraphDatabase.driver(
    "bolt://54.236.224.67:32859", 
    auth=basic_auth("neo4j", "board-ports-specification"))
session = driver.session()


# Insert data
insert_query = '''
UNWIND {pairs} as pair
MERGE (p1:Person {name:pair[0]})
MERGE (p2:Person {name:pair[1]})
MERGE (p1)-[:KNOWS]-(p2);
'''

data = [["Jim","Mike"],["Jim","Billy"],["Anna","Jim"],
          ["Anna","Mike"],["Sally","Anna"],["Joe","Sally"],
          ["Joe","Bob"],["Bob","Sally"]]

session.run(insert_query, parameters={"pairs": data})

# Friends of a friend
foaf_query = '''
MATCH (person:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf) 
WHERE person.name = {name} AND NOT (person)-[:KNOWS]-(foaf)
RETURN foaf.name AS name
'''

results = session.run(foaf_query, parameters={"name": "Jim"})
for record in results:
    print(f"Connecting paths: \n  {record['name']}")


# Common friends
common_friends_query = """
MATCH (user:Person)-[:KNOWS]-(friend)-[:KNOWS]-(foaf:Person)
WHERE user.name = {user} AND foaf.name = {foaf}
RETURN friend.name AS friend
"""

results = session.run(common_friends_query, parameters={"user": "Joe", "foaf": "Sally"})
for record in results:
    print(f"Connecting paths: \n  {record['friend']}")

# Connecting paths
connecting_paths_query = """
MATCH path = shortestPath((p1:Person)-[:KNOWS*..6]-(p2:Person))
WHERE p1.name = {name1} AND p2.name = {name2}
RETURN path
"""

results = session.run(connecting_paths_query, parameters={"name1": "Bob", "name2": "Billy"})
for record in results:
    print (f"Connecting paths: \n  {record['path']}")

session.close()
