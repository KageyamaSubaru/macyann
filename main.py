import random
import math

def be_bln(nto,dt):
    otr=[]
    for i in range(len(dt)):
        if nto == 1:
            otr.append([dt[i]])
        else:
            lsr=be_bln(nto-1,dt[i+1:])
            for j in lsr:
                otr.append(j+[dt[i]])
    return otr

def cvt_tehai(dt,st=0):
    oost=dt.copy()
    if st==0:
        oost.sort()
    while 0 in oost:
        oost.remove(0)
    def convs(pxb):
        if pxb == 0:
            return " "
        elif pxb<10:
            return str(pxb)+"m"
        elif pxb<19:
            return str(pxb-9)+"s"
        elif pxb<28:
            return str(pxb-18)+"p"
        elif pxb<35:
            return "东南西北中发白"[pxb-28]
        else:
            return ["a5m","a5s","a5p"][pxb-35]
    otr=[]
    for i in oost:
        otr.append(convs(i))
    return otr
#####
#是否胡牌
#####
def judge_frn(dt,hls):
    def judge_roon(dt):            
        th=[]
        for i in dt:
            if i==35:
                th.append(5)
            elif i==36:
                th.append(14)
            elif i==37:
                th.append(23)
            else:
                th.append(i)
        th.sort()
            
        if len(th)==3:
            if (judge_type(th[0])==judge_type(th[1])) and (judge_type(th[1])==judge_type(th[2])) and ((th[2]-th[1])== 1) and ((th[1]-th[0])==1):
                return 1
            if (th[0]==th[1]) and (th[1]==th[2]) :
                return 1
            return 0
        if (len(th)% 3 >0):
            #print(th)
            for i in th:
                if th.count(i)>1:
                    tct=th.copy()
                    tct.remove(i)
                    tct.remove(i)
                    #print([i,i])
                    if judge_roon(tct)==1:
                        return 1
            return 0
        else:
            aujk=be_bln(3,th)
            for i in aujk:
                if judge_roon(i):
                    nokori=th.copy()
                    for j in i:
                        nokori.remove(j)
                    if judge_roon(nokori)==1:
                        return 1
            return 0
                
    
    hl=hls.copy()
    dt=dt.copy()
    th=[]
    for i in dt:
        if i==35:
            th.append(5)
        elif i==36:
            th.append(14)
        elif i==37:
            th.append(23)
        else:
            th.append(i)
    th.sort()
    while 0 in hl:
        hl.remove(0)
    for i in hl:
        dt.remove(i)
    futsu=judge_roon(dt)
    if futsu==1:
        return 1
    gokushi=1
    for i in [1,9,10,18,19,27,28,29,30,31,32,33,34]:
        if not(i in dt):
            gokushi=0
            break
    if gokushi==1:
        return 2
    qidui=0
    if len(set(th))==7:
        for i in th:
            if th.count(i)!=2:
                break
        qidui=3
    return qidui

########
#算分
########
def judge_ronn(dt,pn,bonn,cc,frm,xummu,doras,hls):
    #牌 进 场次 状态 frm dora
    yaku=0
    yakumann=0
    ttth=dt+[pn]
    #立直
    if cc[1]!=0:
        yaku=yaku+1
        #一发
        if (xummu-cc[1])<5:
            yaku=yaku+1
    #自摸
    if cc[2]==0 and frm==0:
        yaku=yaku+1
    #中发白
    if ttth.count(34)>2:
        yaku=yaku+1
    if ttth.count(33)>2:
        yaku=yaku+1
    if ttth.count(32)>2:
        yaku=yaku+1
        
def judge_type(dt):
    if ((dt<10) and (dt>0)) or dt==35:
        return "0"
    elif ((dt<19) and (dt>9)) or dt==36:
        return "1"
    elif ((dt<28) and (dt>18)) or dt==37:
        return "2"
    elif dt<35 and dt>0:
        return "3"
    else:
        return None
    
class ma_cyan(object):
    def __init__(self):
        self.endflg=1 #结束
        self.chcuuju=[0,0,0] #场次 bonnba richibonn
        self.sc=[250,250,250,250]
        self.yama=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,35,6,7,8,9,10,11,12,13,14,15,16,17,18,10,11,12,13,14,15,16,17,18,10,11,12,13,14,15,16,17,18,10,11,12,13,36,15,16,17,18,19,20,21,22,23,24,25,26,27,19,20,21,22,23,24,25,26,27,19,20,21,22,23,24,25,26,27,19,20,21,22,37,24,25,26,27,28,29,30,31,32,33,34,28,29,30,31,32,33,34,28,29,30,31,32,33,34,28,29,30,31,32,33,34]
        self.a_te=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.a_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.a_flg=[0,0,0] #位置 richi naku
        self.a_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.b_te=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.b_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.b_flg=[0,0,0] #位置 richi naku
        self.b_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.c_te=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.c_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.c_flg=[0,0,0] #位置 richi naku
        self.c_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.d_te=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.d_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.d_flg=[0,0,0] #位置 richi naku
        self.d_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.dora=[0,0,0,0,0]
        self.xunmu_sg=1
    def start_game(self):
        self.endflg=0 #结束
        self.chcuuju=[0,0,0] #场次 bonnba richibonn
        self.sc=[250,250,250,250]
        self.yama=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,1,2,3,4,35,6,7,8,9,10,11,12,13,14,15,16,17,18,10,11,12,13,14,15,16,17,18,10,11,12,13,14,15,16,17,18,10,11,12,13,36,15,16,17,18,19,20,21,22,23,24,25,26,27,19,20,21,22,23,24,25,26,27,19,20,21,22,23,24,25,26,27,19,20,21,22,37,24,25,26,27,28,29,30,31,32,33,34,28,29,30,31,32,33,34,28,29,30,31,32,33,34,28,29,30,31,32,33,34]
        random.shuffle(self.yama)
        self.a_te=self.yama[:13]+[0]
        self.yama=self.yama[13:]
        self.a_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.a_flg=[0,0,0] #位置 richi naku
        self.a_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.b_te=self.yama[:13]+[0]
        self.yama=self.yama[13:]
        self.b_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.b_flg=[1,0,0] #位置 richi naku
        self.b_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.c_te=self.yama[:13]+[0]
        self.yama=self.yama[13:]
        self.c_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.c_flg=[2,0,0] #位置 richi naku
        self.c_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.d_te=self.yama[:13]+[0]
        self.yama=self.yama[13:]
        self.d_kw=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.d_flg=[3,0,0] #位置 richi naku
        self.d_fls=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        self.dora=[self.yama[-1],0,0,0,0]
        self.xunmu_sg=1
    #返回场况
    def return_bb(self,nm=0):
        if nm==0:
            return self.a_te,self.b_te,self.c_te,self.d_te,self.dora,self.chcuuju,self.yama
        if nm==1:
            return self.a_te+self.a_kw+self.b_kw+self.c_kw+self.d_kw+self.a_flg+self.b_flg+self.c_flg+self.d_flg+self.a_fls+self.b_fls+self.c_fls+self.d_fls+self.dora+self.sc+self.chcuuju+[len(self.yama)]
        if nm==2:
            return self.b_te+self.b_kw+self.c_kw+self.d_kw+self.a_kw+self.b_flg+self.c_flg+self.d_flg+self.a_flg+self.b_fls+self.c_fls+self.d_fls+self.a_fls+self.dora+self.sc+self.chcuuju+[len(self.yama)]
        if nm==3:
            return self.c_te+self.c_kw+self.d_kw+self.a_kw+self.b_kw+self.c_flg+self.d_flg+self.a_flg+self.b_flg+self.c_fls+self.d_fls+self.a_fls+self.b_fls+self.dora+self.sc+self.chcuuju+[len(self.yama)]
        if nm==4:
            return self.d_te+self.d_kw+self.a_kw+self.b_kw+self.c_kw+self.d_flg+self.a_flg+self.b_flg+self.c_flg+self.d_fls+self.a_fls+self.b_fls+self.c_fls+self.dora+self.sc+self.chcuuju+[len(self.yama)]
    #判断
    def judge(self,pn,zj,dtp):
        if zj==1:
            zj_tehai=self.a_te.copy()
            zj_bz=self.a_flg.copy()
            zj_kw=self.a_kw.copy()
        elif zj==2:
            zj_tehai=self.b_te.copy()
            zj_bz=self.b_flg.copy()
            zj_kw=self.b_kw.copy()
        elif zj==3:
            zj_tehai=self.c_te.copy()
            zj_bz=self.c_flg.copy()
            zj_kw=self.c_kw.copy()
        elif zj==4:
            zj_tehai=self.d_te.copy()
            zj_bz=self.d_flg.copy()
            zj_kw=self.d_kw.copy()
        #0ponn 1kann 2chi 3lichi 4zimo 5ronn 6 7
        if dtp==0:
            if (zj_tehai.count(pn)>1):
                return 1
        elif dtp==1:
            zj_tehai.append(pn)
            for i in zj_tehai:
                if zj_tehai.count(i)==4:
                    return 1
            return 0
        elif dtp==2:
            if pn==35:
                pn=5
            elif pn==36:
                pn=14
            elif pn==37:
                pn=23
            if pn <28:
                tp=0
                if ((pn-2) in zj_tehai) and ((pn-1) in zj_tehai):
                    if (judge_type(pn-2)==judge_type(pn-1)) and (judge_type(pn)==judge_type(pn-1)):
                        tp=tp+1
                if ((pn-1) in zj_tehai) and ((pn+1) in zj_tehai):
                    if (judge_type(pn-1)==judge_type(pn+1)) and (judge_type(pn)==judge_type(pn-1)):
                        tp=tp+2
                if ((pn+1) in zj_tehai) and ((pn+2) in zj_tehai):
                    if (judge_type(pn+1)==judge_type(pn+2)) and (judge_type(pn)==judge_type(pn+1)):
                        tp=tp+4
                return tp
        elif ((dtp==3) and (zj_bz[1] !=1) and (zj_bz[2] !=1)):
            zj_tehai=zj_tehai.remove(0)+[pn]
            for tts in range(len(zj_tehai)):
                curtr=zj_tehai.copy()
                curtr.pop(tts)
                for ptr in range(38):
                    if judge_frn(curtr+[ptr],[])>0:
                        return 1
        elif(dtp==4):#自摸无?
            zj_tehai=zj_tehai.remove(0)+[pn]
            if judge_frn(zj_tehai,[])>0:################有役判断
                return 1
        elif(dtp==5):#wuyi
            toronn=[]
            zj_tehai=zj_tehai.remove(0)
            if judge_frn(zj_tehai+[pn])>0:###########有役判断
                for ptr in range(38):
                    if judge_frn(zj_tehai+[ptr],[])>0:
                        toronn.append(ptr)
                if not(pn in toronn):
                    return 1
        return 0
        
    def do(self, nm,acttp,hai):
        #0开局
        if (acttp==0):
            self.start_game()
            can_kang=judge(self,self.yama[0],self.a_te,1)
            can_richi=judge(self,self.yama[0],self.a_te,3)
            can_zimo=judge(self,self.yama[0],self.a_te,4)
            self.a_te.remove(0)
            self.a_te.append(self.yama[0])
            self.yama=self.yama[1:]
            #场况 吃吃吃 碰杠立直自摸胡 谁打的 0=系统
            ntdt=self.return_bb(1)+[0,0,0]+[0,can_kang,can_richi,can_zimo,0]+[0]
            return 1,ntdt,0,0
        elif (acttp==1):
            if nm==1:
                hai=self.a_te.pop(hai)
                self.a_te.append(0)
                can_chi_b=judge(self,hai,self.b_te,2)
                chi_b=[(can_chi_b %2),int(((can_chi_b % 4)/2)),int(can_chi_b/4)]
                can_ponn_b=judge(self,hai,self.b_te,0)
                can_kang_b=judge(self,hai,self.b_te,1)
                can_ronn_b=judge(self,hai,self.b_te,5)
                can_ponn_c=judge(self,hai,self.c_te,0)
                can_kang_c=judge(self,hai,self.c_te,1)
                can_ronn_c=judge(self,hai,self.c_te,5)
                can_ponn_d=judge(self,hai,self.d_te,0)
                can_kang_d=judge(self,hai,self.d_te,1)
                can_ronn_d=judge(self,hai,self.d_te,5)
                if can_ponn_b>0:
                    ntdt=self.return_bb(2)+chi_b+[can_ponn_b,can_kang_b,0,0,can_ronn_b],[nm]
                    return 2,chi_b+[can_ponn_b,can_kang_b,0,0,can_ronn_b],ntdt,0,0
                if can_ponn_c>0:
                    ntdt=self.return_bb(3)+[0,0,0]+[can_ponn_c,can_kang_c,0,0,can_ronn_c],[nm]
                    return 3,[0,0,0]+[can_ponn_c,can_kang_c,0,0,can_ronn_c],ntdt,0,0
                if can_ponn_d>0:
                    ntdt=self.return_bb(4)+[0,0,0]+[can_ponn_d,can_kang_d,0,0,can_ronn_d],[nm]
                    return 4,[0,0,0]+[can_ponn_d,can_kang_d,0,0,can_ronn_d],ntdt,0,0
                if can_chi_b>0:
                    ntdt=self.return_bb(2)+chi_b+[can_ponn_b,can_kang_b,0,0,can_ronn_b],[nm]
                    return 2,chi_b+[can_ponn_b,can_kang_b,0,0,can_ronn_b],ntdt,0,0                    
            elif nm==2:
                hai=self.b_te.pop(hai)
                self.b_te.append(0)
                can_chi_c=judge(self,hai,self.c_te,2)
                chi_c=[(can_chi_c %2),int(((can_chi_c % 4)/2)),int(can_chi_c/4)]
                can_ponn_c=judge(self,hai,self.c_te,0)
                can_kang_c=judge(self,hai,self.c_te,1)
                can_ronn_c=judge(self,hai,self.c_te,5)
                can_ponn_a=judge(self,hai,self.a_te,0)
                can_kang_a=judge(self,hai,self.a_te,1)
                can_ronn_a=judge(self,hai,self.a_te,5)
                can_ponn_d=judge(self,hai,self.d_te,0)
                can_kang_d=judge(self,hai,self.d_te,1)
                can_ronn_d=judge(self,hai,self.d_te,5)
                if can_ponn_c>0:
                    ntdt=self.return_bb(3)+chi_c+[can_ponn_c,can_kang_c,0,0,can_ronn_c],[nm]
                    return 3,chi_c+[can_ponn_c,can_kang_c,0,0,can_ronn_c],ntdt,0,0
                if can_ponn_a>0:
                    ntdt=self.return_bb(1)+[0,0,0]+[can_ponn_a,can_kang_a,0,0,can_ronn_a],[nm]
                    return 1,[0,0,0]+[can_ponn_a,can_kang_a,0,0,can_ronn_a],ntdt,0,0
                if can_ponn_d>0:
                    ntdt=self.return_bb(4)+[0,0,0]+[can_ponn_d,can_kang_d,0,0,can_ronn_d],[nm]
                    return 4,[0,0,0]+[can_ponn_d,can_kang_d,0,0,can_ronn_d],ntdt,0,0
                if can_chi_c>0:
                    ntdt=self.return_bb(3)+chi_c+[can_ponn_c,can_kang_c,0,0,can_ronn_c],[nm]
                    return 3,chi_c+[can_ponn_c,can_kang_c,0,0,can_ronn_c],ntdt,0,0
            elif nm==3:
                hai=self.c_te.pop(hai)
                self.c_te.append(0)
                can_chi_d=judge(self,hai,self.d_te,2)
                chi_d=[(can_chi_d %2),int(((can_chi_d % 4)/2)),int(can_chi_d/4)]
                can_ponn_d=judge(self,hai,self.d_te,0)
                can_kang_d=judge(self,hai,self.d_te,1)
                can_ronn_d=judge(self,hai,self.d_te,5)
                can_ponn_b=judge(self,hai,self.b_te,0)
                can_kang_b=judge(self,hai,self.b_te,1)
                can_ronn_b=judge(self,hai,self.b_te,5)
                can_ponn_a=judge(self,hai,self.a_te,0)
                can_kang_a=judge(self,hai,self.a_te,1)
                can_ronn_a=judge(self,hai,self.a_te,5)
                if can_ponn_d>0:
                    ntdt=self.return_bb(4)+chi_d+[can_ponn_d,can_kang_d,0,0,can_ronn_d],[nm]
                    return 4,chi_d+[can_ponn_d,can_kang_d,0,0,can_ronn_d],ntdt,0,0
                if can_ponn_b>0:
                    ntdt=self.return_bb(2)+[0,0,0]+[can_ponn_b,can_kang_b,0,0,can_ronn_b],[nm]
                    return 2,[0,0,0]+[can_ponn_b,can_kang_b,0,0,can_ronn_b],ntdt,0,0
                if can_ponn_a>0:
                    ntdt=self.return_bb(1)+[0,0,0]+[can_ponn_a,can_kang_a,0,0,can_ronn_a],[nm]
                    return 1,[0,0,0]+[can_ponn_a,can_kang_a,0,0,can_ronn_a],ntdt,0,0
                if can_chi_d>0:
                    ntdt=self.return_bb(4)+chi_d+[can_ponn_d,can_kang_d,0,0,can_ronn_d],[nm]
                    return 4,chi_d+[can_ponn_d,can_kang_d,0,0,can_ronn_d],ntdt,0,0
            elif nm==4:
                hai=self.d_te.pop(hai)
                self.d_te.append(0)
                can_chi_a=judge(self,hai,self.a_te,2)
                chi_a=[(can_chi_a %2),int(((can_chi_a % 4)/2)),int(can_chi_a/4)]
                can_ponn_a=judge(self,hai,self.a_te,0)
                can_kang_a=judge(self,hai,self.a_te,1)
                can_ronn_a=judge(self,hai,self.a_te,5)
                can_ponn_c=judge(self,hai,self.c_te,0)
                can_kang_c=judge(self,hai,self.c_te,1)
                can_ronn_c=judge(self,hai,self.c_te,5)
                can_ponn_b=judge(self,hai,self.b_te,0)
                can_kang_b=judge(self,hai,self.b_te,1)
                can_ronn_b=judge(self,hai,self.b_te,5)
                if can_ponn_a>0:
                    ntdt=self.return_bb(1)+chi_a+[can_ponn_a,can_kang_a,0,0,can_ronn_a],[nm]
                    return 1,chi_a+[can_ponn_a,can_kang_a,0,0,can_ronn_a],ntdt,0,0
                if can_ponn_c>0:
                    ntdt=self.return_bb(3)+[0,0,0]+[can_ponn_c,can_kang_c,0,0,can_ronn_c],[nm]
                    return 3,[0,0,0]+[can_ponn_c,can_kang_c,0,0,can_ronn_c],ntdt,0,0
                if can_ponn_b>0:
                    ntdt=self.return_bb(2)+[0,0,0]+[can_ponn_b,can_kang_b,0,0,can_ronn_b],[nm]
                    return 2,[0,0,0]+[can_ponn_b,can_kang_b,0,0,can_ronn_b],ntdt,0,0
                if can_chi_a>0:
                    ntdt=self.return_bb(1)+chi_a+[can_ponn_a,can_kang_a,0,0,can_ronn_a],[nm]
                    return 1,chi_a+[can_ponn_a,can_kang_a,0,0,can_ronn_a],ntdt,0,0
            else:
                return 0,None,None,None,None

            ntdt=self.return_bb(1)
            return 1,0,ntdt,0,0
#########场况 吃吃吃 碰杠立直自摸胡 谁打的 0=系统
########ntdt=self.return_bb(1)+[0,0,0]+[0,can_kang,can_richi,can_zimo,0]+[0]
        return nxt_nm,okflg,ntdt,edflg,reward
    
gm=ma_cyan()
gm.start_game()
th=gm.return_bb()
