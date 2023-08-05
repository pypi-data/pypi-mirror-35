Description
===========

From a file with a tag description format like:

.. code::


   apps:
     - name: fubar
       url: http://example.org/fubar
       description: a fubar app
       tags:
       - foo1
       - bar1

     - name: foo
       url: http://example.org/foo
       description: a foo app
       tags:
       - foo1
       - foo2

     - name: bar
       url: http://example.org/bar
       description: a bar app
       tags:
       - bar1
       - bar2

Generates a new file after applying a template with the inverted file, that is,
a dict of tags with each app as a dict.

As an example, with the template:

.. code::


    Simple output for tageator

    {% for item in categories | dictsort %}
    - {{ item[0] }}
    {%- for app in item[1] | sort(attribute='name') %}
      - {{ app.name }}: {{ app.description }} ({{ app.url }})
    {%- endfor %}
    {% endfor %}

The previous input file will generate:

.. code::

    Simple output for tageator


    - bar1
      - bar: a bar app (http://example.org/bar)
      - fubar: a fubar app (http://example.org/fubar)

    - bar2
      - bar: a bar app (http://example.org/bar)

    - foo1
      - foo: a foo app (http://example.org/foo)
      - fubar: a fubar app (http://example.org/fubar)

    - foo2
      - foo: a foo app (http://example.org/foo)


