===========
EEA Exhibit
===========
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.exhibit/develop
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.exhibit/job/develop/display/redirect
  :alt: Develop
.. image:: https://ci.eionet.europa.eu/buildStatus/icon?job=eea/eea.exhibit/master
  :target: https://ci.eionet.europa.eu/job/eea/job/eea.exhibit/job/master/display/redirect
  :alt: Master

EEA Exhibit provides Simile Widgets Exhibit framework integration for
eea.app.visualization. See eea.daviz package for more details.


.. image:: https://eea.github.io/_images/eea.daviz.layers.svg


.. contents::


Installation
============

zc.buildout
-----------
If you are using `zc.buildout`_ and the `plone.recipe.zope2instance`_
recipe to manage your project, you can do this:

* Update your buildout.cfg file:

  * Add ``eea.exhibit`` to the list of eggs to install
  * Tell the `plone.recipe.zope2instance`_ recipe to install a ZCML slug

  ::

    [instance]
    ...
    eggs =
      ...
      eea.exhibit

    zcml =
      ...
      eea.exhibit

* Re-run buildout, e.g. with::

  $ ./bin/buildout

You can skip the ZCML slug if you are going to explicitly include the package
from another package's configure.zcml file.

Live demos
==========

* `Basic tutorials <http://www.youtube.com/playlist?list=PLVPSQz7ahsByeq8nVKC7TT9apArEXBrV0>`_
* `Advanced tutorials <http://www.youtube.com/playlist?list=PLVPSQz7ahsBxbe8pwzFWLQuvDSP9JFn8I>`_

Dependencies
============

`EEA Exhibit`_ has the following dependencies:
  - Zope 2.12+
  - rdflib
  - `eea.app.visualization`_


.. image:: https://eea.github.io/_images/eea.daviz.dependencies.svg


Source code
===========

Latest source code (Zope 2 compatible):
- `Plone Collective on Github <https://github.com/collective/eea.exhibit>`_
- `EEA on Github <https://github.com/eea/eea.exhibit>`_

Plone 2 and 3 compatible:
   https://github.com/eea/eea.exhibit/tree/plone25


Copyright and license
=====================
The Initial Owner of the Original Code is European Environment Agency (EEA).
All Rights Reserved.

The EEA Exhibit (the Original Code) is free software;
you can redistribute it and/or modify it under the terms of the GNU
General Public License as published by the Free Software Foundation;
either version 2 of the License, or (at your option) any later
version.

More details under docs/License.txt


Funding
=======

EEA_ - European Environment Agency (EU)

.. _EEA: https://www.eea.europa.eu/
.. _`eea.app.visualization`: https://eea.github.com/docs/eea.app.visualization
.. _`plone.recipe.zope2instance`: https://pypi.python.org/pypi/plone.recipe.zope2instance
.. _`zc.buildout`: https://pypi.python.org/pypi/zc.buildout
