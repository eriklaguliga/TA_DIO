import pandas as pd
import math
import xlrd
a = xlrd.open_workbook("SainsTesting.xlsx")
sains = a.sheet_by_index(0)
b = xlrd.open_workbook("SosialTraining.xlsx")
sosial = b.sheet_by_index(0)
#sains
b_ind_1 = []
b_ing_1 = []
mtk_1 = []
fis_1 = []
jurusan = []


#social
b_ind_2 = []
b_ing_2 = []
mtk_2 = []
fis_2 = []
jurusan_ips = []

#input user
arr_b_in = []
arr_b_ing = []
arr_mtk = []
arr_fis = []




for i in range(1,sains.nrows):
    b_ind_1.append(sains.cell_value(i,2))
    b_ing_1.append(sains.cell_value(i,3))
    mtk_1.append(sains.cell_value(i,4))
    fis_1.append(sains.cell_value(i,5))
    jurusan.append(sains.cell_value(i,11))



for i in range(1,sosial.nrows):
    b_ind_2.append(sosial.cell_value(i,2))
    b_ing_2.append(sosial.cell_value(i,3))
    mtk_2.append(sosial.cell_value(i,4))
    jurusan_ips.append(sosial.cell_value(i,11))

def cari_jarak(x1,x2,y1,y2,k1,k2,c1,c2):
    a = (x1-x2)**2 + (y1-y2)**2 + (k1-k2)**2 + (c1 - c2)**2
    akar = math.sqrt(a)
    return akar

def cari_jarakips(x1,x2,y1,y2,k1,k2):
    a = (x1-x2)**2 + (y1-y2)**2 + (k1-k2)**2
    akar = math.sqrt(a)
    return akar

print("pilih jurusan mu")
print("contoh : 1 . untuk ipa")
print("contoh : 2 . untuk ips")
hasil_input = int(input("pilih jurusan: "))
print("masukkan nilaimu")
b_in =  float(input("bahasa indonesia : "))
arr_b_in.append(b_in)
b_ing =  float(input("bahasa inggris : "))
arr_b_ing.append(b_ing)
mtk =  float(input("matematika : "))
arr_mtk.append(mtk)
fis =  float(input("fisika : "))
arr_fis.append(fis)


def sortFirst(val):
    return val[0]

for i in range(len(arr_b_in)):
    z=[]
    u = []
    a=[]
    e=[]
    g=[]
    p = []
    hoax = 0
    tidak = 0
    #ips
    if(hasil_input == 2):
        for j in range(len(b_ind_2)):
            a= cari_jarakips(b_ind_2[j],arr_b_in[i],b_ing_2[j],arr_b_ing[i],mtk_2[j],arr_mtk[i])
            z.append(a)
    #ipa
    if(hasil_input == 1):
        # print(len(b_ind_2))
        for j in range(len(b_ind_1)):
            ipa = cari_jarak(b_ind_1[j], arr_b_in[i], b_ing_1[j], arr_b_ing[i], mtk_1[j], arr_mtk[i], fis_1[j], arr_fis[i])
            u.append(ipa)
        for k in range(len(b_ind_2)):
            ips = cari_jarakips(b_ind_2[k], arr_b_in[i], b_ing_2[k], arr_b_ing[i], mtk_2[k], arr_mtk[i])
            p.append(ips)
    listHasil = []
    # best = sorted(z)[0:7]
    if(z != None) :
        for k in range(len(z)):
            listHasil.append((z[k],jurusan_ips[k]))


    listHasilIpa = []

    if (u != None):
        for k in range(len(u)):
            listHasilIpa.append((u[k],jurusan[k]))

    listHasilIps = []
    if (p != None):
        for k in range(len(p)):
            listHasilIps.append((p[k],jurusan_ips[k]))

    listHasil.sort(key = sortFirst)
    listHasilIpa.sort(key=sortFirst)
    listHasilIps.sort(key=sortFirst)
    bestIpa = []
    bestIps_ipa = []
    bestIps = []

    if(hasil_input == 2):
        for k in range(7):
            bestIps.append(listHasil[k][1])
            # bestIpa.append(listHasilIpa[k][1])
            # bestIps_ipa.append(listHasilIps[k][1])

    if (hasil_input == 1):
        for k in range(7):
            # bestIps.append(listHasil[k][1])
            bestIpa.append(listHasilIpa[k][1])
            bestIps_ipa.append(listHasilIps[k][1])
    if(len(u) > 0):
        ips = sorted(u)[0:7]


print(bestIps)
print(bestIpa)
print(bestIps_ipa)
# print(best)
# print(ips)


    # for k in best:
    #     if n1[z.index(k)] == 1.0:
    #         hoax+=1
    #     else:
    #         tidak+=1
    # if hoax>tidak:
    #     n2 = 1.0
    # else:
    #     n2 = 0.0
    # wow.append(n2)
    # print(n2)


