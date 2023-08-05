import requests
import click


@click.group()
def cli():
    """Command Line tool to access Github API.

    Know user info--> gitlo user <username>

    get repository-list by user--> gitlo repos <username>


    \b
    get language percentage of particular repository-->
    gitlo languages <username> <reponame> 
    """
    pass


@cli.command()
@click.argument('username')
def user(username):
    r = requests.get('https://api.github.com/users/{}'.format(username)).json()
    print('Name: {}, Repos: {}, Bio: {}'.format(r['name'], r['public_repos'], r['bio']))


@cli.command()
@click.argument('username')
def repos(username):
    r = requests.get('https://api.github.com/users/{}/repos'.format(username)).json()
    for i in range(len(r)):
        print(r[i]['name'])


def calculate_percentage(langs, lang, total_bytes):
    result = langs[lang] * 100 / total_bytes
    return round(result, 2)


def convert_to_percentage(langs):
    total_bytes = sum(langs.values())
    return {lang: calculate_percentage(langs, lang, total_bytes) for (lang, v) in langs.items()}


@cli.command()
@click.argument('username')
@click.argument('reponame')
def languages(username, reponame):
    r = requests.get('https://api.github.com/repos/{}/{}/languages'.format(username, reponame)).json()
    change_r = convert_to_percentage(r)
    for key, value in change_r.items():
        print('{}: {}%'.format(key, value))
