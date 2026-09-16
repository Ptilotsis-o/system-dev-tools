核心提示：修改 parse\_duration，使 "1h30m" 返回 90，保持 "2h" 返回 120。
智能体改动：用正则匹配可选的小时和分钟，返回 h\*60 + m。
人工验证：diff 仅修改 parse\_duration；pytest test\_duration.py -v 两个测试通过。
