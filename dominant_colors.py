# Author: Mustaf Ahmed
# Date: 6/18/2016
# Program: A tool to find the dominant colors within any image, using the k-means clustering algorithm

from PIL import Image
import Tkinter, tkFileDialog
import math 
import random

def default (pixels):
    
    # Returns pixels list of tuples (R,G,B,Cluster Assignment('x' by default))
  
    pixels = [list(x)+ list(('x',)) for x in pixels]
    
    return pixels

def centroids (pixels,k):
    # Checks whether the pixels list is set to default
    # Generates k cluster points in an (R,G,B) color model
    
    if pixels[0][3] == 'x':
        
        centers = [[0] for f in range(0,k)]

        for i in range(0,k):

            j = random.randint(0,255)
            h = random.randint(0,255)
            l = random.randint(0,255)

            centers[i] = [j,h,l]
            
    # Assigns every pixel a centroid based on euclidean distance
    # Recalculates the centroids based on the average of every pixel in the assignment
    # Checks whether the centroids have moved

    distances = [ 0 for f in range(0,k)]
    reset = [[0,0,0] for f in range(0,k)]
    record = [0 for f in range(0,k)]
    
    while(1):
        comparison = list(centers)
        
        for x in pixels:
            for i in range(0,k):
                distances[i] = math.sqrt(((x[0] - centers[i][0])**2+(x[1] - centers[i][1])**2+(x[2] - centers[i][2])**2))
                if i == k - 1:
                    x[3] = distances.index(min(distances))
                    distances = [ f for f in range(0,k)]
        for x in range(0,k):
            centers[x] = reset[x]
            
        for x in pixels:
            centers[x[3]][0] = centers[x[3]][0] + x[0]
            centers[x[3]][1] = centers[x[3]][1] + x[1]
            centers[x[3]][2] = centers[x[3]][2] + x[2]

            record[x[3]] = record[x[3]] + 1
        for x in range(0,k):
            centers[x][0] = int(round(centers[x][0] / record[x]))
            centers[x][1] = int(round(centers[x][1] / record[x]))
            centers[x][2] = int(round(centers[x][2] / record[x]))
        for x in record:
            x = 0
        if comparison == centers:
            return centers

def hexadecimal(centroids):
   # Prints the hexadecimal value of each cluster centroid (Dominant Color)
    for x in centroids:
        print('#%02x%02x%02x' % tuple(x))

def resize(dirname):
   # Resizes image to allow for faster color sampling
   
   basewidth = 200
   img = Image.open(dirname)
   wpercent = (basewidth / float(img.size[0]))
   hsize = int((float(img.size[1]) * float(wpercent)))
   img = img.resize((basewidth, hsize))
   img.save(dirname) 

   return list(img.getdata())

     
while(1):
    # Allows user to select an image
    # Allows user to select # of clusters 'k'
    
    option = input(" type '1' to continue & anything else to quit")

    if option == 1:
        print("Select the file to find its dominant colors") 
        root = Tkinter.Tk()
        dirname = tkFileDialog.askopenfilename()
        k = 3
        
        pixels = resize(dirname) 
        print(hexadecimal((centroids(default(pixels),k))))
        
    else:
        break
        
    

        
    
