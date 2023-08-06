from setuptools import setup

long_des = """
Toasts is an app that shows desktop notifications from various websites like GitHub,
StackExchange, BitBucket, and the likes. It just runs in the background and shows
you a notification when there is one from sites you have enabled. Authentication to
your user account on a particular website is done through a Personal Access Token or
Oauth.

I'm still working on it, so hang tight :)

For the first release, I'm planning to support GitHub only. StackExchange, BitBucket,
Libraries.io, etc, will be supported on subsequent releases.
"""

setup(
    name='toasts',
    version='0.0.0',
    description='Get desktop notifications from programming websites like GitHub, Stack Overflow and the likes :) ',
    long_description=long_des,
    url='https://github.com/gokulsoumya/toasts',
    author='Gokul Soumya',
    author_email='gokulps15@gmail.com',
    packages=[],
    classifiers=['Development Status :: 1 - Planning'],
)
