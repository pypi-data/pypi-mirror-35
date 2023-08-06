# gnucash-portfolio-cli

Gnucash Portfolio CLI

If running a web UI (server + client) is problematic, here is the CLI interface to [GnuCash Portfolio](https://github.com/MisterY/gnucash-portfolio) functions, written in Python. This can be very useful if running the code on Android devices, for example.

Initially, there are a few simple scripts for providing the basic features. That might grow into a full CLI application at a later stage.

## Tips

Set the log level using `-v` parameter.

In general, it should be possible to set the log level with `--log=DEBUG` but this does not work when using argparse.

## Distribution

The new way of distributing packages is wia twine. Install: twine, keyring.
Configure [keyring support](https://twine.readthedocs.io/en/latest/#keyring-support).

Package the distribution: `python3 setup.py sdist bdist_wheel`.

Deploy to test: `twine upload -u <username> --repository-url https://test.pypi.org/legacy/ dist/*`

Deploy to Prod: `twine upload -u <username> --repository-url https://upload.pypi.org/legacy/ dist/*`
