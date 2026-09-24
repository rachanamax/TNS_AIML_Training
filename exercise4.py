import numpy as np


# ---- THE DATA ----

student_names = np.array([
    "Aisha",
    "Ben",
    "Carla",
    "Dev",
    "Eli",
    "Farah"
])

subject_names = np.array([
    "Maths",
    "Physics",
    "English"
])

scores = np.array([
    [78, 65, 82],    # Aisha's marks
    [55, 71, 60],    # Ben's marks
    [91, 88, 79],    # Carla's marks
    [42, 38, 55],    # Dev's marks
    [67, 74, 71],    # Eli's marks
    [83, 97, 68]     # Farah's marks
])


# Print the complete score table
print(scores)

# Print the shape of the array
print("shape:", scores.shape)
