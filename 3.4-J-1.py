# 分析一个水杯的属性和功能，使用类描述并创建对象
# 高度，容积，颜色，材质
# 能存放液体
class cup:
    cupname=0
    def gaodu(self,cm):
        print(self.cupname,"高度有",cm)
    def yanse(self,color):
        print(self.cupname,"的颜色是",color)
    def rongji(self,daxiao):
        print(self.cupname,"容量有",daxiao)
    def caizhi(self,zhiz):
        print(self.cupname,"的材质是",zhiz)

p=cup()
p.cupname="这个杯子"
p.gaodu("20cm")
p.yanse("红色")
p.rongji("750ml")
p.caizhi("塑料")



# 有笔记本电脑（屏幕大小，价格，cpu型号，内存大小，待机时长），行为（打字，打游戏，看视频）
class airbook:
    airbookname=""
    Screen=0
    Price=0
    CpuSize=0
    Memorysize=0
    Standbytime=0
    def Screen(self,cun):
        print(self.airbookname,"的屏幕尺寸有",cun)
    def Price(self,yuan):
        print(self.airbookname,"的价格是",yuan)
    def CpuSize(self,a):
        print(self.airbookname,"的cpu型号是",a)
    def Memorysize(self,g):
        print(self.airbookname,"的内存大小是",g)
    def Standbytime(self,h):
        print(self.airbookname,"的最长待机时长",h)

p=airbook()
p.airbookname="这个电脑"
p.Screen("20")
p.Price("7000")
p.CpuSize("i7")
p.Memorysize("256g")
p.Standbytime("50小时")






