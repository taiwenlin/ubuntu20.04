from get import get_average
class Cars:
    def __init__(self,color,seat):
        self.color=color
        self.seat=seat

    def drive(self):
        print(f"My car is {self.color} and {self.seat} seats.")
if __name__=="__main__":
    mazda=Cars("blue",11)
    mazda.drive()