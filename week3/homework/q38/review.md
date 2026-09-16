标签：Blocking
具体行为：`def add(a, b) -> int` 标注返回 int，但 `add(1.5, 2)` 实际返回 float。
风险：调用方可能按 int 处理，导致精度丢失或类型错误。
建议动作：将返回类型改为 `float`，或在使用前显式转换。`
