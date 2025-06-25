# Stray Pet Mapper   [![Build Status](https://secure.travis-ci.org/codeforamerica/straymapper.png)](http://travis-ci.org/codeforamerica/straymapper)
Reunite more stray animals with their human companions



## <a name="screenshot"></a>Screenshot
![City Petz: Stray Mapper](http://i.imgur.com/ivPZR.png "Stray Mapper")

## <a name="demo"></a>Demo
You can see a running version of the application at
[http://stray.citypetz.com/][demo].

[demo]: http://straymapper.com/

## <a name="environment"></a>Development Environment

### Ubuntu Environment
Instructions for creating a development environment for Ubuntu Linux.  This has been tested using Ubuntu 12.04.

```bash
# Initial libraries needed
$ sudo apt-get install build-essential git-core python-software-properties python-dev python-pip python-virtualenv

# PIL Dependencies
$ sudo apt-get build-dep python-imaging

# Also symlink associated libraries:
$ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libfreetype.so /usr/lib/
$ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libjpeg.so /usr/lib/
$ sudo ln -s /usr/lib/`uname -i`-linux-gnu/libz.so /usr/lib/

# Install PostgreSQL/Postgis
$ sudo apt-get install postgresql-9.1
$ sudo apt-get install postgresql-9.1-postgis
```

### Mac Environment
This project uses PostgreSQL/PostGIS and the best way to get this set up on Mac is by downloading [Postgres.app].

[Homebrew]: http://mxcl.github.com/homebrew/
[Postgres.app]: http://postgresapp.com/

## <a name="installation"></a>Installation
```bash
git clone git://github.com/codeforamerica/straymapper.git
cd straymapper
pip install -r requirements.txt
./manage.py syncdb
```

This will install all the dependencies listed in [`requirements.txt`](requirements.txt) and set up your database.

## <a name="usage"></a>Usage
Start the development server by running:
```bash
./manage.py runserver
```

The application will be available at `http://localhost:8000/`.

## <a name="seed"></a>Seed Data
To populate your database with sample data for testing, run:
```bash
./manage.py loaddata animals/fixtures/animals_testdata.json
```

## <a name="contributing"></a>Contributing
In the spirit of [free software][free-sw], **everyone** is encouraged to help
improve this project.

[free-sw]: http://www.fsf.org/licensing/essays/free-sw.html

Here are some ways *you* can contribute:

* by using alpha, beta, and prerelease versions
* by reporting bugs
* by suggesting new features
* by translating to a new language
* by writing or editing documentation
* by writing specifications
* by writing code (**no patch is too small**: fix typos, add comments, clean up
  inconsistent whitespace)
* by refactoring code
* by closing [issues][]
* by reviewing patches
* [financially][]

[issues]: https://github.com/codeforamerica/straymapper/issues
[financially]: https://secure.codeforamerica.org/page/contribute

## <a name="issues"></a>Submitting an Issue
We use the [GitHub issue tracker][issues] to track bugs and features. Before
submitting a bug report or feature request, check to make sure it hasn't
already been submitted. You can indicate support for an existing issue by
voting it up. When submitting a bug report, please include a [Gist][] that
includes a stack trace and any details that may be necessary to reproduce the
bug, including your Python version, Django version, and operating system. Ideally, a
bug report should include a pull request with failing tests.

[gist]: https://gist.github.com/

## <a name="pulls"></a>Submitting a Pull Request
1. Fork the project.
2. Create a topic branch.
3. Implement your feature or bug fix.
4. Add tests for your feature or bug fix.
5. Run the following command to test your changes:
   ```bash
   ./manage.py test
   ```
   If your changes are not 100% covered, go back to step 4.
6. Commit and push your changes.
7. Submit a pull request. Please do not include changes to the version
   file. (If you want to create your own version for some reason,
   please do so in a separate commit.)

## <a name="copyright"></a>Copyright
Copyright (c) 2012 Code for America. See [LICENSE][] for details.

[license]: LICENSE.mkd
