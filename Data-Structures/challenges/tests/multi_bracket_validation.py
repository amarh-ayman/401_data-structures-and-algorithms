from tests.test_queue_with_stacks import data
from multi_bracket_validation.multi_bracket_validation import check

import pytest

def test_multi_bracket_validation_01():
  assert check('{}{Code}[Fellows](())')==True
  assert check('{}(){}')==True
  assert check('()[[Extra Characters]]')==True
  assert check('{')==False
  assert check('{}')==True
  assert check('{)')==False
  assert check('{)()')==False
  
  assert check('[({}]')==False
  assert check('(](')==False
  assert check('{(})')==False
