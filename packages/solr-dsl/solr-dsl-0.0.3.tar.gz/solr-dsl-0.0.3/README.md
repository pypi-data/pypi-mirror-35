# solr-dsl

A high-level library for querying Solr with Python. Built on the lower-level Pysolr.

## Example

```
from pysolr import Solr
from solr_dsl import Search

solr = Solr("http://localhost:8983/solr/test")
search = Search(solr) \
    .require("doc_type", "solution") \
    .require("domain", "example1", "example2")
    .with_range("date", "2018-01-01T00:00:00Z", "now")

for document in search.scan():
    ...
```
