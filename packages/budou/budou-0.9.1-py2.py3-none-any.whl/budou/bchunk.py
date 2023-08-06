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
import unicodedata
import six

@six.add_metaclass(ABCMeta)
class Chunk(object):
  """Chunk object. This represents a unit for word segmentation.
  """
  SPACE_POS = 'SPACE'
  BREAK_POS = 'BREAK'

  def __init__(self, word, pos=None, label=None, dependency=None):
    self.word = word
    self.pos = pos
    self.label = label
    self.dependency = dependency

  def __repr__(self):
    return 'Chunk(%s, %s, %s, %s)' % (
        repr(self.word), self.pos, self.label, self.dependency)

  @classmethod
  def space(cls):
    """Creates space Chunk."""
    chunk = cls(u' ', cls.SPACE_POS)
    return chunk

  @classmethod
  def breakline(cls):
    """Creates breakline Chunk."""
    chunk = cls(u'\n', cls.BREAK_POS)
    return chunk

  @abstractmethod
  def activate_dependency(self):
    raise NotImplementedError()

  def serialize(self):
    """Returns serialized chunk data in dictionary."""
    return {
        'word': self.word,
        'pos': self.pos,
        'label': self.label,
        'dependency': self.dependency,
        'has_cjk': self.has_cjk(),
    }

  def is_space(self):
    """Checks if this is space Chunk."""
    return self.pos == self.SPACE_POS

  def has_cjk(self):
    """Checks if the word of the chunk contains CJK characters
    Using range from
    https://github.com/nltk/nltk/blob/develop/nltk/tokenize/util.py#L149
    """
    for char in self.word:
      if any([start <= ord(char) <= end for start, end in
          [(4352, 4607), (11904, 42191), (43072, 43135), (44032, 55215),
           (63744, 64255), (65072, 65103), (65381, 65500),
           (131072, 196607)]
          ]):
        return True
    return False

  def update_word(self, word):
    """Updates the word of the chunk."""
    self.word = word

  def add_dependency_on_punct(self):
      try:
        # Getting unicode category to determine the direction.
        # Concatenates to the following if it belongs to Ps or Pi category.
        # Ps: Punctuation, open (e.g. opening bracket characters)
        # Pi: Punctuation, initial quote (e.g. opening quotation mark)
        # Otherwise, concatenates to the previous word.
        # See also https://en.wikipedia.org/wiki/Unicode_character_property
        category = unicodedata.category(self.word)
        self.dependency = category in ('Ps', 'Pi')
      except:
        pass


class NLAPIChunk(Chunk):
  """Chunk object. This represents a unit for word segmentation.
  Attributes:
    word: Surface word of the chunk. (str)
    pos: Part of speech. (str)
    label: Label information. (str)
    dependency: Dependency to neighbor words. None for no dependency, True for
        dependency to the following word, and False for the dependency to the
        previous word. (bool or None)
  """
  DEPENDENT_LABEL = (
      'P', 'SNUM', 'PRT', 'AUX', 'SUFF', 'AUXPASS', 'RDROP', 'NUMBER', 'NUM',
      'PREF')
  PUNCT_POS = 'PUNCT'

  def activate_dependency(self, default_dependency_direction):
    """Adds dependency if any dependency is not assigned yet."""
    if self.dependency is None and self.label in self.DEPENDENT_LABEL:
      self.dependency = default_dependency_direction

    if self.pos == self.PUNCT_POS:
      self.add_dependency_on_punct()


class MecabChunk(Chunk):

  DEPENDENT_POS_FORWARD = set()
  DEPENDENT_POS_BACKWARD = {u'助詞', u'助動詞'}
  DEPENDENT_LABEL_FORWARD = set()
  DEPENDENT_LABEL_BACKWARD = {u'非自立'}
  PUNCT_POS = u'記号'

  def activate_dependency(self):
    """Activates dependency."""
    if self.pos == self.PUNCT_POS:
      self.add_dependency_on_punct()
    elif self.pos in self.DEPENDENT_POS_FORWARD:
      self.dependency = True
    elif self.pos in self.DEPENDENT_POS_BACKWARD:
      self.dependency = False
    elif self.label in self.DEPENDENT_LABEL_FORWARD:
      self.dependency = True
    elif self.label in self.DEPENDENT_LABEL_BACKWARD:
      self.dependency = False


class ChunkList(object):
  """Chunk list. """

  def __init__(self):
    self.chunks = []

  def append(self, chunk):
    self.chunks.append(chunk)

  def get_overlaps(self, offset, length):
    """Returns chunks overlapped with the given range.
    Args:
      offset: Begin offset of the range. (int)
      length: Length of the range. (int)
    Returns:
      Overlapped chunks. (list of Chunk)
    """
    # In case entity's offset points to a space just before the entity.
    if ''.join([chunk.word for chunk in self.chunks])[offset] == ' ':
      offset += 1
    index = 0
    result = []
    for chunk in self.chunks:
      if offset < index + len(chunk.word) and index < offset + length:
        result.append(chunk)
      index += len(chunk.word)
    return result

  def swap(self, old_chunks, new_chunk):
    """Swaps old consecutive chunks with new chunk.
    Args:
      old_chunks: List of consecutive Chunks to be removed. (list of Chunk)
      new_chunk: A Chunk to be inserted. (Chunk)
    """
    indexes = [self.chunks.index(chunk) for chunk in old_chunks]
    del self.chunks[indexes[0]:indexes[-1] + 1]
    self.chunks.insert(indexes[0], new_chunk)

  def resolve_dependencies(self):
    """Resolves chunk dependency by concatenating them.
    Args:
      chunks: a chink list. (NLAPIChunkList)
    Returns:
      A chunk list. (NLAPIChunkList)
    """
    self._concatenate_inner(True)
    self._concatenate_inner(False)
    self._insert_breaklines()

  def _concatenate_inner(self, direction):
    """Concatenates chunks based on each chunk's dependency.
    Args:
      direction: Direction of concatenation process. True for forward. (bool)
    Returns:
      A chunk list. (NLAPIChunkList)
    """
    tmp_bucket = []
    source_chunks = self.chunks if direction else self.chunks[::-1]
    target_chunks = []
    for chunk in source_chunks:
      if (
            # if the chunk has matched dependency, do concatenation.
            chunk.dependency == direction or
            # if the chunk is SPACE, concatenate to the previous chunk.
            (direction == False and chunk.is_space())
        ):
        tmp_bucket.append(chunk)
        continue
      tmp_bucket.append(chunk)
      if not direction: tmp_bucket = tmp_bucket[::-1]
      new_word = ''.join([tmp_chunk.word for tmp_chunk in tmp_bucket])
      chunk.update_word(new_word)
      target_chunks.append(chunk)
      tmp_bucket = []
    if tmp_bucket: target_chunks += tmp_bucket
    if not direction: target_chunks = target_chunks[::-1]
    self.chunks = target_chunks

  def _insert_breaklines(self):
    """Inserts a breakline instead of a trailing space if the chunk is in CJK.
    Args:
      chunks: a chunk list. (NLAPIChunkList)
    Returns:
      A chunk list. (NLAPIChunkList)
    """
    target_chunks = []
    for chunk in self.chunks:
      if chunk.word[-1] == ' ' and chunk.has_cjk():
        chunk.update_word(chunk.word[:-1])
        target_chunks.append(chunk)
        target_chunks.append(chunk.breakline())
      else:
        target_chunks.append(chunk)
    self.chunks = target_chunks


class NLAPIChunkList(ChunkList):
  pass


class MecabChunkList(ChunkList):
  pass
