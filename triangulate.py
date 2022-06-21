#proof of concept triangulation algorithm

def main():

    polygon = [(5, 3), (12, 3), (10, 5), (10, 8), (12, 10), (5, 10), (7, 8), (7, 5), (5, 5)]
    triangles = triangulate(polygon)

    centroids = []
    areas = []
    for i in triangles:
        centroid = [(i[0][0]+i[1][0]+i[2][0])/3 , (i[0][1]+i[1][1]+i[2][1])/3]
        #Ax(By - Cy) + Bx(Cy - Ay) + Cx(Ay - By) / 2
        centroids.append(centroid)

        area = abs((i[0][0] * (i[1][1] - i[2][1]) + i[1][0] * (i[2][1] - i[0][1]) + i[2][0] * (i[0][1] - i[1][1])) / 2)
        areas.append(area)

    whole = sum(areas)
    for i in range(len(centroids)):
        centroids[i][0] *= areas[i]
        centroids[i][1] *= areas[i]
    
    sum_xy = list(map(sum, zip(*centroids)))

    sumX = sum_xy[0]/whole
    sumY = sum_xy[1]/whole

    print(sumX, sumY)
    return 0


def triangulate(cords):
    import math

    triangles = []
    counter = 0
    while 3 < len(cords)-1:
        if counter-1 == -1:
            indexA = len(cords)-1
        else:
            indexA = counter-1
        indexB = counter
        indexC = (counter+1)%len(cords)
        
        current = cords[indexB]
        leftCor = cords[indexA]
        rightCor = cords[indexC]

        vectorA = (current[0]-leftCor[0], current[1]-leftCor[1])
        vectorB = (rightCor[0]-current[0], rightCor[1]-current[1])

        if (vectorA[0]) * (vectorB[1]) - (vectorB[0]) * (vectorA[1]) > 0:
            vectorC = (leftCor[0]-rightCor[0], leftCor[1]-rightCor[1])

            for i in range(0, len(cords)):
                if i == indexA or i == indexB or i == indexC:
                    continue
                else:
                    
                    vectorX = (cords[i][0]-rightCor[0], cords[i][1]-rightCor[1])
                    vectorXLen = math.sqrt(math.pow(vectorX[0], 2) + math.pow(vectorX[1], 2))
                    vectorXAngle = abs(math.asin(vectorX[1]/math.sqrt(math.pow(vectorX[0], 2)+math.pow(vectorX[1], 2))))

                    vectorCLen = math.sqrt(math.pow(vectorC[0], 2) + math.pow(vectorC[1], 2))
                    vectorCAngle = abs(math.asin(vectorC[1]/math.sqrt(math.pow(vectorC[0], 2)+math.pow(vectorC[1], 2))))


                    if vectorXLen < vectorCLen and vectorXAngle < vectorCAngle:
                        break
                    triangles.append((leftCor, current, rightCor))
                    cords.pop(counter)
                    counter = 0
                    
                    break
        counter += 1

    triangles.append((cords[0], cords[1], cords[2]))
    return triangles

if __name__ == "__main__":
    main()
     