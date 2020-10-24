import cv2
import numpy as np
import matplotlib.pyplot as plt

#오츠 알고리즘.pptx 2페이지 참고
#Intra-Class Variance 구현
def thresholdOtsu_min(img):
    #히스토그램 구하기
    hist = cv2.calcHist([img.ravel()], [0], None, [256], [0, 256])
    #히스토그램 정규화
    hist_norm = (hist.ravel() - hist.min()) * (255) / (hist.max() - hist.min())
    min_result = np.inf
    trs = -1

    for std in range(0, 256):
        #임계값 기준으로 픽셀들을 두 클래스로 분류
        c0, c1 = np.hsplit(hist_norm,[std])
        #각 클래스의 비율
        w0, w1 = c0.sum(), c1.sum()
        # 0으로 나누게 될 경우 패스
        if w0 == 0 or w1 == 0:
            continue
        i0, i1 = np.hsplit(np.arange(256),[std])
        #각 클래스의 밝기 평균
        u0, u1 = np.sum(c0 * i0) / w0, np.sum(c1 * i1) / w1
        #각 클래스의 분산
        v0, v1 = np.sum(c0*((i0-u0)**2)) / w0, np.sum(c1*((i1-u1)**2)) / w1
        #계산 결과
        result = w0*v0 + w1*v1
        #결과값이 작을수록 적절한 임계값
        if min_result > result:
            min_result = result
            trs = std
    #임계값, 임계값 기준으로 스레시홀드한 행렬 반환
    return trs, np.where(img > trs, trs, 0)


#오츠 알고리즘.pptx 2페이지 참고
#Inter-Class Variance 구현
def thresholdOtsu_max(img):
    #히스토그램 구하기
    hist = cv2.calcHist([img.ravel()], [0], None, [256], [0, 256])
    #히스토그램 정규화
    hist_norm = (hist.ravel() - hist.min()) * (255) / (hist.max() - hist.min())
    max_result = 0
    trs = -1

    for std in range(0, 256):
        #임계값 기준으로 픽셀들을 두 클래스로 분류
        c0, c1 = np.hsplit(hist_norm,[std])
        #각 클래스의 비율
        w0, w1 = c0.sum(), c1.sum()
        # 0으로 나누게 될 경우 패스
        if w0 == 0 or w1 == 0:
            continue
        #각 클래스의 밝기 평균
        i0, i1 = np.hsplit(np.arange(256),[std])
        u0, u1 = np.sum(c0 * i0) / w0, np.sum(c1 * i1) / w1
        #계산 결과
        result = w0 * w1 * ((u0 - u1)**2)
        #결과값이 클수록 적절한 임계값
        if max_result < result:
            max_result = result
            trs = std
    #임계값, 임계값 기준으로 스레시홀드한 행렬 반환
    return trs, np.where(img > trs, trs, 0)

#비교를 위한 원본
img = cv2.imread('../../Images/DrG.jpg', cv2.IMREAD_GRAYSCALE)
#비교를 위한 openCV 제공 오츠 함수
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#직접 구현한 오츠 알고리즘. 원리는 같지만 식이 다르다.
min_t, myOtsu_min = thresholdOtsu_min(img)
max_t, myOtsu_max = thresholdOtsu_max(img)

imgs = {'original':img, 'otsu:%d'%t: t_otsu, 'myOtsu1:%d'%min_t: myOtsu_min, 'myOtsu2:%d'%max_t: myOtsu_max}
for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 4, i+1)
    plt.title(key)
    plt.imshow(value, cmap='gray')
    plt.xticks([]); plt.yticks([])
plt.show()