#import package
import tkinter
from tkinter.font import Font
from tkinter import messagebox
from sklearn import tree
import pandas

#memasukkan dataset
df = pandas.read_csv('diabetes_data_upload.csv')

#mengubah nilai menjadi 0 dan 1
d = {'Male': 0, 'Female': 1}
df['Gender'] = df['Gender'].map(d)
d = {'Positive': 1, 'Negative': 0}
df['class'] = df['class'].map(d)

#variabel / atribut yang digunakan
features = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss', 'weakness',
            'Polyphagia', 'Genital thrush', 'visual blurring', 'Itching', 'Irritability',
            'delayed healing', 'partial paresis', 'muscle stiffness', 'Alopecia', 'Obesity']

#menentukan variabel dan target (output)
x = df[features]
y = df['class']

#membentuk decision tree
clf = tree.DecisionTreeClassifier()
clf = clf.fit(x, y)

def prog():
    try:
        age = int(input_umur.get())

        if var1.get() == 1:
            gender = 0
        elif var1.get() == 2:
            gender = 1

        if var2.get() == 2:
            polyuria = 0
        elif var2.get() == 1:
            polyuria = 1

        if var3.get() == 2:
            polydipsia = 0
        elif var3.get() == 1:
            polydipsia = 1

        if var4.get() == 2:
            weight = 0
        elif var4.get() == 1:
            weight = 1

        if var5.get() == 2:
            weakness = 0
        elif var5.get() == 1:
            weakness = 1

        if var6.get() == 2:
            polyphagia = 0
        elif var6.get() == 1:
            polyphagia = 1

        if var7.get() == 2:
            genital = 0
        elif var7.get() == 1:
            genital = 1

        if var8.get() == 2:
            visual = 0
        elif var8.get() == 1:
            visual = 1

        if var9.get() == 2:
            itching = 0
        elif var9.get() == 1:
            itching = 1

        if var10.get() == 2:
            irritability = 0
        elif var10.get() == 1:
            irritability = 1

        if var11.get() == 2:
            heal = 0
        elif var11.get() == 1:
            heal = 1

        if var12.get() == 2:
            paresis = 0
        elif var12.get() == 1:
            paresis = 1

        if var13.get() == 2:
            muscle = 0
        elif var13.get() == 1:
            muscle = 1

        if var14.get() == 2:
            alopecia = 0
        elif var14.get() == 1:
            alopecia = 1

        if var15.get() == 2:
            obesity = 0
        elif var15.get() == 1:
            obesity = 1

        #hasil klasifikasi
        if clf.predict([[age, gender, polyuria, polydipsia, weight, weakness, polyphagia, genital,
                         visual, itching, irritability, heal, paresis, muscle, alopecia, obesity]]):
            positif()
        else:
            negatif()

    except ValueError:
        messagebox.showinfo("Error", "MASUKKAN DATA SECARA LENGKAP!!")


def positif():
    messagebox.showinfo("Positif", "ANDA POSITIF DIABETES \n Segeralah periksa ke dokter!")

def negatif():
    messagebox.showinfo("Negatif", "ANDA NEGATIF DIABETES \n Jagalah selalu kesehatan anda!")


main_window = tkinter.Tk()
main_window.geometry("700x600+100+100")

font_judul = Font(family="Times New Roman" ,size=18)
font_pertanyaan = Font(family="Times New Roman", size=11)
font_tombol = Font(family="Times New Roman", size=14)

judul = tkinter.Label(main_window, text="Aplikasi Deteksi Dini Diabetes Melitus", font=font_judul,
                      padx=30, pady=20, anchor='center', width=80)

label_nama = tkinter.Label(main_window, text="Masukkan nama anda : ", font=font_pertanyaan)
input_nama = tkinter.Entry(main_window, bd=3, width=50)

label_umur = tkinter.Label(main_window, text="Masukkan umur anda : ", font=font_pertanyaan)
input_umur = tkinter.Entry(main_window, bd=3, width=10)

label_gender = tkinter.Label(main_window, text="Masukkan jenis kelamin anda : ", font=font_pertanyaan)
var1 = tkinter.IntVar()
gender_lk = tkinter.Radiobutton(main_window, text="Laki-Laki", font=font_pertanyaan, variable=var1, value=1)
gender_pr = tkinter.Radiobutton(main_window, text="Perempuan", font=font_pertanyaan, variable=var1, value=2)

#gejala
label_polyuria = tkinter.Label(main_window, text="1. Apakah anda terlalu sering kencing dan berlebihan? ",
                               font=font_pertanyaan)
var2 = tkinter.IntVar()
polyuria_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var2, value=1)
polyuria_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var2, value=2)

label_polydipsia = tkinter.Label(main_window, text="2. Apakah anda sering merasa kehausan yang berlebihan? ",
                                 font=font_pertanyaan)
var3 = tkinter.IntVar()
polydipsia_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var3, value=1)
polydipsia_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var3, value=2)

label_weight = tkinter.Label(main_window, text="3. Apakah anda mengalami penurunan berat badan "
                                               "yang drastis secara tiba-tiba? ", font=font_pertanyaan)
var4 = tkinter.IntVar()
weight_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var4, value=1)
weight_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var4, value=2)

label_weakness = tkinter.Label(main_window, text="4. Apakah anda sering merasa lemah / lemas? ",
                               font=font_pertanyaan)
var5 = tkinter.IntVar()
weakness_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var5, value=1)
weakness_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var5, value=2)

label_polyphagia = tkinter.Label(main_window, text="5. Apakah anda sering merasa kelaparan yang berlebihan? ",
                                 font=font_pertanyaan)
var6 = tkinter.IntVar()
polyphagia_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var6, value=1)
polyphagia_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var6, value=2)

label_genital = tkinter.Label(main_window, text="6. Apakah anda mengalami infeksi di kemaluan? ",
                              font=font_pertanyaan)
var7 = tkinter.IntVar()
genital_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var7, value=1)
genital_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var7, value=2)

label_visual = tkinter.Label(main_window, text="7. Apakah anda mengalami penurunan penglihatan (buram)? ",
                             font=font_pertanyaan)
var8 = tkinter.IntVar()
visual_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var8, value=1)
visual_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var8, value=2)

label_itching = tkinter.Label(main_window, text="8. Apakah anda sering mengalami gatal-gatal di kulit? ",
                              font=font_pertanyaan)
var9 = tkinter.IntVar()
itching_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var9, value=1)
itching_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var9, value=2)

label_irritability = tkinter.Label(main_window, text="9. Apakah anda sering merasa marah (iritabilitas)? ",
                                   font=font_pertanyaan)
var10 = tkinter.IntVar()
irritability_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var10, value=1)
irritability_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var10, value=2)

label_heal = tkinter.Label(main_window, text="10. Apakah penyembuhan luka anda sangat lambat? ",
                           font=font_pertanyaan)
var11 = tkinter.IntVar()
heal_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var11, value=1)
heal_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var11, value=2)

label_paresis = tkinter.Label(main_window, text="11. Apakah terdapat tubuh anda yang mengalami kelumpuhan? ",
                              font=font_pertanyaan)
var12 = tkinter.IntVar()
paresis_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var12, value=1)
paresis_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var12, value=2)

label_muscle = tkinter.Label(main_window, text="12. Apakah anda sering mengalami kaku otot? ",
                             font=font_pertanyaan)
var13 = tkinter.IntVar()
muscle_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var13, value=1)
muscle_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var13, value=2)

label_alopecia = tkinter.Label(main_window, text="13. Apakah anda mengalami kerontokan rambut yang parah? ",
                               font=font_pertanyaan)
var14 = tkinter.IntVar()
alopecia_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var14, value=1)
alopecia_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var14, value=2)

label_obesity = tkinter.Label(main_window, text="14. Apakah anda mengalami obesitas atau kelebihan berat badan? ",
                              font=font_pertanyaan)
var15 = tkinter.IntVar()
obesity_yes = tkinter.Radiobutton(main_window, text="Ya", font=font_pertanyaan, variable=var15, value=1)
obesity_no = tkinter.Radiobutton(main_window, text="Tidak", font=font_pertanyaan, variable=var15, value=2)

#button
tombol=tkinter.Button(main_window, text='CEK', font=font_tombol, width=8, height=1, command=prog)

#letak
judul.pack()

label_nama.place(x=20, y=80)
input_nama.place(x=230, y=80)

label_umur.place(x=20, y=105)
input_umur.place(x=230, y=105)

label_gender.place(x=20, y=130)
gender_lk.place(x=230, y=130)
gender_pr.place(x=350, y=130)

label_polyuria.place(x=20, y=170)
polyuria_yes.place(x=510, y=170)
polyuria_no.place(x=560, y=170)

label_polydipsia.place(x=20, y=195)
polydipsia_yes.place(x=510, y=195)
polydipsia_no.place(x=560, y=195)

label_weight.place(x=20, y=220)
weight_yes.place(x=510, y=220)
weight_no.place(x=560, y=220)

label_weakness.place(x=20, y=245)
weakness_yes.place(x=510, y=245)
weakness_no.place(x=560, y=245)

label_polyphagia.place(x=20, y=270)
polyphagia_yes.place(x=510, y=270)
polyphagia_no.place(x=560, y=270)

label_genital.place(x=20, y=295)
genital_yes.place(x=510, y=295)
genital_no.place(x=560, y=295)

label_visual.place(x=20, y=320)
visual_yes.place(x=510, y=320)
visual_no.place(x=560, y=320)

label_itching.place(x=20, y=345)
itching_yes.place(x=510, y=345)
itching_no.place(x=560, y=345)

label_irritability.place(x=20, y=370)
irritability_yes.place(x=510, y=370)
irritability_no.place(x=560, y=370)

label_heal.place(x=20, y=395)
heal_yes.place(x=510, y=395)
heal_no.place(x=560, y=395)

label_paresis.place(x=20, y=420)
paresis_yes.place(x=510, y=420)
paresis_no.place(x=560, y=420)

label_muscle.place(x=20, y=445)
muscle_yes.place(x=510, y=445)
muscle_no.place(x=560, y=445)

label_alopecia.place(x=20, y=470)
alopecia_yes.place(x=510, y=470)
alopecia_no.place(x=560, y=470)

label_obesity.place(x=20, y=495)
obesity_yes.place(x=510, y=495)
obesity_no.place(x=560, y=495)

tombol.place(x=300, y=530)

main_window.mainloop()


