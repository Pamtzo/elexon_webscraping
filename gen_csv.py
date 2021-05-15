import os

step = 1
dataset = os.listdir("dataset/")
output = open("file.csv", 'w+')

for file in dataset:
    if file.endswith(".csv"):
        print("STEP:",step,"OF",len(dataset))
        data = open(os.path.join("dataset/", file), 'r')
        lines = data.readlines()
        data.close()

        del lines[0]
        del lines[-1]

        for line in lines:
            output.write(line)
        step += 1

output.close()