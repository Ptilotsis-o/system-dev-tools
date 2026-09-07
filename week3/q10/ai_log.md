1. 核心提示：要求当 --name 参数值为纯空白时，程序必须调用 sys.exit(2) 退出，不可输出问候语，且不影响正常非空输入。
2. 智能体改动：在 cli.py 的 parse\_args 后增加 if not a.name.strip(): sys.exit(2)，并补全了 import sys。
3. 人工验证：运行 git diff 确认未改动其他文件；执行 pytest tests/，测试通过。
