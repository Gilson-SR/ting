from ting_file_management.priority_queue import PriorityQueue
import pytest


mock_data = [
    {
        "nome_do_arquivo": "file.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["1", "2", "3", "4", "5"],
    },
    {
        "nome_do_arquivo": "file2.txt",
        "qtd_linhas": 5,
        "linhas_do_arquivo": ["6", "7", "8", "9", "10"],
    },
    {
        "nome_do_arquivo": "file3.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": ["11", "12", "13", "14"],
    },
]


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    priority_queue.enqueue(mock_data[0])
    priority_queue.enqueue(mock_data[1])
    priority_queue.enqueue(mock_data[2])
    assert len(priority_queue) == 3
    assert priority_queue.search(0) == mock_data[2]
    priority_queue.dequeue()
    assert priority_queue.search(0) == mock_data[0]
    assert priority_queue.search(1) == mock_data[1]
    with pytest.raises(IndexError):
        priority_queue.search(-1)
