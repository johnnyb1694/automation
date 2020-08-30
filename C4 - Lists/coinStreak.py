import random

num_streaks = 0

for experimentNumber in range(10000):
    # Code that creates a list of 100 'heads' or 'tails' values.
    trial_results = []
    for t in range(100):
        trial_results.append(random.randint(0, 1))

    # Code that checks if there is a streak of 6 heads or tails in a row.
    for slice_start in range(94):

        slice_end = slice_start + 5
        trial_slice = trial_results[slice_start:slice_end]
        if (trial_slice.count(trial_slice[0]) == len(trial_slice)):
            num_streaks = num_streaks + 1
            break

output_message = f'There were {num_streaks} streaks recorded in 10,000 trials.'

print(output_message)
