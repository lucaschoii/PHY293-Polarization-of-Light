import os

def process_data(directory, filename, x_uncertainty=0, y_uncertainty=0, window=0):


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
    data.sort(key=lambda pair: pair[0])
    current_window_start = data[0][0]
    window_results = []

    while current_window_start <= data[-1][0]:
    # Define the window range
        window_end = current_window_start + window
        
        # Filter points in the current window
        window_points = [y for x, y in data if current_window_start <= x < window_end]
        
        if window_points:  # Only compute if there are points in the window
            max_y = max(window_points)
            window_results.append((current_window_start, max_y))
    
        current_window_start += window

    new_filename = f'{directory}/processed/'

    if not os.path.exists(new_filename): 
      
        # if the demo_folder directory is not present  
        # then create it. 
        os.makedirs(new_filename) 


    with open(f'{directory}/processed/{filename}', 'w') as f:
        f.write('x\ty\tdx\tdy\n')
        for i in range(len(window_results)):
            f.write(f'{window_results[i][0]:.5f}\t{window_results[i][1]:.5f} \t{x_uncertainty:.6f}\t{y_uncertainty:.6f}')
            if i != len(data) - 1:
                f.write('\n')



process_data('data/3', 'horizontal_polarizer.txt', 0.000005, 0.000005, 0.001)
process_data('data/3', 'vertical_polarizer.txt', 0.000005, 0.000005, 0.05)
process_data('data/3', 'no_polarizer.txt', 0.000005, 0.000005, 0.4)
