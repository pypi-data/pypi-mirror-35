#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
import os
import sys
import errno
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup
from setuptools.command.install import install as InstallCommand
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()


def _fix_ownership(path):
    uid = os.environ.get('SUDO_UID')
    gid = os.environ.get('SUDO_GID')
    if uid is not None:
        os.chown(path, int(uid), int(gid))


class PyInstall(InstallCommand):

    def run(self):
        InstallCommand.run(self)
        self.setup_config_dirs()

    def setup_config_dirs(self):
        sys.stdout.write("Writing config files\n")
        default_config_file = 'data/gitlab_tools.conf'
        for main_dir in ['/etc/deployv', os.path.expanduser('~/.config/deployv')]:
            addon_dir = os.path.join(main_dir, 'conf.d')
            config_file_name = os.path.join(addon_dir, 'gitlab_tools.conf')
            error_msg = "Couldn't write config file: '{file}' (skipped)\n"
            ok_msg = "Created config file: '{file}'\n"
            is_user_dir = os.path.expanduser('~/') in main_dir
            try:
                os.makedirs(addon_dir)
            except OSError as error:
                if error.errno != errno.EEXIST:
                    sys.stdout.write(error_msg.format(file=config_file_name))
                    continue
            else:
                if is_user_dir:
                    for path in [main_dir.replace('/deployv', ''), main_dir, addon_dir]:
                        _fix_ownership(path)
            config = ConfigParser()
            config.read([default_config_file, config_file_name])
            try:
                with open(config_file_name, 'w+') as config_file:
                    config.write(config_file)
            except (OSError, IOError) as error:
                sys.stdout.write(error_msg.format(file=config_file_name))
            else:
                sys.stdout.write(ok_msg.format(file=config_file_name))
                if is_user_dir:
                    _fix_ownership(config_file_name)


setup(
    name='deployv-addon-gitlab-tools',
    version='0.2.21',
    license='BSD',
    description='Deployv addon: Gitlab tools. Generated by cookiecutter and cookiecutter-deploy-addon.',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Vauxoo',
    author_email='info@vauxoo.com',
    url='https://github.com/Vauxoo/deployv-addon-gitlab-tools',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    package_data={'': ['data/*']},
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=[
        'deployv'
    ],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
    cmdclass={
        'install': PyInstall,
    },
    entry_points={
        'console_scripts': [
            'deployv-addon-gitlab-tools = deployv_addon_gitlab_tools:cli',
        ]
    },
)
