# Introduction 

Filter sqlalchemy query with json data.

This is an early stage version of the project a lot of change is coming.

# Installation

```bash
pip install sqla-filter
```

# Getting Started

Create an instance of the JSONFilterParser with the json string.

Example:
```python
# Sqlalchemy setup ... + model definition

# Create a JSON parser instance
parser = JSONFiltersParser(raw_json_string)

# you now have a tree available as a property in the parser
print(parser.tree)

# You can finaly filter your query
query = session.query(Post)
filtered_query = parser.tree.filter(query)

# Get the results
query.all()
```

## Operators

The following operators are or will be implemented:

| support | operators |          name         |        code        |
|:-------:|:----------|:---------------------:|-------------------:|
|   [ ]   | like      | like                  | like()             |
|   [x]   | eq        | equal                 | operators.eq       |
|   [x]   | not_eq    | not equal             | operators.ne       |
|   [x]   | null      | null                  | is None            |
|   [x]   | not_null  | not null              | is not None        |
|   [x]   | gt        | greater than          | operators.gt       |
|   [x]   | gte       | greater than or equal | operators.ge       |
|   [x]   | lt        | lower than            | operators.lt       |
|   [x]   | lte       | lower than or equal   | operators.le       |
|   [x]   | in        | in                    | in_()              |
|   [x]   | not_in    | not in                | ~.in_()            |
|   [ ]   | contains  | contains              | operators.contains |

## Formats

### JSON

```json
{
    "type": "and",
    "data": [
        {
            "type": "or",
            "data": [
                {
                    "type": "operator",
                    "data": {
                        "attribute": "name",
                        "operator": "eq",
                        "value": "toto"
                    }
                },
                {
                    "type": "operator",
                    "data":{
                        "attribute": "name",
                        "operator": "eq",
                        "value": "tata"
                    }
                }
            ]
        },
        {
            "type": "operator",
            "data": {
                "attribute": "age",
                "operator": "eq",
                "value": 21
            }
        }
    ]
}
```

/!\ Json format can change in the futur. /!\

### Tree result

```
                                      +----------------------+
                                      |                      |
                                      |          and         |
                                      |                      |
                                      -----------------------+
                                                 ||
                                                 ||
                                                 ||
                    +----------------------+     ||     +----------------------+
                    |                      |     ||     |                      |
                    |          or          <------------>      age == 21       |
                    |                      |            |                      |
                    +----------------------+            +----------------------+
                               ||
                               ||
                               ||
+----------------------+       ||       +----------------------+
|                      |       ||       |                      |
|     name == toto     <---------------->     name == tata     |
|                      |                |                      |
+----------------------+                +----------------------+
```

# Contribute

Fork the repository and run the following command to install the dependencies and the dev dependencies.

`pip install -e '.[dev]'`
