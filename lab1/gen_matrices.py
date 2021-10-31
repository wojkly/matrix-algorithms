from oct2py import Oct2Py

oc = Oct2Py()

for i in range(2,20):
    for j in range(2,3):
        filename = "matrices/iga" + str(i) + "_" + str(j) + ".csv"
        oc.gen_mat(0,i,j,0, filename)
        oc.restart()
        print("file " + filename + "done")

oc.exit()