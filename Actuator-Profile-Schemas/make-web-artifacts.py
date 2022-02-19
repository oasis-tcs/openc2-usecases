import jadn
import json
import os
import re
from collections import defaultdict
from urllib.request import urlopen, Request
from urllib.parse import urlparse
from urllib.error import HTTPError

"""
Generate JADN information model and JSON serialization from SPDXv3 template files
"""

TEMPLATE_ROOT_DIR = os.path.join('..', 'spec-v3-template', 'model')
TEMPLATE_ROOT_REPO = 'https://api.github.com/repos/spdx/spdx-3-model/contents/model'
TEMPLATE_ROOT = TEMPLATE_ROOT_REPO           # Select source of template files

OUTPUT_DIR = 'Out'

AUTH = {'Authorization': 'token ' + os.environ['GitHubToken']}      # GitHub public_repo personal access token


class WebDirEntry:
    """
    Fake os.DirEntry type for GitHub filesystem
    """
    def __init__(self, name, path, url):
        self.name = name
        self.path = path
        self.url = url


def dd():
    """
    Return a recursive defaultdict
    """
    return defaultdict(dd)


def list_dir(dirname: str) -> dict:
    """
    Return a dict listing the files and directories in a directory on local filesystem or GitHub repo.

    :param dirname: str - a filesystem path or GitHub API URL
    :return: dict {files: [DirEntry*], dirs: [DirEntry*]}
    Local Filesystem: Each list item is an os.DirEntry structure containing name and path attributes
    GitHub Filesystem: Each list item has name, path, and url (download URL) attributes
    """

    files, dirs = [], []
    if dirname.startswith('https://'):
        with urlopen(Request(dirname, headers=AUTH)) as d:
            for dl in json.loads(d.read().decode()):
                url = 'url' if dl['type'] == 'dir' else 'download_url'
                entry = WebDirEntry(dl['name'], dl[url], dl['url'])
                (dirs if dl['type'] == 'dir' else files).append(entry)
    else:
        with os.scandir(dirname) as dlist:
            for entry in dlist:
                (dirs if os.path.isdir(entry) else files).append(entry)
    return {'files': files, 'dirs': dirs}


def read_file(path: str) -> str:
    if path.startswith('https://'):
        with urlopen(Request(path, headers=AUTH)) as fp:
            doc = fp.read().decode()
    else:
        with open(path) as fp:
            doc = fp.read()
    return doc


"""

    def _d(path: str) -> str:
        print(f'  dir: {path}')
        return path.removeprefix(rootdir)

    def _f(path: str) -> str:
        print(f'  file: {path}')
        model = urlparse(path).path.removeprefix(urlparse(rootdir).path)
        return path.removeprefix(path.removesuffix(model))

    templ = dd()
    t1 = list_dir(rootdir)
    for f1 in t1['files']:
        print(f'    {_f(f1.path)} -- file at root level ignored')
    for d1 in t1['dirs']:
        t2 = list_dir(d1.path)

    return dict(templ)
"""

if __name__ == '__main__':
    print(f'Installed JADN version: {jadn.__version__}\n')

    # Load data from directory tree of individual files
    print(f'Scanning template files from "{TEMPLATE_ROOT}"')
    templates = load_template_from_list_dirs(TEMPLATE_ROOT)


        # Generate information model (.jadn, .jidl) and JSON Schema (.json)
        # TODO: generate XML schema (.xsd), YAML, spreadsheet, Tag:Value, etc.
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        jadn.dump(schema, os.path.join(OUTPUT_DIR, OUTPUT_FILE + '.jadn'))
        jadn.convert.jidl_dump(schema, os.path.join(OUTPUT_DIR, OUTPUT_FILE + '.jidl'))
        jadn.translate.json_schema_dump(schema, os.path.join(OUTPUT_DIR, OUTPUT_FILE + '.json'))

        # Check for completeness
        try:
            print('\n', '\n'.join([f'{k:>15}: {v}' for k, v in jadn.analyze(jadn.check(schema)).items()]))
        except ValueError as e:
            print(f'\n{e}')
