=========
scrapimdb
=========


.. image:: https://img.shields.io/pypi/v/scrap-imdb.svg
        :target: https://pypi.python.org/pypi/scrap-imdb

.. image:: https://img.shields.io/travis/dsteinberger/scrapimdb.svg
        :target: https://travis-ci.org/dsteinberger/scrapimdb

.. image:: https://pyup.io/repos/github/dsteinberger/scrapimdb/shield.svg
     :target: https://pyup.io/repos/github/dsteinberger/scrapimdb/
     :alt: Updates



Scrap Imdb website to retrieve detail informations from movies or tvshows


Install
-------

.. code-block:: shell

    pip install scrap-imdb


Usages
------

.. code-block:: python

    from scrapimdb import ImdbSpider

    im = ImdbSpider('terminator')

    im.get_rating()
    im.get_original_title()
    im.get_year()



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage


=======
History
=======


0.1.1 (2018-01-09)
------------------

* Fix rating css selector


0.1.0 (2018-04-06)
------------------

* Add Imdb spider with scrapping: rate, title, url and date


