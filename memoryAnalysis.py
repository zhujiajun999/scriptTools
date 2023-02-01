import re
import matplotlib.pyplot as plt

LOG_LIST = ["WCKB_20220722.xlog.log"]  # 要解析的日志文件
TOPNUM = 40   # 指定返回内存最高的前N个log
MORENUM = 40  # 指定返回内存大于N的所有log


def main():
    for i in LOG_LIST:
        # 逐行读取log文件，筛选出[I]开头的
        logs = filterLog(i)
        # 获取所有log的时间戳和消耗内存 存至列表，[2022-07-05 +80 11:28:26.003, 50.36]，并去重
        msgItemList = getAllMsgItemUnique(logs)
        # 获取内存最高的前N个log
        topN = getTopN(TOPNUM, msgItemList)
        # 获取内存大于N的所有log
        moreList = getMoreThanN(MORENUM, msgItemList)
        # 输出文件的名字
        topNPath = "topN-"+i+".txt"
        morePath = "moreList-"+i+".txt"
        figPath = "fig-"+i+".png"

        print("------- TopN --------")
        printList(topN)
        writeList(topNPath, topN)
        print("------- Memory more than N -------")
        printList(moreList)
        writeList(morePath, moreList)
        outputFig(figPath, msgItemList)
        print("------- 文件输出 -------")
        print("内存消耗前N个 输出至：topN-xxx.txt")
        print("内存大于N的所有 输出至：moreList-xxx.txt")
        print("折线图 输出至：fig-xxx.png")


def filterLog(path):
    # 逐行读取log文件，过滤出[I]开头的日志，以列表返回
    logs = []
    file = open(path, "r")
    lines = file.readlines()
    msg = []
    flag = 0
    for l in lines:
        line = l.rstrip()
        # print("line:", line)
        if line.startswith("[I]"):
            if re.match('.*mem = [0-9\.]*[a-zA-Z]$', line) != None:
                logs.append(line[3:])
                print(line[3:])
            else:
                msg.append(line)
                flag = 1
        else:
            if flag == 1:
                if re.match('.*mem = [0-9\.]*[a-zA-Z]$', line) == None:
                    msg.append(line)
                else:
                    msg.append(line)
                    logs.append("".join(msg)[3:])
                    print("".join(msg)[3:])
                    flag = 0
                    msg = []
        # print("msg:", msg)
        # print("flag", flag)
        # print("logs", logs)
        # print("\n")
    file.close()
    return logs


def getMsgItem(log):
    # 将一行log的时间戳和内存提取出来
    time = log.split("[")[1][:-1]
    mem = float(log.split(" ")[-1][:-1])
    return [time[15:27], mem]


def getTopN(N, logList):
    # 获取内存消耗前N条log
    topN = sorted(logList, key=lambda k: k[1], reverse=True)
    topN = topN[:N]
    # topN = sorted(topN, key=lambda k:k[0], reverse=False)  # 按时间排序
    return topN


def getMoreThanN(N, logList):
    # 获取内存消耗大于等于N的log
    moreList = []
    for l in logList:
        if l[1] >= N:
            moreList.append(l)
    return moreList


def getAllMsgItemUnique(logs):
    msgItemList = []
    for log in logs:
        msgItem = getMsgItem(log)
        # 去除时间戳和占用内存都一样的msg
        if msgItem not in msgItemList:
            msgItemList.append(msgItem)
    return msgItemList


def printList(alist):
    for i in alist:
        print(i)


def writeList(path, msgItemList):
    with open(path, 'w') as file:
        for i in msgItemList:
            file.write(i[0])
            file.write("  ")
            file.write(str(i[1]))
            file.write("M")
            file.write("\n")


def outputFig(figPath, msgItemList):
    x = [i[0] for i in msgItemList]
    y = [i[1] for i in msgItemList]
    plt.figure(figsize=(20, 8), dpi=90)
    plt.plot(x, y)
    plt.savefig(figPath)


if __name__ == "__main__":
    main()
