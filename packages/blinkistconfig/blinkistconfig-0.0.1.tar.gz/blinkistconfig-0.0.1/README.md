# blinkist-config-python
The package simplifies accessing different configuration stores. The current supported stores are:
ENV - read from the application's environment variable
SSM - read from the AWS SSM Parameter Store
## Usage
### ENV
```python
import blinkistconfig.Config

# Setup the Config to use the ENV as config store
config = blinkistconfig.Config(env="development", app_name="my_nice_app", adapter_type="ENV")

my_config_value = config.get("some/folder/config")

# This is being translated to ENV["SOME_FOLDER_CONFIG"]

```

### SSM
For SSM this tool simulates namespace/directory functionality with each application
having its own. By default requesting a parameter myparam1 within the application
called my_nice_app will query the SSM parameter store for /application/my_nice_app/myparam1.

This harmonizes nicely with the ability of the SSM param store to do a prefix search.
The /application/my_nice_app prefix is the default "private" scope.


```python
import blinkistconfig.Config

# setup the Config to use the SSM as config store
config = blinkistconfig.Config(env="development", adapter_type="SSM", app_name="my_nice_app")

my_config_value = config.get("some/folder/config")

# This will try to get a parameter from SSM at "/application/my_nice_app/some/folder/config"

```

It is also possible to also have other scopes, possibly shared between the applications.
For example
```
my_config_value = config.get("another/config", scope="global")

# This will replace `my_nice_app` with `global` and try to resolve "/application/global/another/config"
```

## Development

To install development requirements

```bash
pip install -r requirements/dev.txt
pip install -e .
```

To run tests

```bash
AWS_DEFAULT_REGION="us-east-1" pytest --spec
```

## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/blinkist/blinkist-config-python.

## License

The package is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
