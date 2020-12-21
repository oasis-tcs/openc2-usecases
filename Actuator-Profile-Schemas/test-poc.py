from collections import defaultdict
from urllib.request import urlopen, Request
import json
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import ValidationError
import os

"""
Validate OpenC2 commands and responses for profiles stored on GitHub under "base"
Environment variable "GitHubToken" must have a Personal Access Token to prevent rate limiting

/base
|-- profile-A
|   |-- schema-A.json
|   |-- Good-command
|   |   |-- command.json
|   |   |-- command.json
|   |-- Bad-command
|   |   |-- command.json
|   |-- Good-response
|   |   |-- response.json
|   |-- Bad-response
|   |   |-- response.json
|-- profile-B
|   |-- schema-B.json
     ...
"""

base = 'https://api.github.com/repos/oasis-tcs/openc2-usecases/contents/Actuator-Profile-Schemas/'
auth = {'Authorization': f'token {os.environ["GitHubToken"]}'}


def gh_get(url):            # Read contents from GitHub API
    with urlopen(Request(url, headers=auth)) as e:
        entry = json.loads(e.read().decode())
    return entry


def find_tests(api_url):    # Search for GitHub folders containing schemas and test data
    def _ft(url, tests):    # Internal recursive search
        gdir = gh_get(url)
        dirs = {e['name']: e['url'] for e in gdir if e['type'] == 'dir'}
        if 'Good-command' in dirs:      # Directory name indicates test data
            files = {e['name']: e['download_url'] for e in gdir if e['type'] == 'file'}
            json_url = [u for f, u in files.items() if os.path.splitext(f)[1] == '.json']
            if len(json_url) == 1:      # Must have exactly one .json file
                tests.append({'dirs': dirs, 'files': files, 'schema': json_url[0]})
            else:
                print('No json schema in', url)
        else:
            for child in dirs.values():
                _ft(child, tests)

    test_list = []          # Initialize, build test list, and return it
    _ft(api_url, test_list)
    return test_list


def run_test(tdir):         # Check correct validation of good and bad commands and responses
    json_schema = gh_get(tdir['schema'])
    print(f'\nSchema: {tdir["schema"]}\nNamespace: {json_schema["$id"]}')
    tcount = defaultdict(int)       # Total instances tested
    ecount = defaultdict(int)       # Error instances
    for cr in ('command', 'response'):
        for gb in ('Good', 'Bad'):
            pdir = f'{gb}-{cr}'
            if pdir in tdir['dirs']:
                print(pdir)
                fdir = gh_get(tdir['dirs'][pdir])
                files = {e['name']: e['download_url'] for e in fdir if e['type'] == 'file'}
                for n, (fn, url) in enumerate(files.items(), start=1):
                    print(f'{n:>4} {fn:<50}', end='')
                    try:
                        instance = {'openc2_' + cr: gh_get(url)}  # Read message, wrap it as command or response
                        validate(instance, json_schema, format_checker=draft7_format_checker)
                        tcount[pdir] += 1
                        ecount[pdir] += 1 if gb == 'Bad' else 0
                        print()
                    except ValidationError as e:
                        tcount[pdir] += 1
                        ecount[pdir] += 1 if gb == 'Good' else 0
                        print(f' Fail: {e.message}')
                    except json.decoder.JSONDecodeError as e:
                        print(f' Bad JSON: {e.msg} "{e.doc}"')
            else:
                print(pdir, 'No tests')
    print('\nValidation Errors:', {k: str(dict(ecount)[k]) + '/' + str(dict(tcount)[k]) for k in tcount})


print(f'Test Data: {base}')
for test in find_tests(base):
    run_test(test)
