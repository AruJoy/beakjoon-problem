n = int(input('자료수를 입력하세요.: '))
inputList = []

for i in range(n):
    value = int(input(f'{i+1} 번째 값을 입력하세요.: '))
    inputList.append(value)

listUpList = []

def listUp(a, n):
    global listUpList
    #=============선언조건 명시===========
    if n == 0:
        listUpList.append(a[n])
        return
    listUp(a, n-1)
    #===============탈출 명시 ==========
    if len(a) == len(listUpList):
        return listUpList
    #=============== 진행 명시 =========
    for i in range(len(listUpList)):
        if a[n] >= listUpList[i]:
            listUpList.insert(i,a[n])
            return
    listUpList.append(a[n])

def listUp2(a, n, listUpList):
    #=============선언조건 명시===========
    if n == 0:
        listUpList.append(a[n])
        return
    listUp2(a, n-1, listUpList)  # 재귀 호출: 리스트의 이전 값들을 정렬

    #===============탈출 명시 ==========
    if len(a) == len(listUpList):  # 탈출 조건: 리스트가 정확히 정렬됨
        return listUpList
    
    #=============== 진행 명시 =========
    for i in range(len(listUpList)):  # 진행 조건: 리스트를 순회하며 적절한 위치를 찾음
        if a[n] >= listUpList[i]:
            listUpList.insert(i, a[n])  # 적절한 위치에 값을 삽입하고 함수 종료
            return
    listUpList.append(a[n])  # 삽입할 위치를 찾지 못한 경우, 리스트의 맨 끝에 값을 추가


listUp(inputList, n)
print(listUpList)

listUpList = []
listUp2(inputList, n-1, listUpList)
print(listUpList)