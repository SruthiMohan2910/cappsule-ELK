import json
from elasticsearch import Elasticsearch

# create an Elasticsearch instance
es = Elasticsearch(['http://localhost:9200/'])

# define the medicine name
medicine_name = "Allegra"

# define the search query
query = {
    "query": {
        "bool": {
            "should": [
                {
                    "wildcard": {
                        "product_name": {
                            "value": f"*{medicine_name}*"
                        }
                    }
                },
                {
                    "wildcard": {
                        "composition": {
                            "value": f"*{medicine_name}*"
                        }
                    }
                },
                {
                    "wildcard": {
                        "manufacturer": {
                            "value": f"*{medicine_name}*"
                        }
                    }
                }
            ]
        }
    },
    "_source": {
        "excludes": ["description"]
    }
}

# execute the search query and get the results
results = es.search(index="pharmacy_inventory", body=query)

# serialize the hits field of the results variable
hits = [hit['_source'] for hit in results['hits']['hits']]

# write the results to a file
with open("search_results.json", "w") as f:
    json.dump(hits, f, indent=4)

