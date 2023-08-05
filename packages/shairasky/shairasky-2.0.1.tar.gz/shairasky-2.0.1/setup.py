from setuptools import setup
setup(
    name='shairasky',        #* Your package name 
    packages=['shairasky'],  #* Name the package again
    version='2.0.1',        #* To be increased every time you change library
    license='MIT',          # Type of a license. More here: https://help.github.com/articles/licensing-a-repository
    description='Weather forecast data',    # Short description of your library
    author='Bohdan Jakym',                  # Your name
    author_email='dania88@seznam.cz',       # Your email
    url='https://example.com',              # Homepage of your library (github)
    keywords=['weather', 'forecast', 'openweather'],    # Keyword users can search
    install_requires=[
        'requests',
    ],                                                  # Other 3-rd party libs pip needs to install
    classifiers=[
        'Development Status :: 3 - Alpha',              # Choose "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools', # Who is the audience of a library
        'License :: OSI Approved :: MIT License',       # Type of a license again
        'Programming Language :: Python :: 3.5',        # Python versions that your library supports
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)