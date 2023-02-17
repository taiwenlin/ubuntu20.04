#! /usr/bin/python3
import numpy as np
from math import cos ,sin, acos ,atan2 ,pi ,degrees
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#設定繪圖視窗大小
fig = plt.figure()

ax = Axes3D(fig)
#角度,弳度轉換公式
r2d = 1/180*pi

JointAngle = [0,0,0]    #各軸角度(全0為零度姿態)
Od = [0,0,0]            #末端點(x,y,z)

pos = [ [None] * 3 for i in range(4) ]  #用於存放計算好的點位 
ax = plt.subplot(111, projection='3d')  #創建一個三维的繪圖

# 正運動學(齊次轉換矩陣)
def Tran_List(JointAngle,stop):
    #DH連桿表
    #                a  alpha    d        theta
    DH = np.array([[  0 ,  90    ,  10  ,   JointAngle[0]           +   0 ],
                   [  17 ,  0    ,  0  ,    JointAngle[1]          +   0 ],
                   [  11 ,  0    ,  0  ,    JointAngle[2]          +   0 ]])


    Tranoriginal=np.eye(4) #4x4單位矩陣（https://blog.csdn.net/m0_37393514/article/details/814559）
    for i in range(0,stop):#round(https://www.runoob.com/python/func-number-round.html)
        tran=np.array([[ round(cos(DH[i][3]*r2d) ,3) , round(-sin(DH[i][3]*r2d)*cos(DH[i][1]*r2d) ,3) , round(sin(DH[i][3]*r2d)*sin(DH[i][1]*r2d) ,3) , round(DH[i][0]*cos(DH[i][3]*r2d) ,3) ],
                       [ round(sin(DH[i][3]*r2d) ,3) , round(cos(DH[i][3]*r2d)*cos(DH[i][1]*r2d) ,3) , round(-cos(DH[i][3]*r2d)*sin(DH[i][1]*r2d) ,3) , round(DH[i][0]*sin(DH[i][3]*r2d) ,3) ],
                       [ round(0 ,3) , round(sin(DH[i][1]*r2d) ,3) , round(cos(DH[i][1]*r2d) ,3) , round(DH[i][2] ,3) ],
                       [ round(0 ,3) , round(0 ,3) , round(0 ,3) , round(1 ,3) ]])
        
        Tranoriginal=np.dot(Tranoriginal,tran)#dot函數包含：多維矩陣乘法、矩陣與向量乘法、向量內積（https://zhuanlan.zhihu.com/p/353753915）
        Tran=Tranoriginal

    return(Tran)

# 正運動學 函式	
def direct_Kinematics(JointAngle):
    Tran1 = Tran_List(JointAngle,1)
    Tran2 = Tran_List(JointAngle,2)
    Tran3 = Tran_List(JointAngle,3)
    
    pos =np.array([ [0,0,0],
                    [Tran1[0][3],Tran1[1][3],Tran1[2][3]],
                    [Tran2[0][3],Tran2[1][3],Tran2[2][3]],
                    [Tran3[0][3],Tran3[1][3],Tran3[2][3]]])

    return pos

# 逆運動學 函式
def inver_Kinematics(JointAngle,Od):

    Link = np.array([ 10 , 17 , 11 ])

    JointAngle[0] = atan2(Od[1],Od[0])
    D = ((Od[0])**2+(Od[1])**2+(Od[2]-Link[0])**2)**0.5
    JointAngle[2] = atan2((1-(((Link[1])**2+(Link[2])**2-D**2)/(2*Link[1]*Link[2]))**2)**0.5,((Link[1])**2+(Link[2])**2-D**2)/(2*Link[1]*Link[2]))
    JointAngle[1] = atan2(Od[2]-Link[0],((Od[0])**2+(Od[1])**2)**0.5)-atan2(Link[2]*sin(JointAngle[2]*r2d),Link[1]+Link[2]*cos(JointAngle[2]*r2d))

    JointAngle = [angle*180/pi for angle in JointAngle]

    return JointAngle

def kinematics(pos,Od,JointAngle):
    # 逆運動學
    JointAngle = inver_Kinematics(JointAngle,Od)

    # 正運動學
    pos = direct_Kinematics(JointAngle)

    return pos

def plt_3D_robot(X,Y,Z):

    ax.plot(X,Y,Z,"go-",label='3-axis robot arm') #label是指定義圖例
    
    ax.set_xlabel('X')     # 座標軸
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')  
    ax.set_xlim3d(-40, 40)
    ax.set_ylim3d(-40, 40)
    ax.set_zlim3d(0, 40)
    plt.title('robot_arm') # 設置標題
    plt.legend() # 顯示上面定義的圖例

    plt.show()


	
# 選擇輸入求各軸角度或末端點位
while(1):
    a_input = int(input('"逆運動學"求各軸角度(輸入1)  "開始動作"(輸入2): '))

    if a_input == 1:	#主要透過"逆運動學"算出手臂各軸角度,在透過"正運動學"算出手臂末端點
        print('請輸入末端點位置： x y z')
        Od = np.array([float(num) for num in input().split()])
        print(f"輸入的末端點為:\n {Od}\n")

        pos = kinematics(pos,Od,JointAngle)# 經正逆運動學 求角度 與末端點



        x = pos[:,0]  #接收回傳陣列的第1行
        y = pos[:,1]  #接收回傳陣列的第2行
        z = pos[:,2]  #接收回傳陣列的第3行

        print(f"各軸角度為: \n{JointAngle}\n") #顯示各軸角度


    elif a_input == 2:

        plt_3D_robot(x,y,z)

        print('See you next time')

