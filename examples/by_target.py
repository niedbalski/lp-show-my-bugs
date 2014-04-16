#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'Jorge Niedbalski R. <jnr@metaklass.org>'

from lp_show_my_bugs import LaunchpadShowMyBugs

lp = LaunchpadShowMyBugs('niedbalski')

lp.add_filter('bug_target_name', 'any-project')
lp.sort_by('date_created', 'desc')

tasks = lp.fetch()

for task in tasks:
    print task.date_created, task.title
