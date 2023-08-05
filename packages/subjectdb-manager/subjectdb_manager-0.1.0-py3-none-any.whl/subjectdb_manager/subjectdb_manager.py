''' subjectdb manager for local subjectdb only '''

import uuid
import sys

import click
import yaml


# define the cli group
@click.group()
def cli():
    '''
    Click command group
    '''

    pass


@click.command()
@click.argument('file')
@click.option('--list-orgs', is_flag=True, help='List only the organizations')
@click.option('--org-name', type=str, default='all',
              help="List a specific org only")
def ls(file, list_orgs, org_name):
    '''
    List the subjectdb file
    '''

    subject_db = _read_db_file(file)

    if list_orgs:
        for org in subject_db.keys():
            print(org)
    else:
        for org, subjects in subject_db.items():
            if 'all' in org_name or org in org_name:
                print(org)
                for subject, subject_guid in subjects.items():
                    print(f' {subject}: {subject_guid}')
            # elif org in org_name:
            #     print(org)
            #     for subject, subject_guid in subjects.items():
            #         print(f' {subject}: {subject_guid}')


@click.command()
@click.argument('file')
@click.option('--subject_id', '-u', required=True)
@click.option('--org_id', required=True)
def add_subject(file, subject_id=None, org_id=None):
    '''
    Add a single subject to a db
    '''

    # read in the file
    subject_db = _read_db_file(file)

    print(subject_db.keys())
    # check to see if the subject_id already exists
    if subject_id in subject_db[org_id].keys():
        print(f'subject_id {subject_id} already exists in {org_id}.')
        if 'y' not in input('Overwrite? ').lower():
            print('Quitting without update!')
            sys.exit()

    # Generate subject and add to the db
    subject_guid = uuid.uuid4().hex

    subject_db[org_id][subject_id] = subject_guid

    _write_db_file(file, subject_db)

    print(f'Added subject: {subject_id}: {subject_guid}')


def _read_db_file(file):
    '''
    Internal function to load yaml in as a dict we can work with
    '''

    try:
        with open(file, 'r') as in_file:
            subject_db = in_file.read()
    except Exception as e:
        print(f'Unable to read file: {e}')

    return yaml.full_load(subject_db)


def _write_db_file(file, subject_db):
    '''
    Internal function to write dict to yaml file
    '''
    subject_id = yaml.dump(subject_db)

    try:
        with open(file, 'w') as out_file:
            out_file.write(subject_id)
    except Exception as e:
        print(f'Unable to write yaml db: {e}')


cli.add_command(ls)
cli.add_command(add_subject)
