from  detect_model import card_detector
import time
import cv2
import random
import os

#test
def start_detection():
    print("Starting card detection...")
    card_detector_instance = card_detector.Card_Detector()
    detection = card_detector.detect_and_transmit(card_detector_instance)

    print(f"Detected cards: {detection}")
    return detection

def test_detections_continues(system_status):

    for _ in range(5):
        detection = start_detection()
        system_status["log"].append(f"detected: {detection}")
        system_status["deck_order"].append(detection)
        time.sleep(2)

def get_image_from_path(image_path):
    return(cv2.imread(image_path))

def get_virtual_deck(folder_path=r'test_deck'):
    '''Loads all images in test_deck directory and returns a shuffled list of images'''
    image_list = []
    
    # Load all image file paths from the folder
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
            print(filename)
            image_path = os.path.join(folder_path, filename)
            image_list.append(get_image_from_path(image_path))
    
    #random.shuffle(image_list)    
    return image_list

def test_virtual_deck(system_status):
    print("testing virtual deck")
    system_status["virtual_deck"] = get_virtual_deck()
    card_detector_instance = card_detector.Card_Detector()
    count = 0
    fail_count = 0
    while len(system_status["virtual_deck"]) > 0:
        curr_card  = system_status["virtual_deck"].pop()
        count+=1
        #print(count)
        #print(system_status["deck_order"][-1])
        detection = card_detector_instance.detect_from_image(curr_card)
        if detection == None:
            print("failed to detect!")
            fail_count += 1
        else:
            system_status["deck_order"].extend(detection)
        time.sleep(0.2)
    print(f"detected {count-fail_count}/{count} cards")