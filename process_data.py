import os

def process_data(directory, filename, x_uncertainty=0, y_uncertainty=0):

    data = []
    with open(f'{directory}/{filename}', "r") as file:
        for line in file:
            parts = line.strip().split()
            try:
                # Attempt to convert both parts to floats
                position, intensity = map(float, parts[:2])
                data.append((position, intensity))
            except ValueError:
                # If conversion fails, skip this line as it's likely part of the header
                continue


    # write data to a file


    new_filename = f'{directory}/processed/'

    if not os.path.exists(new_filename): 
      
        # if the demo_folder directory is not present  
        # then create it. 
        os.makedirs(new_filename) 


    if '1' in directory:

        with open(f'{directory}/processed/{filename}', 'w') as f:
            f.write('x\ty\tdx\tdy\n')
            for i in range(len(data)):
                
                if data[i][0] >= -0.000005:
                    f.write(f'{data[i][0]:.5f}\t{data[i][1]:.5f} \t{x_uncertainty:.6f}\t{y_uncertainty:.6f}')
                    if i != len(data) - 1:
                        f.write('\n')
    else:
        with open(f'{directory}/processed/{filename}', 'w') as f:
            f.write('x\ty\tdx\tdy\n')
            for i in range(len(data)):
                f.write(f'{data[i][0]:.5f}\t{data[i][1]:.5f} \t{x_uncertainty:.6f}\t{y_uncertainty:.6f}')
                if i != len(data) - 1:
                    f.write('\n')



process_data('exercise_data_1', 'x.txt', 0.000005, 0.000005)
process_data('exercise_data_1', 'cosx.txt', 0.000005, 0.000005)
process_data('exercise_data_1', 'cos2x.txt', 0.000005, 0.000005)
process_data('exercise_data_1', 'cos2_2x.txt', 0.000005, 0.000005)

process_data('exercise_data_2', 'x.txt', 0.000005, 0.000005)
process_data('exercise_data_2', 'cosx.txt', 0.000005, 0.000005)
process_data('exercise_data_2', 'cos2x.txt', 0.000005, 0.000005)
process_data('exercise_data_2', 'cos2_2x.txt', 0.000005, 0.000005)

