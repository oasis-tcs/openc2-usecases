from collections import defaultdict
from urllib.request import urlopen, Request
import json
from jsonschema import validate, draft7_format_checker
from jsonschema.exceptions import ValidationError
import os

"""
Validate OpenC2 commands and responses stored on GitHub under "base"
Use credential stored in environment variable "GitHubToken" to prevent rate limiting
"""

base = 'https://api.github.com/repos/oasis-tcs/openc2-usecases/contents/SBOM-PoC/Schemas/'


def gh_get(url):                        # Read contents from GitHub API
    with urlopen(Request(url, headers=auth)) as e:
        entry = json.loads(e.read().decode())
    return entry


def find_tests(api_url, testdirs):      # Search for GitHub folders containing schemas and test data
    dir = gh_get(api_url)
    dirs =  {e['name']: e['url'] for e in dir if e['type'] == 'dir'}
    if 'Good-command' in dirs:          # Folder name indicates test data
        files = {e['name']: e['download_url'] for e in dir if e['type'] == 'file'}
        json_url = [u for f, u in files.items() if os.path.splitext(f)[1] == '.json']
        if len(json_url) == 1:          # Must have exactly one .json file
            testdirs.append({'dirs': dirs, 'files': files, 'schema': json_url[0]})
        else:
            print('Did not find json schema in dir', dir['name'])
    else:
        for child in dirs.values():
            find_tests(child, testdirs)


def run_test(tdir):                     # Check correct validation of good and bad commands and responses
    json_schema = gh_get(tdir['schema'])
    print(f'   Schema: {json_schema["$id"]}\n')
    tcount = defaultdict(int)           # Total instances tested
    ecount = defaultdict(int)           # Error instances
    for cr in ('command', 'response'):
        for gb in ('Good', 'Bad'):
            pdir = f'{gb}-{cr}'
            if pdir in tdir['dirs']:
                print(pdir)
                fdir = gh_get(tdir['dirs'][pdir])
                files = {e['name']: e['download_url'] for e in fdir if e['type'] == 'file'}
                for n, (fn, url) in enumerate(files.items(), start=1):
                    print(f'{n:>4} {fn:<50}', end='')
                    instance = {'openc2_' + cr: gh_get(url)}    # Read message, label it as command/response for schema
                    tcount[pdir] += 1
                    try:
                        validate(instance, json_schema, format_checker=draft7_format_checker)
                        ecount[pdir] += 1 if gb == 'Bad' else 0
                        print()
                    except ValidationError as e:
                        ecount[pdir] += 1 if gb == 'Good' else 0
                        print(f' Fail: {e.message}')
                    except json.decoder.JSONDecodeError as e:
                        print(f' Bad JSON: {e.msg} "{e.doc}" |')
            else:
                print(pdir, 'No tests')
    print('\nValidation Errors:', {k: str(dict(ecount)[k]) + '/' + str(dict(tcount)[k]) for k in tcount})


print(f'Test Data: {base}')
auth = {'Authorization': 'token ' + os.environ['GitHubToken']}
tests = []
find_tests(base, tests)
for test in tests:
    run_test(test)
