Buildout Extension for SlapOS's shared feature
================================================

slapos.extension.shared is a buildout extension that creates .shared
file in a software release directory if shared-parts is defined in buildout
section. .shared file is used to know if a software release is made with
shared feature.

Usage
-----

Add ``slapos.extension.shared`` in ``[buildout]`` section's ``extensions`` option like :

::

  [buildout]
  extensions = slapos.extension.shared

