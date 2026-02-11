def solution(record):
    logs = []
    uid_nickname_dict = {}
    result = []
    for log in record:
        splited_log = log.split(" ")
        #enter
        if splited_log[0] == "Enter":
            uid, nick_name = splited_log[1], splited_log[2]
            logs.append(("E", uid))
            uid_nickname_dict[uid]=nick_name
        #leave
        elif splited_log[0] == "Leave":
            uid = splited_log[1]
            logs.append(("L", uid))
        #Change
        else:
            uid, nick_name = splited_log[1], splited_log[2]
            uid_nickname_dict[uid]=nick_name

    for log in logs:
        action, uid = log
        if action == "E":
            result.append(f"{uid_nickname_dict[uid]}님이 들어왔습니다.")
        if action == "L":
            result.append(f"{uid_nickname_dict[uid]}님이 나갔습니다.")
    return result