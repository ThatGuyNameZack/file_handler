import os


def main():
    i = 0
    path = "./" #any path
    for filename in os.listdir(path):
        my_dest = "img" + str(i) + ".jpg"
        my_source = os.path.join(path, filename)
        my_dest = os.path.join(path, my_dest) #it works on mac and winddows
        os.rename(my_source, my_dest)
        i += 1
    
if __name__ == '__main__':
    main()



