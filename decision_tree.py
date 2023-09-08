#import package
from matplotlib import pyplot as plt
from sklearn.tree import DecisionTreeClassifier
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
features = ['Age', 'Gender', 'Polyuria', 'Polydipsia', 'sudden weight loss',
            'weakness', 'Polyphagia', 'Genital thrush', 'visual blurring',
            'Itching', 'Irritability', 'delayed healing', 'partial paresis',
            'muscle stiffness', 'Alopecia', 'Obesity']

#menentukan variabel dan target (output)
x = df[features]
y = df['class']

#membentuk decision tree
clf = DecisionTreeClassifier()
model = clf.fit(x, y)

#menampilkan text decision tree
text_representation = tree.export_text(clf)
print(text_representation)
#menyimpannya dalam file text "decision tree"
with open("decision_tree.log", "w") as fout:
    fout.write(text_representation)

#menampilkan image decision tree
fig = plt.figure(figsize=(25,20))
_ = tree.plot_tree(clf, feature_names=features, class_names='class', filled=True)
#menyimpannya dalam file png "decision tree"
fig.savefig("decision_tree.png")

