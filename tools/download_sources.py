#!/usr/bin/env python3

# Copyright 2025 Benjamin Gilbert <bgilbert@backtick.net>

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations
from argparse import ArgumentParser
from hashlib import sha256
import json
from pathlib import Path
import subprocess

def main():
    parser = ArgumentParser(
        prog='download_sources.py',
        description='Download sources for updated (or all) wraps.'
    )
    parser.add_argument(
        '-a', '--all', action='store_true',
        help='select all wraps',
    )
    parser.add_argument(
        '-k', '--cache-key', action='store_true',
        help='generate cache key for selected sources',
    )
    args = parser.parse_args()

    with open('releases.json') as fh:
        releases = json.load(fh)

    if args.all:
        names = sorted(releases)
    else:
        tags = set(
            subprocess.check_output(['git', 'tag'], text=True).splitlines()
        )
        names = sorted(
            name
            for name, info in releases.items()
            if f'{name}_{info["versions"][0]}' not in tags
        )

    if args.cache_key:
        hash = sha256()
        for name in names:
            hash.update(name.encode())
            hash.update(Path('subprojects', f'{name}.wrap').read_bytes())
            hash.update(b'=====')
        print(hash.hexdigest()[:16])
    elif names:
        subprocess.check_call(['meson', 'subprojects', 'download'] + names)


if __name__ == '__main__':
    main()
