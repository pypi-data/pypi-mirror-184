# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cachetools']

package_data = \
{'': ['*']}

install_requires = \
['redis>=3.5.3,<4.0.0']

setup_kwargs = {
    'name': 'py-redis-cachetools',
    'version': '0.1.2',
    'description': 'cachetools core + redis',
    'long_description': '# py-redis-cachetools\ncachetools core + redis\n\nRequirements:\n-------------\nredis 3.5.3\n\n\nInstallation:\n-------------\n\n    pip install py-redis-cachetools\n\nenv variables:\n-------------\n    REDIS_HOST\n    REDIS_DB\n\n\nUsage:\n------\n\n    import time\n    import cachetools, cachetools.rcache\n\n\n    # cache = cachetools.rcache.RedisCache(ttl=60)\n\n    cache = cachetools.rcache.PrefixedRedisCache("hb-cachetools-cache", ttl=60)\n\n\n    @cachetools.cached(cache=cache)\n    def test(a, b):\n        return {\n            \'hi\': \'hello\'\n        }\n\n\n\n    a = 1\n    while True:\n        print(test(a, 2))\n        print(a)\n        time.sleep(1)\n        a = a+1',
    'author': '500apps',
    'author_email': 'satyabrata.swain@500apps.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://500apps.com',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
