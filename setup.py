# !/usr/bin/python

from setuptools import setup, find_packages
from distutils.sysconfig import get_python_lib


def get_version():
    f = open('insights_client/constants.py')
    for line in f:
        if 'version' in line:
            return eval(line.split('=')[-1])

VERSION = get_version().split('-')[0]
SHORT_DESC = "Red Hat Insights"
LONG_DESC = """
Uploads insightful information to Red Hat
"""

if __name__ == "__main__":
    logpath = "/var/log/insights-client"

    # where stuff lands
    confpath = "/etc/insights-client"

    man5path = "/usr/share/man/man5/"
    man8path = "/usr/share/man/man8/"

    rpmpath = "/var/lib/insights_client"

    setup(
        name="insights-client",
        version=VERSION,
        author="Jeremy Crafts <jcrafts@redhat.com>, Dan Varga <dvarga@redhat.com>",
        author_email="jcrafts@redhat.com",
        license="GPL",
        packages=find_packages(),
        install_requires=['requests'],
        include_package_data=True,
        scripts=[
            "scripts/insights-client"
        ],
        entry_points={'console_scripts': ['insights-client = insights_client:_main']},
        data_files=[
            # config files
            (confpath, ['etc/insights-client.conf',
                        'etc/.fallback.json',
                        'etc/.fallback.json.asc',
                        'etc/redhattools.pub.gpg',
                        'etc/api.access.redhat.com.pem',
                        'etc/cert-api.access.redhat.com.pem',
                        'etc/.exp.sed',
                        'etc/insights-client-container.cron',
                        'etc/insights-client.cron']),

            # man pages
            (man5path, ['docs/insights-client.conf.5']),
            (man8path, ['docs/insights-client.8']),

            (logpath, []),

            # included portable client .gz
            (rpmpath, ['insights-client-' + VERSION + '.tar.gz'])
        ],
        description=SHORT_DESC,
        long_description=LONG_DESC
    )
