from dataclasses import dataclass
@dataclass
class data:
    job:str
    profit:int
    deadline:int
array=[['j1',250,2],
       ['j2',150,1],
       ['j3',200,1],
       ['j4',50,2 ],
       ['j5',100,1]]
print("The data required for job sequence: ")
for i in array:
    print(i)
