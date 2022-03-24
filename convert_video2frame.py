from ntpath import join
import cv2
import logging
import os
import random
import string

def rand_string(length):
    rand_str = "".join(random.choice('y') for i in range(length))
    return rand_str

def length_of_video(video_path):
    cap = cv2.VideoCapture(video_path)
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def extracting_frames(video_path, save_path, skip_frames = 10):
    _, file_name = os.path.split(video_path)
    file_name_without_ext=os.path.splitext(file_name)[0]
    # check length
    length = length_of_video(video_path)
    if length == 0:
        print('Length is 0, exiting extracting phase')
        return 0
    
    cap = cv2.VideoCapture(video_path)
    count = 0
    random_string = rand_string(0) # for naming
    #test first frame
    ret,frame = cap.read()
    test_file_path = os.path.join(
        save_path,
        file_name_without_ext+ \
            '{}_{}.jpg'.format(random_string,count))
    cv2.imwrite(test_file_path,frame)
    if os.path.isfile(test_file_path):
        print('Saving Test Frame was Successful' + 'Continuing Extraction Phase')
        count = 1
        while ret:
            ret,frame = cap.read()
            if ret and count % skip_frames == 0:
                cv2.imwrite(os.path.join(
                    save_path,
                    file_name_without_ext+
                    '{}_{}.jpg'.format(random_string,count)), frame)
                count += 1
                print(count)
            else:
                count += 1
    else:
        print('Problem with saving test frame cv2 encoding, cannot save file')
        return 0
    cap.release()
    print('FINISH EXTRACTION')

if __name__ == '__main__':
    video = ["lovelycat.mp4"]
    save_path = "output"
    for i in video:
        print(i)
        extracting_frames(i,save_path,skip_frames=10)