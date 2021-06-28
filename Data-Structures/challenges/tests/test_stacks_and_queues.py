from stacks_and_queues.stacks_and_queues import *
import pytest

def test_StackPush_1_2():
    stack=Stack()
    assert stack.top==None
    stack.push(1)
    assert stack.top.value==1
    stack.push('a')
    assert stack.top.value=='a'
    assert stack.top.next.value == 1
    
def test_StackPush_3_4(stack_data01):
    stack=stack_data01
    assert stack.top.value == 3
    stack.pop()
    assert stack.top.value == 2
    stack.pop()
    assert stack.top.value == 1
    stack.pop()
    assert stack.top == None
    assert stack.is_empty()==True

def test_StackPeek5(stack_data01):
    stack=stack_data01
    assert stack.peek()==3

def test_StackpeekandPop_Empty6_7():
    stack=Stack()
    assert stack.is_empty()==True
    with pytest.raises(ValueError):
        stack = Stack()
        assert stack.pop()
    with pytest.raises(ValueError):
        stack = Stack()
        assert stack.peek()    

# ///////////////////////////////////////////////////

def test_enqueue_dequeue_peek_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.rear.value == 1
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    assert queue.front.next.next.next.value == 4
    queue.dequeue()
    assert queue.front.next.next.value == 4
    assert queue.rear.value == 4
    assert queue.front.value == 2
    assert queue.peek() == 2
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    assert queue.front == None

def test_enqueue_dequeue_peek_queue2():
    queue = Queue()
    queue.enqueue(1)
    assert queue.dequeue() ==1
    queue.enqueue(5)
    assert queue.dequeue() ==5

def test_QueuepeekandPop_Empty13_14():
    queue=Queue()
    assert queue.is_empty()==True
    with pytest.raises(ValueError):
        assert queue.dequeue()
    with pytest.raises(ValueError):
        assert queue.peek()    


@pytest.fixture
def stack_data01():
    data = Stack()
    data.push(1)
    data.push(2)
    data.push(3)
    return data
    



