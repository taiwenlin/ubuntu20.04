"""
    YOLO & Python 環境需求
        1. .data
        2. .name
        3. .cfg
        4. .weight
        5. darknet(shared library)
        6. darknet.py
        7. libdarknet.so
"""


import time
import cv2
import numpy as np
import darknet
import pyrealsense2 as rs



pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)
sensor = pipeline.get_active_profile().get_device().query_sensors()[1]
sensor.set_option(rs.option.auto_exposure_priority, True)


# 神經網路檔案位置
data_path = 'cfg/mouse_yolotest.data'
cfg_path = 'cfg/yolov4-tiny.cfg'
weights_path = 'cfg/weights/yolov4-tiny_last.weights'




"""
載入神經網路
"""
network, class_names, class_colors = darknet.load_network(
        cfg_path,
        data_path,
        weights_path,
        batch_size=1
)




"""
影像檢測
    輸入:(影像位置,神經網路,物件名稱集,信心值閥值(0.0~1.0))
    輸出:(檢測後影像,檢測結果)
    註記:
"""
def image_detection(image, network, class_names, class_colors, thresh):
    width = darknet.network_width(network)
    height = darknet.network_height(network)
    darknet_image = darknet.make_image(width, height, 3)

    
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (width, height),
                               interpolation=cv2.INTER_LINEAR)

    darknet.copy_image_from_bytes(darknet_image, image_resized.tobytes())
    detections = darknet.detect_image(network, class_names, darknet_image, thresh=thresh)
    darknet.free_image(darknet_image)
    image = darknet.draw_boxes(detections, image_resized, class_colors)

    print(detections)

    return detections



"""
座標轉換
    輸入:(YOLO座標,原圖寬度,原圖高度)
    輸出:(框的左上座標,框的右下座標)
    註記:
"""
def bbox2points(bbox,W,H):
    """
    From bounding box yolo format
    to corner points cv2 rectangle
    """ 
    width = darknet.network_width(network)      # YOLO壓縮圖片大小(寬)
    height = darknet.network_height(network)    # YOLO壓縮圖片大小(高)

    x, y, w, h = bbox                           # (座標中心x,座標中心y,寬度比值,高度比值)
    x = x*W/width
    y = y*H/height
    w = w*W/width
    h = h*H/height
    x1 = int(round(x - (w / 2)))
    x2 = int(round(x + (w / 2)))
    y1 = int(round(y - (h / 2)))
    y2 = int(round(y + (h / 2)))
    
    return x1, y1, x2, y2



"""
原圖繪製檢測框線
    輸入:(檢測結果,原圖位置,框線顏色集)
    輸出:(影像結果)
    註記:
"""
def draw_boxes(detections, image, colors):
    H,W,_ = image.shape
    img = image.copy()

    for label, confidence, bbox in detections:
        x1, y1, x2, y2 = bbox2points(bbox,W,H)

        cv2.rectangle(img, (x1, y1), (x2, y2), colors[label], 1)
        cv2.putText(img, "{} [{:.2f}]".format(label, float(confidence)),
                    (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    colors[label], 2)
        # 輸出框座標_加工格式座標(左上點座標,右上點座標)
        print("\t{}\t: {:3.2f}%    (x1: {:4.0f}   y1: {:4.0f}   x2: {:4.0f}   y2: {:4.0f})".format(label, float(confidence), x1, y1, x2, y2))


    return img




"""
主程式
    程式流程:
    1. 檢測影像
    2. 在原圖繪製結果
    3. 輸出影像
"""
if __name__ == "__main__":

    while True:

        frames = pipeline.wait_for_frames()
        img = frames.get_color_frame()
        img = np.asanyarray(img.get_data())

        detections = image_detection(img,network, class_names, class_colors, thresh=0.8)
        out_img = draw_boxes(detections, img, class_colors)

        cv2.imshow('out', out_img)
        cv2.waitKey(1)


cv2.destroyAllWindows()

