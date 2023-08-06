importreqs
==========

A simple Python lib for extracting reqs.txt from currently imported libs
in the context.

Usage
-----

::

    # import your own projects
    # for example "import app"

    import importreqs

    print(importreqs.generate_reqs())


