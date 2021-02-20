import requests
import json
import operator

# 1. Removing irrelevant results
# 2. Sorting the results such that:
#   - Whole name matches have the most importance, and are suggested first
#     (eg. when a user types 'Mary', and a user's name is 'Mary Smith',
# this result should be prioritized).
#   - Email matches take precedent over name matches, except for the rule
# above.

# check for a substring match for the search term
# full name matches to the top
# next, full email matches
# next partial name matches
# print list of names appended together

term = input('Enter a search term: ').lower()
res = requests.get(f'http://127.0.0.1:8080/?search={term}')
results = res.json()
print('results', json.dumps(results, indent=2))

search_results = []

for result in results:
    if term == result['name'].split()[0].lower() or term == result['name'].split()[1].lower():
        search_results.append(result)
        results.remove(result)

for result in results:
    if term in result['email'].lower():
        search_results.append(result)
        results.remove(result)

for result in results:
    if term in result['name'].lower():
        search_results.append(result)

print('search_results', json.dumps(search_results, indent=2))
