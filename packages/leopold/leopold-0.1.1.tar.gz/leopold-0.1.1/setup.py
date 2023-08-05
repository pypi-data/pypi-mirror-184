# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['leopold']

package_data = \
{'': ['*'],
 'leopold': ['Device Groups/CSV/*',
             'Device Groups/HTML/*',
             'Device Groups/JSON/*',
             'Device Groups/Markdown/*',
             'Device Groups/Mindmap/*',
             'Device Groups/YAML/*',
             'Devices Config YANG Library/CSV/*',
             'Devices Config YANG Library/HTML/*',
             'Devices Config YANG Library/JSON/*',
             'Devices Config YANG Library/Markdown/*',
             'Devices Config YANG Library/Mindmap/*',
             'Devices Config YANG Library/YAML/*',
             'Devices Config YANG Modules State/CSV/*',
             'Devices Config YANG Modules State/HTML/*',
             'Devices Config YANG Modules State/JSON/*',
             'Devices Config YANG Modules State/Markdown/*',
             'Devices Config YANG Modules State/Mindmap/*',
             'Devices Config YANG Modules State/YAML/*',
             'Devices Live Status YANG Library/CSV/*',
             'Devices Live Status YANG Library/HTML/*',
             'Devices Live Status YANG Library/JSON/*',
             'Devices Live Status YANG Library/Markdown/*',
             'Devices Live Status YANG Library/Mindmap/*',
             'Devices Live Status YANG Library/YAML/*',
             'Devices Live Status YANG Modules State/CSV/*',
             'Devices Live Status YANG Modules State/HTML/*',
             'Devices Live Status YANG Modules State/JSON/*',
             'Devices Live Status YANG Modules State/Markdown/*',
             'Devices Live Status YANG Modules State/Mindmap/*',
             'Devices Live Status YANG Modules State/YAML/*',
             'Devices/CSV/*',
             'Devices/HTML/*',
             'Devices/JSON/*',
             'Devices/Markdown/*',
             'Devices/Mindmap/*',
             'Devices/YAML/*']}

install_requires = \
['aiofiles>=22.1.0,<23.0.0',
 'aiohttp>=3.8.3,<4.0.0',
 'jinja2>=3.1.2,<4.0.0',
 'pyyaml>=6.0,<7.0',
 'rich-click>=1.6.0,<2.0.0']

entry_points = \
{'console_scripts': ['aceye = leopold.script:run']}

setup_kwargs = {
    'name': 'leopold',
    'version': '0.1.1',
    'description': 'Business ready documents from Cisco Network Services Orchestrator',
    'long_description': '# ISEhole\n\nBusiness Ready Documents for Cisco Identity Services Engine\n\n## Current API Coverage\n\nActive Directory\n\nActive Sessions\n\nAdmin Users\n\nAllowed Protocols\n\nAuthentication Dictionaries\n\nAuthorization Dictionaries\n\nAuthorization Profiles\n\nCommand Sets\n\nConditions\n\nCSRs\n\nDACLs\n\nDeployment Nodes\n\nEndpoint Groups\n\nEndpoints\n\nEval Licenses\n\nFailure Reasons\n\nHot Patches\n\nIdentity Groups\n\nIdentity Store Sequences\n\nIdentity Stores\n\nInternal Users\n\nLast Backup\n\nLicense Connection Type\n\nLicense Feature Map\n\nLicense Register\n\nLicense Smart State\n\nLicense Tier State\n\nNBAR Apps\n\nNetwork Access Condition Authentication\n\nNetwork Access Condition Authorization\n\nNetwork Access Condition Policy Sets\n\nNetwork Access Conditions\n\nNetwork Access Dictionary Authentication\n\nNetwork Access Dictionary Authorization\n\nNetwork Access Dictionary Policy Sets\n\nNetwork Access Dictionaries\n\nNetwork Access Identity Stores\n\nNetwork Access Policy Sets\n\nNetwork Access Security Groups\n\nNetwork Access Service Names\n\nNetwork Authorization Profiles\n\nNetwork Device Groups\n\nNetwork Devices\n\nNode Interfaces\n\nNode Profiles\n\nNodes\n\nPAN HA\n\nPatches\n\nPolicy Set Dictionary\n\nPolicy Sets\n\nPortals\n\nPosture Count\n\nProfiler Count\n\nProfilers\n\nProxies\n\nRepositories\n\nSelf Registration Portals\n\nService Names\n\nSGT ACLs\n\nSGTs\n\nShell Profiles\n\nSponsor Groups\n\nSponsored Guest Portals\n\nSponsor Portals\n\nSystem Certificates\n\nTransport Gateways\n\nTrusted Certificates\n\nVersion\n## Installation\n\n```console\n$ python3 -m venv ISE\n$ source ISE/bin/activate\n(ACI) $ pip install isehole\n```\n\n## Usage - Help\n\n```console\n(ISE) $ isehole --help\n```\n\n## Usage - In-line\n\n```console\n(ISE) $ isehole --url <url to ISE> --username <ISE username> --password <ISE password>\n```\n\n## Usage - Interactive\n\n```console\n(ISE) $ isehole\nISE URL: <URL to ISE>\nISE Username: <ISE Username>\nISE Password: <ISE Password>\n```\n\n## Usage - Environment Variables\n\n```console\n(ISE) $ export URL=<URL to ISE>\n(ISE) $ export USERNAME=<ISE Username>\n(ISE) $ export PASSWORD=<ISE Password>\n```\n\n## Recommended VS Code Extensions\n\nExcel Viewer - CSV Files\n\nMarkdown Preview - Markdown Files\n\nMarkmap - Mindmap Files\n\nOpen in Default Browser - HTML Files\n\n## Contact\n\nPlease contact John Capobianco if you need any assistance\n',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
