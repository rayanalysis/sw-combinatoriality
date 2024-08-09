import matplotlib.pyplot as plt


# Function to parse a single row of data
def parse_list(data):
    # Ensure the row has the expected length
    if len(data) < 32:
        raise ValueError(f"Row length is less than expected: {len(data)}")
    
    return {
        "REC": data[0],
        "nClicks": int(data[1]),
        "Duration": float(data[2]),
        "ICI": [float(data[i]) for i in range(3, 3 + int(data[1])) if data[i] != '0'],  # Inter Click Intervals
        "Whale": int(data[31]),
        "TsTo": float(data[32])
    }

# Function to parse the entire dataset
def parse_dataset(dataset):
    parsed_data = []
    for row in dataset:
        try:
            parsed_data.append(parse_list(row))
        except ValueError as e:
            print(f"Skipping row due to error: {e}")
    return parsed_data

# Function to plot trends from the dataset
def plot_trends(dataset):
    parsed_data = parse_dataset(dataset)
    
    # Prepare data for plotting
    timestamps = [data["TsTo"] for data in parsed_data]
    click_counts = [data["nClicks"] for data in parsed_data]
    durations = [data["Duration"] for data in parsed_data]
    whales = [data["Whale"] for data in parsed_data]
    all_ici = [ici for data in parsed_data for ici in data["ICI"]]

    # Plot click counts over time
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 2, 1)
    plt.plot(timestamps, click_counts, marker='o')
    plt.xlabel('Timestamp')
    plt.ylabel('Number of Clicks')
    plt.title('Number of Clicks Over Time')

    # Plot duration of recordings over time
    plt.subplot(2, 2, 2)
    plt.plot(timestamps, durations, marker='o', color='orange')
    plt.xlabel('Timestamp')
    plt.ylabel('Duration (seconds)')
    plt.title('Duration of Recordings Over Time')

    # Plot histogram of inter-click intervals (ICI)
    plt.subplot(2, 2, 3)
    plt.hist(all_ici, bins=30, color='green')
    plt.xlabel('Inter-Click Interval (seconds)')
    plt.ylabel('Frequency')
    plt.title('Distribution of Inter-Click Intervals')

    # Plot whale activity over time (with different colors for each whale)
    plt.subplot(2, 2, 4)
    unique_whales = list(set(whales))
    # print(whales)
    # print(unique_whales)
    for whale in unique_whales:
        whale_timestamps = [timestamps[i] for i in range(len(timestamps)) if whales[i] == whale]
        whale_click_counts = [click_counts[i] for i in range(len(click_counts)) if whales[i] == whale]
        plt.scatter(whale_timestamps, whale_click_counts, label=f'Whale {whale}', alpha=0.7)
    plt.xlabel('Timestamp')
    plt.ylabel('Number of Clicks')
    plt.title('Whale Activity Over Time')
    plt.legend()

    plt.tight_layout()
    plt.show()

# Example dataset
sw061b003_dataset = []

# Open a particular pre-grouped audio recording data file
with open('sw061b003.txt') as whale_expressions_data:
    whale_data = whale_expressions_data.read()
    # print(whale_data)
    whale_recordings_list = []
    previous_filename = ''
    line_counter = 0
    filegroup_holder = []

    for line in whale_data.split('\n'):
        line_counter += 1
        sub_list = line.split(' ')
        whale_recordings_list.append(sub_list)
        filegroup_holder = []
        
        # print(previous_filename)
        previous_filename = sub_list[0]
        
    whale_expressions_data.close()
    # print(whale_recordings_list)
    sw061b003_dataset = whale_recordings_list

# Plot trends for the dataset
plot_trends(sw061b003_dataset)
