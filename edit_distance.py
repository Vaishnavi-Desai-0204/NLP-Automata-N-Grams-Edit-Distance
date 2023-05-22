def calc_min_edit_dist(source, target):
    m = len(source)
    n = len(target)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i

    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if source[i - 1] == target[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + 2)

    return dp[m][n]

def align(s1, s2):
    m = len(s1)
    n = len(s2)
    # Initialize the matrix
    D = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        D[i][0] = i
    for j in range(1, n+1):
        D[0][j] = j
    # Initialize the backtrace matrix
    B = [[None for j in range(n+1)] for i in range(m+1)]
    # Fill in the matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                D[i][j] = D[i-1][j-1]
                B[i][j] = 'MATCH'
            else:
                insert = D[i][j-1] + 1
                delete = D[i-1][j] + 1
                substitute = D[i-1][j-1] + 1
                min_val = min(insert, delete, substitute)
                D[i][j] = min_val
                if min_val == insert:
                    B[i][j] = 'INSERT'
                elif min_val == delete:
                    B[i][j] = 'DELETE'
                else:
                    B[i][j] = 'SUBSTITUTE'
    # Backtrace
    i = m
    j = n
    source_alignment = []
    target_alignment = []
    operations = []
    while i > 0 or j > 0:
        if B[i][j] == 'MATCH':
            source_alignment.append(s1[i-1])
            target_alignment.append(s2[j-1])
            i -= 1
            j -= 1
            operations.append('x')
        elif B[i][j] == 'INSERT':
            target_alignment.append(s2[j-1])
            source_alignment.append('*')
            j -= 1
            operations.append('i')
        elif B[i][j] == 'DELETE':
            source_alignment.append(s1[i-1])
            target_alignment.append('*')
            i -= 1
            operations.append('d')
        else:
            source_alignment.append(s1[i-1])
            target_alignment.append(s2[j-1])
            i -= 1
            j -= 1
            operations.append('s')
    # Reverse the lists to get them in the correct order
    source_alignment.reverse()
    target_alignment.reverse()
    operations.reverse()
    return source_alignment, target_alignment, operations



