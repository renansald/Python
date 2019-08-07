from sys import exit

file = "EuclidesMDC.mif"
file2 = "euclidesMDC.mif"
pFile = open(file, "r");
pFile2 = open(file2, "r");
line1 = pFile.readline();
line2 = pFile2.readline();
print(line1)
while line1:
    print("while")
    if(line1 != line2):
        print("ERROO");
        print(line1);
        exit();
    line1 = pFile.readline();
    line2 = pFile2.readline();
print("Sucesso");
