from setuptools import setup

setup(name='slackbotmaker',
            version='0.0.1',
            description='Trivial framework for building a slackbot rtm client',
            url='http://github.com/dmf24/slackbotmaker',
            author='Doug Feldmann',
            author_email='doug@feldmann.com',
            license='MIT',
            packages=['slackbotmaker'],
            install_requires=[
                    'slackclient',
                ],
            zip_safe=False)
