import cv2

# 이미지 열기
img = cv2.imread("C:/Users/user/Desktop/gray/gray.jpg")

# 흑백 이미지로 변환
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 변환된 이미지 보기
cv2.imshow('Black and White Image', gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지 저장
cv2.imwrite('black_and_white.jpg', gray_img)