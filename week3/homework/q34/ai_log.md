核心提示：修改 divide，使除零返回 None 并向 stderr 输出 "division by zero"，保持正常除法。
智能体改动：在 divide 中判断 b == 0，打印错误到 stderr 并返回 None。
人工验证：diff 仅见该判断；pytest test\_divide.py -v 全部通过。
