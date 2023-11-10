def solution(routes):
    camera = 0          # 카메라 개수
    camera_pos = 30001  # 이전 카메라의 위치
    routes.sort(key=lambda x:x[1])

    for route in routes:
        enter_point, exit_point = route
        if enter_point <= camera_pos <= exit_point:
            continue
        camera_pos = exit_point
        camera += 1

    return camera