from .cursor import Cursor


class Search():

    def __init__(self, solr):
        self.solr = solr
        self.queries = []

    def require(self, key, *values):
        body = " ".join(f"{key}:\"{value}\"" for value in values)
        query = f"+({body})"
        self.queries.append(query)
        return self

    def prohibit(self, key, *values):
        body = " ".join(f"{key}:\"{value}\"" for value in values)
        query = f"-({body})"
        self.queries.append(query)
        return self

    def with_range(self, key, start="*", stop="*"):
        self.queries.append(f"+({key}:[{start} TO {stop}])")
        return self

    def scan(self):
        """Iterate over documents that match the search."""
        return Cursor(self.solr, self.build())

    def build(self):
        """Construct the query."""
        return " ".join(self.queries) or "*:*"
