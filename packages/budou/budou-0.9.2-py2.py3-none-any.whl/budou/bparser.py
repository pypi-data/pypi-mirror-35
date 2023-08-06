# -*- coding: utf-8 -*-
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from abc import ABCMeta, abstractmethod
import six
from xml.etree import ElementTree as ET
import html5lib
import re
from .mecabsegmenter import MecabSegmenter
from .nlapisegmenter import NLAPISegmenter

DEFAULT_CLASS_NAME = 'chunk'

@six.add_metaclass(ABCMeta)
class Parser(object):

  def __init__(self, options=None):
    self.options = options

  def parse(self, source, attributes={}, language=None, max_length=None):
    source = preprocess(source)
    chunks = self.segmenter.segment(source, language)
    attributes = parse_attributes(attributes)
    html_code = html_serialize(chunks, attributes, max_length=max_length)
    return {
        'chunks': chunks.chunks,
        'html_code': html_code,
    }


class NLAPIParser(Parser):

  def __init__(self, options=None):
    super(NLAPIParser, self).__init__(options)
    self.segmenter = NLAPISegmenter()


class MecabParser(Parser):

  def __init__(self, options=None):
    super(MecabParser, self).__init__(options)
    self.segmenter = MecabSegmenter()


def parse_attributes(self, attributes={}):
  attributes.setdefault('class', DEFAULT_CLASS_NAME)
  return attributes

def html_serialize(chunks, attributes, max_length=None):
  """Returns concatenated HTML code with SPAN tag.
  Args:
    chunks: The list of chunks to be processed. (ChunkList)
    attributes: If a dictionary, it should be a map of name-value pairs for
        attributes of output SPAN tags. If a string, it should be a class name
        of output SPAN tags. If an array, it should be a list of class names
        of output SPAN tags. (str or dict or list of str)
    max_length: Maximum length of span enclosed chunk. (int, optional)
  Returns:
    The organized HTML code. (str)
  """
  doc = ET.Element('span')
  for chunk in chunks.chunks:
    if chunk.is_space():
      if doc.getchildren():
        if doc.getchildren()[-1].tail is None:
          doc.getchildren()[-1].tail = ' '
        else:
          doc.getchildren()[-1].tail += ' '
      else:
        if doc.text is not None:
          # We want to preserve space in cases like "Hello 你好"
          # But the space in " 你好" can be discarded.
          doc.text += ' '
    else:
      if chunk.has_cjk() and not (max_length and len(chunk.word) > max_length):
        ele = ET.Element('span')
        ele.text = chunk.word
        for k, v in attributes.items():
          ele.attrib[k] = v
        doc.append(ele)
      else:
        # add word without span tag for non-CJK text (e.g. English)
        # by appending it after the last element
        if doc.getchildren():
          if doc.getchildren()[-1].tail is None:
            doc.getchildren()[-1].tail = chunk.word
          else:
            doc.getchildren()[-1].tail += chunk.word
        else:
          if doc.text is None:
            doc.text = chunk.word
          else:
            doc.text += chunk.word
  result = ET.tostring(doc, encoding='utf-8').decode('utf-8')
  result = html5lib.serialize(
      html5lib.parseFragment(result), sanitize=True,
      quote_attr_values="always")
  return result

def preprocess(source):
  """Removes unnecessary break lines and white spaces.
  Args:
    source: HTML code to be processed. (str)
  Returns:
    Preprocessed HTML code. (str)
  """
  doc = html5lib.parseFragment(source)
  source = ET.tostring(doc, encoding='utf-8', method='text').decode('utf-8')
  source = source.replace(u'\n', u'').strip()
  source = re.sub(r'\s\s+', u' ', source)
  return source
