# Shoelace's formula for calculating polygon's area

def polygonArea(X, Y, n): 
  
    # Initialze area 
    area = 0.0
  
    # Calculate value of shoelace formula 
    j = n - 1
    for i in range(0,n): 
        area += (X[j] + X[i]) * (Y[j] - Y[i]) 
        j = i   # j is previous vertex to i 
      
  
    # Return absolute value 
    return int(abs(area / 2.0))


# (X,Y) : coordinates of polygon's vertices
# n : number of vertices
