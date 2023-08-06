# envconfig2

envconfig2 is a simple library to make it easier to read config settings from
the environment.  It is modeled loosely after Kelsey Hightower's
[envconfig](https://github.com/kelseyhightower/envconfig) for Go.

## Examples

### String Example

    >>> import os
    >>> os.environ['DB_HOST'] = 'localhost'
    >>> os.environ['DB_PORT'] = '5432'
    >>> import envconfig2
    >>> envconfig2.string('DB_HOST')
    'localhost'
    >>> envconfig2.integer('DB_PORT')
    5432

### Integer Example

    >>> import os
    >>> os.environ['PORT'] = '80'
    >>> import envconfig2
    >>> envconfig2.integer('PORT')
    80

### Boolean Example

    >>> import os
    >>> os.environ['DEBUG'] = 'true'
    >>> import envconfig2
    >>> envconfig2.boolean('DEBUG')
    True

### List Example

    >>> import os
    >>> os.environ['USERS'] = 'user1,user2,user3'
    >>> import envconfig2
    >>> envconfig2.list('USERS')
    ['user1', 'user2', 'user3']

### JSON Example

    >>> import os
    >>> os.environ['JSON'] = '{"debug": true}'
    >>> import envconfig2
    >>> envconfig2.json('JSON')
    {u'debug': True}

### URL Example

By default envconfig2 will just verify that the given value can be parsed by urlparse.urlparse

    >>> import os
    >>> os.environ['URL'] = 'https://example.com'
    >>> import envconfig2
    >>> envconfig2.url('URL')
    'https://example.com'

If you would rather get a urlparse.Parse result you can tell envconfig2 to expand the url.

    >>> import os
    >>> os.environ['URL'] = 'https://example.com'
    >>> import envconfig2
    >>> envconfig2.url('URL', expand=True)
    ParseResult(scheme='https', netloc='example.com', path='', params='', query='', fragment='')

### Required Example

    >>> import envconfig2
    >>> envconfig2.string('API_KEY', required=True)
    ValueError: required environmnet variable API_KEY not set

### Default Example

    >>> import envconfig2
    >>> envconfig2.string('DB_HOST', default='localhost')
    'localhost'

### Prefixes

Sometimes it's useful to require a prefix on each variable as well.  This can
be done by setting `prefix` on the module itself.  envconfig2 will then look
for `{prefix}_{name}` as well as `name`.

    >>> import os
    >>> os.environ['MYAPP_DEBUG'] = 'True'
    >>> import envconfig2
    >>> envconfig2.prefix = 'MYAPP'
    >>> envconfig2.boolean('DEBUG')
    True

You can also set `prefix_required` to only look for `{prefix}_{name}`.

    >>> import os
    >>> os.environ['DEBUG'] = 'True'
    >>> import envconfig2
    >>> envconfig2.prefix = 'MYAPP'
    >>> envconfig2.boolean('DEBUG')
    True
    >>> envconfig2.prefix_required = True
    >>> envconfig2.boolean('DEBUG')
    None

Also, if a prefix is set, a variable having the prefix will be used before the
none prefixed variable.

    >>> import os
    >>> os.environ['MYAPP_USERNAME'] = 'user1'
    >>> os.environ['USERNAME'] = 'user2'
    >>> import envconfig2
    >>> envconfig2.prefix = 'MYAPP'
    >>> envconfig2.string('USERNAME')
    'user1'

## Licensing

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software Foundation,
Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301  USA

