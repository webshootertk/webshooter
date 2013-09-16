# Webshooter
Webshooter is a command-line assistant to the static website generator
[Hyde][hyde/hyde]. It produces Hyde-ready websites in the user's choice of
layout and automates page creation and site configuration through user prompts
and command line arguments.

Webshooter is built to be compatible with the following site layouts, but should
still work in templates that have matching variable names in `config.yaml`:

  * [Bootstrap][twitter/bootstrap] via [aims-group/hyde-bootstrap][]
  * [aims-group/one.5lab][aims-group/one.5lab]
  * [aims-group/tshirt][aims-group/tshirt]

## Requirements

### Packages
* Python
* pip
* distribute==0.6.19
* fs==0.4.0
* hyde==0.8.4
* wsgiref==0.1.2

### Set Up Working Environment

* [Documentation][documentation]

## Usage

### Generating a new site
To generate a new site, run

    ./webshooter.py new

which will prompt you for a details about your desired site, then create a new
folder in the current working directory to hold it.


### Regenerating an existing site
To regenerate the static content of an existing site, run

    ./webshooter.py gen <path>

where `path` is the full or relative path to a site which has been generated
with `new`. For now, this is identical to running `hyde gen` inside `path`.

### Updating your site with its template's changes
If the template you're using gets updated after you've generated your site and
you want to incorporate some or all of those changes into your site, you can use
`git cherry-pick` to selectively grab the commits you want.

Let's assume your
website is its own git repository, with no more ties to the template repo. Let's
also assume you're using hyde-bootstrap as your template (though the process is
the same for other templates as well).

First, set up your parent template as a remote and fetch its changes:

    git remote add hyde-bootstrap git://github.com/aims-group/hyde-bootstrap
    git fetch hyde-bootstrap

Fetching doesn't overwrite anything or try to merge any code (pulling does).
Once you've fetched changes, you can cherry-pick the ones you want. If you just
want the changes performed by the most recent commit of hyde-bootstrap, you can
do

    git cherry-pick hyde-bootstrap/master

Otherwise you can specify a specific commit hash or use one of several other
ways of specifying commits. See `man git-cherry-pick` for more info.

When you're done, just `git commit`, add to the prepopulated commit message if
you like, and you're ready to push.

# HTML Cleaner

## Requirements

### Packages

* html5lib

## Usage

    ./htmlcleaner.py -help
    usage: htmlcleaner.py [-h] [--preserve PRESERVE] infile outfile

    Extracts text from body of an HTML document

    positional arguments:
      infile                Path to HTML file
      outfile               Path to desired output file

    optional arguments:
      -h, --help            show this help message and exit
      --preserve PRESERVE, -p PRESERVE
                            Repeatable parameter that adds a tag name to preserve
                            (e.g. htmlcleaner.py -p a -p img)

    ./htmlcleaner.py inputFile outputFile -p ignore-tag
 

[hyde/hyde]:                 https://github.com/hyde/hyde
[twitter/bootstrap]:         https://github.com/twitter/bootstrap
[aims-group/one.5lab]:       https://github.com/aims-group/one.5lab
[aims-group/hyde-bootstrap]: https://github.com/aims-group/hyde-bootstrap
[aims-group/tshirt]:         https://github.com/aims-group/tshirt
[documentation]:             https://github.com/aims-group/esgf-site/wiki
