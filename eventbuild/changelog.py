from base64 import b64encode

import github
import re
import time
import datetime
import requests

# changelog = eventlog.get_file_contents('ChangeLog')


date_time = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})')
release = re.compile(r'release.*|preparation.*')

def _get_commits_by_time(repo):
    commits = repo.get_commits()
    sections = [commit for commit in commits if datetime.match(commit.commit.message)]


def _is_header(entry):
  return release.search(entry.commit.message.split('\n')[0]) != None


def _generate_raw_draft(entries, msg=None):
    draft = []
    if msg:
        draft.append({ 'title': msg, 'body': []})

    for entry in entries:
       if _is_header(entry):
         draft.append({'title': entry, 'body': []})
       else:
         if len(draft) != 0:
           draft[-1]["body"].append(entry)

    return draft
        
def format_title(title, user):
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if not (isinstance(title, unicode) or isinstance(title, str)):
        title = title.commit.message.split('\n')[0]
    
    
    return '''\n{} {} <{}>
        Summary:
          {}
    '''.format(date, user.name.encode('latin1'), user.email, title)


def format_body(entries):
    body = """
        Revisions:
    """

    for entry in entries:
        
        body += '\t\t* {}\n'.format(entry.commit.message.split('\n')[0])
        
    return body + '\n\n'

def date_last_entry(repo, path="Changelog"):
    changelog = repo.get_file_contents(path)
    changelog_content  = changelog.decoded_content.split('\n')
    last_entry = filter(lambda entry: date_time.match(entry), changelog_content)[0]
    strtime = date_time.search(last_entry).group(0)
    epoch = time.mktime(time.strptime(strtime, "%Y-%m-%d %H:%M:%S"))
    return datetime.datetime.fromtimestamp(epoch)


def get_new_entries(repo, time):
    return repo.get_commits(since=time)


def generate_draft(entries, user, msg=None):
    draft = ''
    raw_draft = _generate_raw_draft(entries, msg)
    for entry in raw_draft:
        draft += format_title(entry['title'], user)
        draft += format_body(entry['body'])

    return draft


def update_changelog(gh, repo, user, msg, path='Changelog', branch='master'):
    changelog = repo.get_file_contents(path)
    changelog_content  = changelog.decoded_content

    last_entry = date_last_entry(repo, path)
    entries = get_new_entries(repo, last_entry)

    draft = generate_draft(entries, user, msg)

    put_parameters = {
        'path': path,
        'message': msg,
        'content': b64encode(draft + '\n' + changelog_content),
        'sha': changelog.sha,
        'branch': branch
    }

    status, headers, data = gh._Github__requester.requestJson('PUT',
                                                              '/repos/{}/{}/contents/{}'.format(repo.owner.login, repo.name, path), 
                                                              input=put_parameters)

    return [status, headers, data] 
