=====
Notes
=====

TODO: Pick up at "Document Title / Subtitle" http://docutils.sourceforge.net/docs/user/rst/quickstart.html

TODO: figure out how do templating "rst template"

TODO: figure out how to do section breaks

Q: Is there a best practice for where to put directives that don't render in place?  Ex. header, footer, footnotes, etc.

.. list-table:: Frozen Delights!
   :header-rows: 1
   
   * - Treat
     - Price
     - Description
   * - Ice cream cone
     - 2.49
     - So delicious
   * - a
     - b
     - c
   * - d
     - e
     - f

i read the docutils rst docs... thoroughly

.. header:: my header

.. footer:: my footer

eipgraph / block quote

.. epigraph::

   Foo bar.

   -- Python

what this is???

.. target-notes::

.. compound::

  This is a dangerous command:

  .. code::

    cd /
    rm -rf *

  and running it would be bad.

.. pull-quote::
  i am a pull-quote
  —foo

.. highlights::
  I
  am a
  blockquote!

.. sectnum::

directives have short and long names: you can use ``sectnum`` or ``section-numbering``

.. contents::
   :depth: 10

table of contents omg finally

* toc backlinks dont seem to work on gh

1-2 3–4 5—6

.. I can haz comments.

..
  I can
  haz
  block comments.

they also don't work on github, at least preview

citations are cool [Getting Things Done]_ and global (not sure how i feel about that)

oh my god i finally have footnotes [#fn1]_

real footnotes!!! [#fn2]_

but they don't seem to work on github :(

  use .. to begin an explicit markup block; it's also what directives use

.. DANGER::
  foo

an image

.. image:: http://cache2.asset-cache.net/xc/471994542.jpg?v=2&c=IWSAsset&k=2&d=br4flZlAJPtjfG2Zkf_ovE3B9QhSVLVmFfKoX6XVWL8ugfjiSAvbZT8Aa2AdN9UE0

######
part 1
######

Note this style is just a Python convention.

****
ch 1
****

a

next level
==========

b

foo
---

c

bar
~~~

d

****
ch 2
****

######
part 2
######

****
ch 3
****

Note: apparently not everything in `reStructuredText Primer <http://www.sphinx-doc.org/en/stable/rest.html>`_ works on GitHub

=====  =====
Col 1  Col 2
=====  =====
a      b
c      d
=====  =====

this is `my link`_ and again `my link`_

`an inline link <http://google.com>`_

A literal link is converted automatically http://www.apple.com

foo
  this is a def

foo2
  a longer
  
  def
  
  spanning paras

a quote

  blah blah blah
  far bar car

a quote with wrapping

  | blah blah blah
  | far bar car

here comes some code::

  x = 5
  y = x**2
  print(y)

.. code-block:: python

  print('hi')
  print('hey whats up hello')
  x = 5
  y = x**2
  print(y)
  

* foo

  * a def in a list?
      yes maam

* bar

#. a
#. b

* 1

  * 4
  * 5

* 2

  * 6

* 3

- a

  - b
  - c

- d

*bar2*

**bar3**


.. rubric:: Footnotes

.. [#f1] footnote 1 text
.. [#f2] foo


.. _`my link`: http://www.example.com

.. [Getting Things Done] The book or whatever
