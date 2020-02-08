# -*- coding: utf
#משימה ראשונה-הכפלת מטריצות
  import numpy as np

def mul_of_2d_arrys():
    arry1=np.array([[3,7],[9,3],[2,3]]) # הגדרת מערך
    arry2=np.array([[0,5,8],[0,5,2]]) # הגדרת מערך
    arry3=np.zeros((a.shape[0],b.shape[1]), dtype=int) # הגדרת מערך ריק שיורכב מ2 המערכים הראשונים שהוגדרו
    sizeofarr=arry3.shape #  מייצג את גודל המערך השלישי
    for row in range(size[0]): # חוזר כמספר השורות
        for tor in range(size[1]): # חוזר כמספר הטורים
            for mul in range(arry1.shape[1]):
                arry3[row][tor] += arry1[row][mul]*arry2[mul][tor] # הכפלת כל איבר במטריצה הראשונה והשנייה והוספתה למטריצה השלישית
    print (arry3)
if __name__ == "__main__":
