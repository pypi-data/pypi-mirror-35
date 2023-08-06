#pylint: disable=all
"""Release information regarding sysmonitor.agent"""

RELEASE_LEVELS = [ALPHA, BETA, RELEASE_CANDIDATE, FINAL] = ['alpha', 'beta', 'candidate', 'final']
RELEASE_LEVELS_DISPLAY = {ALPHA: ALPHA,
                          BETA: BETA,
                          RELEASE_CANDIDATE: 'rc',
                          FINAL: ''}

version_info = (2, 2, 0, FINAL, 0)
version = '.'.join(str(s) for s in version_info[:2]) + RELEASE_LEVELS_DISPLAY[version_info[3]] + str(version_info[4] or '')
series = serie = major_version = '.'.join(str(s) for s in version_info[:2])

product_name = "sysmonitor-agent"
description = "System Monitor Agent"
long_desc = "Agent that runs on server to report status to main server"
classifiers = """Development Status :: 5 - Production/Stable
Environment :: No Input/Output (Daemon)
Intended Audience :: System Administrators
License :: OSI Approved :: BSD License
Programming Language :: Python :: 3 :: Only
Operating System :: Unix
Topic :: System :: Monitoring
"""
url = "https://git.hugorodrigues.net/hugorodrigues/sysmonitor-agent"
author = "Hugo Rodrigues"
author_email = "me@hugorodrigues.net"
license = "BSD-3-Clause"
