# -*- coding: utf-8 -*-
import math
import numpy as np
from matplotlib import pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
from math import cos ,sin, acos ,atan2 ,pi ,degrees

class kinematics():
    def __init__(self, link):
        self.link = link                        ## 各軸連桿長度的陣列
        self.joint = [0, 0, 0, 0, 0, 0]         ## 各軸旋轉角度的陣列
        self.end_position = []                  ## 末端點的位置 [x, y, z]
        self.end_orientation = []               ## 末端點的姿態 [Pitch, Roll, Yaw]
        self.dof = 6                            ## 手臂自由度
        self.all_pos = np.zeros((1,3))          ## 各軸位置資訊
        self.all_or_n = np.zeros((1,3))         ## 各軸X向量資訊
        self.all_or_o = np.zeros((1,3))         ## 各軸Y向量資訊
        self.all_or_a = np.zeros((1,3))         ## 各軸Z向量資訊
        self.wrist = [0, 0, 0]                  ## 手腕位置 [x, y, z]

    def demo(self, end_position, end_orientation):
        self.end_position = end_position        ## 儲存末端點位置
        self.end_orientation = end_orientation  ## 儲存末端點姿態
        self.inverse_kinamatics()               ## 逆運動學
        self.forward_kinematics()               ## 正運動學
        self.plot()                             ## 繪圖

    ### 計算逆運動學
    def inverse_kinamatics(self):
        ###  定義手臂末端點姿態矩陣(旋轉順序)
        deg_p = self.end_orientation[0]
        deg_y = self.end_orientation[2]
        deg_r = self.end_orientation[1]

        ###  定義 Roll, Pitch, Yaw旋轉軸並且放到相對應的 Rz, Ry, Rx
        ###  end_o為大地座標對手臂的旋轉矩陣
        Rz = np.matrix([  [cos(deg_r) , -sin(deg_r) , 0],
                [sin(deg_r)  , cos(deg_r)  , 0],
                [    0     ,    0      , 1]
            ])
        Rx = np.matrix([  [1 ,          0 ,           0],
                [0 , cos(deg_y) , -sin(deg_y)],
                [0 , sin(deg_y) ,  cos(deg_y)]
            ])
        Ry = np.matrix([  [cos(deg_p) , 0  , sin(deg_p)],
                [0 ,1           ,         0],
                [-sin(deg_p) , 0 , cos(deg_p)]
            ])
        end_o = np.matrix([[0,1,0],[0,0,1],[1,0,0]])
        R_YPR = end_o*Rx*Ry*Rz

        ###  計算手腕中心
        ###  分別計算手腕中心的位置並且放到 wrist陣列中
        self.wrist[0] = self.end_position[0] - self.link[3]*R_YPR[0,2]
        self.wrist[1] = self.end_position[1] - self.link[3]*R_YPR[1,2]
        self.wrist[2] = self.end_position[2] - self.link[3]*R_YPR[2,2]

        ###  逆位置運動學
        ###  使用逆位置運動學求出第一、二、三軸的角度
        if(abs(self.wrist[0]) <0.0001 and abs(self.wrist[1])<0.0001):
            self.joint[0]=0
        else:
            self.joint[0]=degrees(atan2(-self.wrist[0],self.wrist[1]))
        cos_d = (self.wrist[0]**2 + self.wrist[1]**2 + \
                (self.wrist[2]-self.link[0])**2 -(self.link[1]**2+self.link[2]**2))/\
                (2*self.link[1]*self.link[2])
        self.joint[2] = degrees(atan2( -1*math.sqrt(1-cos_d**2),cos_d))
        self.joint[1] = degrees(atan2((self.wrist[2]-self.link[0]) ,
                        math.sqrt(self.wrist[0]**2+self.wrist[1]**2))) - \
                        degrees(atan2(self.link[2]*sin(math.radians(self.joint[2])) ,
                        (self.link[1]+self.link[2]*cos(math.radians(self.joint[2])))))

        ###  逆姿態運動學
        dh=self.dh_list()

        s_1=sin(math.radians(self.joint[0])+dh[0,3])
        c_1=cos(math.radians(self.joint[0])+dh[0,3])
        s_23=sin(math.radians(self.joint[1])+math.radians(self.joint[2])+dh[1,3]+dh[2,3])
        c_23=cos(math.radians(self.joint[1])+math.radians(self.joint[2])+dh[1,3]+dh[2,3])
        ###  求出 R0_3(第一到三軸的旋轉矩陣)，並且透過 R0_3與 R_YPR求出 R3_6
        R0_3 = np.array([[c_1*c_23 ,  s_1 , c_1*s_23],
                         [s_1*c_23 , -c_1 , s_1*s_23],
                         [s_23     ,  0   , -c_23   ]] )
        R3_6 = np.dot(R0_3.T, R_YPR)
        ###  使用 R3_6分別計算出四、五、六軸的角度
        if( abs( R3_6[2,2])>0.99999):
            self.joint[3] = 0
            self.joint[4] = degrees(atan2(-math.sqrt(1-R3_6[2,2]**2),-R3_6[2,2]))
            self.joint[5] = degrees(atan2( R3_6[2,1], R3_6[2,0]))
        else:
            self.joint[3] = degrees(atan2( -R3_6[1,2], R3_6[0,2]))
            self.joint[4] = degrees(atan2( -math.sqrt(1-R3_6[2,2]**2),-R3_6[2,2]))
            self.joint[5] = degrees(atan2( -R3_6[2,1], R3_6[2,0]))

    ###  DH連桿表
    def dh_list(self):
        pi=math.pi
        ###  製作 dh連桿表陣列，每一列為各軸，每一行分別為 a, α, d, θ
        ###  並且將製作好的 dh連桿表回傳回去
        ######                    a          α            d            θ     #####
        dh = np.array([ [         0    ,    pi/2   ,   self.link[0]   ,    pi/2 ],
                        [     self.link[1]  ,     0     ,      0      ,     0   ],
                        [         0    ,   -pi/2   ,      0      ,   -pi/2 ],
                        [         0    ,    pi/2   ,   self.link[2]   ,     0   ],
                        [         0    ,   -pi/2   ,      0      ,     0   ],
                        [         0    ,     0     ,   self.link[3]   ,     0   ]

        ])
        return dh

    ### 計算正運動學
    def forward_kinematics(self):
        T=np.identity(4)
        dh=self.dh_list()
        for i in range(0, self.dof):
            ###  輸入各軸的角度以及 dh連桿表的資訊到齊次轉換矩陣中來獲得各軸 A矩陣(齊次轉換矩陣)
            A=self.GenerateTransformationMatrices(math.radians(self.joint[i]),dh[i])
            ###  計算各軸旋轉矩陣 T
            T=np.dot(T,A)
            ###  從T矩陣中儲存各軸的位置(pos), x向量(n), y向量(o), z向量(a)
            self.all_pos = np.vstack((self.all_pos, T[0:3,3]))
            self.all_or_n = np.vstack((self.all_or_n, T[0:3,0]))
            self.all_or_o = np.vstack((self.all_or_o, T[0:3,1]))
            self.all_or_a = np.vstack((self.all_or_a, T[0:3,2]))
            print(T)

    ### 計算齊次轉換矩陣
    def GenerateTransformationMatrices(self, Theta, dh):
        ###  將旋轉的角度和連桿資訊放到齊次轉換矩陣中來獲得 A矩陣，並且回傳A矩陣
        c_theta = cos(Theta +dh[3])
        s_theta = sin(Theta +dh[3])
        c_alpha = cos(dh[1])
        s_alpha = sin(dh[1])
        A = np.array( [ [c_theta , -s_theta*c_alpha  ,  s_theta*s_alpha , dh[0]*c_theta],
                        [s_theta ,  c_theta*c_alpha  , -c_theta*s_alpha , dh[0]*s_theta],
                        [    0   ,    s_alpha        ,c_alpha           ,  dh[2]       ],
                        [    0   ,          0        ,         0        ,        1     ]
                        ])
        return A

    ### 畫圖
    def plot(self):
        ax = plt.subplot(111, projection='3d')
        self.all_pos=np.around(self.all_pos,decimals=3)
        self.all_or_n=np.around(self.all_or_n,decimals=3)
        self.all_or_o=np.around(self.all_or_o,decimals=3)
        self.all_or_a=np.around(self.all_or_a,decimals=3)
        print(self.all_pos)
        ###  畫出各關節的位置
        ax.scatter(self.all_pos[:,0], self.all_pos[:,1],self.all_pos[:,2], c='r')
        ###  將各關節的位置進行連線
        ax.plot(self.all_pos[:,0],self.all_pos[:,1],self.all_pos[:,2],c='y')

        ###  畫出各關節的姿態
        for i in range(0, self.dof+1):
            ###  畫出 x向量(n)
            flag_n=self.all_pos[i, :]
            flag_n=np.vstack((flag_n,self.all_pos[i, :]+self.all_or_n[i, :]*20))
            ax.plot(flag_n[:,0],flag_n[:,1],flag_n[:,2],c='r')
            ###  畫出 y向量(o)
            flag_a=self.all_pos[i, :]
            flag_a=np.vstack((flag_a, self.all_pos[i, :]+self.all_or_a[i, :]*20))
            ax.plot(flag_a[:,0], flag_a[:,1], flag_a[:,2],c='b')
            ###  畫出 z向量(a)
            flag_o=self.all_pos[i, :]
            flag_o=np.vstack((flag_o,self.all_pos[i, :]+self.all_or_o[i, :]*20))
            ax.plot(flag_o[:,0],flag_o[:,1],flag_o[:,2],c='g')

        ax.set_xlim(-150, 150)
        ax.set_ylim(-150, 150)
        ax.set_zlim(  0 , 150)
        ax.set_zlabel('Z')
        ax.set_ylabel('Y')
        ax.set_xlabel('X')
        plt.show()

    ###  測試正運動學
    def demo_forward(self,joint):
        self.joint = joint
        self.forward_kinematics()
        self.plot()

if __name__ == "__main__":
    ###  手臂連桿的長度
    link = [10, 60, 50, 20]
    six_dof_link = kinematics(link)

    ###  手臂各關節角度
    joint = [0, 0, 0, 0, 0, 0]
    # six_dof_link.demo_forward(joint)

    ###  手臂末端點位置
    x = 60
    y = 60
    z = 10
    end_position = [x, y, z]
    ###  手臂末端點姿態
    pitch = math.radians(0)
    roll  = math.radians(0)
    yaw   = math.radians(0)
    end_orientation = [pitch, roll, yaw]

    six_dof_link.demo(end_position, end_orientation)
    
