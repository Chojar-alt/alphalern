import numpy as np
import cv2
from PIL import Image

image2 = cv2.imread(r'iron.jpg')
mask = np.zeros(image2.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect = (1,30,665,344)
cv2.grabCut(image2,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
image2 = image2*mask2[:,:,np.newaxis]
black_mask = np.all(image2 == 0, axis=-1)
alpha = np.uint8(np.logical_not(black_mask)) * 255
image2 = np.dstack((image2, alpha))
cv2.imwrite("rgba21.png", image2)
#image2.save('test.png')


cv2.waitKey(0)
cv2.destroyAllWindows()