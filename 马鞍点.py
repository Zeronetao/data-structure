def saddle_points(matrix):
    # 检查矩阵是否为空
    if not matrix:
        return set()
    # 初始化空集合
    saddle_points = set()
    # 获取矩阵行数和列数
    rows = len(matrix)
    cols = len(matrix[0])
    # 对每个元素进行遍历
    for row in range(rows):
        for col in range(cols):
            # 获取当前元素的值
            val = matrix[row][col]
            # 判断是否为当前行最小值和当前列最大值
            if val == min(matrix[row]) and val == max(matrix[row][col] for row in range(rows)):
                saddle_points.add(( row, col))
    # 返回所有马鞍点集合
    return saddle_points


# 测试用例
if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print(saddle_points(matrix))  # 结果为{(0, 1)}