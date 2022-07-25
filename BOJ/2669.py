"""
BOJ 2669 직사각형 네개의 합집합의 면적 구하기
"""


def get_rect_list():
    rect_coords = []
    # 네 직사각형의 좌표 정보 획득
    for _ in range(4):
        x1, y1, x2, y2 = map(int, input().split(' '))
        rect_coords.append([x1, y1, x2, y2])
    return rect_coords


rect_coords = get_rect_list()

answer = 0

# x축 돌기
for x in range(0, 100):
    # y축 돌기
    for y in range(0, 100):
        # 직사각형 돌기
        for x1, y1, x2, y2 in rect_coords:
            if x1 <= x < x2 and y1 <= y < y2:
                answer += 1
                break

print(answer)
