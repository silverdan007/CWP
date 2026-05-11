C = 1
S = 2
E = 0
start_state = [C, C, C, E, S, S, S]
goal_state = [S, S, S, E, C, C, C]


def succesor(stable):
    empty_index = stable.index(E)
    #recording e at the present time
    #limiting search to possible moves by creating a new list without the empty index
    possible_positions = [empty_index - 2, 
                          empty_index - 1, 
                          empty_index + 1, 
                          empty_index + 2
                          ]
    
    
    for present_position in possible_positions: #looping through new list to check individual elements
        if 0 <= present_position < len(stable): #ensuring we stay within the availble positions of the state
            piece = stable[present_position]
            if piece == C and present_position < empty_index:    #if cow and immediately left of empty
                if empty_index - present_position == 1:
                    new_state = stable.copy()
                    new_state[empty_index], new_state[present_position] = new_state[present_position], new_state[empty_index]
                    yield new_state
                elif empty_index - present_position == 2 and stable[present_position + 1] == S: #jumping over an S
                    new_state = stable.copy()
                    new_state[empty_index], new_state[present_position] = new_state[present_position], new_state[empty_index]
                    yield new_state
            elif piece == S and present_position > empty_index:
                if present_position - empty_index == 1:
                    new_state = stable.copy()
                    new_state[empty_index], new_state[present_position] = new_state[present_position], new_state[empty_index]
                    yield new_state
                elif present_position - empty_index == 2 and stable[present_position - 1] == C:
                    new_state = stable.copy()
                    new_state[empty_index], new_state[present_position] = new_state[present_position], new_state[empty_index]
                    yield new_state


def solution(stable, depth = 0):
    print("  " * depth + f"Exploring: {stable}")


    if stable == goal_state:
        return stable
    for next_state in succesor(stable):
        print("  " * depth + f"Trying move -> {next_state}")
        result = solution(next_state, depth + 1)
        print(f"depth is {depth}")

        if result is not None:
            return [stable] + result
    print("  " * depth + "Dead end, backtracking...")
    return None

print("thinking")
solve = solution(start_state)
if solve:
    for step in solve:
        print(step)
else:
    print("i'm sorry")



    









# succesor(start_state)