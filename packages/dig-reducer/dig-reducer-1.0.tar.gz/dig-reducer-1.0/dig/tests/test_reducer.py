import pytest
from dig.reducer.jsonld_reducer import JSONLDReducer




@pytest.mark.parametrize('obj1, obj2, result', [
    ({"a": ["Class"], "uri": "Class1", "value": "hello"},
     {"a": ["Class"], "uri": "Class1", "value": "hello2"},
     {"a": ["Class"], "uri": "Class1", "value": ["hello", "hello2"]}),

    ({"a": ["Class"], "uri": "Class1", "value": "hello",  "nested": {"a": "NestedObject", "name": "obj1"}},
     {"a": ["Class"], "uri": "Class1", "value": "hello2", "nested": {"a": "NestedObject", "name": "obj2"}},
     {"a": ["Class"], "uri": "Class1", "value": ["hello", "hello2"], "nested":[{"a": "NestedObject", "name": "obj1"},{"a": "NestedObject", "name": "obj2"}]}),

    ({"a": ["Class"], "uri": "Class1", "value": "hello",  "nested": {"a": ["NestedObject"], "uri": "nested1", "name": "obj1"}},
     {"a": ["Class"], "uri": "Class1", "value": "hello2", "nested": {"a": ["NestedObject"], "uri": "nested1", "name": "obj2"}},
     {"a": ["Class"], "uri": "Class1", "value": ["hello", "hello2"], "nested":{"a": ["NestedObject"], "uri": "nested1", "name": ["obj1", "obj2"]}})

])
def test_reducer(obj1, obj2, result):
    reducer = JSONLDReducer()
    merged = reducer.merge_json_objects(obj1, obj2)
    assert merged == result


@pytest.mark.parametrize('obj1, obj2, result', [
    (    {
            "a": [
              "PersonOrOrganization"
            ],
            "publisher": "isi-news",
            "dateRecorded": "2018-07-17T10:16:00",
            "name": "Rappler.com",
            "uri": "http://effect.isi.edu/data/person/rapplercom",
            "source": "isi-news/FFFFFFFFC519C2A4"
          },
        {"a": ["PersonOrOrganization"], "publisher": "isi-news", "dateRecorded": "2018-07-25T10:06:24",
                "name": "Rappler.com", "uri": "http://effect.isi.edu/data/person/rapplercom",
                "source": "isi-news/FFFFFFFFC59C09EB",
        },
        {
            "a": [
              "PersonOrOrganization"
            ],
            "publisher": "isi-news",
            "dateRecorded": "2018-07-17T10:16:00",
            "name": "Rappler.com",
            "uri": "http://effect.isi.edu/data/person/rapplercom",
            "source": "isi-news/FFFFFFFFC519C2A4"
          }
    )

])
def test_reducer_provenance(obj1, obj2, result):
    reducer = JSONLDReducer(provenance_properties={'source':'str', 'dateRecorded':'str'})
    merged = reducer.merge_json_objects(obj1, obj2)
    assert merged == result