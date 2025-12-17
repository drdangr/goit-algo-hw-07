from avl import build_avl, inorder_values


def find_min(root):
    """Task 2: smallest value in AVL tree. Returns None if empty."""
    if root is None:
        return None
    cur = root
    while cur.left is not None:
        cur = cur.left
    return cur.key


def left_path_keys(root):
    path = []
    cur = root
    while cur is not None:
        path.append(cur.key)
        cur = cur.left
    return path


if __name__ == "__main__":
    values = [10, 20, 30, 40, 50, 25]
    root = build_avl(values)

    print("Values:", values)
    print("In-order (sorted):", inorder_values(root))
    print("Left path:", left_path_keys(root))
    print("Min value:", find_min(root))  # expected: 10
