.. image:: https://travis-ci.org/bartTC/django-staticinline.svg?branch=master
    :target: https://travis-ci.org/bartTC/django-staticinline

.. image:: https://api.codacy.com/project/badge/Coverage/8e64345e99ea49888dc1bd9303c89a35
    :target: https://www.codacy.com/app/bartTC/django-staticinline?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bartTC/django-staticinline&amp;utm_campaign=Badge_Coverage

.. image:: https://api.codacy.com/project/badge/Grade/8e64345e99ea49888dc1bd9303c89a35
    :target: https://www.codacy.com/app/bartTC/django-staticinline?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=bartTC/django-staticinline&amp;utm_campaign=Badge_Grade

===================
django-staticinline
===================

Similiar to Django's ``static`` templatetag, but this includes
the file directly in the template, rather than a link to it.

Example:

.. code:: django

    {% load staticinline %}

    <style type="text/css">{% staticinline "myfile.css" %}</style>
    <script>{% staticinline "myfile.js" %}</script>

Becomes:

.. code:: html

    <style type="text/css">body{ color: red; }</style>
    <script>alert("Hello World");</script>

For further information and installation instructions see the docs on
https://docs.elephant.house/django-staticinline/.
