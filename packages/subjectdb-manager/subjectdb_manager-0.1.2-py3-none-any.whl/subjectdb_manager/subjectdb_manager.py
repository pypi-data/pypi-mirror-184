''' subjectdb manager for local subjectdb only '''

import os
from pprint import pprint
import sys
import uuid

import arrow
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
@click.option('--org-id', type=str, default='all',
              help="List a specific org only")
def ls(file, list_orgs, org_id):
    '''
    List the subjectdb file
    '''

    subject_db = _read_db_file(file)

    if list_orgs:
        for org in subject_db.keys():
            print(org)
    elif 'all' not in org_id:
        pprint(subject_db[org_id])
    else:
        pprint(subject_db)
    # else:
    #     for org, subjects in subject_db.items():
    #         if 'all' in org_id or org in org_id:
    #             print(org)
    #             for subject, subject_guid in subjects.items():
    #                 print(f' {subject}: {subject_guid}')
    #         # elif org in org_id:
    #         #     print(org)
    #         #     for subject, subject_guid in subjects.items():
    #         #         print(f' {subject}: {subject_guid}')


@click.command()
@click.argument('file')
@click.option('--subject-id', required=True)
@click.option('--org-id', required=True)
def add_subject(file, subject_id=None, org_id=None):
    '''
    Add a single subject to a db
    '''

    # read in the file
    subject_db = _read_db_file(file)

    print(subject_db.keys())
    # check to see if the subject_id already exists
    if subject_id in subject_db[org_id]['subjects'].keys():
        print(f'subject_id {subject_id} already exists in {org_id}.')
        if 'y' not in input('Overwrite? ').lower():
            print('Quitting without update!')
            sys.exit()

    # Generate subject and add to the db
    subject_guid = _make_subject_record(subject_id)

    subject_db[org_id]['subjects'][subject_id] = subject_guid

    _write_db_file(file, subject_db)

    print(f'Added subject: {subject_id}: {subject_guid}')


@click.command()
@click.argument('file')
@click.option('--subject-id', '-u', required=True)
@click.option('--org-id', required=True)
def remove_subject(file, subject_id, org_id):
    '''
    remove a single subject from a db
    '''

    # read in the file
    subject_db = _read_db_file(file)

    if subject_id in subject_db[org_id]['subjects'].keys():
        subject_db[org_id]['subjects'].pop(subject_id)
        _write_db_file(file, subject_db)
        print(f'Removed {subject_id} from org: {org_id}')
    else:
        print(f'Unable to remove subject {subject_id}: Not Found')


@click.command()
@click.argument('import_file')
@click.argument('output_file')
@click.option('--org-id', required=True, help='org_id for this subject group')
@click.option('--dryrun', is_flag=True,
              help='Print result instead of writing file')
def import_subjects(import_file, output_file, org_id, dryrun):
    '''
    read in a text file and create or add to a subject db file
    NOTE: existing users will not be overwritten!
    '''

    # Check to see if the output db file exists first
    # if the file exists ask if new subjects should be merged in
    if os.path.exists(output_file):
        print(f'File already exists: {output_file}')
        if 'y' in input('Merge new subjects? ').lower():
            # go ahead and read the file in
            subject_db = _read_db_file(output_file)
            if org_id not in subject_db.keys():
                # init the org
                subject_db[org_id] = {}
        else:
            print('Bye!')
            sys.exit()

    else:
        # create an empty db dict
        subject_db = {
            org_id: {
                'created_on': arrow.now().for_json(),
                'org_guid': uuid.uuid4().hex,
                'subjects': {}
                }
            }

    # open the source file
    for new_subject in open(import_file, 'r').readlines():

        new_subject = new_subject.strip()
        if len(new_subject) < 1:
            continue

        if new_subject in subject_db[org_id]['subjects'].keys():
            print(f'Subject exists, skipping: {new_subject}')
            continue

        subject_db[org_id]['subjects'][new_subject] = \
            _make_subject_record(new_subject)

        print(f'Added subject {new_subject}: \
              {subject_db[org_id]["subjects"][new_subject]}')

    # are we a dry run?
    if dryrun is True:
        print(yaml.dump(subject_db))
    else:
        # write out the db file
        _write_db_file(output_file, subject_db)
        print('Done!')


def _make_subject_record(subject_id):

    return {
        'subject_guid': uuid.uuid4().hex,
        'created_on': arrow.now().for_json()
        }


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
cli.add_command(remove_subject)
cli.add_command(import_subjects)
