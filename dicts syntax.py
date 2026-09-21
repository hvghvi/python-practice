#create
d = {}                          # empty dict
d = {"name": "Alice", "age": 20}
d = dict(name="Alice", age=20)

#access
d["name"]                       # raises KeyError if key doesn't exist
d.get("name")                   # returns None if key doesn't exist
d.get("name", "default")        # returns "default" if key doesn't exist

#Adding / Updating
d["city"] = "Auckland"          # add or update
d.update({"age": 21, "city": "Wellington"})

#Removing
del d["age"]                    # delete a key
d.pop("age")                    # remove and return the value
d.pop("age", None)              # safe version (no error if missing)
d.clear()                       # remove everything

#Checking keys
"name" in d                     # True / False
"name" not in d

#Getting keys, values, items
d.keys()                        # all keys
d.values()                      # all values
d.items()                       # key-value pairs as tuples

#Looping
for key in d:                   # loop over keys
for key in d.keys():
for value in d.values():
for key, value in d.items():    # most useful

#Nested dictionaries
d["grades"]["math"]       # access nested value
d["grades"].get("math")


#length
len(d)