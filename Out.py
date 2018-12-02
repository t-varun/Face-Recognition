import numpy as np
import cv2
from random import shuffle

train_data = np.load('training_data.npy')

TOTAL = []

for data in train_data:
    img = data[0]
    person = data[1]
    if person == 'VARUN':
        TOTAL.append([img, person])
    elif person == 'BUNNY':
        TOTAL.append([img, person])

shuffle(TOTAL)
if TOTAL is not None:
    np.save('training_data_cleaned.npy', TOTAL)
    print("Done")
else:
    print("No Matches.")

##for data in np.load('training_data_cleaned.npy'):
##    img = data[0]
##    person = data[1]
##    cv2.imshow('test', img)
##    print(person)
##    if cv2.waitKey(25) & 0xFF == ord('q'):
##        cv2.destroyAllWindows()
##        break
    
