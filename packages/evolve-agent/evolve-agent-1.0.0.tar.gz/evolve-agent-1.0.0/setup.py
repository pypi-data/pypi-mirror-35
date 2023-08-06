from setuptools import setup
from glob import glob
import evolveagent


with open('README.md', 'r') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='evolve-agent',
    version=evolveagent.__version__,
    author=evolveagent.__author__,
    author_email='evolve-pypi@threatintelligence.com',
    packages=[
        'evolveagent',
        'evolveagent.iws',
        'evolveagent.iws.agent'
    ],
    description='Evolve Agent to connect your systems to the Evolve Security Automation and Orchestration Platform.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=evolveagent.__license__,
    url="https://evolve.threatintelligence.com",
    scripts=['bin/evolve-agent'],
    data_files=[
        ('/etc/evolve-agent/systemd', glob('conf/systemd/*')),
        ('/etc/evolve-agent/upstart', glob('conf/upstart/*')),
        ('/etc/evolve-agent/sysvinit', glob('conf/sysvinit/*')),
    ],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Security',
        'Topic :: System',
        'Topic :: Utilities'
    ]
)
