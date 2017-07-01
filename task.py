razmer = int(input("Введите число "))

result=[]
for i in range(razmer):
    result.append([0 for j in range(razmer)]) #заполнение массива нулями

currentSide = razmer #текущая сторона
offset = 0; #текущее смещение квадрата
currentNumber = 1; 
    
while offset < (razmer/2.0) :#повторяем, пока не достигнем центра квадрата
        #рисуем правую линию
    for i in range(currentSide):
        result[razmer-1-offset-i][razmer-1-offset]= currentNumber
        currentNumber+=1
            
        #рисуем верхнюю линию
    for i in range(currentSide-1):
        result[offset][razmer-2-offset-i] = currentNumber
        currentNumber+=1 ##все правильно до сюда
        
        #рисуем левую линию
    for i in range(currentSide-2):
        result[1+offset+i][offset] = currentNumber
        currentNumber+=1

        #рисуем нижнюю линию
    if (razmer/2 - offset -1 > 0):
       for i in range(currentSide-1):
            result[razmer-1-offset][offset+i] = currentNumber
            currentNumber+=1
        
    # увеличиваем смещение, уменьшаем текущую сторону
    offset+=1
    currentSide-=2;
            
if(razmer%2==0): # если квадрат четный рисуем центр
    result[int(razmer/2)][int(razmer/2-1)]=razmer**2
#вывод        
for i in range(razmer):
  str = ''
  pb=' '
  for j in range(razmer):
    if(result[i][j]<10000): pb=' '
    if(result[i][j]<1000): pb='  '
    if(result[i][j]<100): pb='   '
    if(result[i][j]<10): pb='    '
    str1+= str(result[i][j]) + pb
  print(str)

    
    
