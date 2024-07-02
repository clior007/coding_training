import sort

def test_sort():
    assert sort.bubble_sort([8, 6, 5, 4, 2]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    print("bubble_sort passed\n\n")
    assert sort.bubble_sort([2, 4, 5, 6, 8]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    print("bubble_sort passed\n\n")

    assert sort.insertion_sort([8, 2, 6, 4, 5]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    print("insertion_sort passed\n\n")
    assert sort.insertion_sort([2, 4, 5, 6, 8]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    print("insertion_sort passed\n\n")

    assert sort.merge_sort([8, 2, 6, 4, 5]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    print("merge_sort passed\n\n")
    assert sort.merge_sort([2, 4, 5, 6, 8]) == [2, 4, 5, 6, 8], "Should be [2, 4, 5, 6, 8]"
    
if __name__ == "__main__":
    test_sort()
    print("Everything passed")
