import requests
import json

# 1. Removing irrelevant results
# 2. Sorting the results such that:
#   - Whole name matches have the most importance, and are suggested first
#     (eg. when a user types 'Mary', and a user's name is 'Mary Smith',
# this result should be prioritized).
#   - Email matches take precedent over name matches, except for the rule
# above.

term = input('Enter a search term: ')
res= requests.get(f'http://127.0.0.1:8080/?search={term}')
print('status code', res.status_code)
results = res.json()
print('results', json.dumps(results, indent=2))

search_results = []

# search whole name matches, if term found in a whole name, put in front



# search email addresses, prioritize next


# search incomplete names, append to the end of results

