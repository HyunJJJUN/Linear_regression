import math
import matplotlib.pyplot as plt

# 데이터 포인트 입력 받기
n = int(input("데이터 포인트의 개수: "))
points = []
for i in range(n):
    x, y = map(float, input("x, y 좌표 입력: ").split())
    points.append((x, y))

# x, y 평균 계산
x_mean = sum([p[0] for p in points]) / n
y_mean = sum([p[1] for p in points]) / n

# 분자, 분모 계산
numerator = sum([(p[0] - x_mean) * (p[1] - y_mean) for p in points])
denominator = sum([(p[0] - x_mean) ** 2 for p in points])

# 추세선 계수 계산
m = numerator / denominator
b = y_mean - m * x_mean

# 데이터와 추세선 사이의 거리 계산
distances = []
for p in points:
    x, y = p
    y_pred = m * x + b
    distance = math.sqrt((y - y_pred) ** 2)
    distances.append(distance)

# 평균 거리 출력
mean_distance = sum(distances) / n
print("평균 거리: {:.2f}".format(mean_distance))

# 추세선 및 데이터 그래프 출력
plt.scatter([p[0] for p in points], [p[1] for p in points])
plt.plot([p[0] for p in points], [m * p[0] + b for p in points])
plt.show()
