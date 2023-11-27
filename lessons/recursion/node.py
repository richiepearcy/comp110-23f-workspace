"""Node Class."""

from __future__ import annotations


class Node:
    """My Node class for linked lists."""
    
    data: int
    next: Node | None
    
    def __init__(self, data: int, next: Node | None):
        """Construct Node."""
        self.data = data
        self.next = next
        
    def __str__(self) -> str:
        """Produce a string visualization of the linked list."""
        if self.next is None:
            # base case (where it ends!)
            return f"{self.data} -> None"
        else:
            return f"{self.data} -> {self.next}"
        
    def head(self) -> int:
        """Producing the int of the first element of linked list."""
        if self.next.next is None:
            # base case
            return self.data
    
    def tail(self) -> Node | None:
        """Producing linked list minus the head."""
        if self.next.next is not None:
            # non base case
            return f"{self.data} -> {self.next.data} -> None"
        else:
            return "None"
    
    def last(self) -> int:
        """Producing int of last element of linked list."""
        if self.next is None:
            # base case
            return self.data
        else: 
            return self.next.next.data