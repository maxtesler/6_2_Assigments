from decorators.task3 import check_types

@check_types
def add(a: int, b: int) -> int:
    return a + b

add("1", "2")
add(1, 2)