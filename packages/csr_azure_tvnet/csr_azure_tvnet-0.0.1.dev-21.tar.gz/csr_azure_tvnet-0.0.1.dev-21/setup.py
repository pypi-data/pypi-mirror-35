from distutils.core import setup
project_name = 'csr_azure_tvnet'
project_ver = '0.0.1.dev-21'
setup(
    name=project_name,
    # packages=[project_name],  # this must be the same as the name above
    version=project_ver,
    description='Transit Vnet Azure Package',
    author='Vamsi Kalapala',
    author_email='vakalapa@cisco.com',
    # use the URL to the github repo
    url='https://github4-chn.cisco.com/csr1000v-azure/' + project_name,
    download_url='https://pypi.python.org/pypi?:action=display&name=%s&version=%s' % (project_name, project_ver),
    keywords=['cisco', 'azure', 'guestshell', 'dmvpn', 'csr1kv', 'csr1000v'],
    classifiers=[],
    license="MIT",
    install_requires=[
        'azure_storage',
        'futures',
        'requests[security]'
    ],
)
