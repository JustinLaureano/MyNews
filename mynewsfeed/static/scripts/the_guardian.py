import json
import requests
from os import makedirs
from os.path import join, exists
from datetime import date, timedelta
import re
from pprint import pprint

ARTICLES_DIR = join('tempdata', 'articles')
makedirs(ARTICLES_DIR, exist_ok=True)
# Sample URL
#
# http://content.guardianapis.com/search?from-date=2016-01-02&
# to-date=2016-01-02&order-by=newest&show-fields=all&page-size=200
# &api-key=your-api-key-goes-here

MY_API_KEY = open("creds_guardian.txt").read().strip()
API_ENDPOINT = 'http://content.guardianapis.com/search'
my_params = {
    'from-date': "",
    'to-date': "",
    'order-by': "newest",
    'show-fields': 'all',
    'page-size': 200,
    'api-key': MY_API_KEY
}


# day iteration from here:
# http://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates

YEAR = date.today().year
MONTH = date.today().month
DAY = date.today().day

start_date = date(YEAR, MONTH, DAY)
end_date = date(YEAR, MONTH, DAY)
dayrange = range((end_date - start_date).days + 1)
for daycount in dayrange:
    dt = start_date + timedelta(days=daycount)
    datestr = dt.strftime('%Y-%m-%d')
    fname = join(ARTICLES_DIR, datestr + '.json')
    if not exists(fname):
        # then let's download it
        print("Downloading", datestr)
        all_results = []
        my_params['from-date'] = datestr
        my_params['to-date'] = datestr
        current_page = 1
        total_pages = 1
        while current_page <= total_pages:
            print("...page", current_page)
            my_params['page'] = current_page
            resp = requests.get(API_ENDPOINT, my_params)
            data = resp.json()
            all_results.extend(data['response']['results'])
            # if there is more than one page
            current_page += 1
            total_pages = data['response']['pages']

        with open(fname, 'w') as f:
            print("Writing to", fname)

            # re-serialize it for pretty indentation
            f.write(json.dumps(all_results, indent=2))


datestr = start_date.strftime('%Y-%m-%d')
filepath = 'tempdata/articles/%s.json' % datestr

with open(filepath, 'r') as file:
    data = json.loads(file.read())

new_list = []
unique_id = 1
TAG_RE = re.compile(r'<[^>]+>')

for story in data[:10]:
    trailText_html = story["fields"]['trailText']
    trailText = TAG_RE.sub('', trailText_html)

    new_dict = {"model": "mynewsfeed.GuardianPost", "pk": unique_id,
                "fields": {"title": story["fields"]['headline'],
                           "url": story["fields"]['shortUrl'],
                           "trailText": trailText}}

    new_list.append(new_dict)
    unique_id += 1

pprint(new_list)
with open('../../fixtures/guardian.json', 'w') as file:
    file.write(json.dumps(new_list))


# Guardian json keys
# 'id'
# 'pillarName'
# 'sectionName'
# 'webTitle'
# 'webUrl'
# 'apiUrl'
# 'fields'
#     'bodyText'
#     'byline'
#     'headline'
#     'shortUrl'
#     'thumbnail'
#     'trailText'
