# =============================================================================
#  Name:            ReversePolishSolver
#  Purpose:
#
#  Author:          Winnie Ding
#  Date Created:    10/29/2020
# =============================================================================

class Stack():
    """
    Stack container
    """
    def __init__(self):
        self.stack = list()

        # Count of elements in stack
        self.count = 0

        # Index of top of stack
        self.top = -1

    def push(self, value):
        """
        Push a value onto stack.
        """
        # Move top tracker
        self.top += 1

        # Add new value to stack
        self.stack.append(value)

        # Increment count
        self.count += 1

    def pop(self):
        """
        Remove and return value at top of stack.
        """
        if self.count > 0:
            # Store value at top of stack
            output = self.stack[self.top]

            # Remove top value from stack
            del self.stack[self.top]

            # Move top tracker
            self.top -= 1

            # Decrement count
            self.count -= 1

            return output

        return None


def ReversePolishSolver(combinations_list):
    """
    Solves a given problem in reverse polish notation
    """

