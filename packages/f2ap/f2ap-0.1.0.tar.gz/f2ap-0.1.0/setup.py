# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f2ap']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'feedparser>=6.0,<7.0',
 'markdown>=3.4.1,<4.0.0',
 'mdx-linkify>=2.1,<3.0',
 'pycryptodome>=3.16.0,<4.0.0',
 'pydantic>=1.10.2,<2.0.0',
 'pyhumps>=3.8.0,<4.0.0',
 'requests>=2.28.1,<3.0.0',
 'toml>=0.10.2,<0.11.0',
 'uvicorn[standard]>=0.20.0,<0.21.0']

entry_points = \
{'console_scripts': ['f2ap = f2ap.__main__:main']}

setup_kwargs = {
    'name': 'f2ap',
    'version': '0.1.0',
    'description': 'Put your website on the Fediverse thanks to your RSS/Atom feed',
    'long_description': '# ![f2ap](logo.svg)\n\nf2ap (_Feed to ActivityPub_) is a web application that uses the RSS/Atom feed of your website to expose it on the Fediverse\nthrough ActivityPub.\n\n## How to use it\n\n### Prerequisite\n\nThe only prerequisite to use f2ap is that your website provides an RSS or Atom feed.\nIf you don\'t have one yet, you might want to make it first, as it is a Web standard that allows your visitors to stay in touch with your content with any compatible application. Plus, it is very easy to implement. \n\n### Installation\n\n#### With PyPI\n\n_**Required:** Python 3.9+_\n\nInstall the `f2ap` package:\n\n```bash\npip install f2ap\n```\n\nThe application will be runnable with the `f2ap` command.\nYou will need to use a runner like systemd to start it as a service.\n\n#### Docker\n\n_**Required:** Docker_\n\nGrab the image from Docker Hub:\n\n```bash\ndocker pull deuchnord/f2ap\n```\n\nYou can get a specific version with the following syntax: `deuchnord/f2ap:<tag>`, where tag is one of the following (`i`, `j` and `k` being numbers):\n- `latest`: the last version (default)\n- `i`: the last version of the `i` major version\n- `i.j`: the last version of the `i.j` minor version\n- `i.j.k`: the version `i.j.k`\n- `unstable`: the last commit in the Git history.\n  It is heavily discouraged to use it in production, as it can have bugs, crash, put fire in your house or, worse, kill your kitten.\n\n##### Docker-Compose\n\nIf you want to use f2ap through Docker-Compose, check the [`docker-compose.dist.yml`](docker-compose.dist.yml) for an example of configuration.\n\n### Configuration\n\nTo make f2ap work, you will need to write a configuration file that will define its behavior.\nIt is a boring simple TOML file. You can find a self-documented file in [config.dist.toml](config.dist.toml).\nIf you run f2ap with Docker, make sure to name it `config.toml` and to place it in the `/data` folder.\n\n### Configuring the server\n\nTo provide a better integration to your website, you are encouraged to add some configuration lines to your server.\nThis will ensure the social applications will correctly discover your website\'s ActivityPub API.\n\n#### Nginx\n\nEdit your configuration file and add the following lines to your `server` section.\nDon\'t forget to adapt:\n- the IP address on the `proxy_pass` lines to match f2ap\'s configuration;\n- the `<username>` part in the last `location` to match the username of your actor.\n\n```nginx\nserver {\n    ## ...\n    \n    # Propagate the domain name to f2ap\n    proxy_set_header Host $host;\n    \n    # The webfinger allows the social applications to find out that your website serves an ActivityPub API.\n    location /.well-known/webfinger {\n        proxy_pass http://127.0.0.1:8000;\n    }\n    \n    location / {\n        # Match any request asking for an ActivityPub content\n        if ( $http_accept ~ .*application/activity\\+json.* ) {\n            proxy_pass http://127.0.0.1:8000;\n        }\n\n        # Match any request sending an ActivityPub content\n        if ( $http_content_type = "application/activity+json" ) {\n            proxy_pass http://127.0.0.1:8000;\n        }\n    }\n    \n    # Exposes the avatar and the header of the profile\n    # Change the <username> here with the username of the actor you expose (for instance: blog)\n    location ~ /actors/<username>/(avatar|header) {\n        proxy_pass http://127.0.0.1:8000;\n    }\n    \n    ## ... \n}\n```\n\n### Limitations\n\nBecause f2ap uses your RSS/Atom feed to connect your website to ActivityPub, the time before a new entry pops on the Fediverse will depend on the refresh frequency. You might want to choose a frequency that matches your update regularity.\n  \n**If this behavior is a problem**, f2ap is probably not the right solution for you, and you might need to integrate ActivityPub to your application on your own.\n',
    'author': 'Jérôme Deuchnord',
    'author_email': 'jerome@deuchnord.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Deuchnord/f2ap',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
