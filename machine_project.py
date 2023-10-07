import numpy as np

def SOM():
    output_number = int(input("Enter the number of output values: "))

    vectors_com = int(input("Enter the vectors com: "))
    vectors_number = int(input("Enter the vectors number: "))

    vectors = []
    for i in range(vectors_number):
        vector = []
        print(f"Enter values for vector {i+1} (consisting of {vectors_com} values):")
        for j in range(vectors_com):
            value = float(input(f"Enter value {j+1}: "))
            vector.append(value)
        vectors.append(vector)

    generate_random_matrix = input("Generate random matrix? (yes/no): ").lower()

    if generate_random_matrix == "yes":
        matrix = np.random.rand(vectors_com, output_number)
    else:
        matrix = []
        for i in range(vectors_com):
            row = []
            print(f"Enter values for matrix row {i+1} (consisting of {output_number} values):")
            for j in range(output_number):
                value = float(input(f"Enter value {j+1}: "))
                row.append(value)
            matrix.append(row)
        matrix = np.array(matrix)

    outputs = []
    winners = [] 
    learning_rate = 0.5 

    for vector in vectors:
        output = []
        for j in range(output_number):
            value = 0 
            for i in range(vectors_com):
                value += ((matrix[i][j] - vector[i]) ** 2)
            output.append(value)
        outputs.append(output)
        winner_index = output.index(min(output))
        winners.append(winner_index)

    neighborhood_size = 1 

    for i, winner_index in enumerate(winners):
        for j in range(-neighborhood_size, neighborhood_size + 1):
            if j != 0 and 0 <= winner_index + j < output_number:
                neighbor_column = matrix[:, winner_index + j]  # Extract the neighbor column
                for k in range(vectors_com):
                    matrix[k, winner_index + j] += learning_rate * (vectors[i][k] - matrix[k, winner_index + j])

        print("\nUpdated Matrix:")
        print(matrix)


def calculate_distance_k_mean(p1, p2):
    return ((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2) ** 0.5


def calculate_equation_max_net(inhibitory, signals):
    new_list = []
    for i, num in enumerate(signals):
        sum_except_current = sum(signals[:i] + signals[i+1:])
        result = num - inhibitory * sum_except_current
        if result<0:
            result =0
        new_list.append(result)
    return new_list

def max_net():
    num_signals = int(input("Enter the number of signals: "))
    signals = []
    for _ in range(num_signals):
        x = float(input(f"Enter the signal {_+1}: "))
        signals.append(x)
    
    inhibitory = float(input("Enter the inhibitory weight: "))
    
    while True:
        results = calculate_equation_max_net(inhibitory, signals)
        print(f"Results iteration: {results}")
        signals= results
        nonzero_count = sum(1 for result in results if result != 0)
        if nonzero_count == 1:
            winner_index = results.index(next(result for result in results if result != 0))
            print(f"signal {winner_index + 1} is the winner!")
            break


def k_mean():
    num_points = int(input("Enter the number of points: "))
    points = []
    for _ in range(num_points):
        x, y = map(float, input("Enter x and y coordinates (separated by a space): ").split())
        points.append((x, y))

    num_m_points = int(input("Enter the number of reference points (m): "))
    m_points = []
    for _ in range(num_m_points):
        x, y = map(float, input(f"Enter x and y coordinates for m point {len(m_points) + 1} (separated by a space): ").split())
        m_points.append((x, y))

    print("m points:", m_points)

    closer_to_m = [[] for _ in range(num_m_points)]

    for point in points:
        distances = [calculate_distance_k_mean(m_point, point) for m_point in m_points]
        closest_index = distances.index(min(distances))
        closer_to_m[closest_index].append(point)

    new_m_points = []
    new_closer_to_m = [[] for _ in range(num_m_points)]

    for point_list in closer_to_m:
        new_m_x = sum(point[0] for point in point_list) / len(point_list)
        new_m_y = sum(point[1] for point in point_list) / len(point_list)
        new_m_points.append((new_m_x, new_m_y))

    for point in points:
        distances = [calculate_distance_k_mean(new_m_point, point) for new_m_point in new_m_points]
        closest_index = distances.index(min(distances))
        new_closer_to_m[closest_index].append(point)

    same_closer_points = [old_list == new_list for old_list, new_list in zip(closer_to_m, new_closer_to_m)]

    for i, (old_ref, new_ref, same) in enumerate(zip(m_points, new_m_points, same_closer_points)):
        print(f"Old m  {i + 1}: {old_ref}")
        print(f"New m  {i + 1}: {new_ref}")
        print(f"Points closer to old m  {i + 1}: {closer_to_m[i]}")
        print(f"Points closer to new m  {i + 1}: {new_closer_to_m[i]}")
        print(f"Are points closer to old and new m  {i + 1} the same? {'Yes' if same else 'No'}\n")

    for i, (old_list, new_list) in enumerate(zip(closer_to_m, new_closer_to_m)):
        print(f"Number of smallest  in old m point {i + 1}: {len(old_list)}")
        print(f"Number of smallest  in new m point {i + 1}: {len(new_list)}")

def SCN ():
    output_number = int(input("Enter the number of output values: "))

    vectors_com = int(input("Enter the vectors com: "))
    vectors_number = int(input("Enter the vectors number: "))

    vectors = []
    for i in range(vectors_number):
        vector = []
        print(f"Enter values for vector {i+1} (consisting of {vectors_com} values):")
        for j in range(vectors_com):
            value = float(input(f"Enter value {j+1}: "))
            vector.append(value)
        vectors.append(vector)

    generate_random_matrix = input("Generate random matrix? (yes/no): ").lower()

    if generate_random_matrix == "yes":
        matrix = np.random.rand(vectors_com, output_number)
    else:
        matrix = []
        for i in range(vectors_com):
            row = []
            print(f"Enter values for matrix row {i+1} (consisting of {output_number} values):")
            for j in range(output_number):
                value = float(input(f"Enter value {j+1}: "))
                row.append(value)
            matrix.append(row)
        matrix = np.array(matrix)

    outputs = []
    winners = []  

    learning_rate = 0.5  

    for vector in vectors:
        output = []
        for j in range(output_number):
            value = 0  
            for i in range(vectors_com):
                value += ((matrix[i][j] - vector[i]) ** 2)
            output.append(value)
        outputs.append(output)
        winner_index = output.index(min(output))
        winners.append(winner_index)

    for i, vector in enumerate(vectors):
        print(f"Vector {i+1}: {vector} -> Output: {outputs[i]}, Winner Output: {outputs[i][winners[i]]}")

    for i, winner_index in enumerate(winners):
        winner_column = matrix[:, winner_index]  
        for j in range(vectors_com):
            matrix[j, winner_index] += learning_rate * (vectors[i][j] - matrix[j, winner_index])
            

    print("\nUpdated Matrix:")
    print(matrix)

if __name__ == "__main__":
    while True:
        print("Select an algorithm:")
        print("1. K-Means")
        print("2. MaxNet")
        print("3. SOM")
        print("4. SCN")

        choice = input("Enter your choice (1 OR 2 OR 3 OR 4): ")

        if choice == '1':
            k_mean()
            break
        elif choice == '2':
            max_net()
            break
        elif choice == '3':
            SOM()
            break
        elif choice == '4':
            SCN()
            break
        else:
            print("Invalid choice. Please enter '1' for K-Means or '2' for MaxNet. or '3' for SOM. or '4' for SCN  ")