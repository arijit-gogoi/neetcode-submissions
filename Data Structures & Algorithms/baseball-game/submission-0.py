class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res, stack = 0, []
        for op in operations:
            if op == "+":
                sum_ = stack[-1] + stack[-2]
                res += sum_
                stack.append(sum_)
            elif op == "D":
                doubled = 2 * stack[-1]
                res += doubled
                stack.append(doubled)
            elif op == "C":
                res -= stack.pop()
            else:
                res += int(op)
                stack.append(int(op))
        return res