def pop(heap):
    if len(heap) == 0:
        raise IndexError("pop from empty heap")
    elif len(heap) == 1:
        return heap.pop()

    root = heap[0]
    heap[0] = heap.pop()
    parent_index = 0

    while True:
        left_child_index = 2 * parent_index + 1
        right_child_index = 2 * parent_index + 2

        if left_child_index >= len(heap):
            break

        if right_child_index >= len(heap):
            if heap[left_child_index] < heap[parent_index]:
                heap[left_child_index], heap[parent_index] = heap[parent_index], heap[left_child_index]
            break

        if heap[left_child_index] < heap[right_child_index]:
            child_index = left_child_index
        else:
            child_index = right_child_index

        if heap[child_index] < heap[parent_index]:
            heap[child_index], heap[parent_index] = heap[parent_index], heap[child_index]
            parent_index = child_index
        else:
            break

    return root

heap = [3, 4, 5, 6, 9, 8, 10, 7]
pop(heap)

def push(heap, value):
    heap.append(value)
    child_index = len(heap) - 1
    parent_index = (child_index - 1) // 2
    while child_index > 0 and heap[child_index] < heap[parent_index]:
        heap[child_index], heap[parent_index] = heap[parent_index], heap[child_index]
        child_index, parent_index = parent_index, (parent_index - 1) // 2

heap = [3, 4, 7, 6, 9, 8, 10]
push(heap, 5)
