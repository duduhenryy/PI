import matplotlib.pyplot as plt
import cv2

img = cv2.imread("tarefa1/sources/amor.jpeg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # converte o bgr para o rgb

plt.imshow(img_rgb)
plt.axis('off')
plt.show()
