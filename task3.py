from avl import build_avl, inorder_values


def sum_values(root) -> int:
    """Task 3: sum of all keys in AVL tree."""
    if root is None:
        return 0
    return root.key + sum_values(root.left) + sum_values(root.right)


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50, 25]
    root = build_avl(values)

    print("Values:", values)
    print("In-order (sorted):", inorder_values(root))
    print("Sum:", sum_values(root))  # expected: 175
