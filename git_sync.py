# System
import os
import subprocess


# Globals
script_dir = os.path.dirname(os.path.realpath(__file__))
mirror_dir = os.path.join(script_dir, "local-mirrors")


def safe_filename(prospective_filename):
    """
    Removes unsafe characters from a string
    """

    safe_filename = ""

    for character in prospective_filename:
        if character.isalpha() or character.isdigit() or character == ' ':
            safe_filename += character

    return safe_filename


def update_local_mirror(origin):
    """
    Create or update a local version of the git repository
    with 'git clone --mirror'
    """

    if not os.path.exists(mirror_dir):
        os.makedirs(mirror_dir)

    local_mirror_dirname = safe_filename(origin)
    local_mirror_dirpath = os.path.join(
        mirror_dir,
        local_mirror_dirname + '.git'
    )

    if not os.path.exists(local_mirror_dirpath):
        mirror_command = 'git clone --mirror {url} {dir}'.format(
            url=origin, dir=local_mirror_dirpath
        )

        print "\n= " + mirror_command + " ="
        print subprocess.check_output(
            mirror_command.split(),
            stderr=subprocess.STDOUT
        )
        print "= Cloned " + origin + " =\n"
    else:
        original_dir = os.getcwd()
        os.chdir(local_mirror_dirpath)

        update_command = 'git remote update'

        print "\n= " + update_command + " ="
        print subprocess.check_output(update_command.split())
        print "= Updated " + local_mirror_dirpath + " =\n"

        os.chdir(original_dir)

    return local_mirror_dirpath


def upload_mirror(local_mirror_dir, destination):
    """
    Upload a local mirrored repository to remote destination
    """

    original_dir = os.getcwd()
    os.chdir(local_mirror_dir)

    upload_command = 'git push --mirror {destination}'.format(
        destination=destination
    )

    print "\n= " + upload_command + " ="
    print subprocess.check_output(upload_command.split())
    print "= Uploaded to " + destination + " =\n"

    os.chdir(original_dir)


def copy_repository(origin, destination):
    """
    Copy a remote origin repository to a remote destination
    """

    local_dir = update_local_mirror(origin)
    upload_mirror(local_dir, destination)
