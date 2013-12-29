Since one year, i create more and more python projects. That for this reason i have decided create a Python template. This template is ready for create a Python project with:

* Setuptools_ for push python code to Pypi_ site 
* Unittest_ for unit testing
* Pep8_ for source code checking
* Coverage_ for test coverage sources

.. _Setuptools: http://pythonhosted.org/setuptools/
.. _Pypi: http://pypi.python.org/pypi
.. _Unittest: http://docs.python.org/2/library/unittest.html
.. _Pep8: http://pypi.python.org/pypi/pep8
.. _Coverage: http://nedbatchelder.com/code/coverage/



Howto use
---------

Here the steps for create a new python project

#. Clone the ``python-project-template`` and replace ``projectname`` by your project name you want::

        cd your_root_projects_directories
        git clone https://github.com/badele/python-project-template.git projectname
        cd projectname

#. Edit the ``PROJECT`` variables in the initproject.py and run::

        ./initproject.py
        rm ./initproject.py

#. Verify the personal text in this files::

       README.rst
       LICENSE
       CHANGELOG.txt
       setup.py

#. Reinit git repository::

        rm -rf .git && git init

#. (Optional) install virtualenv::

        mkvirtualenv --no-site-packages -p /usr/bin/python2.7 env_projectname

#. (Optional) Run the minimal test::

        pip install -r requirements/test.txt
        make test

#. (Optional) Test minimal application::

        make install
        projectname -h
