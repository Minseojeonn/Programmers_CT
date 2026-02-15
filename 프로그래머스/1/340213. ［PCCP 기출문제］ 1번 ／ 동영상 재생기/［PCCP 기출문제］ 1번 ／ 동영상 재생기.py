def solution(video_len, pos, op_start, op_end, commands):
    
    def compare(pos, target):
        pos_min, pos_sec = pos.split(":")
        target_min, target_sec = target.split(":")
        pos_converted = int(pos_min)* 60 + int(pos_sec) 
        target_converted = int(target_min)* 60  + int(target_sec)        
        return pos_converted - target_converted
    
    def next_func(pos, o_start, o_end):
        if compare(pos, o_start) >= 0 and compare(pos, o_end) <= 0:
            pos = o_end
        
        pos_min, pos_sec = pos.split(":")
        converted = int(pos_min)*60 + int(pos_sec) + 10
        next_pos = f"{converted // 60:02d}:{converted % 60:02d}"
        
        if compare(next_pos, o_start) >= 0 and compare(next_pos, o_end) <= 0:
            return o_end
        else:
            return next_pos
    
    def prev_func(pos, o_start, o_end):
        if compare(pos, o_start) >= 0 and compare(pos, o_end) <= 0:
            pos = o_end
        pos_min, pos_sec = pos.split(":")
        converted = int(pos_min)*60 + int(pos_sec) - 10
        if converted < 0:
            converted = 0
        next_pos = f"{converted // 60:02d}:{converted % 60:02d}"
        if compare(next_pos, o_start) >= 0 and compare(next_pos, o_end) <= 0:
            return o_end
        return next_pos
    
    for command in commands:
        if command == "next":
            pos = next_func(pos, op_start, op_end)
        elif command == "prev":
            pos = prev_func(pos, op_start, op_end)
        else:
            print("something error")
        
        if compare(pos, video_len) >= 0:
            pos = video_len
        
    return pos