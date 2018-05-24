def read_txt(path):
    L = []
    # L = [["[OTO]EV-01按摩椅家用全身腰部靠垫多功能全自动太空舱沙发椅老人", "1"], ["我爱我家", "2"]]
    with open(path, encoding="utf-8") as f:
        for line in f:
            # 去除行中的换行符
            l1 = line.replace("\n", "")
            l2 = l1.split("|")
            L.append(l2)
    return L[1:]


def read_csv():
    pass
