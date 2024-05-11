import matplotlib.pyplot as plt

# 数据
x = [8, 16, 32, 64, 128, 256]
y = [2.929126, 1.573351, 0.801574, 0.438791, 0.304817, 0.160913]
result = [a * b for a, b in zip(x, y)]
# 创建画布和子图
fig, ax = plt.subplots()

# 绘制折线图
ax.plot(x, result, marker='o', linestyle='-')
ax.set_xticks(x)
ax.set_yticks(result)

# 添加标题和标签
ax.set_title('Execution time * Processes - Processes')
ax.set_xlabel('Processes')
ax.set_ylabel('Time*Processes(Core*s)')

# 显示图形
plt.show()
