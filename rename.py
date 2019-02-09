import os
os.chdir("C:/Users/ilham/Downloads/music")
print(os.getcwd())


for f in os.listdir():
    f_name, f_ext = os.path.split(f)
    var = "-spcs.me"
    #defining spesific string which I want to remove
    if var in f_ext:
        new_ext = f_ext.replace(var, " ")
        new_ext = new_ext.replace(" ","")
        #replacing spaces
        print(new_ext)
        os.rename(f,new_ext)
