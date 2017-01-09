"""
Script for importing feedhenry repo data from GitHub. Written in Python because
I didn't have time to learn Ruby :) Should probably be rewritten in Ruby to be
consistent with Jekyll.

How to run:

$ pip install requests
$ pip install --pre github3.py
$ python _get_repo_data.py
"""

import json
import github3

def get_repo_data(org_name):
    repos = github3.repositories_by(org_name)
    repos_dict = {}
    for r in repos:
        repos_dict[r.name] = {
            'name': r.name,
            'description': r.description,
            'html_url': r.html_url,
            'stargazers_count': r.stargazers_count,
            'forks_count': r.forks_count
        }
    return repos_dict

if __name__ == '__main__':
    all_repos = get_repo_data('feedhenry')
    all_repos.update(get_repo_data('feedhenry-raincatcher'))
    all_repos.update(get_repo_data('feedhenry-templates'))
    all_repos.update(get_repo_data('aerogear'))

    with open('_data/feedhenry-repos.json', 'w') as f:
        json.dump(all_repos, f, indent=4, sort_keys=True)
