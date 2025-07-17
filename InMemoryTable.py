class InMemoryDB:
    def __init__(self, data = None):
        self.data = data
    
    def where(self, col, op, value):
        selected_entries = []
        for entry in self.data:
            if op == "=":
                if entry[col] == value:
                    selected_entries.append(entry)
            if op == ">":
                if entry[col] > value:
                    selected_entries.append(entry)
            if op == "<":
                if entry[col] < value:
                    selected_entries.append(entry)
        return InMemoryDB(selected_entries)

    def select(self, columns):
        selected_entries = []
        for row in self.data:
            entry = {}
            for col in columns:
                entry[col] = row[col]
            selected_entries.append(entry)
        return InMemoryDB(selected_entries)

    def order_by(self, col, reverse = False):
        to_sort = []
        for entry in self.data:
            to_sort.append((entry[col], entry))
        sorted_entries = sorted(to_sort, reverse= reverse)
        return InMemoryDB([entry for _, entry in sorted_entries])

    def all(self):
        return self.data
    
data = [{"id" : 1, "name" : "Vijay", "age" : 27}, {"id" : 2, "name" : "TK", "age" : 28}, {"id" : 3, "name" : "MK", "age" : 28}]
table = InMemoryDB(data)
result = table.where("age", "=", 28).select(["id", "name"]).order_by("id", reverse= True).all()
print(result)
result = table.where("age", "<", 28).select(["id", "name"]).order_by("id").all()
print(result)


