def distance(curr_pos, target_pos):
    return abs(curr_pos[0]-target_pos[0])+ abs(curr_pos[1]-target_pos[1])


def solution(numbers, hand):
    pad_pos = { 
            1:(0,0), 2:(0,1), 3:(0,2),
            4:(1,0), 5:(1,1), 6:(1,2),
            7:(2,0), 8:(2,1), 9:(2,2),
            "*":(3,0), 0:(3,1), "#":(3,2)
        }
    result = []
    left_hand_pos = pad_pos["*"]
    right_hand_pos = pad_pos["#"]

    for i in numbers:
        if i in [1,4,7,"*"]:
            result.append("L")
            left_hand_pos = pad_pos[i]
        
        elif i in [3,6,9,"#"]:
            result.append("R")
            right_hand_pos = pad_pos[i]
        
        else:
            left = distance(left_hand_pos, pad_pos[i])
            right = distance(right_hand_pos, pad_pos[i])

            if left == right:
                if hand == "right":
                    result.append("R")
                    right_hand_pos = pad_pos[i]
                else:
                    result.append("L")
                    left_hand_pos = pad_pos[i]

            elif left > right:
                result.append("R")
                right_hand_pos = pad_pos[i]

            elif right > left:
                result.append("L")
                left_hand_pos = pad_pos[i]            
    return "".join(result)

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
solution(numbers, hand)
