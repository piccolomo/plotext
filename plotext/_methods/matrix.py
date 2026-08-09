# Utilities to join and compose matrix instances into larger matrices

from plotext._primitives.matrix import matrix


# Join a grid of matrices into a single matrix
def join_matrices(matrices):
    if not matrices or not matrices[0]:
        return matrix(0, 0)

    rows, cols = len(matrices), len(matrices[0])
    widths = [m.width() for m in matrices[0]]
    heights = [matrices[r][0].height() for r in range(rows)]

    total_width = sum(widths)
    total_height = sum(heights)
    M = matrix(total_width, total_height)

    for r in range(rows):
        y_offset = sum(heights[:r])
        for c in range(cols):
            x_offset = sum(widths[:c])
            M._insert_matrix(x_offset, y_offset, matrices[r][c])

    return M