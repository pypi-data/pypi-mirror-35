import hashlib
import io
import os
import re
import sys
import zipfile
from glob import glob
from contextlib import contextmanager
import subprocess
from io import BytesIO
from shutil import rmtree
from tarfile import TarFile

from time import sleep

from genius_cli.blocks import render_blocks


@contextmanager
def chdir(path):
    cwd = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(cwd)


def write_generated_file(path, source):

    # special hack for settings.py->SECRET_KEY
    if path.endswith('app/settings.py'):
        if os.path.exists(path):
            with open(path, 'r') as f:
                found = re.search('^SECRET_KEY\s*=.*$', f.read(), flags=re.MULTILINE)
                if found:
                    current_key = found.group(0)
                    new_key = re.search('^\s*SECRET_KEY\s*=.*$', source, flags=re.MULTILINE).group(0)
                    source = source.replace(new_key, current_key)

    dirname = os.path.dirname(path)
    if dirname and len(dirname) and not os.path.exists(dirname):
        os.makedirs(dirname)

    chksum = source_hash(source)

    tag = f"generated: {chksum}"

    # print('---')
    # print(path)
    if path.endswith('.py') or path.endswith('requirements.txt') or path.endswith('Dockerfile'):
        source_prefix = f"# {tag}\n\n"

    elif path.endswith('.js') or path.endswith('.jsx'):
        source_prefix = f"//# {tag}\n\n"
        # print('js!')

    elif ('/templates/' in path or '/themes/' in path) and path.endswith('.html'):
        source_prefix = f"{{# {tag} #}}\n\n"

    else:
        source_prefix = ''
    #     print('exists: ', path)

    if os.path.exists(path):
        generated, changed, file_checksum = is_generated_file(path)

        if generated:
            if changed:
                print(f'Warning: file {path} is skipped, as it has #generated marker, but was modified by hands.'
                      f'Either delete file to regenerate file, or remove marker to hide this warning.')
                return  # checksum failed. Changed by hands?
            else:
                if file_checksum == chksum:
                    return  # already up to date
        else:
            # print(f'skip: {path}')
            return  # file intentionally overridden. Do not overwrite!

    with open(path, 'w') as f:
        if source_prefix:
            f.write(source_prefix)
        f.write(source)
        # print(f'write: {path}')


def is_generated_file(path):
    """
    Checks if file is generated, and is it changed
    :param path:

    :return: generated, changed, checksum
    """
    with open(path, 'r') as f:
        content = f.read()
        match = re.match('^({|//)?# generated: ([a-f0-9]{32})( #})?\n\n', content)
        if match:
            file_chk_expected = match.group(2)
            real_source = content[len(match.group(0)):]
            file_chk_real = source_hash(real_source)

            if file_chk_expected != file_chk_real:
                print(f'Warning: file {path} is skipped, as it has #generated marker, but was modified by hands.'
                      f'Either delete file to regenerate file, or remove marker to hide this warning.')

                return True, True, file_chk_real  # checksum failed. Changed by hands?
            else:
                return True, False, file_chk_real
        else:
            return False, False, None


def source_hash(source):
    hash_md5 = hashlib.md5()
    source = source.strip()
    hash_md5.update(source.encode())

    return hash_md5.hexdigest()


def copy_generated_tree(source_path, target_path, glob_expr="**/*"):
    files = []

    with chdir(source_path):
        for file in glob(glob_expr, recursive=True):
            with open(file, 'r') as f:
                files.append((file, f.read()))

    with chdir(target_path):
        for path, source in files:
            write_generated_file(path, source)


def clean_up_generated_files(path, file_list, remove_root=False):
    for file in os.listdir(path):
        if file == 'node_modules':
            continue

        fullpath = os.path.join(path, file)

        if os.path.isdir(fullpath):
            clean_up_generated_files(fullpath, file_list, remove_root=True)
        else:
            if file.split('.')[-1] in ('js', 'jsx', 'py', 'html'):
                generated, changed, file_checksum = is_generated_file(fullpath)

                if generated and not changed and fullpath not in file_list:
                    os.unlink(fullpath)
                    print('removing: ', fullpath)

    if len(os.listdir(path)) == 0 and remove_root:
        os.rmdir(path)
        print('removing: ', path)


def extract_files(dst, file_bytes):
    files = zipfile.ZipFile(BytesIO(file_bytes), mode='r', compression=zipfile.ZIP_LZMA)

    for path in files.namelist():
        full_path = os.path.join(dst, path)
        write_generated_file(full_path, files.read(path).decode())

    clean_up_generated_files('.', [f"./{x}" for x in files.namelist()])


def collect_files(src):
    with chdir(src):
        f = io.BytesIO()
        files = zipfile.ZipFile(f, mode='w', compression=zipfile.ZIP_LZMA)

        for path in get_user_paths():
            generated, changed, checksum = is_generated_file(path)

            if not generated or changed:
                files.write(path)
        files.close()

        f.seek(0)

    return f


def get_user_paths():
    paths = []
    paths += list(glob('*.col'))
    paths += list(glob('react/src/**/*.js', recursive=True))
    paths += list(glob('react/src/**/*.jsx', recursive=True))
    paths += list(glob('react/*.js'))
    paths += list(glob('react/*.json'))

    return set(paths)


def collect_app_names():
    collections = []
    for filename in os.listdir('.'):
        if os.path.isfile(filename) and filename.endswith('.col'):
            if not re.match('^[a-zA-Z][a-zA-Z0-9_]+\.col$', filename):
                print('Collection file has incorrect name: {}'.format(filename))
            app_name = filename[0:-4]
            collections.append(app_name)
    return collections


def migrate_db(apps, features=None):
    django_command = get_django_command(features)

    for app_name in apps:
        subprocess.run('{} makemigrations {}'.format(django_command, app_name), shell=True, check=True)
        try:
            subprocess.run('{} migrate'.format(django_command), shell=True, check=True)
            # subprocess.run('{} migrate {}'.format(django_command, app_name), shell=True, check=True)
        except subprocess.CalledProcessError:
            pass

        # if cratis
        if django_command == 'django':
            subprocess.run('{} sync_translation_fields_safe'.format(django_command), shell=True, check=True)


def run_django(features=None, run_host='127.0.0.1:8000'):
    django_command = get_django_command(features,)
    print(django_command)
    return subprocess.Popen('{} runserver --noreload {}'.format(django_command, run_host), shell=True)


def remove_db(apps, features=None):
    django_command = get_django_command(features)

    for app_name in apps:
        filename = '{}.col'.format(app_name)
        if not os.path.exists(filename):
            print('No such collection: {}'.format(app_name))
        app_name = app_name

        print('Unapplying migrations')
        subprocess.run('{} migrate {} zero'.format(django_command, app_name), shell=True, check=True)

        print('Removing migrations')
        rmtree('{}/migrations'.format(app_name))


def get_django_command(features):
    is_cratis = features and 'cratis' in features
    if is_cratis:
        django_command = 'django'
    else:
        django_command = 'python manage.py'
    return django_command


def install_deps():
    subprocess.run('pip install -r requirements.txt', shell=True, check=True)


def wait_for_file_changes(paths, initial=True, watch=True):
    if initial:
        yield

    if watch:
        initial_hash = files_hash(paths)

        while True:
            sleep(1.0)
            new_hash = files_hash(paths)
            if initial_hash != new_hash:
                initial_hash = new_hash
                yield


def files_hash(paths):
    hash_md5 = hashlib.md5()

    for filename in paths:
        try:
            with open(filename, "rb") as f:
                for chunk in iter(lambda: f.read(2 ** 20), b""):
                    hash_md5.update(chunk)
        except (FileNotFoundError, IOError):
            pass

    return hash_md5.hexdigest()
