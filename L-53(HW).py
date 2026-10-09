def total_points_formula(n):
    """Method 1: Formula - O(1) Time, O(1) Space"""
    return (n * (n + 1)) // 2


def total_points_loop(n):
    """Method 2: Single Loop - O(N) Time, O(1) Space"""
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


def total_points_nested(n):
    """Method 3: Nested Loop - O(N^2) Time, O(1) Space"""
    total = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            total += 1
    return total


# --- Example Test Execution ---
if __name__ == "__main__":
    days = 100
    print(f"Tracking points for {days} days:\n" + "-"*30)
    print(f"Formula Result:     {total_points_formula(days)} points")
    print(f"Single Loop Result: {total_points_loop(days)} points")
    print(f"Nested Loop Result: {total_points_nested(days)} points")
