#!/usr/bin/env python

from distutils.core import setup

setup(name="eventbuild",
  version="0.0.1",
  description="Package the project eventlog using docker as jail.",
  author='Miguel Angel Gordian',
  author_email="os.aioria@gmail.com",
  url="https://github.com/zoek1/eventbuild",
  packages=['eventbuild'],
  scripts=['scripts/eventlog-build'],
  package_data={
      'eventbuild': ['Dockerfile', 'bin/*']
  }
)
