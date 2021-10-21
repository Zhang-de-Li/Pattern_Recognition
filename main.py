from scipy import stats
import math

data = [-2.67, -3.55, -1.24, -0.98,
        -0.79, -2.85, -2.76, -3.73,
        -3.54, -2.27, -3.45, -3.08,
        -1.58, -1.49, -0.74, -0.42,
        -1.12, 4.25, -3.99, 2.88,
        -0.98, 0.79, 1.19, 3.07]

std1 = math.sqrt(1.5)
std2 = math.sqrt(2)
p_x_w1 = stats.norm.pdf(data, loc = -2, scale = std1)  # 类条件概率
p_x_w2 = stats.norm.pdf(data, loc = 2, scale = std2)
p_w1 = 0.9  # 先验概率
p_w2 = 0.1
p_x = p_w1 * p_x_w1 + p_x_w2 * p_w2  # 全概率
p_w1_x = p_x_w1 * p_w1 / p_x    # 后验概率
p_w2_x = 1 - p_w1_x
lose11 = 0
lose22 = 0
lose12 = 7
lose21 = 2
Conditional_risk1 = lose11 * p_w1_x + lose12 * p_w2_x
Conditional_risk2 = lose21 * p_w1_x + lose22 * p_w2_x

ret = []
for i in range(24): # 最小风险
    if Conditional_risk1[i] < Conditional_risk2[i]:
        ret.append(0)
    else:
        ret.append(1)
ret2 = []
for i in range(24): # 最小错误率
    if p_w1_x[i] > p_w2_x[i]:
        ret2.append(0)
    else:
     ret2.append(1)
print("最小风险决策分类结果如下：")
print(ret)
print("最小错误率决策分类结果如下：")
print(ret2)
