# feedhenry.org

Website for the FeedHenry project. Built with Jekyll, Bootstrap 4,
Font Awesome, and hosted with GitHub pages.

## Requirements

1. Ensure you have Ruby >= 2.3:

    ```
    $ ruby -v
    ruby 2.3.3p222 (2016-11-21 revision 56859) [x86_64-darwin15]
    ```

2. Install Bundler

    ```
    gem install bundler
    ```

3. Install dependencies

    ```
    bundle install
    ```

## Development

```
bundle exec jekyll serve
```

Then, visit http://127.0.0.1:4000/.


## Updating GitHub metadata

The [projects page](http://feedhenry.org/projects/) uses GitHub metadata
(stars, forks, descriptions) when listing repositories. Since our repositories
span multiple GitHub organizations, we couldn't rely on [repository metadata](https://help.github.com/articles/repository-metadata-on-github-pages/)
provided to Jekyll sites hosted on GitHub pages. Therefore, we have a small
script for fetching this data and dumping it to `_data/feedhenry-repos.json`.
It should be run periodically and the changes committed.

```
pip install requests
pip install --pre github3.py
python _get_repo_data.py
```
