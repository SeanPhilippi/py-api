import requests

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

term = input('Search for a name: ').lower()
res = requests.get(f'http://127.0.0.1:8080/?search={term}')
results = res.json()

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
if len(results):
    print('Here are your results:')
    for result in search_results:
        print(result)
else:
    print(f'No results found for {term}')
