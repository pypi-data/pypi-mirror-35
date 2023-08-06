.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

=======================
visaplan.plone.infohubs
=======================

This product establishes a "mini language" for the calculation and re-use of
information from Plone instances during the processing of a single request,
e.g. when creating breadcrumbs; e.g., if the login state is important for the
breadcrumb for ``/foo``, that same state might be important for the
``/foo/bar`` breadcrumb as well.

The purpose of this package (for now) is *not* to provide new functionality
but to factor out existing functionality from an existing monolitic Zope product.
Thus, it is more likely to lose functionality during further development
(as parts of it will be forked out into their own packages,
or some functionality may even become obsolete because there are better
alternatives in standard Plone components).


Features
--------

- The ``info`` dictionary holds the collected information of interest
  during processing of the request.
- The ``hub`` dictionary holds the tools which were used to get those
  information chunks.

  - For now, some of those tools are quite proprietary adapters or browsers,
    usually now factored out to the ``visaplan.plone.adapters`` and
    ``visaplan.plone.browsers`` packages, respectively.

    This is not ideal, and it will change; we'd rather depend directly on
    standard Plone tools and/or the ``plone.api`` instead.


Examples
--------

This add-on can be seen in action at the following sites:

- https://www.unitracc.de
- https://www.unitracc.com


Documentation
-------------

Full documentation for end users can be found in the "docs" folder.


Installation
------------

Install visaplan.plone.infohubs by adding it to your buildout::

    [buildout]

    ...

    eggs =
        visaplan.plone.infohubs


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/visaplan/visaplan.plone.infohubs/issues
- Source Code: https://github.com/visaplan/visaplan.plone.infohubs


Support
-------

If you are having issues, please let us know;
please use the issue tracker mentioned above.


License
-------

The project is licensed under the GPLv2.

.. vim: tw=79 cc=+1 sw=4 sts=4 si et
