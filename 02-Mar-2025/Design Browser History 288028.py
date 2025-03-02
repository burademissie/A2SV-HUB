# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class ListNode:
    def __init__(self,val, pre=None , next = None):
        self.val = val
        self.pre = pre
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url , self.cur)
        self.cur = self.cur.next
        

    def back(self, steps: int) -> str:
        while self.cur.pre and steps:
            self.cur = self.cur.pre
            steps -= 1
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        while self.cur.next and steps:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)