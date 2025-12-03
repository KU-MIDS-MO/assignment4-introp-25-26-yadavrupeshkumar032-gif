import numpy as np

def mask_and_classify_scores(arr):
   if len(arr) < 4:
        return None

   n=len(arr)

   for i in range(n):
        if len(arr[i]) != n:
            return None

   cleaned = arr.copy()

   for i in range(n):
        for j in range(n):
            if cleaned[i][j] < 0:
                cleaned[i][j] = 0

            if cleaned[i][j] > 100:
                cleaned[i][j] = 100

   levels = np.zeros((n,n), dtype=int)

   for i in range(n):
        for j in range(n):
            value = cleaned[i][j]

            if value < 40:
                levels[i][j] = 0

            if value >= 40 and value < 70:
                levels[i][j] = 1

            if value >= 70:
                levels[i][j] = 2

   row_pass_counts = np.zeros(n, dtype=int)

   for i in range(n):
        count = 0
        for j in range(n):
            if cleaned[i][j] >= 50:
                count = count + 1
        row_pass_counts[i] = count

   return cleaned, levels, row_pass_counts
