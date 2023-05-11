from calendar import c
from operator import mod
import numpy as np
from ctypes import *
import time
import rospy

import cv2
import darknet
import pyrealsense2 as rs
'''
    DO(int DO_Num, int x)                                                         # 1 -> on ; 0 -> off                                          
    HOME(int state)                                                               # 1 RUN
    PTP(int type, int vel, int acc, int TOOL, int BASE, double *Angle)            # 0 -> joint ; 1 -> coordinate
    LIN(int type,double *XYZ, int vel, int acc, int TOOL, int BASE)               # 0 -> joint ; 1 -> coordinate
    CIRC(double *CIRC_s, double *CIRC_end, int vel, int acc, int TOOL, int BASE) 
    JOG(int joint,int dir)
'''

so_file = "./Hiwin_API.so"
modbus = CDLL(so_file)

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 1280, 720, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 1280, 720, rs.format.bgr8, 30)
pipeline.start(config)
sensor = pipeline.get_active_profile().get_device().query_sensors()[1]
sensor.set_option(rs.option.auto_exposure_priority, True)


# 神經網路檔案位置
data_path = '/home/lintaiwen/yolo_video_detect/cfg/mouse_yolotest.data'
cfg_path = '/home/lintaiwen/yolo_video_detect/cfg/yolov4-tiny.cfg'
weights_path = '/home/lintaiwen/yolo_video_detect/cfg/weights/yolov4-tiny_final.weights'




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
def show_img(img,delay_time):
    cv2.namedWindow('new', cv2.WINDOW_FREERATIO)
    cv2.imshow('new', img)
    cv2.waitKey(delay_time)


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
    
    return img,x1,y1,x2,y2
    # return img,x1,y1,x2,y2
def CtoA(Cx,Cy):
    Ax=-387.5+0.6054*Cx
    Ay=667.5-0.604*Cy
    return Ax,Ay

def go_to_point(Angleorxyz,ptporlin,num,speed,acc):
    if Angleorxyz == 'XYZ':
        if ptporlin == 'PTP':
            PTP_XYZ   = num    # XYZABC
            C_PTP_XYZ = (c_double * len(PTP_XYZ))(*PTP_XYZ)
            while 1:
                modbus.PTP(1, speed, acc, 1, 0, C_PTP_XYZ)
                if(modbus.Arm_State_REGISTERS() == 1):
                    print("status_in= ",modbus.Arm_State_REGISTERS())
                    break
        else:
            LIN_XYZ   = num    # XYZABC
            C_LIN_XYZ = (c_double * len(LIN_XYZ))(*LIN_XYZ)
            while 1:
                modbus.LIN(1, speed, acc, 1, 0, C_LIN_XYZ)
                if(modbus.Arm_State_REGISTERS() == 1):
                    print("status_in= ",modbus.Arm_State_REGISTERS())
                    break
    else:
        if ptporlin == 'PTP':
            PTP_Angle   = num    # XYZABC
            C_PTP_Angle = (c_double * len(PTP_Angle))(*PTP_Angle)
            while 1:
                modbus.PTP(1, speed, acc, 1, 0, C_PTP_Angle)
                if(modbus.Arm_State_REGISTERS() == 1):
                    print("status_in= ",modbus.Arm_State_REGISTERS())
                    break
        else:
            LIN_Angle   = num    # XYZABC
            C_LIN_Angle = (c_double * len(LIN_Angle))(*LIN_Angle)
            while 1:
                modbus.LIN(1, speed, acc, 1, 0, C_LIN_Angle)
                if(modbus.Arm_State_REGISTERS() == 1):
                    print("status_in= ",modbus.Arm_State_REGISTERS())
                    break

def suck_cup_lid():
    cup_lid_point[2] += 130
    go_to_point('XYZ','PTP',cup_lid_point,100,40)
    go_to_point('XYZ','PTP',cup_lid_point,100,40)
    modbus.DO(300,1)
    modbus.DO(303,1)
    cup_lid_point[2] -= 130
    go_to_point('XYZ','PTP',cup_lid_point,100,40)
    go_to_point('XYZ','PTP',cup_lid_point,100,40)
    
    cup_lid_point[2] += 130
    go_to_point('XYZ','PTP',cup_lid_point,100,10)
    go_to_point('XYZ','PTP',cup_lid_point,100,10)
    cup_lid_point[2] -= 130
    
def suck_left_cup():
    cup_left_point[2] += 130
    go_to_point('XYZ','PTP',cup_left_point,100,40)
    go_to_point('XYZ','PTP',cup_left_point,100,40)
    modbus.DO(300,1)
    modbus.DO(303,1)
    cup_left_point[2] -= 130
    go_to_point('XYZ','PTP',cup_left_point,100,40)
    go_to_point('XYZ','PTP',cup_left_point,100,40)
    
    cup_left_point[2] += 130
    go_to_point('XYZ','PTP',cup_left_point,100,10)
    go_to_point('XYZ','PTP',cup_left_point,100,10)
    cup_left_point[2] -= 130
    
def put_cup_at_ws():
    cup_ws[2] += 130
    go_to_point('XYZ','PTP',cup_ws,100,40)
    go_to_point('XYZ','PTP',cup_ws,100,40)
    cup_ws[2] -= 100
    go_to_point('XYZ','PTP',cup_ws,100,40)
    go_to_point('XYZ','PTP',cup_ws,100,40)
    cup_ws[2] -= 30
    go_to_point('XYZ','PTP',cup_ws,100,40)
    go_to_point('XYZ','PTP',cup_ws,100,40)
    modbus.DO(300,0)
    modbus.DO(303,0)
    cup_ws[2] += 130
    go_to_point('XYZ','PTP',cup_ws,100,40)
    go_to_point('XYZ','PTP',cup_ws,100,40)
    cup_ws[2] -= 130

def put_cup_lid_at_ws():
    cup_lid_ws[2] += 130
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    cup_lid_ws[2] -= 130
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    modbus.DO(300,0)
    modbus.DO(303,0)
    cup_lid_ws[2] += 130
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    go_to_point('XYZ','PTP',cup_lid_ws,100,40)
    cup_lid_ws[2] -= 130

def suck_close_item():
    close_item_point[2] += 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    close_item_point[2] -= 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    modbus.DO(300,1)
    modbus.DO(303,1)
    close_item_point[2] += 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    close_item_point[2] -= 130

def put_close_item_at_ws():
    close_item_ws[2] += 60
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    close_item_ws[2] -= 40
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    close_item_ws[2] -= 20
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    modbus.DO(300,0)
    modbus.DO(303,0)

def push_close_item():
    go_to_point('XYZ','PTP',close_item_push,100,40)
    go_to_point('XYZ','PTP',close_item_push,100,40)
def put_close_item_back():
    modbus.DO(300,1)
    modbus.DO(303,1)
    close_item_ws[2] += 40
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    go_to_point('XYZ','PTP',close_item_ws,100,40)
    close_item_ws[2] -= 40
    close_item_point[2] += 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    close_item_point[2] -= 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    modbus.DO(300,0)
    modbus.DO(303,0)
    close_item_point[2] += 130
    go_to_point('XYZ','PTP',close_item_point,100,40)
    go_to_point('XYZ','PTP',close_item_point,100,40)
    close_item_point[2] -= 130
def check_finish():
    # check_finish_point[3]+=30
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    # check_finish_point[3]-=30
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    # check_finish_point[4]-=40
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    # go_to_point('XYZ','PTP',check_finish_point,100,40)
    go_to_point('XYZ','PTP',check_finish_point,100,10)
    go_to_point('XYZ','PTP',check_finish_point,100,10)

def suck_finish_cup():
    finish_cup_ws[2] += 110
    go_to_point('XYZ','PTP',finish_cup_ws,100,40)
    go_to_point('XYZ','PTP',finish_cup_ws,100,40)
    modbus.DO(300,1)
    modbus.DO(303,1)
    finish_cup_ws[2] -= 110
    go_to_point('XYZ','PTP',finish_cup_ws,100,40)
    go_to_point('XYZ','PTP',finish_cup_ws,100,40)
    finish_cup_ws[2] += 110
    go_to_point('XYZ','PTP',finish_cup_ws,100,20)
    go_to_point('XYZ','PTP',finish_cup_ws,100,20)
    finish_cup_ws[2] -= 110

def put_finish_cup():
    finish_space[2]+=140
    go_to_point('XYZ','PTP',finish_space,100,20)
    go_to_point('XYZ','PTP',finish_space,100,20)
    finish_space[2]-=140
    go_to_point('XYZ','PTP',finish_space,100,40)
    go_to_point('XYZ','PTP',finish_space,100,40)
    modbus.DO(300,0)
    modbus.DO(303,0)
    finish_space[2]+=140
    go_to_point('XYZ','PTP',finish_space,100,40)
    go_to_point('XYZ','PTP',finish_space,100,40)
    finish_space[2]-=140
    go_to_point('XYZ','PTP',home_point,100,40)
"""
主程式
    程式流程:
    1. 檢測影像
    2. 在原圖繪製結果
    3. 輸出影像
"""

if __name__ == "__main__":
    Arm_state = 0
    PTP_Angle = [0, 0, 0, 0, -90, 0]                 # ANGLE
    PTP_XYZ   = [0,450, 400, 180, 0, 90]    # XYZABC
    LIN_Angle = [0, 0, 0, 0, -90, 90]                # ANGLE
    LIN_XYZ   = [204.049, 368, 110, 180, 0, 90]      # XYZABC
    CIRC_centre = [0, 460.823, 293.5, 180, 0, 90]      # CIRC centre point
    CIRC_end  = [-204.049, 368, 293.5, 180, 0, 90]   # CIRC end point
    IO_Port = 301 # D0
    # video place-----------------------------------------------------------------------------
    home_point = [-0,368,293.5,180,0,90]
    cup_lid_point = [274.649,211.585,161.129,180,0,90]
    cup_left_point = [270.989,334.068,180.856,180,0,90]
    cup_ws = [-288.982,339.336,121.239,180,0,90]
    cup_lid_ws = [-288.482,340.336,237.549,180,0,90]
    close_item_point = [-25.458,339.836,31.055,180,0,90]
    close_item_ws = [-288.982,340.336,250.79,180,0,90]
    close_item_push = [-288.982,340.336,233.023,180,0,90]
    check_finish_point = [-250,330,355.796,180,10,90]
    finish_cup_ws = [-288.982,340.336,230.188,180,0,90]
    finish_space = [-126.262,485.202,130.738,180,0,90]
    arm_back = [-19.216,561.781,-46.846,-77.587,0,90]
    
    C_PTP_Angle = (c_double * len(PTP_Angle))(*PTP_Angle)       # C Array
    C_PTP_XYZ = (c_double * len(PTP_XYZ))(*PTP_XYZ)             # C Array
    C_CIRC_centre = (c_double * len(CIRC_centre))(*CIRC_centre) # C Array
    C_CIRC_end = (c_double * len(CIRC_end))(*CIRC_end)          # C Array
    
    modbus.DO.argtypes = [c_int, c_int]
    modbus.PTP.argtypes = [c_int, c_int, c_int, c_int, c_int]
    modbus.CIRC.argtypes = [c_int, c_int, c_int, c_int]

    # while 1:
    modbus.libModbus_Connect()
    modbus.Holding_Registers_init()

    # modbus.PTP(0, 10, 10, 1, 0, C_PTP_Angle)
    # modbus.CIRC(10, 10, 1, 0, C_CIRC_centre, C_CIRC_end)

    # modbus.DO(IO_Port,0) # 1 -> on ; 0 -> off
    # PTP_XYZ   = cup_left_point    # XYZABC
    # C_PTP_XYZ = (c_double * len(PTP_XYZ))(*PTP_XYZ)
    # modbus.PTP(1, 100, 10, 1, 0, C_PTP_XYZ)
    # while 1:
    #     modbus.PTP(1, 100, 10, 1, 0, C_PTP_XYZ)
    #     if(modbus.Arm_State_REGISTERS() == 1):
    #         print("status_in= ",modbus.Arm_State_REGISTERS())
    #         break
    # go_to_point('XYZ','PTP',home_point,100,40)
    go_to_point('XYZ','PTP',home_point,100,40)
    times=0
    while times<6:
        suck_left_cup()
        put_cup_at_ws()
        suck_cup_lid()
        put_cup_lid_at_ws()
        suck_close_item()
        put_close_item_at_ws()
        push_close_item()
        put_close_item_back()
        suck_finish_cup()
        check_finish()
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        color_image = np.asanyarray(color_frame.get_data())
        cv2.imwrite('/home/lintaiwen/cup.jpg',color_image)
        org = cv2.imread('/home/lintaiwen/cup.jpg')
        show_img(org,1000)

        put_finish_cup()
        go_to_point('XYZ','PTP',home_point,100,40)
        cup_left_point[2]-=9.109
        cup_lid_point[2]-=6.238
        times+=1
        if times<3:
            finish_space = [-126.262,485.202,130.738,180,0,90]
            finish_space[0]=130*times+finish_space[0]
        else:
            finish_space = [-126.262,485.202,130.738,180,0,90]
            finish_space[1]+=100
            finish_space[0]=130*(times-3)+finish_space[0]
    # modbus.DO(300,1)
    # modbus.DO(303,1)
     

    # go_to_point('XYZ','PTP',home_point,100,10)
    modbus.DO(300,0)
    modbus.DO(303,0)
modbus.Modbus_Close()
print("Modbus Close")  

    

