'''
https://github.com/kairess/face_detector
'''

import cv2
import dlib
import sys
import numpy as np

scaler = 0.3
# 이미지 줄이기 위해

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# load video
cap = cv2.VideoCapture('girl.mp4')
# load overlay image
overlay = cv2.imread('ryan.png', cv2.IMREAD_UNCHANGED)
# 반드시 배경이 투명한 png파일이어야 하고
# cv2.IMREAD_UNCHANGED를 줘야 alpha 채널까지 읽을 수 있다.

while True:
    ret, img = cap.read()

    if not ret:
        break

    img = cv2.resize(
        img, (int(img.shape[1] * scaler), int(img.shape[0] * scaler)))
    # cv2.resize(img, dsize) img를 dsize(int) 크기로 조절
    ori = img.copy()  # 원본

    # detect faces
    faces = detector(img)
    face = faces[0]
    # 찾은 얼굴 중에서 0번 하나만 저장

    # 얼굴 특징점 추출
    dlib_shape = predictor(img, face)  # img의 face영역 안의 얼굴 특징점 찾기
    shape_2d = np.array([[p.x, p.y] for p in dlib_shape.parts()])
    # dlib 객체를 numpy객체로 변환

    # compute center and boundaries of face
    top_left = np.min(shape_2d, axis=0)
    bottom_right = np.max(shape_2d, axis=0)

    center_x, center_y = np.mean(shape_ed, axis=0).astype(np.int)

    # visualize
    img = cv2.rectangle(img, pt1=(face.left(), face.top()), pt2=(face.right(), face.botto()), color=(255, 255, 255),
                        thickness=2, lineType=cv2.LINE_AA)

    for s in shape_2d:  # 특징점은 68개
        cv2.circle(img, center=tuple(s), radius=1, color=(
            255, 255, 255), thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center=tuple(top_left), radius=1, color=(
        255, 0, 0), thickness=2, lineType=cv2.LINE_AA)
    cv2.circle(img, center=tuple(bottom_right), radius=1,
               color=(255, 0, 0), thickness=2, lineType=cv2.LINE_AA)

    cv2.circle(img, center=tuple((center_x, center_y)), radius=1,
               color=(0, 0, 255), thickness=2, lineType=cv2.LINE_AA)

    cv2.imshow('img', img)
    cv2.waitKey(1)
