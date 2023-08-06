# -*- coding: utf-8 -*-
from distutils.core import setup

packages = \
['pokeapi_ditto']

package_data = \
{'': ['*']}

install_requires = \
['flask-cors>=3.0,<4.0',
 'flask>=1.0,<2.0',
 'genson>=1.0,<2.0',
 'gevent>=1.3,<2.0',
 'requests>=2.19,<3.0']

entry_points = \
{'console_scripts': ['ditto = pokeapi_ditto.main:Ditto']}

setup_kwargs = {
    'name': 'pokeapi-ditto',
    'version': '0.2.0',
    'description': "Ditto is a server that serves a static copy of PokeAPI's data.",
    'long_description': "![image](https://img.shields.io/docker/pulls/pokesource/ditto.svg?maxAge=3600%20:target:%20https://hub.docker.com/r/pokesource/ditto/)\n\n# Ditto\n\n[https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pokémon)](https://bulbapedia.bulbagarden.net/wiki/Ditto_(Pok%C3%A9mon))\n\nThis repository contains:\n\n -   a static copy of the JSON data generated from\n     [PokeAPI](https://github.com/PokeAPI/pokeapi) based on\n     [Veekun’s data](https://github.com/veekun/pokedex)\n -   a PokeAPI schema generated from the above data\n -   a script to serve the data in the same form as PokeAPI\n -   a script to crawl an instance of PokeAPI to regenerate the data\n -   a script to analyze the generated data and produce a JSON Schema\n\n## Usage\n\nThis project is on Docker Hub. If you just want to run it, you just have\nto run one command. Replace `8080` with the port of your choice.\n\n``` bash\ndocker run -p 8080:80 pokesource/ditto\n```\n\n## Development\n\nIf you plan to edit the project, you can install it locally for\ndevelopment. [Poetry](https://poetry.eustace.io/) is required.\n\n``` bash\ncd ~\ngit clone https://github.com/PokeAPI/ditto.git\ncd ditto\npoetry install\n\n# now you can run ditto!\npoetry run ditto --help\n```\n\n## Advanced\n\nYou can manually update the data if necessary. If I abandon this\nproject, here’s how to update it. It's a bit of an involved process.\n\nBefore starting, you’ll need to install [Docker and Docker\nCompose](https://docs.docker.com/compose/install/).\n\nThese instructions assume you've already set up the project for\ndevelopment in \\~/ditto.\n\nFirst clone the PokeAPI repository:\n\n``` bash\ncd ~\ngit clone https://github.com/PokeAPI/pokeapi.git\n```\n\nApply the patch to disable rate limiting on your local PokeAPI:\n\n``` bash\n# Assuming you have the repos in ~\ncd ~/pokeapi\ngit apply ~/ditto/extra/disable-rate-limit.patch\n```\n\nRun PokeAPI using docker-compose:\n\n``` bash\ndocker volume create --name=redis_data\ndocker volume create --name=pg_data\ndocker-compose up -d\n```\n\nBuild the PokeAPI database:\n\n``` bash\ndocker-compose exec app python manage.py migrate\ndocker-compose exec app python manage.py shell\n```\n\n``` python\nfrom data.v2.build import build_all\nbuild_all()\n```\n\nThe above step can take a really long time to complete. Once it’s done,\nyou can finally update Ditto’s data:\n\n``` bash\ncd ~/ditto\nrm -r ./data\npoetry install\npoetry run ditto clone --source http://localhost/ --destination ./data\npoetry run ditto analyze --api-dir ./data/api --schema-dir ./data/schema\n```\n\nThis will crawl your local instance of PokeAPI, copy all the data to\n./data, and regenerate the schema. Once that's finished, you can serve\nthe freshly updated data!\n\n``` bash\npoetry run ditto serve --port 8080\n```\n",
    'author': 'Sargun Vohra',
    'author_email': 'sargun.vohra@gmail.com',
    'url': 'https://github.com/PokeAPI/ditto',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
