
# This file was generated by 'versioneer.py' (0.23) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

import json

version_json = '''
{
 "date": "2023-01-03T17:06:36+0000",
 "dirty": false,
 "error": null,
 "full-revisionid": "1c449c903299af58bd479f71197f42d63e10e0da",
 "version": "1.17.1.post0.dev937"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
