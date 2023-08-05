# !/usr/bin/python -u

"""
Copyright (C) 2018 LingoChamp Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import re

from okreport.html import add_td

VALUE_FROM_TABLE_REGEX = re.compile(r'.*>(\d+)<.*')

PERFORMANCE_WARN = "Performance"
BAD_PRACTICE_WARN = "Bad Practice"
MULTITHREADED_WARN = "Multi-Thread Issue"
VULNERABILITY_WARN = "Vulnerability"
OTHER_WARN = "Others"


class FindBugs:
    performanceWarnCount = 0
    badPracticeWarnCount = 0
    multiThreadedWarnCount = 0
    vulnerabilityWarnCount = 0
    otherWarnCount = 0

    performanceScope = False
    badPracticeScope = False
    multiThreadedScope = False
    vulnerabilityScope = False
    otherScope = False

    def parse_line(self, line=""):
        match_value = VALUE_FROM_TABLE_REGEX.match(line)

        if match_value:
            value = int(match_value.groups()[0])
            if self.performanceScope:
                self.performanceWarnCount += value
            elif self.badPracticeScope:
                self.badPracticeWarnCount += value
            elif self.multiThreadedScope:
                self.multiThreadedWarnCount += value
            elif self.vulnerabilityScope:
                self.vulnerabilityWarnCount += value
            else:
                self.otherWarnCount += value

            self.reset()
            return

        if "Performance Warnings" in line:
            self.reset()
            self.performanceScope = True
        elif "Bad practice Warnings" in line:
            self.reset()
            self.badPracticeScope = True
        elif "Multithreaded correctness Warnings" in line:
            self.reset()
            self.multiThreadedScope = True
        elif "Malicious code vulnerability Warnings" in line:
            self.reset()
            self.vulnerabilityScope = True
        elif "href=" in line:
            self.reset()
            self.otherScope = True

    def reset(self):
        self.performanceScope = False
        self.badPracticeScope = False
        self.multiThreadedScope = False
        self.vulnerabilityScope = False
        self.otherScope = False

    def parse(self, findbugs_html_path=""):
        stream = open(findbugs_html_path, "r")
        started = False
        for line in stream:
            if "Summary" in line:
                started = True
                # start
            if started:
                self.parse_line(line)
                if line == "</table>":
                    break

    def dump(self):
        print(u''.join("%s:%d" % (PERFORMANCE_WARN, self.performanceWarnCount)).encode('utf-8'))
        print(u''.join("%s:%d" % (BAD_PRACTICE_WARN, self.badPracticeWarnCount)).encode('utf-8'))
        print(u''.join("%s:%d" % (MULTITHREADED_WARN, self.multiThreadedWarnCount)).encode('utf-8'))
        print(u''.join("%s:%d" % (VULNERABILITY_WARN, self.vulnerabilityWarnCount)).encode('utf-8'))
        print(u''.join("%s:%d" % (OTHER_WARN, self.otherWarnCount)).encode('utf-8'))

    def dump_html(self):
        fragment = """<h2>OkFindbugs</h2>
<table width="500" cellpadding="5" cellspacing="2">
<tr class="tableheader">
<th align="left">Type</th>
<th align="right">Count</th>
</tr>"""
        fragment += """<tr class="tablerow0">"""
        fragment += add_td(PERFORMANCE_WARN)
        fragment += add_td(self.performanceWarnCount.__str__(), True)
        fragment += "</tr>"

        fragment += """<tr class="tablerow1">"""
        fragment += add_td(BAD_PRACTICE_WARN)
        fragment += add_td(self.badPracticeWarnCount.__str__(), True)
        fragment += "</tr>"

        fragment += """<tr class="tablerow0">"""
        fragment += add_td(MULTITHREADED_WARN)
        fragment += add_td(self.multiThreadedWarnCount.__str__(), True)
        fragment += "</tr>"

        fragment += """<tr class="tablerow1">"""
        fragment += add_td(VULNERABILITY_WARN)
        fragment += add_td(self.vulnerabilityWarnCount.__str__(), True)
        fragment += "</tr>"

        fragment += """<tr class="tablerow0">"""
        fragment += add_td(OTHER_WARN)
        fragment += add_td(self.otherWarnCount.__str__(), True)
        fragment += "</tr>"
        fragment += "</table>\n"
        return fragment

    def __init__(self):
        pass

    def to_cache(self):
        fragment = "okFindBugs\n"
        fragment += "0:%d\n" % self.performanceWarnCount
        fragment += "1:%d\n" % self.badPracticeWarnCount
        fragment += "2:%d\n" % self.multiThreadedWarnCount
        fragment += "3:%d\n" % self.vulnerabilityWarnCount
        fragment += "4:%d\n" % self.otherWarnCount
        fragment += "end\n"
        return fragment

    def from_cache(self, conf_path):
        started = False
        for line in open(conf_path):
            line = line.strip()
            if line == "okFindBugs":
                started = True
            if started:
                if "end" == line:
                    break
                values = line.split(":")
                if values[0] == "0":
                    self.performanceWarnCount = int(values[1])
                elif values[0] == "1":
                    self.badPracticeWarnCount = int(values[1])
                elif values[0] == "2":
                    self.multiThreadedWarnCount = int(values[1])
                elif values[0] == "3":
                    self.vulnerabilityWarnCount = int(values[1])
                elif values[0] == "4":
                    self.otherWarnCount = int(values[1])


def equals(left=FindBugs(), right=FindBugs()):
    if left == right:
        return True

    if left.performanceWarnCount != right.performanceWarnCount:
        return False
    if left.badPracticeWarnCount != right.badPracticeWarnCount:
        return False
    if left.multiThreadedWarnCount != right.multiThreadedWarnCount:
        return False
    if left.vulnerabilityWarnCount != right.vulnerabilityWarnCount:
        return False
    if left.otherWarnCount != right.otherWarnCount:
        return False

    return True
