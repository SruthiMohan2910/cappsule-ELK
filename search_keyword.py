import json
from elasticsearch import Elasticsearch

# create an Elasticsearch instance
es = Elasticsearch(['http://localhost:9200/'])

# dynamically get the search key - TO BE IMPLIMENTED

# define the search query
query = {
    "query": {
        "bool": {
            "should": [
                {
                    "wildcard": {
                        "product_name": {
                            "value": "*Allegra*"
                        }
                    }
                },
                {
                    "wildcard": {
                        "composition": {
                            "value": "*Allegra*"
                        }
                    }
                },
                {
                    "wildcard": {
                        "manufacturer": {
                            "value": "*Allegra*"
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

