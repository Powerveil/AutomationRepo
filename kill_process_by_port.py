import psutil


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


port_number = int(input("请输入端口号："))
processes = get_process_by_port(port_number)

if not processes:
    print("未找到该端口的进程")
    exit()

process = processes[0]
print("进程ID: {}, 进程名称: {}\n".format(process["pid"], process["name"]))


while True:
    flagStr = str(input("是否删除该进程(Y/N，默认删除第一个)")).upper()
    # print("flagStr:" + flagStr)

    if flagStr == 'Y':
        psutil.Process(process["pid"]).terminate()
        print("您已经删除了该进程！！！")
        break
    elif flagStr == 'N':
        print("您取消了删除该进程")
        break
    else:
        print("请输入Y或N")
