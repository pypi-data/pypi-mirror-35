# drf-keyvalue

![coverage](https://gitlab.com/gitlab-org/gitlab-ce/badges/master/coverage.svg?job=coverage)

> Store and retrieve data in a consistent way in a key-value store using Django Rest Framework serializers

## About

**Supported backends**

* Redis

## Installation

```
pip install drf-keyvalue
```

## Setup

```

```

## Usage

For detailed usage, see the tests

```python

from drf_keyvalue.keyvalue import get_client

import redis
redis.StrictRedis(host='localhost', port=6379, db=0)

client = get_client('keyvalue.backends.RedisBackend', connection)

```

# Development

## Updating pypi repo:

1. Bump the version:

```

```

