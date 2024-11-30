from aima.search import *
from positions_properties import *
import random

pos = POSITIONS
man_pos = MANDATORY_POSITIONS

""" 
state:  (current position,
        number of moves, 
        time to arrive at current position, 
        list of previous positions) 
"""

# Defining the choreography planning problem, inheriting from the Problem class.
class Choreography(Problem):  

    def __init__(self, initial, goal):
        """
        Initializing the problem with the initial and goal states.
        - `initial`: The starting state as a tuple (position, counter, time, moves).
        - `goal`: The desired state as a tuple (position, counter, time, moves).
        Converts `moves` to tuples to ensure immutability.
        """
        self.initial = (initial[0], 
                        initial[1],
                        initial[2], 
                        tuple(initial[-1], ))
        self.goal = (goal[0], 
                     goal[1], 
                     goal[2], 
                     tuple(goal[-1]))
        
        Problem.__init__(self, initial, goal)

    def is_valid(self, state):
        """
        Checks if a state is valid.
        - `time` must be less than the goal time.
        - The goal position must not already be in the `moves`.
        - The position must not be in the last 12 moves of `planned_choreography`.
        """
        position, counter, time, moves = state
        return (time < self.goal[2] and 
                self.goal[0] not in moves and 
                position not in planned_choreography[-1:-13:-1])

    def actions(self, state):
        """
        Generates possible actions from the current state.
        - If the state is invalid, return no actions (`[]`).
        - For 'Sit' or 'SitRelax' positions we prioritize standing up.
        - Otherwise, return all valid transitions.
        """
        if not self.is_valid(state):
            return []

        l = list(pos.keys())  # Gets possible positions
        random.shuffle(l)  # Shuffles to introduce randomness

        position, counter, time, moves = state

        if position == 'Sit' or position == 'SitRelax':
            # Defines possible standing positions from seated positions
            stand_up_positions = ['DiagonalRight', 'DiagonalLeft', 'MoveForward', 'MoveBackward']
            random.shuffle(stand_up_positions)

            # Finds the next standing position that is not recently used
            i = 0
            next_position = 'MoveForward'  # Default fallback
            while i < len(stand_up_positions):
                if stand_up_positions[i] not in planned_choreography:
                    next_position = stand_up_positions[i]
                    break
                i += 1
            
            # Action: moves from current to next position
            return [(position, next_position)]  

        # General case: Adds all valid positions not in moves
        result = [(position, next_position)
                  for next_position in l if next_position not in moves]
        result.append((position, self.goal[0]))  # Always includes action to goal
        return result

    def result(self, state, action):
        """
        Defines the result of applying the action to the current state.
        - Updating position, counter, time, and moves based on the action performed.
        """
        position, counter, time, moves = state
        next_position = action[-1]  # Extracts the next position from the action

        # Appends the next position to the moves list
        list_moves = list(moves)
        list_moves.append(next_position)

        # Updates the state based on the type of position
        if next_position in pos.keys():
            return (next_position, 
                    counter + 1, 
                    time + pos[next_position],  # Increments time by the cost of the position
                    tuple(list_moves))
        if next_position in man_pos.keys():
            return (next_position, 
                    counter + 1, 
                    time,  # Mandatory positions do not affect time evaluation
                    tuple(list_moves))

    def goal_test(self, state):
        """
        Checks if the current state satisfies the final goal conditions:
        - The position matches the final goal position.
        - The counter meets or exceeds the required value.
        - The time is within an acceptable range of the goal time.
        """
        position, counter, time, moves = state
        positionGoal, counterGoal, timeGoal, moves = self.goal

        return (position == positionGoal and 
                counter >= counterGoal and 
                (timeGoal - 0.5 <= time <= timeGoal))  # Allows slight time tolerance

# Declaring the exception raised with planning errors
class PlanningException(Exception):
    pass

def generate_plan(start, end, time):
    """
    Creates a Choreography planning problem.
    - `start`: Starting position.
    - `end`: Goal position.
    - `time`: Target time to complete the choreography.
    """
    return Choreography((start, 0, 0, (start, )),  # Initial state
                        (end, 2, time, ()))       # Goal state



def main():
    # initialization of the list of the planned choreography and acquisition of initial and final positions
    global planned_choreography
    planned_choreography = []
    initial_position = 'StandInit'
    final_position = 'Crouch'
    
    # retrieving all the mandatory positions besides the first and the last
    # and subsequently shuffle of the order 
    mandatory_order = list(man_pos)[1:-1]
    random.shuffle(mandatory_order)

    # imposition of the constraint that positions Sit and SitRelax have to be separated at least by another mandatory position
    # if the shuffle produces the list with the aforementioned result a swap occurs with the elements in the near positions  
    # the policy is "push forward the second one, treating the list as a circular array"
    i_s = mandatory_order.index("Sit")
    i_sr = mandatory_order.index("SitRelax")
    n_man_pos = len(mandatory_order)
    if i_s-1 == i_sr:
        mandatory_order[(i_s+1) % n_man_pos], mandatory_order[i_s] = mandatory_order[i_s], mandatory_order[(i_s+1) % n_man_pos]
    elif i_s == i_sr-1:
        mandatory_order[(i_sr+1) % n_man_pos], mandatory_order[i_sr] = mandatory_order[i_sr], mandatory_order[(i_sr+1) % n_man_pos]

    # adding initial and final positions to the mandatory_order list
    mandatory_order.insert(0, initial_position)
    mandatory_order.append(final_position)

    # printing of the order of the list of mandatory moves
    print('\nMANDATORY POSITIONS EXECUTION ORDER')
    print('-'*90)
    print(mandatory_order)
    print('-'*90)

    # times evaluation
    time_budget = 120   # amount of available time, 120 seconds 
    time_mandatory_moves = sum(list(man_pos.values()))
    time_slot = (time_budget - time_mandatory_moves) / (len(list(man_pos)) - 1)

    # start of planning
    print("\nCHOREOGRAPHY GENERATION")

    # cycle of iterative deepening searches between equally timed frames enclosed by mandatory moves
    for i in range(len(mandatory_order) - 1):
        problem = generate_plan(mandatory_order[i], mandatory_order[i+1], time_slot)
        solution = iterative_deepening_search(problem)
        if solution == None:
            raise PlanningException("Empty set of solutions")
        else:
            planned_choreography += solution.state[-1][:-1]

        print('\n-> (' + str(solution.state[3]) + ', ' + str(round(solution.state[2], 2)) + ', ' + str(solution.state[1] - 1) + ')')

    # ending with the goal state
    planned_choreography.append(final_position)

    # exporting the choreography in the file choreography.txt
    with open("../choreography_player/choreography.txt", "w") as file:
        for position in planned_choreography:
            if position == final_position:
                file.write(str(position))
            else:
                file.write(str(position) + '\n')

if __name__ == '__main__':
    main()
