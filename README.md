# Webshooter
Webshooter is a command-line assistant to the static website generator
[Hyde][hyde/hyde]. It produces Hyde-ready websites in the user's choice of
layout and automates page creation and site configuration through user prompts
and command line arguments.

Webshooter is built to be compatible with the following site layouts, but should
still work in templates that have matching variable names in `config.yaml`:

  * [Bootstrap][twitter/bootstrap] via [aims-group/hyde-bootstrap][]
  * ~~[aims-group/one.5lab][]~~ (not yet)
  * ~~[aims-group/tshirt][]~~ (not yet)

## Usage
To generate a new site, run

    ./webshooter.py new

which will prompt you for a details about your desired site, then create a new
folder in the current working directory to hold it.

To regenerate the static content of an existing site, run

    ./webshooter.py gen <path>

where `<path>` is the full or relative path to a site which has been generated
with `new`.

[hyde/hyde]: https://github.com/hyde/hyde
[twitter/bootstrap]: https://github.com/twitter/bootstrap
[aims-group/one.5lab]: https://github.com/aims-group/one.5lab
[aims-group/hyde-bootstrap]: https://github.com/aims-group/hyde-bootstrap
[aims-group/tshirt]: https://github.com/aims-group/tshirt
