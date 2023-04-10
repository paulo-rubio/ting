from ting_file_management.priority_queue import PriorityQueue
from tests.priority_queue.mockqueue import mock1
from tests.priority_queue.mockqueue import mock2
import pytest


def test_basic_priority_queueing():
    priority = PriorityQueue()

    assert priority.__len__() == 0
    assert priority.is_priority(mock1) is True
    assert priority.is_priority(mock2) is True
    assert priority.dequeue() is None
    assert priority.enqueue(mock1) is None
    assert priority.enqueue(mock2) is None
    assert priority.__len__() == 2
    assert priority.search(0) is mock1
    assert priority.search(1) is mock2
    assert priority.dequeue() is mock1
    assert priority.__len__() == 1
    assert priority.dequeue() is mock2
    assert priority.__len__() == 0

    with pytest.raises(IndexError):
        priority.search(100) is None
        priority.search(-1) is None




