import pandas as pd
from dataclasses import dataclass
from math import comb, factorial as fact


def C_vD(v:int, n:int):
    return NEW_C_vD(v, n)

def OLD_C_vD(v:int, n:int):
    header = (v - 1)
    numerator = header * fact(n * v)
    denominator = 1
    for i in range(v): denominator *= fact(n + i)
    quota = numerator // denominator
    return quota

def NEW_C_vD(v:int, n:int):
    header = 1
    for i in range(v): header *= fact(i)
    numerator = header * fact(n * v)
    denominator = 1
    for i in range(v): denominator *= fact(n + i)
    quota = numerator // denominator
    return quota


def exportToExcel(data, file_name:str):
    df = pd.DataFrame(data).T
    df.to_excel(excel_writer = "C:/Users/freahl03/OneDrive - Privat/OneDrive/Dokument/Programering/GyA/" + file_name + ".xlsx")
def exportToTxt(data, file_name:str):
    """Make sure data is a list where each element will be converted to a string on a separete line"""
    data = [str(element) for element in data]
    with open(f"{file_name}.txt", "w") as outfile:
        outfile.write("\n".join(data))
        outfile.close()
@dataclass
class pos:
    x:int
    y:int
    z:int
def total_roads(sizeX:int, sizeY:int, sizeZ:int):
    x, y, z, = sizeX, sizeY, sizeZ
    return comb(x + y + z, x) * comb(y + z, y)
def total_roadsP(dimensions:pos):
    x, y, z = dimensions.x, dimensions.y, dimensions.z
    return total_roads(x, y, z)



def verify_cata3d(path:str):
    dic = {"X": 0, "Y":1, "Z":2}
    sum = [0, 0, 0]
    for c in path:
        sum[dic[c]] += 1
        if sum[0] < sum[1]: return False
        if sum[1] < sum[2]: return False
    return True
def verify_buffer(pathBuffer):
    for path in pathBuffer:
        if not verify_cata3d(path): return False
    return True


def moveOneStepInDimension(dimensionIndex:int, position:list):
    positionCopy = position.copy()
    positionCopy[dimensionIndex] += 1
    return positionCopy

