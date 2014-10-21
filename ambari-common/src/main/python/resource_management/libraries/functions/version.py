#!/usr/bin/env python
"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Ambari Agent

"""


def _normalize(v, desired_segments=0):
  """
  :param v: Input string of the form "#.#.#" or "#.#.#.#"
  :param desired_segments: If greater than 0, and if v has fewer segments this parameter, will pad v with segments
  containing "0" until the desired segments is reached.
  :return: Returns a list of integers representing the segments of the version
  """
  v_list = v.split(".")
  if desired_segments > 0 and len(v_list) < desired_segments:
    v_list = v_list + ((desired_segments - len(v_list)) * ["0", ])
  return [int(x) for x in v_list]


def format_hdp_stack_version(input):
  """
  :param input: Input string, e.g. "2.2"
  :return: Returns a well-formatted HDP stack version of the form #.#.#.# as a string.
  """
  if input:
    normalized = _normalize(str(input))
    if len(normalized) == 2:
      normalized = normalized + [0, 0]
    elif len(normalized) == 3:
      normalized = normalized + [0, ]
    normalized = [str(x) for x in normalized]   # need to convert each number into a string
    return ".".join(normalized)
  return ""


def compare_versions(version1, version2):
  """
  Used to compare either Ambari Versions, or Stack versions
  E.g., Ambari version 1.6.1 vs 1.7.0,
  Stack Version 2.0.6.0 vs 2.2.0.0
  :param version1: First parameter for version
  :param version2: Second parameter for version
  :return: Returns -1 if version1 is before version2, 0 if they are equal, and 1 if version1 is after version2
  """
  max_segments = max(len(version1.split(".")), len(version2.split(".")))
  return cmp(_normalize(version1, desired_segments=max_segments), _normalize(version2, desired_segments=max_segments))