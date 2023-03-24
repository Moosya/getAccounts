import pandas as pd
import json

# Load the JSON file into a pandas DataFrame
with open('data.json', 'r') as f:
    data = json.load(f)
df = pd.json_normalize(data, record_path=['person', 'pets', 'toys'], 
                       meta=[['person', 'name'], ['person', 'age'], ['person', 'address', 'city']])

# Extract a few of the deeper name/value pairs
df = df[['person.name', 'person.age', 'person.address.city', 'name', 'color']]

# Print the resulting DataFrame
print(df.head())



{
  "person": {
    "name": "John Doe",
    "age": 30,
    "address": {
      "street": "123 Main St",
      "city": "Anytown",
      "state": "CA",
      "zip": "12345",
      "phone_numbers": [
        {
          "type": "home",
          "number": "555-1234"
        },
        {
          "type": "work",
          "number": "555-5678"
        }
      ]
    },
    "pets": [
      {
        "name": "Fluffy",
        "type": "cat",
        "toys": [
          {
            "name": "ball of yarn",
            "color": "red"
          },
          {
            "name": "mouse",
            "color": "gray"
          }
        ]
      },
      {
        "name": "Rover",
        "type": "dog",
        "toys": [
          {
            "name": "tennis ball",
            "color": "yellow"
          },
          {
            "name": "bone",
            "color": "white"
          }
        ]
      }
    ]
  }
}
