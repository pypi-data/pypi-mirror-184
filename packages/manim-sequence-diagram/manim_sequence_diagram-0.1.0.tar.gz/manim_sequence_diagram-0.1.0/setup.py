# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['manim_sequence_diagram']

package_data = \
{'': ['*']}

install_requires = \
['manim>=0.3']

entry_points = \
{'manim.plugins': ['manim_sequence_diagram = manim_sequence_diagram']}

setup_kwargs = {
    'name': 'manim-sequence-diagram',
    'version': '0.1.0',
    'description': 'Manim extension to generate UML sequence diagrams',
    'long_description': '# Manim Sequence Diagrams\n\n[![watch the sequence diagram video](docs/seq-diagram.png)](./docs/ClientRaceDatabaseNetwork.mp4)\n\n## Installation\n\nFollowing manim\'s guide on how to install plugins on [this guide](https://docs.manim.community/en/stable/plugins.html), but TL;DR is:\n\nrun\n\n```sh\npip install manim-sequence-diagram\nmanim cfg write\n```\n\nthis will generate a `manim.cfg` file somewhere, you\'ll need to add to it this package\n\n```\n[CLI]\nenable_wireframe = False\ndry_run = False\ntex_template =\nplugins = manim_sequence_diagram\n```\n\nYou\'ll know if you have it working if you run\n\n```sh\nmanim plugins -l\n```\n\nand it shows something like\n\n```\nManim Community v0.16.0.post0\n\nPlugins:\n • manim_sequence_diagram\n```\n\n### Generate Examples\n\n```sh\nmanim -pql docs/examples.py ClientRaceDatabaseNetwork\n```\n\nAlthough one day, we\'d like to support proper sequence diagram syntax, for now, it\'s all in python.\n\nHere\'s a quick example of how it works\n\n```python\nfrom manim import *\nfrom manim_sequence_diagram import *\n\nclass ClientRaceDatabaseNetwork(MovingCameraScene):\n    def construct(self):\n        actor_client = SeqActor(name="client")\n        actor_delivery = SeqActor(name="delivery")\n        actor_server = SeqActor(name="server")\n        actor_db = SeqActor(name="database")\n        for anime in SeqAction.introduce_actors(actor_client, actor_server, actor_delivery, actor_db):\n            self.play(anime)\n\n        # Move the camera yourself!\n        self.play(self.camera.frame.animate.move_to(DOWN * 3))\n\n        for anime in SeqAction.subject_gives_gift_to_target(\n            subject=actor_client,\n            gift=SeqObject(name="async getData"),\n            target=actor_delivery\n        ):\n            self.play(anime)\n```\n\n## Development\n\nYou\'ll need poetry to properly get this to work, checkout their guide [here](https://python-poetry.org/docs/) for how to install. Once you do, do the following to setup\n\n```sh\nmake install\nmake dev\n```\n\nIn order to generate examples, you\'ll need to setup your manim cfg\n',
    'author': 'Thomas Chen',
    'author_email': 'tom.chen@sony.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/foxnewsnetwork/manim-sequence-diagram',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
