import cv2
import numpy as np

video_path = 'lullaby.mp4'
cap = cv2.VideoCapture(video_path)  # 비디오 읽어오기

# 영상 저장 사이즈
output_size = (375, 667)  # (width, height)

# initialize writing video 영상 저장 함수
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')  # mp4v라는 코텍으로 저장
out = cv2.VideoWriter('%s_output.mp4' % (video_path.split(
    '.')[0]), fourcc, cap.get(cv2.CAP_PROP_FPS), output_size)
# VideoWriter (내보낼 파일 이름, 코덱, FPS(1초당 프레임(이미지)의 개수, 내보낼 사이즈)
# cap.get(cv2.CAP_PROP_FPS) : cap에 로드된 동영상의 FPS를 반환한다.

if not cap.isOpened():
    exit()

tracker = cv2.TrackerCSRT_create()
# csrt tracker initialize

# Region of Interest
ret, img = cap.read()  # 첫 프레임을 불러온다.

# ROI 지정할 윈도우 이름 설정
cv2.namedWindow('Select Window')
# Select Window에 첫번째 프레임 보여주기
cv2.imshow('Select Window', img)

# seting ROI
rect = cv2.selectROI('Select Window', img,
                     fromCenter=False, showCrosshair=True)
# Select Window에서 ROI를 설정해라
# img 의 Center에서 시작하지 말고, 중심점을 보여라. -> 십자가 모양으로 보여줌
# drog로 ROI지정 후 space bar 누르면 rect에 저장됨.
cv2.destroyWindow('Select Window')
# ROI 선택 후 윈도우 닫기

# initialize tracker
tracker.init(img, rect)

while True:  # 동영상 재생
    ret, img = cap.read()  # 1프레임씩 읽어옴
    # 잘못 읽거나 비디오가 끝나면 ret이 False가 됨

    if not ret:
        exit()

    success, box = tracker.update(img)
    # tracker.update(img) img에서 rect로 설정한 이미지와 비슷한 물체의 위치를 찾아 반환한다.
    # success는 성공 여부 boolean

    left, top, width, height = [int(v) for v in box]

    center_x = left + width/2
    center_y = top + height/2

    '''
    추후 과제

    + 잘라낼 동영상의 위치와 크기를 이동평균(moving average)를 사용해 계산해보자
    + 예외처리
    
    '''
    result_top = int(center_y - output_size[1] / 2)
    result_bottom = int(center_y - output_size[1] / 2)
    result_left = int(center_y - output_size[0] / 2)
    result_right = int(center_y - output_size[0] / 2)

    result_img = img[result_top:result_bottom, result_left:result_right].copy()
    # numpy.copy()로 numpy array를 복사, 밑에 확인용 tracking 사각형이 같이 저장되지는 않음.

    # 제대로 잘렸는지 확인
    #cv2.imshow('result_img', result_img)
    # 'result_img'라는 윈도우에 result_img 띄우기

    # 비디오 저장!
    out.write(result_img)

    # 제대로 트래킹을 하는지 확인을 위해 사각형 그리기
    cv2.rectangle(img, pt1=(left, top), pt2=(
        left + width, top + height), color=(255, 255, 255), thickness=3)
    #pt1 = (왼쪽, 위), pt2 = (오른쪽, 아래)
    cv2.imshow()  # 윈도우에 이미지 출력
    if cv2.waitKey(1) == ord('q'):
        # ord('q')에 해당하는 아스키 코드 int 반환
        break  # 윈도우에서 키 입력을 기다리다가 q입력시 종료
    # cv2.waitKey(n) 키 입력을 n밀리세컨드간 기다린다
    # waitKey를 안 쓰면 윈도우가 백그라운드에서 혼자 돌다가 꺼진다.

    # 영상 저장
