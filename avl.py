class AVLNode:
    def __init__(self, key: int):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


def get_height(node) -> int:
    return node.height if node else 0


def get_balance(node) -> int:
    return get_height(node.left) - get_height(node.right) if node else 0


def right_rotate(y: AVLNode) -> AVLNode:
    x = y.left
    t2 = x.right

    x.right = y
    y.left = t2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x


def left_rotate(x: AVLNode) -> AVLNode:
    y = x.right
    t2 = y.left

    y.left = x
    x.right = t2

    x.height = 1 + max(get_height(x.left), get_height(x.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y


def insert(root, key: int):
    if root is None:
        return AVLNode(key)

    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))
    balance = get_balance(root)

    # Left Left
    if balance > 1 and key < root.left.key:
        return right_rotate(root)

    # Right Right
    if balance < -1 and key > root.right.key:
        return left_rotate(root)

    # Left Right
    if balance > 1 and key > root.left.key:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    # Right Left
    if balance < -1 and key < root.right.key:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder_values(root) -> list[int]:
    """In-order traversal: returns sorted keys for BST/AVL."""
    if root is None:
        return []
    return inorder_values(root.left) + [root.key] + inorder_values(root.right)


def build_avl(values: list[int]):
    """Helper: build AVL tree from list of ints."""
    root = None
    for v in values:
        root = insert(root, v)
    return root
