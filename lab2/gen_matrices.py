from oct2py import Oct2Py
oc = Oct2Py()


#gen fems

for i in range(2,20):
    filename = "matrices/fem_" + str(i)  + ".csv"
    oc.gen_mat(1,i,2,0, filename)
    oc.restart()
    print("file " + filename + "done")

#gen igas
for i in range(2,20):
    filename = "matrices/iga_" + str(i)  + ".csv"
    oc.gen_mat(0,i,2,0, filename)
    oc.restart()
    print("file " + filename + "done")

oc.exit()
