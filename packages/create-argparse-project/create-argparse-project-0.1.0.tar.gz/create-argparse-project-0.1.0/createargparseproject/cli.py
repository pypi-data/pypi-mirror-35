import argparse
from pathlib import Path
import shutil
import os
from .__init__ import __version__


def show_version():
    print('Create Click Project v{}'.format(__version__))


def fill_empty_input(value, text):
    if value is None:
        return input(text + ' > ')
    return value


def main():
    show_version()
    parser = argparse.ArgumentParser(
        description='Create new argparse project.')
    parser.add_argument('-n', '--project-name', dest='project_name', type=str,
                        help='project name show on start project(Create Argparse Project)')
    parser.add_argument('-p', '--package', dest='package_name',
                        help='package name(createargparseproject)')
    parser.add_argument('-a', '--author', dest='author_name',
                        help='author name')
    parser.add_argument('-e', '--email', dest='author_email',
                        help='author email')
    parser.add_argument('-u', '--repository', dest='repository_url',
                        help='repository url')
    parser.add_argument('-d', '--description', dest='description',
                        help='project description')
    parser.add_argument('-c', '--command-name',
                        dest='command_name', help='command name')
    args = parser.parse_args()
    project_name = fill_empty_input(args.project_name, 'Project Name')
    package_name = fill_empty_input(args.package_name, 'Package Name')
    author_name = fill_empty_input(args.author_name, 'Author Name')
    author_email = fill_empty_input(args.author_email, 'Author Email')
    repository_url = fill_empty_input(args.repository_url, 'Repository URL')
    description = fill_empty_input(args.description, 'Description')
    command_name = fill_empty_input(args.command_name, 'Command Name')
    p = Path('.')
    project_dir = p / project_name.lower().replace(' ', '-')
    if project_dir.exists():
        if project_dir.is_dir():
            try:
                project_dir.rmdir()
            except OSError:
                print(
                    'Fail to initialize the project directory. The directory is not empty.')
                exit(1)
        else:
            print('Fail to create a project directory. A same name file exists.')
            exit(1)
    template_dir = Path(__file__).parent.parent / \
        'createargparseproject_template'
    print('Copying template ...', end='')
    shutil.copytree(str(template_dir), str(project_dir))
    print(' done.')
    print('Generating files .', end='')
    default_package_dir = project_dir / 'PACKAGE_NAME'
    package_dir = project_dir / package_name
    shutil.move(default_package_dir, package_dir)
    print('.', end='')
    for p in project_dir.glob('**/*'):
        if not p.is_file():
            continue
        if p.parent.name == '__pycache__':
            continue

        print('.', end='')
        print(str(p))
        with p.open() as f:
            texts = f.read()
        texts = texts.replace('PROJECT_NAME', project_name)
        texts = texts.replace('PACKAGE_NAME', package_name)
        texts = texts.replace('AUTHOR_NAME', author_name)
        texts = texts.replace('AUTHOR_EMAIL', author_email)
        texts = texts.replace('REPOSITORY_URL', repository_url)
        texts = texts.replace('DESCRIPTION', description)
        texts = texts.replace('COMMAND_NAME', command_name)
        with p.open(mode='w') as f:
            f.write(texts)
    print(' done.')
    print('Deleting unnecesarry files ...', end='')
    os.remove(str(project_dir / '__init__.py'))
    shutil.rmtree(str(project_dir / '__pycache__'))
    shutil.rmtree(str(package_dir / '__pycache__'))
    print(' done.')
    print('')
    print('Finished.')


if __name__ == '__main__':
    main()
