class Solution:
    def calPoints(self, operations: List[str]) -> int:
        res, stack = 0, []
        for x in operations:
            if x == "+":
                sum_ = stack[-1] + stack[-2]
                res += sum_
                stack.append(sum_)
            elif x == "D":
                doubled = 2 * stack[-1]
                res += doubled
                stack.append(doubled)
            elif x == "C":
                res -= stack.pop()
            else:
                num = int(x)
                res += num
                stack.append(num)
        return res