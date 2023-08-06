from setuptools import setup

version = "23"

setup(  name='embarcaderomindmachine',
        version=version,
        description='The extensible framework for running Github bot flocks.',
        url='https://pages.charlesreid1.com/embarcadero-mind-machine',
        author='charlesreid1',
        author_email='embarcadero@charlesreid1.com',
        test_suite='nose.collector',
        tests_require=['nose'],
        license='MIT',
        packages=['embarcaderomindmachine'],
        install_requires=[
            'boringmindmachine==23',
            'requests_oauthlib>=1.0',
            'PyGithub>=1.39'
        ],
        zip_safe=False)

