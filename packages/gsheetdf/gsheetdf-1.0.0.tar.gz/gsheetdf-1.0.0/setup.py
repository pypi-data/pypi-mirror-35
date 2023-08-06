from setuptools import setup

setup(
    name='gsheetdf',
    version='1.0.0',
    description='Export Google Sheet to Pandas dataframe',
    url='https://github.com/kunanit/gsheetdf',
    author='Andrew Ang',
    author_email='marc.kunanit@gmail.com',
    license='MIT',
    packages=['gsheetdf'],
    install_requires=[
        'pandas==0.23.4',
        'google-auth==1.5.1',
        'google-auth-oauthlib==0.2.0',
        'gspread==3.0.1'
    ]
)
