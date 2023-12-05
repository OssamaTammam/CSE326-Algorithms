def activitySelectionIterative(startTimes, finishTimes):
    ans = []

    # Always take the first finishing activity
    ans.append(startTimes[0])

    # Points to the last selected activity
    lastSelectedIndex = 0
    for j in range(1, len(finishTimes)):
        # If the activity starts after the last selected activity finished append it
        if startTimes[j] >= finishTimes[lastSelectedIndex]:
            ans.append(startTimes[j])
            lastSelectedIndex = j

    return ans


startTimes = [1, 3, 0, 5, 8, 5]
finishTimes = [2, 4, 6, 7, 9, 9]

print(
    f"Selected activities start times are {activitySelectionIterative(startTimes, finishTimes)}"
)
