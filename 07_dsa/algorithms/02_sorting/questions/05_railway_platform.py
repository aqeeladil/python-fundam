# Find the Minimum Number of Platforms Required for a Railway Station
# Given arrival and departure times of trains, find the minimum number of platforms required such that no train has to wait.

def find_min_platforms(arrivals, departures):
    arrivals.sort()
    departures.sort()

    platform_needed, max_platforms = 1, 1
    i, j = 1, 0

    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platform_needed += 1
            i += 1
        else:
            platform_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platform_needed)

    return max_platforms

# Example usage:
arrivals = [900, 940, 950, 1100, 1500, 1800]
departures = [910, 1200, 1120, 1130, 1900, 2000]
print(find_min_platforms(arrivals, departures))  # Output: 3


