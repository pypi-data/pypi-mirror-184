# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['graphene_djmoney', 'graphene_djmoney.schema']

package_data = \
{'': ['*']}

install_requires = \
['Django>2',
 'django-money>=3.0.0,<4.0.0',
 'graphene-django>=2',
 'graphene>=2.1.7,<3',
 'graphql-core>=2.1.0',
 'psycopg2-binary>=2.8.5,<3.0.0']

setup_kwargs = {
    'name': 'graphene-djmoney',
    'version': '0.2.2',
    'description': 'GraphQL Money types for Django using graphene and django-money (djmoney).',
    'long_description': '# graphene-djmoney\n\n![python package](https://github.com/UpliftAgency/graphene-djmoney/actions/workflows/pythonpackage.yml/badge.svg)\n\n[![Build Status](https://travis-ci.org/UpliftAgency/graphene-djmoney.svg?branch=master)](https://travis-ci.org/UpliftAgency/graphene-djmoney) [![PyPI version](https://badge.fury.io/py/graphene-djmoney.svg)](https://badge.fury.io/py/graphene-djmoney)\n\n## Introduction\n\nGraphQL Money types for Django using graphene and django-money (djmoney). If you use `django`, `graphene_django`, and `django-money`, this library is for you.\n\nSupported on:\n\n* Python 3.7+ (likely earlier versions too, needs tested)\n* Django 2+\n* graphene-django 2+\n* django-money 1+\n\nHere\'s how it works. Automagically get this query:\n\n```graphql\nquery Products {\n    products {\n        id\n        cost {\n            ...moneyFragment\n        }\n    }\n}\n\nfragment moneyFragment on Money {\n    asString  # "123.45 USD"\n    amount    # 123.45\n    amountStr # "123.45"\n    currency {\n        code  # "USD"\n        name  # "US Dollar"\n        # These are not as commonly used, see tests:\n        numeric\n        symbol\n        prefix\n    }\n}\n```\n\nWith this code:\n\n```python\n# yourapp/models.py\nfrom django.conf import settings\nfrom django.contrib.auth.models import AbstractUser\nfrom django.db import models\nfrom djmoney.models.fields import MoneyField\n\n\nclass User(AbstractUser):\n    pass\n\n\nclass Product(models.Model):\n    creator = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)\n    title = models.CharField(max_length=2000)\n    cost = MoneyField(\n        max_digits=settings.CURRENCY_MAX_DIGITS,\n        decimal_places=settings.CURRENCY_DECIMAL_PLACES,\n        default_currency=settings.BASE_CURRENCY,\n        null=True,\n        blank=True,\n    )\n\n# yourapp/schema/types.py\n\nimport graphene\nfrom graphene_django import DjangoObjectType\n\nfrom yourapp import models\n\n\nclass Product(DjangoObjectType):\n    class Meta:\n        model = models.Product\n        interfaces = (graphene.relay.Node,)\n        fields = ("id", "cost")\n\n# yourapp/schema/__init__.py\n\nimport graphene\n\nfrom .. import models\nfrom .types import Product\n\nclass Queries(graphene.ObjectType):\n\n    products = graphene.List(graphene.NonNull(types.Product), required=True)\n\n    def resolve_products(self, info, **kwargs):\n        return models.Product.objects.all()\n\n\nschema = graphene.Schema(query=Queries, types=[Product])\n\n# yourapp/settings.py\n\nINSTALLED_APPS += [\n    "graphene_djmoney",\n]\n\nGRAPHENE = {\n    "SCHEMA": "yourapp.schema.schema",\n}\n\n```\n\n## Installation\n\n```bash\npip install graphene-djmoney\n```\n\n### Changelog\n\n**0.2.0**\n\n    - #5, #6, #7 Upgrade to py-moneyed 2.0, add babel format support (new field, `formatted`)\n    - **Breaking change**: removes `suffix` from schema, since babel doesn\'t support out of the box.\n\n\n**0.1.3**\n\n    Initial release, sort of.\n\n## Contributing\n\nRunning tests:\n\n```bash\npoetry run pytest\n```\n\nStill TODO. For now, please open a pull request or issue.\n',
    'author': 'Paul Craciunoiu',
    'author_email': 'paul@craciunoiu.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/UpliftAgency/graphene-djmoney',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
