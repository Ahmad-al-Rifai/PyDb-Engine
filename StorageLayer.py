from BTree import BTree
from Lexer import Lexer, QueryPlan

class UserRecord:
    
    # Represents a single row in the 'users' table.

    __slots__ = ['id', 'name', 'age', 'city']

    def __init__(self, user_id: int, name: str, age: int, city: str):
        self.id = user_id
        self.name = name
        self.age = age
        self.city = city

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', age={self.age}, city='{self.city}')"

class Table:
    
    # Manages records and B-Tree indexes for a specific table.
    
    def __init__(self, name: str):
        self.name = name
        self.records = []
        # Index on the primary key (id)
        self.index = BTree(t=3)

    def insert(self, record: UserRecord):
        self.records.append(record)
        self.index.insert(record.id, record)

    def find_by_id(self, user_id: int):
        return self.index.search(user_id)

    def select_all(self):
        return self.records

class SQLEngine:
    
    # The orchestrator that connects the Parser to the Storage/Table.
    
    def __init__(self):
        self.tables = {}
        self.lexer = Lexer()

    def add_table(self, table: Table):
        self.tables[table.name] = table

    def execute(self, sql_string: str):
        # 1. Tokenize
        tokens = self.lexer.tokenize(sql_string)
        
        # 2. Parse/Plan
        plan = QueryPlan(tokens)
        plan.parse()

        # 3. Optimize & Execute
        if plan.table_name not in self.tables:
            return f"Error: Table {plan.table_name} not found."
        
        target_table = self.tables[plan.table_name]

        # Use Index if filtering by ID
        if plan.filter_col == "id":
            print(f"--- Optimizer: Using B-Tree Index for id={plan.filter_val} ---")
            result = target_table.find_by_id(plan.filter_val)
            return [result] if result else []
        else:
            print(f"--- Optimizer: Linear Scan (O(n)) ---")
            # Basic linear scan logic would go here
            return []

# --- Integrated Test ---
if __name__ == "__main__":
    # Initialize Engine and Data
    db_engine = SQLEngine()
    users = Table("users")
    for item in [(10, "Alice", 30, "NY"), (20, "Bob", 25, "SF"), (5, "Charlie", 35, "LDN")]:
        users.insert(UserRecord(*item))
    db_engine.add_table(users)

    # Run Query
    query = input("Enter your query: ") #Sample "SELECT name FROM users WHERE id = 20"
    print(f"Query: {query}")
    results = db_engine.execute(query)
    
    for row in results:
        print(f"Row found: {row}")