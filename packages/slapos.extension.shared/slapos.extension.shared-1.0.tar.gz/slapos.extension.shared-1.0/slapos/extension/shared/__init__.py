import os

def finish(buildout):
  if buildout['buildout'].get('shared-parts'):
    open(os.path.join(buildout['buildout']['directory'], '.shared'), 'w').close()
