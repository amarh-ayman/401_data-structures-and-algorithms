from tests.test_queue_with_stacks import data
from multi_bracket_validation.multi_bracket_validation import multi_bracket_validation

import pytest

def test_multi_bracket_validation_01():
  data=multi_bracket_validation()
  assert data.check('{}{Code}[Fellows](())')==True
  assert data.check('{}(){}')==True
  assert data.check('()[[Extra Characters]]')==True
  assert data.check('{')==False
  assert data.check('{}')==True
  assert data.check('{)')==False
  assert data.check('{)()')==False
  
  assert data.check('[({}]')==False
  assert data.check('(](')==False
  assert data.check('{(})')==False
