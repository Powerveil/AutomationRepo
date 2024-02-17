import psutil
import re

def get_process_by_port(port):
    # 创建一个集合用于存储已经发现的进程ID
    found_pids = set()

    # 创建一个列表用于存储找到的进程ID
    process_ids = []

    for conn in psutil.net_connections(kind='inet'):
        if conn.laddr.port == port:
            pid = conn.pid
            # 如果当前进程ID已经在集合中，则跳过
            if pid in found_pids:
                continue
            found_pids.add(pid)
            try:
                process = psutil.Process(pid)
                process_info = {"pid": process.pid, "name": process.name()}
                process_ids.append(process_info)
            except psutil.NoSuchProcess:
                process_info = {"pid": pid, "name": "未知"}
                process_ids.append(process_info)
    return process_ids


def is_positive_integer(str):
    # 使用正则表达式判断字符串是否是大于零的整数
    return bool(re.match(r'^[1-9]\d*$', str))

def kill_processes(processes):
    if not processes:
        print("未找到该端口的进程")
        return

    for index, process in enumerate(processes):
        print("索引: {}, 进程ID: {}, 进程名称: {}".format(
            index + 1, process["pid"], process["name"]))

    while True:
        flagStr = str(input("是否删除该进程(Y/N，删除下标（默认第一个）。[Y 1]或[1])"))
        # print("flagStr:" + flagStr)

        index = 0
        if is_positive_integer(flagStr[0]):
            flag = 'Y'
            index = int(flagStr[0]) - 1
        else:
            flag = flagStr[0].upper()
            if len(flagStr) == 3:
                index = int(flagStr[2]) - 1

        if flag == 'Y':
            process = processes[index]
            psutil.Process(process["pid"]).terminate()
            print("您已经删除了该进程！！！")
            print("已删除进程信息==>索引: {}, 进程ID: {}, 进程名称: {}".format(
                index + 1, process["pid"], process["name"]))
            break
        elif flag == 'N':
            print("您取消了删除进程")
            break
        else:
            print("是否删除该进程(Y/N，删除下标（默认第一个）。[Y 1]或[1])")


def main():
    while True:
        input_info = input("请输入端口号（输入N退出）：")
        if is_positive_integer(input_info):
            port_number = int(input_info)
            processes = get_process_by_port(port_number)
            kill_processes(processes)
        elif input_info.upper() == 'N':
            exit()
        else:
            print("请输入正确的端口号")
            continue



if __name__ == '__main__':
    main()