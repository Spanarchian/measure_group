
from neo4j.v1 import GraphDatabase, basic_auth
driver = GraphDatabase.driver("bolt://hobby-jemomenbpiokgbkeepnkiodl.dbs.graphenedb.com:24787", auth=basic_auth("magicspanarchian", "b.DJuNReIhBxtM.LebI9GHhqFV6o47e"))


def get_gdb():
    return driver
