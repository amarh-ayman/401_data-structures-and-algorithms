from stacks_and_queues.stacks_and_queues import *
from fifo_animal_shelter.fifo_animal_shelter import *
import pytest



def test_AnimalShelter_dequeue(data):
    assert data.dequeue('cat') == 'cat'
    assert data.dequeue('cat') == 'cat'
    assert data.dequeue('dog') == 'dog'
    assert data.dequeue('dog') == 'dog'
    assert data.dequeue('dog') == 'not there'
    assert data.dequeue('cat') == 'not there'
    assert data.dequeue('bird') == 'not in the shelf for ignore it'

def test_AnimalShelter_enqueue(data):
    assert data.cat.front.value=='cat'
    assert data.cat.front.next.value=='cat'
    assert data.dog.front.value=='dog'
    assert data.dog.front.next.value=='dog'
    assert data.enqueue('dd')=='not in the list'



    

@pytest.fixture
def data():
    my_queue = AnimalShelter()
    my_queue.enqueue('cat')
    my_queue.enqueue('cat')
    my_queue.enqueue('dog')
    my_queue.enqueue('dog')
    return my_queue