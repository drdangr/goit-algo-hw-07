from avl import build_avl, inorder_values


def find_max(root):
    """Task 1: largest value in AVL tree. Returns None if empty."""
    if root is None:
        return None
    cur = root
    while cur.right is not None:
        cur = cur.right
    return cur.key


def right_path_keys(root):
    path = []
    cur = root
    while cur is not None:
        path.append(cur.key)
        cur = cur.right
    return path


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50, 25]
    root = build_avl(values)

    print("Values:", values)
    print("In-order (sorted):", inorder_values(root))
    print("Right path:", right_path_keys(root))
    print("Max value:", find_max(root))  # expected: 50
