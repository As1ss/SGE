
# List
fruits = ["apple", "banana", "cherry"]
print(fruits)

# Tuple
colors = ("red", "green", "blue")
print(colors)

# Set
numbers = {1, 2, 3, 4, 5}
print(numbers)

# Dictionary
person = {"name": "John", "age": 36, "country": "USA"}
print(person)

# Deque
from collections import deque
queue = deque(["Alice", "Bob", "Charlie"])
queue.append("Dave")
queue.popleft()
print(queue)

# Counter
from collections import Counter
fruits = ["apple", "banana", "cherry", "apple"]
fruit_count = Counter(fruits)
print(fruit_count)

# OrderedDict
from collections import OrderedDict
person = OrderedDict()
person["name"] = "John"
person["age"] = 36
person["country"] = "USA"
print(person)

# defaultdict
from collections import defaultdict
fruit_dict = defaultdict(lambda: "unknown")
fruit_dict["apple"] = "a fruit"
print(fruit_dict["apple"])
print(fruit_dict["orange"])
