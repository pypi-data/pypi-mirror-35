import bson
import pymongo
import pytest
import flexmock

from sacredboard.app.data.datastorage import Cursor
from sacredboard.app.data.pymongo.genericdao import GenericDAO


def test_find_record_when_record_does_not_exist():
    test_query = {"_id": "NON_EXISTING_ID"}
    collection = flexmock()
    collection.should_receive("find").once().with_args(test_query).and_return([])
    mongo_client = {"testdb": {"runs": collection}}
    generic_dao = GenericDAO(mongo_client, "testdb")

    r = generic_dao.find_record("runs", test_query)

    assert r is None


def test_find_record():
    test_query = {"_id": bson.ObjectId("58163443b1758523257c69ca")}
    collection = flexmock()
    collection.should_receive("find").once().with_args(test_query).and_return([{"config": {"seed": 185616783}}])
    mongo_client = {"testdb": {"runs": collection}}
    generic_dao = GenericDAO(mongo_client, "testdb")

    r = generic_dao.find_record("runs", test_query)

    assert r is not None
    assert r["config"] is not None
    assert r["config"]["seed"] == 185616783


def test_find_records_in_empty_collection():
    mongo_cursor = flexmock(DummyIterator())
    mongo_cursor.should_receive("skip").once().with_args(0).and_return(mongo_cursor)
    mongo_cursor.should_receive("count").and_return(0)
    mongo_cursor.should_receive("__next__").and_raise(StopIteration)

    collection = flexmock()
    collection.should_receive("find").once().with_args({}).and_return(mongo_cursor)
    mongo_client = {"testdb": {"EMPTY_COLLECTION": collection}}
    generic_dao = GenericDAO(mongo_client, "testdb")

    r = generic_dao.find_records("EMPTY_COLLECTION")

    assert isinstance(r, Cursor)
    assert r.count() == 0
    assert len(list(r)) == 0


def test_find_records_in_non_empty_collection():
    mongo_cursor = flexmock(DummyIterator())
    mongo_cursor.should_receive("skip").once().with_args(0).and_return(mongo_cursor)
    mongo_cursor.should_receive("count").and_return(0)
    mongo_cursor.should_receive("__next__").and_return({"host": {"hostname": "ntbacer"}})\
        .and_return({"host": {"hostname": "martin-virtual-machine"}})\
        .and_raise(StopIteration)
    mongo_cursor.should_receive("count").and_return(2)

    collection = flexmock()
    collection.should_receive("find").once().with_args({}).and_return(mongo_cursor)
    mongo_client = {"testdb": {"runs": collection}}
    generic_dao = GenericDAO(mongo_client, "testdb")

    runs = list(generic_dao.find_records("runs"))

    assert len(runs) == 2
    assert runs[0]["host"]["hostname"] == "ntbacer"
    assert runs[1]["host"]["hostname"] == "martin-virtual-machine"


def test_find_records_limit():
    limit = 42
    mongo_cursor = flexmock(DummyIterator())
    collection = flexmock()
    mongo_client = {"testdb": {"runs": collection}}

    mongo_cursor.should_receive("limit").once().with_args(limit).and_return(mongo_cursor)
    collection.should_receive("find").once().with_args({}).and_return(mongo_cursor)


    generic_dao = GenericDAO(mongo_client, "testdb")
    generic_dao.find_records("runs", limit=limit)


def test_find_records_order_ascending():
    collection = flexmock()
    mongo_cursor = flexmock(DummyIterator())
    mongo_client = {"testdb": {"runs": collection}}

    collection.should_receive("find").once().with_args({}).and_return(mongo_cursor)
    mongo_cursor.should_receive("sort").once().with_args("host.python_version", pymongo.ASCENDING).and_return(mongo_cursor)

    generic_dao = GenericDAO(mongo_client, "testdb")

    generic_dao.find_records("runs", sort_by="host.python_version")


def test_find_records_order_descending():
    collection = flexmock()
    mongo_cursor = flexmock(DummyIterator())
    mongo_client = {"testdb": {"runs": collection}}

    collection.should_receive("find").once().with_args({}).and_return(mongo_cursor)
    mongo_cursor.should_receive("sort").once().with_args("host.python_version", pymongo.DESCENDING).and_return(mongo_cursor)

    generic_dao = GenericDAO(mongo_client, "testdb")

    generic_dao.find_records("runs", sort_by="host.python_version", sort_direction="desc")



def test_find_records_filter():
    filter = {"result": 2403.52}
    collection = flexmock()
    mongo_cursor = flexmock(DummyIterator())
    mongo_client = {"testdb": {"runs": collection}}

    collection.should_receive("find").once().with_args(filter).and_return(mongo_cursor)

    generic_dao = GenericDAO(mongo_client, "testdb")
    generic_dao.find_records("runs", query=filter)



class DummyIterator:

    def __iter__(self):
        return self

    def __next__(self):
        pass

    def skip(self, n):
        return self

    def count(self):
        pass

    def limit(self, n):
        pass

    def sort(self, field, direction):
        pass