import tkinter as tk
window=tk.Tk()
points_table={}
t1_1=tk.Label(window)
t1_2=tk.Label(window)
t1_3=tk.Label(window)
t1_4=tk.Label(window)
t1_5=tk.Label(window)
t2_1=tk.Label(window)
t2_2=tk.Label(window)
t2_3=tk.Label(window)
t2_4=tk.Label(window)
t2_5=tk.Label(window)
t3_1=tk.Label(window)
t3_2=tk.Label(window)
t3_3=tk.Label(window)
t3_4=tk.Label(window)
t3_5=tk.Label(window)
t4_1=tk.Label(window)
t4_2=tk.Label(window)
t4_3=tk.Label(window)
t4_4=tk.Label(window)
t4_5=tk.Label(window)
t5_1=tk.Label(window)
t5_2=tk.Label(window)
t5_3=tk.Label(window)
t5_4=tk.Label(window)
t5_5=tk.Label(window)
t6_1=tk.Label(window)
t6_2=tk.Label(window)
t6_3=tk.Label(window)
t6_4=tk.Label(window)
t6_5=tk.Label(window)
t7_1=tk.Label(window)
t7_2=tk.Label(window)
t7_3=tk.Label(window)
t7_4=tk.Label(window)
t7_5=tk.Label(window)
t8_1=tk.Label(window)
t8_2=tk.Label(window)
t8_3=tk.Label(window)
t8_4=tk.Label(window)
t8_5=tk.Label(window)
t9_1=tk.Label(window)
t9_2=tk.Label(window)
t9_3=tk.Label(window)
t9_4=tk.Label(window)
t9_5=tk.Label(window)
t10_1=tk.Label(window)
t10_2=tk.Label(window)
t10_3=tk.Label(window)
t10_4=tk.Label(window)
t10_5=tk.Label(window)
labels=[t1_1,t1_2,t1_3,t1_4,t1_5,t2_1,t2_2,t2_3,t2_4,t2_5,t3_1,t3_2,t3_3,t3_4,t3_5,t4_1,t4_2,t4_3,t4_4,t4_5,t5_1,t5_2,t5_3,t5_4,t5_5,t6_1,t6_2,t6_3,t6_4,t6_5,t7_1,t7_2,t7_3,t7_4,t7_5,t8_1,t8_2,t8_3,t8_4,t8_5,t9_1,t9_2,t9_3,t9_4,t9_5,t10_1,t10_2,t10_3,t10_4,t10_5]
for i in range(90):
    points_table[i]=" "
Pak,Ind,Eng,Aus,Sa,Sl,Ned,Nz,Afg,Ban=["Pakistan"],["India"],["England"],["Australia"],["SouthAfrica"],["Srilanka"],["Netherland"],["Newzealand"],["Afghanistan"],["Bangladesh"]
teams=[Pak,Ind,Eng,Aus,Sa,Sl,Ned,Nz,Afg,Ban]
team=[]
c=tk.Label(window,text="")
def final_1_1(a):
    c.config(text=f"Champions:     {a}")
    c.place(x=750,y=550)
def final_1_2(a):
    c.config(text=f"Champions:     {a}")
    c.place(x=750,y=550)
f_1=tk.Button(window,text="",command=lambda: final_1_1(f_1["text"]))
f_2=tk.Button(window,text="",command=lambda: final_1_2(f_2["text"]))
def s_1(arg):
    label_final=tk.Label(window,text="Final :")
    label_final.place(x=750,y=510)
    f_1.config(text=f"{arg}")
    f_1.place(x=900,y=510)
def s_2(arg):
    label_final=tk.Label(window,text="Final :")
    label_final.place(x=750,y=510)
    f_1.config(text=f"{arg}")
    f_1.place(x=900,y=510)
def s_3(arg):
    label_final=tk.Label(window,text="Final :")
    label_final.place(x=750,y=510)
    f_2.config(text=f"{arg}")
    f_2.place(x=980,y=510)
def s_4(arg):
    label_final=tk.Label(window,text="Final :")
    label_final.place(x=750,y=510)
    f_2.config(text=f"{arg}")
    f_2.place(x=980,y=510)
sf_1_1=tk.Button(window,text="",command=lambda:s_1(sf_1_1["text"]))
sf_1_2=tk.Button(window,text="",command=lambda:s_2(sf_1_2["text"]))
sf_2_1=tk.Button(window,text="",command=lambda:s_3(sf_2_1["text"]))
sf_2_2=tk.Button(window,text="",command=lambda:s_4(sf_2_2["text"]))
sf_2_label=tk.Label(window,text="Semi final 2 :")
sf_1_label=tk.Label(window,text="Semi final 1 :")
def myfunc(tea):
    w=0
    for i in range(len(teams)):
        if teams[i].count(2)+teams[i].count(0)!=9:
            w=1
    if(w==0):
        sf_1_label.place(x=750,y=430)
        sf_2_label.place(x=750,y=470)
        sf_1_1.config(text=f"{tea[0][0]}")
        sf_1_1.place(x=900,y=430)
        sf_1_2.config(text=f"{tea[3][0]}")
        sf_1_2.place(x=980,y=430)
        sf_2_1.config(text=f"{tea[1][0]}")
        sf_2_1.place(x=900,y=470)
        sf_2_2.config(text=f"{tea[2][0]}")
        sf_2_2.place(x=980,y=470)
def table():
    results=[i for i in points_table.values()]
    start,end=0,8
    for i in range(len(teams)):
        teams[i]=[teams[i][0]]
        for j in range(start,end+1):
            teams[i].append(results[j])
        start+=9
        end+=9
    team=sorted(teams,key=lambda x:2*x.count(2),reverse=True)
    j=0
    for i in range(0,len(labels),5):
        labels[i].config(text=f"{team[j][0]}")
        labels[i+1].config(text=f"{team[j].count(2)+team[j].count(0)}")
        labels[i+2].config(text=f"{team[j].count(2)}")
        labels[i+3].config(text=f"{team[j].count(0)}")
        labels[i+4].config(text=f"{2*team[j].count(2)}")
        j+=1
    myfunc(team)
x,y=800,30
count=0
for i in range(len(labels)):
    labels[i].place(x=x,y=y)
    x+=60
    count+=1
    if(count==5):
        count=0
        x=800
        y+=40
    if(count==1 or count==6 or count==11 or count==16 or count==21 or count==26 or count==31 or count==36 or count==41 or count==46 or count==51):
        continue
    else:
        labels[i].config(text=f"{0}")
label=[t1_1,t2_1,t3_1,t4_1,t5_1,t6_1,t7_1,t8_1,t9_1,t10_1]
duration=30
for i in range(len(label)):
    label[i].config(text=f"{teams[i][0]}")
    label[i].place(x=750,y=duration)
    duration+=40
def pak_1():
    if(pak_1.flag==False):
        points_table[0],points_table[54]=2,0
        pak_1.flag,ned_1.flag=True,False
        label_2.config(text="PAK")
        table()
def pak_2():
    if(pak_2.flag==False):
        points_table[1],points_table[46]=2,0
        pak_2.flag,sl_2.flag=True,False
        label_9.config(text="PAK")
        table()
def pak_3():
    if(pak_3.flag==False):
        points_table[2],points_table[11]=2,0
        pak_3.flag,ind_3.flag=True,False
        label_13.config(text="PAK")
        table()
def pak_4():
    if(pak_4.flag==False):
        points_table[3],points_table[30]=2,0
        pak_4.flag,aus_4.flag=True,False
        label_18.config(text="PAK")
        table()
def pak_5():
    if(pak_5.flag==False):
        points_table[4],points_table[76]=2,0
        pak_5.flag,afg_5.flag=True,False
        label_22.config(text="PAK")
        table()
def pak_6():
    if(pak_6.flag==False):
        points_table[5],points_table[41]=2,0
        pak_6.flag,sa_6.flag=True,False
        label_26.config(text="PAK")
        table()
def pak_7():
    if(pak_7.flag==False):
        points_table[6],points_table[87]=2,0
        pak_7.flag,ban_7.flag=True,False
        label_31.config(text="PAK")
        table()
def pak_8():
    if(pak_8.flag==False):
        points_table[7],points_table[70]=2,0
        pak_8.flag,nz_8.flag=True,False
        label_36.config(text="PAK")
        table()
def pak_9():
    if(pak_9.flag==False):
        points_table[8],points_table[26]=2,0
        pak_9.flag,eng_9.flag=True,False
        label_44.config(text="PAK")
        table()
def ind_1():
    if(ind_1.flag==False):
        points_table[9],points_table[27]=2,0
        ind_1.flag,aus_1.flag=True,False
        label_5.config(text="IND")
        table()
def ind_2():
    if(ind_2.flag==False):
        points_table[10],points_table[73]=2,0
        ind_2.flag,afg_2.flag=True,False
        label_8.config(text="IND")
        table()
def ind_3():
    if(ind_3.flag==False):
        points_table[11],points_table[2]=2,0
        ind_3.flag,pak_3.flag=True,False
        label_13.config(text="IND")
        table()
def ind_4():
    if(ind_4.flag==False):
        points_table[12],points_table[84]=2,0
        ind_4.flag,ban_4.flag=True,False
        label_17.config(text="IND")
        table()
def ind_5():
    if(ind_5.flag==False):
        points_table[13],points_table[67]=2,0
        ind_5.flag,nz_5.flag=True,False
        label_21.config(text="IND")
        table()
def ind_6():
    if(ind_6.flag==False):
        points_table[14],points_table[23]=2,0
        ind_6.flag,eng_6.flag=True,False
        label_29.config(text="IND")
        table()
def ind_7():
    if(ind_7.flag==False):
        points_table[15],points_table[51]=2,0
        ind_7.flag,sl_7.flag=True,False
        label_33.config(text="IND")
        table()
def ind_8():
    if(ind_8.flag==False):
        points_table[16],points_table[43]=2,0
        ind_8.flag,sa_8.flag=True,False
        label_37.config(text="IND")
        table()
def ind_9():
    if(ind_9.flag==False):
        points_table[17],points_table[62]=2,0
        ind_9.flag,ned_9.flag=True,False
        label_43.config(text="IND")
        table()
def eng_1():
    if(eng_1.flag==False):
        points_table[18],points_table[63]=2,0
        eng_1.flag,nz_1.flag=True,False
        label_1.config(text="ENG")
        table()
def eng_2():
    if(eng_2.flag==False):
        points_table[19],points_table[82]=2,0
        eng_2.flag,ban_2.flag=True,False
        label_7.config(text="ENG")
        table()
def eng_3():
    if(eng_3.flag==False):
        points_table[20],points_table[74]=2,0
        eng_3.flag,afg_3.flag=True,False
        label_11.config(text="ENG")
        table()
def eng_4():
    if(eng_4.flag==False):
        points_table[21],points_table[39]=2,0
        eng_4.flag,sa_4.flag=True,False
        label_19.config(text="ENG")
        table()
def eng_5():
    if(eng_5.flag==False):
        points_table[22],points_table[49]=2,0
        eng_5.flag,sl_5.flag=True,False
        label_25.config(text="ENG")
        table()
def eng_6():
    if(eng_6.flag==False):
        points_table[23],points_table[14]=2,0
        eng_6.flag,ind_6.flag=True,False
        label_29.config(text="ENG")
        table()
def eng_7():
    if(eng_7.flag==False):
        points_table[24],points_table[33]=2,0
        eng_7.flag,aus_7.flag=True,False
        label_35.config(text="ENG")
        table()
def eng_8():
    if(eng_8.flag==False):
        points_table[25],points_table[61]=2,0
        eng_8.flag,ned_8.flag=True,False
        label_40.config(text="ENG")
        table()
def eng_9():
    if(eng_9.flag==False):
        points_table[26],points_table[8]=2,0
        eng_9.flag,pak_9.flag=True,False
        label_44.config(text="ENG")
        table()
def aus_1():
    if(aus_1.flag==False):
        points_table[27],points_table[9]=2,0
        aus_1.flag,ind_1.flag=True,False
        label_5.config(text="AUS")
        table()
def aus_2():
    if(aus_2.flag==False):
        points_table[28],points_table[37]=2,0
        aus_2.flag,sa_2.flag=True,False
        label_10.config(text="AUS")
        table()
def aus_3():
    if(aus_3.flag==False):
        points_table[29],points_table[47]=2,0
        aus_3.flag,sl_3.flag=True,False
        label_14.config(text="AUS")
        table()
def aus_4():
    if(aus_4.flag==False):
        points_table[30],points_table[3]=2,0
        aus_4.flag,pak_4.flag=True,False
        label_18.config(text="AUS")
        table()
def aus_5():
    if(aus_5.flag==False):
        points_table[31],points_table[58]=2,0
        aus_5.flag,ned_5.flag=True,False
        label_24.config(text="AUS")
        table()
def aus_6():
    if(aus_6.flag==False):
        points_table[32],points_table[68]=2,0
        aus_6.flag,nz_6.flag=True,False
        label_28.config(text="AUS")
        table()
def aus_7():
    if(aus_7.flag==False):
        points_table[33],points_table[24]=2,0
        aus_7.flag,eng_7.flag=True,False
        label_35.config(text="AUS")
        table()
def aus_8():
    if(aus_8.flag==False):
        points_table[34],points_table[79]=2,0
        aus_8.flag,afg_8.flag=True,False
        label_39.config(text="AUS")
        table()
def aus_9():
    if(aus_9.flag==False):
        points_table[35],points_table[89]=2,0
        aus_9.flag,ban_9.flag=True,False
        label_45.config(text="AUS")
        table()
def sa_1():
    if(sa_1.flag==False):
        points_table[36],points_table[45]=2,0
        sa_1.flag,sl_1.flag=True,False
        label_4.config(text="SA")
        table()
def sa_2():
    if(sa_2.flag==False):
        points_table[37],points_table[28]=2,0
        sa_2.flag,aus_2.flag=True,False
        label_10.config(text="SA")
        table()
def sa_3():
    if(sa_3.flag==False):
        points_table[38],points_table[56]=2,0
        sa_3.flag,ned_3.flag=True,False
        label_15.config(text="SA")
        table()
def sa_4():
    if(sa_4.flag==False):
        points_table[39],points_table[21]=2,0
        sa_4.flag,eng_4.flag=True,False
        label_19.config(text="SA")
        table()
def sa_5():
    if(sa_5.flag==False):
        points_table[40],points_table[85]=2,0
        sa_5.flag,ban_5.flag=True,False
        label_23.config(text="SA")
        table()
def sa_6():
    if(sa_6.flag==False):
        points_table[41],points_table[5]=2,0
        sa_6.flag,pak_6.flag=True,False
        label_26.config(text="SA")
        table()
def sa_7():
    if(sa_7.flag==False):
        points_table[42],points_table[69]=2,0
        sa_7.flag,nz_7.flag=True,False
        label_32.config(text="SA")
        table()
def sa_8():
    if(sa_8.flag==False):
        points_table[43],points_table[16]=2,0
        sa_8.flag,ind_8.flag=True,False
        label_37.config(text="SA")
        table()
def sa_9():
    if(sa_9.flag==False):
        points_table[44],points_table[80]=2,0
        sa_9.flag,afg_9.flag=True,False
        label_42.config(text="SA")
        table()
def sl_1():
    if(sl_1.flag==False):
        points_table[45],points_table[36]=2,0
        sl_1.flag,sa_1.flag=True,False
        label_4.config(text="SL")
        table()
def sl_2():
    if(sl_1.flag==False):
        points_table[46],points_table[1]=2,0
        sl_2.flag,pak_2.flag=True,False
        label_9.config(text="SL")
        table()
def sl_3():
    if(sl_3.flag==False):
        points_table[47],points_table[29]=2,0
        sl_3.flag,aus_3.flag=True,False
        label_14.config(text="SL")
        table()
def sl_4():
    if(sl_4.flag==False):
        points_table[48],points_table[57]=2,0
        sl_4.flag,ned_4.flag=True,False
        label_20.config(text="SL")
        table()
def sl_5():
    if(sl_5.flag==False):
        points_table[49],points_table[22]=2,0
        sl_5.flag,eng_5.flag=True,False
        label_25.config(text="SL")
        table()
def sl_6():
    if(sl_6.flag==False):
        points_table[50],points_table[77]=2,0
        sl_6.flag,afg_6.flag=True,False
        label_30.config(text="SL")
        table()
def sl_7():
    if(sl_7.flag==False):
        points_table[51],points_table[15]=2,0
        sl_7.flag,ind_7.flag=True,False
        label_33.config(text="SL")
        table()
def sl_8():
    if(sl_8.flag==False):
        points_table[52],points_table[88]=2,0
        sl_8.flag,ban_8.flag=True,False
        label_38.config(text="SL")
        table()
def sl_9():
    if(sl_9.flag==False):
        points_table[53],points_table[71]=2,0
        sl_9.flag,nz_9.flag=True,False
        label_41.config(text="SL")
        table()
def ned_1():
    if(ned_1.flag==False):
        points_table[54],points_table[0]=2,0
        ned_1.flag,pak_1.flag=True,False
        label_2.config(text="NED")
        table()
def ned_2():
    if(ned_2.flag==False):
        points_table[55],points_table[64]=2,0
        ned_2.flag,nz_2.flag=True,False
        label_6.config(text="NED")
        table()
def ned_3():
    if(ned_3.flag==False):
        points_table[56],points_table[38]=2,0
        ned_3.flag,sa_3.flag=True,False
        label_15.config(text="NED")
        table()
def ned_4():
    if(ned_4.flag==False):
        points_table[57],points_table[48]=2,0
        ned_4.flag,sl_4.flag=True,False
        label_20.config(text="NED")
        table()
def ned_5():
    if(ned_5.flag==False):
        points_table[58],points_table[31]=2,0
        ned_5.flag,aus_5.flag=True,False
        label_24.config(text="NED")
        table()
def ned_6():
    if(ned_6.flag==False):
        points_table[59],points_table[86]=2,0
        ned_6.flag,ban_6.flag=True,False
        label_27.config(text="NED")
        table()
def ned_7():
    if(ned_7.flag==False):
        points_table[60],points_table[78]=2,0
        ned_7.flag,afg_7.flag=True,False
        label_34.config(text="NED")
        table()
def ned_8():
    if(ned_8.flag==False):
        points_table[61],points_table[25]=2,0
        ned_8.flag,eng_8.flag=True,False
        label_40.config(text="NED")
        table()
def ned_9():
    if(ned_9.flag==False):
        points_table[62],points_table[17]=2,0
        ned_9.flag,ind_9.flag=True,False
        label_43.config(text="NED")
        table()
def nz_1():
    if(nz_1.flag==False):
        points_table[63],points_table[18]=2,0
        nz_1.flag,eng_1.flag=True,False
        label_1.config(text="NZ")
        table()
def nz_2():
    if(nz_2.flag==False):
        points_table[64],points_table[55]=2,0
        nz_2.flag,ned_2.flag=True,False
        label_6.config(text="NZ")
        table()
def nz_3():
    if(nz_3.flag==False):
        points_table[65],points_table[83]=2,0
        nz_3.flag,ban_3.flag=True,False
        label_12.config(text="NZ")
        table()
def nz_4():
    if(nz_4.flag==False):
        points_table[66],points_table[75]=2,0
        nz_4.flag,afg_4.flag=True,False
        label_16.config(text="NZ")
        table()
def nz_5():
    if(nz_5.flag==False):
        points_table[67],points_table[13]=2,0
        nz_5.flag,ind_5.flag=True,False
        label_21.config(text="NZ")
        table()
def nz_6():
    if(nz_6.flag==False):
        points_table[68],points_table[32]=2,0
        nz_6.flag,aus_6.flag=True,False
        label_28.config(text="NZ")
        table()
def nz_7():
    if(nz_7.flag==False):
        points_table[69],points_table[42]=2,0
        nz_7.flag,sa_7.flag=True,False
        label_32.config(text="NZ")
        table()
def nz_8():
    if(nz_8.flag==False):
        points_table[70],points_table[7]=2,0
        nz_8.flag,pak_8.flag=True,False
        label_36.config(text="NZ")
        table()
def nz_9():
    if(nz_9.flag==False):
        points_table[71],points_table[53]=2,0
        nz_9.flag,sl_9.flag=True,False
        label_41.config(text="NZ")
        table()
def afg_1():
    if(afg_1.flag==False):
        points_table[72],points_table[81]=2,0
        afg_1.flag,ban_1.flag=True,False
        label_3.config(text="AFG")
        table()
def afg_2():
    if(afg_2.flag==False):
        points_table[73],points_table[10]=2,0
        afg_2.flag,ind_2.flag=True,False
        label_8.config(text="AFG")
        table()
def afg_3():
    if(afg_3.flag==False):
        points_table[74],points_table[20]=2,0
        afg_3.flag,eng_3.flag=True,False
        label_11.config(text="AFG")
        table()
def afg_4():
    if(afg_4.flag==False):
        points_table[75],points_table[66]=2,0
        afg_4.flag,nz_4.flag=True,False
        label_16.config(text="AFG")
        table()
def afg_5():
    if(afg_5.flag==False):
        points_table[76],points_table[4]=2,0
        afg_5.flag,pak_5.flag=True,False
        label_22.config(text="AFG")
        table()
def afg_6():
    if(afg_6.flag==False):
        points_table[77],points_table[50]=2,0
        afg_6.flag,sl_6.flag=True,False
        label_30.config(text="AFG")
        table()
def afg_7():
    if(afg_7.flag==False):
        points_table[78],points_table[60]=2,0
        afg_7.flag,ned_7.flag=True,False
        label_34.config(text="AFG")
        table()
def afg_8():
    if(afg_8.flag==False):
        points_table[79],points_table[34]=2,0
        afg_8.flag,aus_8.flag=True,False
        label_39.config(text="AFG")
        table()
def afg_9():
    if(afg_9.flag==False):
        points_table[80],points_table[44]=2,0
        afg_9.flag,sa_9.flag=True,False
        label_42.config(text="AFG")
        table()
def ban_1():
    if(ban_1.flag==False):
        points_table[81],points_table[72]=2,0
        ban_1.flag,afg_1.flag=True,False
        label_3.config(text="BAN")
        table()
def ban_2():
    if(ban_2.flag==False):
        points_table[82],points_table[19]=2,0
        ban_2.flag,eng_2.flag=True,False
        label_7.config(text="BAN")
        table()
def ban_3():
    if(ban_3.flag==False):
        points_table[83],points_table[65]=2,0
        ban_3.flag,nz_3.flag=True,False
        label_12.config(text="BAN")
        table()
def ban_4():
    if(ban_4.flag==False):
        points_table[84],points_table[12]=2,0
        ban_4.flag,ind_4.flag=True,False
        label_17.config(text="BAN")
        table()
def ban_5():
    if(ban_5.flag==False):
        points_table[85],points_table[40]=2,0
        ban_5.flag,sa_5.flag=True,False
        label_23.config(text="BAN")
        table()
def ban_6():
    if(ban_6.flag==False):
        points_table[86],points_table[59]=2,0
        ban_6.flag,ned_6.flag=True,False
        label_27.config(text="BAN")
        table()
def ban_7():
    if(ban_7.flag==False):
        points_table[87],points_table[6]=2,0
        ban_7.flag,pak_7.flag=True,False
        label_31.config(text="BAN")
        table()
def ban_8():
    if(ban_8.flag==False):
        points_table[88],points_table[52]=2,0
        ban_8.flag,sl_8.flag=True,False
        label_38.config(text="BAN")
        table()
def ban_9():
    if(ban_9.flag==False):
        points_table[89],points_table[35]=2,0
        ban_9.flag,aus_9.flag=True,False
        label_45.config(text="BAN")
        table()
        

pak_1.flag=ind_1.flag=aus_1.flag=eng_1.flag=sa_1.flag=sl_1.flag=ned_1.flag=nz_1.flag=ban_1.flag=afg_1.flag=False
pak_2.flag=ind_2.flag=aus_2.flag=eng_2.flag=sa_2.flag=sl_2.flag=ned_2.flag=nz_2.flag=ban_2.flag=afg_2.flag=False
pak_3.flag=ind_3.flag=aus_3.flag=eng_3.flag=sa_3.flag=sl_3.flag=ned_3.flag=nz_3.flag=ban_3.flag=afg_3.flag=False
pak_4.flag=ind_4.flag=aus_4.flag=eng_4.flag=sa_4.flag=sl_4.flag=ned_4.flag=nz_4.flag=ban_4.flag=afg_4.flag=False
pak_5.flag=ind_5.flag=aus_5.flag=eng_5.flag=sa_5.flag=sl_5.flag=ned_5.flag=nz_5.flag=ban_5.flag=afg_5.flag=False
pak_6.flag=ind_6.flag=aus_6.flag=eng_6.flag=sa_6.flag=sl_6.flag=ned_6.flag=nz_6.flag=ban_6.flag=afg_6.flag=False
pak_7.flag=ind_7.flag=aus_7.flag=eng_7.flag=sa_7.flag=sl_7.flag=ned_7.flag=nz_7.flag=ban_7.flag=afg_7.flag=False
pak_8.flag=ind_8.flag=aus_8.flag=eng_8.flag=sa_8.flag=sl_8.flag=ned_8.flag=nz_8.flag=ban_8.flag=afg_8.flag=False
pak_9.flag=ind_9.flag=aus_9.flag=eng_9.flag=sa_9.flag=sl_9.flag=ned_9.flag=nz_9.flag=ban_9.flag=afg_9.flag=False



Pak_1=tk.Button(window,text="Pak",command=pak_1)
Pak_2=tk.Button(window,text="Pak",command=pak_2)
Pak_3=tk.Button(window,text="Pak",command=pak_3)
Pak_4=tk.Button(window,text="Pak",command=pak_4)
Pak_5=tk.Button(window,text="Pak",command=pak_5)
Pak_6=tk.Button(window,text="Pak",command=pak_6)
Pak_7=tk.Button(window,text="Pak",command=pak_7)
Pak_8=tk.Button(window,text="Pak",command=pak_8)
Pak_9=tk.Button(window,text="Pak",command=pak_9)
Ind_1=tk.Button(window,text="Ind",command=ind_1)
Ind_2=tk.Button(window,text="Ind",command=ind_2)
Ind_3=tk.Button(window,text="Ind",command=ind_3)
Ind_4=tk.Button(window,text="Ind",command=ind_4)
Ind_5=tk.Button(window,text="Ind",command=ind_5)
Ind_6=tk.Button(window,text="Ind",command=ind_6)
Ind_7=tk.Button(window,text="Ind",command=ind_7)
Ind_8=tk.Button(window,text="Ind",command=ind_8)
Ind_9=tk.Button(window,text="Ind",command=ind_9)
Eng_1=tk.Button(window,text="Eng",command=eng_1)
Eng_2=tk.Button(window,text="Eng",command=eng_2)
Eng_3=tk.Button(window,text="Eng",command=eng_3)
Eng_4=tk.Button(window,text="Eng",command=eng_4)
Eng_5=tk.Button(window,text="Eng",command=eng_5)
Eng_6=tk.Button(window,text="Eng",command=eng_6)
Eng_7=tk.Button(window,text="Eng",command=eng_7)
Eng_8=tk.Button(window,text="Eng",command=eng_8)
Eng_9=tk.Button(window,text="Eng",command=eng_9)
Sa_1=tk.Button(window,text="Sa",command=sa_1)
Sa_2=tk.Button(window,text="Sa",command=sa_2)
Sa_3=tk.Button(window,text="Sa",command=sa_3)
Sa_4=tk.Button(window,text="Sa",command=sa_4)
Sa_5=tk.Button(window,text="Sa",command=sa_5)
Sa_6=tk.Button(window,text="Sa",command=sa_6)
Sa_7=tk.Button(window,text="Sa",command=sa_7)
Sa_8=tk.Button(window,text="Sa",command=sa_8)
Sa_9=tk.Button(window,text="Sa",command=sa_9)
Aus_1=tk.Button(window,text="Aus",command=aus_1)
Aus_2=tk.Button(window,text="Aus",command=aus_2)
Aus_3=tk.Button(window,text="Aus",command=aus_3)
Aus_4=tk.Button(window,text="Aus",command=aus_4)
Aus_5=tk.Button(window,text="Aus",command=aus_5)
Aus_6=tk.Button(window,text="Aus",command=aus_6)
Aus_7=tk.Button(window,text="Aus",command=aus_7)
Aus_8=tk.Button(window,text="Aus",command=aus_8)
Aus_9=tk.Button(window,text="Aus",command=aus_9)
Nz_1=tk.Button(window,text="Nz",command=nz_1)
Nz_2=tk.Button(window,text="Nz",command=nz_2)
Nz_3=tk.Button(window,text="Nz",command=nz_3)
Nz_4=tk.Button(window,text="Nz",command=nz_4)
Nz_5=tk.Button(window,text="Nz",command=nz_5)
Nz_6=tk.Button(window,text="Nz",command=nz_6)
Nz_7=tk.Button(window,text="Nz",command=nz_7)
Nz_8=tk.Button(window,text="Nz",command=nz_8)
Nz_9=tk.Button(window,text="Nz",command=nz_9)
Ban_1=tk.Button(window,text="Ban",command=ban_1)
Ban_2=tk.Button(window,text="Ban",command=ban_2)
Ban_3=tk.Button(window,text="Ban",command=ban_3)
Ban_4=tk.Button(window,text="Ban",command=ban_4)
Ban_5=tk.Button(window,text="Ban",command=ban_5)
Ban_6=tk.Button(window,text="Ban",command=ban_6)
Ban_7=tk.Button(window,text="Ban",command=ban_7)
Ban_8=tk.Button(window,text="Ban",command=ban_8)
Ban_9=tk.Button(window,text="Ban",command=ban_9)
Afg_1=tk.Button(window,text="Afg",command=afg_1)
Afg_2=tk.Button(window,text="Afg",command=afg_2)
Afg_3=tk.Button(window,text="Afg",command=afg_3)
Afg_4=tk.Button(window,text="Afg",command=afg_4)
Afg_5=tk.Button(window,text="Afg",command=afg_5)
Afg_6=tk.Button(window,text="Afg",command=afg_6)
Afg_7=tk.Button(window,text="Afg",command=afg_7)
Afg_8=tk.Button(window,text="Afg",command=afg_8)
Afg_9=tk.Button(window,text="Afg",command=afg_9)
Sl_1=tk.Button(window,text="Sl",command=sl_1)
Sl_2=tk.Button(window,text="Sl",command=sl_2)
Sl_3=tk.Button(window,text="Sl",command=sl_3)
Sl_4=tk.Button(window,text="Sl",command=sl_4)
Sl_5=tk.Button(window,text="Sl",command=sl_5)
Sl_6=tk.Button(window,text="Sl",command=sl_6)
Sl_7=tk.Button(window,text="Sl",command=sl_7)
Sl_8=tk.Button(window,text="Sl",command=sl_8)
Sl_9=tk.Button(window,text="Sl",command=sl_9)
Ned_1=tk.Button(window,text="Ned",command=ned_1)
Ned_2=tk.Button(window,text="Ned",command=ned_2)
Ned_3=tk.Button(window,text="Ned",command=ned_3)
Ned_4=tk.Button(window,text="Ned",command=ned_4)
Ned_5=tk.Button(window,text="Ned",command=ned_5)
Ned_6=tk.Button(window,text="Ned",command=ned_6)
Ned_7=tk.Button(window,text="Ned",command=ned_7)
Ned_8=tk.Button(window,text="Ned",command=ned_8)
Ned_9=tk.Button(window,text="Ned",command=ned_9)
window.geometry("1300x1800")
Eng_1.place(x=10,y=10)
Nz_1.place(x=40,y=10)
Pak_1.place(x=100,y=10)
Ned_1.place(x=130,y=10)
Ban_1.place(x=190,y=10)
Afg_1.place(x=220,y=10)
Sa_1.place(x=280,y=10)
Sl_1.place(x=310,y=10)
Ind_1.place(x=370,y=10)
Aus_1.place(x=400,y=10)
Nz_2.place(x=10,y=80)
Ned_2.place(x=40,y=80)
Eng_2.place(x=100,y=80)
Ban_2.place(x=130,y=80)
Ind_2.place(x=190,y=80)
Afg_2.place(x=220,y=80)
Pak_2.place(x=280,y=80)
Sl_2.place(x=310,y=80)
Aus_2.place(x=370,y=80)
Sa_2.place(x=400,y=80)
Eng_3.place(x=10,y=150)
Afg_3.place(x=40,y=150)
Nz_3.place(x=100,y=150)
Ban_3.place(x=130,y=150)
Ind_3.place(x=190,y=150)
Pak_3.place(x=220,y=150)
Aus_3.place(x=280,y=150)
Sl_3.place(x=310,y=150)
Sa_3.place(x=370,y=150)
Ned_3.place(x=400,y=150)
Afg_4.place(x=10,y=220)
Nz_4.place(x=40,y=220)
Ind_4.place(x=100,y=220)
Ban_4.place(x=130,y=220)
Pak_4.place(x=190,y=220)
Aus_4.place(x=220,y=220)
Eng_4.place(x=280,y=220)
Sa_4.place(x=310,y=220)
Sl_4.place(x=370,y=220)
Ned_4.place(x=400,y=220)
Ind_5.place(x=10,y=290)
Nz_5.place(x=40,y=290)
Pak_5.place(x=100,y=290)
Afg_5.place(x=130,y=290)
Sa_5.place(x=190,y=290)
Ban_5.place(x=220,y=290)
Aus_5.place(x=280,y=290)
Ned_5.place(x=310,y=290)
Sl_5.place(x=370,y=290)
Eng_5.place(x=400,y=290)
Pak_6.place(x=10,y=360)
Sa_6.place(x=40,y=360)
Ban_6.place(x=100,y=360)
Ned_6.place(x=130,y=360)
Nz_6.place(x=190,y=360)
Aus_6.place(x=220,y=360)
Ind_6.place(x=280,y=360)
Eng_6.place(x=310,y=360)
Sl_6.place(x=370,y=360)
Afg_6.place(x=400,y=360)
Ban_7.place(x=10,y=430)
Pak_7.place(x=40,y=430)
Nz_7.place(x=100,y=430)
Sa_7.place(x=130,y=430)
Ind_7.place(x=190,y=430)
Sl_7.place(x=220,y=430)
Afg_7.place(x=280,y=430)
Ned_7.place(x=310,y=430)
Eng_7.place(x=370,y=430)
Aus_7.place(x=400,y=430)
Nz_8.place(x=10,y=500)
Pak_8.place(x=40,y=500)
Ind_8.place(x=100,y=500)
Sa_8.place(x=130,y=500)
Ban_8.place(x=190,y=500)
Sl_8.place(x=220,y=500)
Aus_8.place(x=280,y=500)
Afg_8.place(x=310,y=500)
Eng_8.place(x=370,y=500)
Ned_8.place(x=400,y=500)
Nz_9.place(x=10,y=570)
Sl_9.place(x=40,y=570)
Sa_9.place(x=100,y=570)
Afg_9.place(x=130,y=570)
Ind_9.place(x=190,y=570)
Ned_9.place(x=220,y=570)
Pak_9.place(x=280,y=570)
Eng_9.place(x=310,y=570)
Aus_9.place(x=370,y=570)
Ban_9.place(x=400,y=570)
label_1=tk.Label(window)
label_1.place(x=25,y=45)
label_2=tk.Label(window)
label_2.place(x=115,y=45)
label_3=tk.Label(window)
label_3.place(x=205,y=45)
label_4=tk.Label(window)
label_4.place(x=295,y=45)
label_5=tk.Label(window)
label_5.place(x=385,y=45)
label_6=tk.Label(window)
label_6.place(x=25,y=115)
label_7=tk.Label(window)
label_7.place(x=115,y=115)
label_8=tk.Label(window)
label_8.place(x=205,y=115)
label_9=tk.Label(window)
label_9.place(x=295,y=115)
label_10=tk.Label(window)
label_10.place(x=385,y=115)
label_11=tk.Label(window)
label_11.place(x=25,y=185)
label_12=tk.Label(window)
label_12.place(x=115,y=185)
label_13=tk.Label(window)
label_13.place(x=205,y=185)
label_14=tk.Label(window)
label_14.place(x=295,y=185)
label_15=tk.Label(window)
label_15.place(x=385,y=185)
label_16=tk.Label(window)
label_16.place(x=25,y=255)
label_17=tk.Label(window)
label_17.place(x=115,y=255)
label_18=tk.Label(window)
label_18.place(x=205,y=255)
label_19=tk.Label(window)
label_19.place(x=295,y=255)
label_20=tk.Label(window)
label_20.place(x=385,y=255)
label_21=tk.Label(window)
label_21.place(x=25,y=325)
label_22=tk.Label(window)
label_22.place(x=115,y=325)
label_23=tk.Label(window)
label_23.place(x=205,y=325)
label_24=tk.Label(window)
label_24.place(x=295,y=325)
label_25=tk.Label(window)
label_25.place(x=385,y=325)
label_26=tk.Label(window)
label_26.place(x=25,y=395)
label_27=tk.Label(window)
label_27.place(x=115,y=395)
label_28=tk.Label(window)
label_28.place(x=205,y=395)
label_29=tk.Label(window)
label_29.place(x=295,y=395)
label_30=tk.Label(window)
label_30.place(x=385,y=395)
label_31=tk.Label(window)
label_31.place(x=25,y=465)
label_32=tk.Label(window)
label_32.place(x=115,y=465)
label_33=tk.Label(window)
label_33.place(x=205,y=465)
label_34=tk.Label(window)
label_34.place(x=295,y=465)
label_35=tk.Label(window)
label_35.place(x=385,y=465)
label_36=tk.Label(window)
label_36.place(x=25,y=535)
label_37=tk.Label(window)
label_37.place(x=115,y=535)
label_38=tk.Label(window)
label_38.place(x=205,y=535)
label_39=tk.Label(window)
label_39.place(x=295,y=535)
label_40=tk.Label(window)
label_40.place(x=385,y=535)
label_41=tk.Label(window)
label_41.place(x=25,y=605)
label_42=tk.Label(window)
label_42.place(x=115,y=605)
label_43=tk.Label(window)
label_43.place(x=205,y=605)
label_44=tk.Label(window)
label_44.place(x=295,y=605)
label_45=tk.Label(window)
label_45.place(x=385,y=605)
another_label=tk.Label(window,text="ICC Cricket World Cup 2023")
another_label.place(x=500,y=5)
table_label=tk.Label(window,text="Points Table Predictor")
table_label.place(x=518,y=25)
team_label=tk.Label(window,text="Team")
team_label.place(x=750,y=0)
played_label=tk.Label(window,text="Played")
played_label.place(x=840,y=0)
won_label=tk.Label(window,text="Won")
won_label.place(x=910,y=0)
lose_label=tk.Label(window,text="Lost")
lose_label.place(x=970,y=0)
points_label=tk.Label(window,text="Points")
points_label.place(x=1030,y=0)
window.mainloop()




