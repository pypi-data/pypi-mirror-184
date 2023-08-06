# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['secured_fields',
 'secured_fields.fields',
 'secured_fields.management.commands']

package_data = \
{'': ['*']}

install_requires = \
['cryptography>=35', 'django>=3.1']

setup_kwargs = {
    'name': 'django-secured-fields',
    'version': '0.4.2',
    'description': '',
    'long_description': '# Django Secured Fields\n\n[![GitHub](https://img.shields.io/github/license/C0D1UM/django-secured-fields)](https://github.com/C0D1UM/django-secured-fields/blob/main/LICENSE)\n[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/C0D1UM/django-secured-fields/ci.yml?branch=main)](https://github.com/C0D1UM/django-secured-fields/actions/workflows/ci.yml)\n[![codecov](https://codecov.io/gh/C0D1UM/django-secured-fields/branch/main/graph/badge.svg?token=PN19DJ3SDF)](https://codecov.io/gh/C0D1UM/django-secured-fields)\n[![PyPI](https://img.shields.io/pypi/v/django-secured-fields)](https://pypi.org/project/django-secured-fields/)  \n[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-secured-fields)](https://github.com/C0D1UM/django-secured-fields)\n\nDjango encrypted fields with search enabled.\n\n## Features\n\n- Automatically encrypt/decrypt field value using [cryptography](https://github.com/pyca/cryptography)\'s [Fernet](https://cryptography.io/en/latest/fernet)\n- Built-in search lookup on the encrypted fields from [hashlib](https://docs.python.org/3/library/hashlib.html)\'s _SHA-256_ hash value. `in` and `isnull` lookup also supported.\n- Supports most of available Django fields including `BinaryField`, `JSONField`, and `FileField`.\n\n## Installation\n\n```bash\npip install django-secured-fields\n```\n\n## Setup\n\n1. Add `secured_fields` into `INSTALLED_APPS`\n\n   ```python\n   # settings.py\n\n   INSTALLED_APPS = [\n       ...\n       \'secured_fields\',\n   ]\n   ```\n\n2. Generate a new key using for encryption\n\n   ```bash\n   $ python manage.py generate_key\n   KEY: TtY8MAeXuhdKDd1HfGUwim-vQ8H7fXyRQ9J8pTi_-lg=\n   HASH_SALT: 500d492e\n   ```\n\n3. Put generated key and hash salt in settings\n\n   ```python\n   # settings.py\n\n   SECURED_FIELDS_KEY = \'TtY8MAeXuhdKDd1HfGUwim-vQ8H7fXyRQ9J8pTi_-lg=\'\n   SECURED_FIELDS_HASH_SALT = \'500d492e\'  # optional\n   ```\n\n## Usage\n\n### Simple Usage\n\n```python\n# models.py\nimport secured_fields\n\nphone_number = secured_fields.EncryptedCharField(max_length=10)\n```\n\n### Enable Searching\n\n```python\n# models.py\nimport secured_fields\n\nid_card_number = secured_fields.EncryptedCharField(max_length=18, searchable=True)\n```\n\n## Supported Fields\n\n- `EncryptedBinaryField`\n- `EncryptedBooleanField`\n- `EncryptedCharField`\n- `EncryptedDateField`\n- `EncryptedDateTimeField`\n- `EncryptedDecimalField`\n- `EncryptedFileField`\n- `EncryptedImageField`\n- `EncryptedIntegerField`\n- `EncryptedJSONField`\n- `EncryptedTextField`\n\n## Settings\n\n| Key | Required | Default | Description |\n| --- | -------- | ------- | ----------- |\n| `SECURED_FIELDS_KEY` | Yes | | Key for using in encryption/decryption with Fernet. Usually generated from `python manage.py generate_key`. |\n| `SECURED_FIELDS_HASH_SALT` | No | `\'\'` | Salt to append after the field value before hashing. Usually generated from `python manage.py generate_key`. |\n| `SECURED_FIELDS_FILE_STORAGE` | No | `\'secured_fields.storage.EncryptedFileSystemStorage\'` | File storage class used for storing encrypted file/image fields. See [EncryptedStorageMixin](#encryptedstoragemixin) |\n\n## APIs\n\n### Field Arguments\n\n| Name | Type | Required | Default | Description |\n| ---- | ---- | -------- | ------- | ----------- |\n| `searchable` | `bool` | No | `False` | Enable search function |\n\n### Encryption\n\n```python\n> from secured_fields.fernet import get_fernet\n\n> data = b\'test\'\n\n> encrypted_data = get_fernet().encrypt(data)\n> encrypted_data\nb\'gAAAAABh2_Ry_thxLTuFFXeMc9hNttah82979JPuMSjnssRB0DmbgwdtEU5dapBgISOST_a_egDc66EG_ZtVu_EqF_69djJwuA==\'\n\n> get_fernet().decrypt(encrypted_data)\nb\'test\'\n```\n\n### `EncryptedMixin`\n\nIf you have a field which does not supported by the package, you can use `EncryptedMixin` to enable encryption and search functionality for that custom field.\n\n```python\nimport secured_fields\nfrom django.db import models\n\nclass EncryptedUUIDField(secured_fields.EncryptedMixin, models.UUIDField):\n    pass\n\ntask_id = EncryptedUUIDField(searchable=True)\n```\n\n### `EncryptedStorageMixin`\n\nIf you use a custom file storage class (e.g. defined in `settings.py`\'s `DEFAULT_FILE_STORAGE`), you can enable file encryption using `EncryptedStorageMixin`.\n\n```python\nimport secured_fields\nfrom minio_storage.storage import MinioMediaStorage\n\nclass EncryptedMinioMediaStorage(\n    secured_fields.EncryptedStorageMixin,\n    MinioMediaStorage,\n):\n    pass\n```\n\n## Known Limitation\n\n- `in` lookup on `JSONField` is not available\n- Large files are not performance-friendly at the moment (see [#2](https://github.com/C0D1UM/django-secured-fields/issues/2))\n- Search on `BinaryField` does not supported at the moment (see [#6](https://github.com/C0D1UM/django-secured-fields/issues/6))\n- Changing `searchable` value in a field with the records in the database is not supported (see [#7](https://github.com/C0D1UM/django-secured-fields/issues/7))\n\n## Development\n\n### Requirements\n\n- Docker\n- Poetry\n- MySQL Client\n  - `brew install mysql-client`\n  - `echo \'export PATH="/usr/local/opt/mysql-client/bin:$PATH"\' >> ~/.bash_profile`\n\n### Running Project\n\n1. Start backend databases\n\n   ```bash\n   make up-db\n   ```\n\n2. Run tests (see: [Testing](#testing))\n\n### Linting\n\n```bash\nmake lint\n```\n\n### Testing\n\n```bash\nmake test\n```\n\n### Fix Formatting\n\n```bash\nmake yapf\n```\n',
    'author': 'CODIUM',
    'author_email': 'support@codium.co',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/C0D1UM/django-secured-fields',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
