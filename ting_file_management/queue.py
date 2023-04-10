from ting_file_management.abstract_queue import AbstractQueue


class Queue(AbstractQueue):
    def __init__(self):
        self.queue = list()

    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return "Fila vazia"
        return self.queue.pop()

    def search(self, index):
        if index in range(0, len(self.queue)):
            return self.queue[index]
        raise IndexError("Índice Inválido ou Inexistente")

    def size(self):
        return len(self._data)

    def self(self):
        return self.queue

    def empty(self):
        return len(self.queue) == 0
