from setuptools import setup, find_packages

setup(
    name = 'mvs_rpc',
    version = '0.1.3',
    keywords = ['mvs sdk', 'mvs client'],
    description = 'python implement of mvs rpc, update to mvs-0.8.3, update to api v3',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
    ],
    license = 'MIT License',
    install_requires = ['requests>=2.18.4'],
    author = 'chengzhpchn',
    author_email = 'chengzhpchn@163.com',
    packages = find_packages(),
    platforms = 'all',
    url = 'https://github.com/mvshub/mvs_rpc_python.git',
)