import numba as nb # Use numba instead


# Compile a Python function into native code
@nb.jit(
    #  func(        paths,             values,            t_ys,            t_xs     )
    nb.void(nb.int32[:, :, ::1], nb.float32[:, :, ::1], nb.int32[::1], nb.int32[::1]),
    nogil = True,
    nopython = True
)


def maximum_path_nb(paths, values, t_ys, t_xs):
    # float max_neg_val = -1e9
    max_neg_val = -1e9
    # int b = paths.shape[0]
    b = paths.shape[0]
    # int i
    # for i in prange(b)
    for i in range(int(b)):
        # int[:,::1] path = paths[i]
        path = paths[i]
        # float[:,::1] value = values[i]
        value = values[i]
        # int t_y = t_ys[i]
        t_y = t_ys[i]
        # int t_x = t_xs[i])
        t_x = t_xs[i]

    # float v_prev
    v_prev = 0.0
    # float v_cur
    v_cur = 0.0
    # int index = t_x - 1
    index = t_x - 1

    for y in range(t_y):
        for x in range(max(0, t_x + y - t_y), min(t_x, y + 1)):
            if x == y:
                v_cur = max_neg_val
            else:
                v_cur = value[y - 1, x]
            if x == 0:
                if y == 0:
                    v_prev = 0.
                else:
                    v_prev = max_neg_val
            else:
                v_prev = value[y - 1, x - 1]
            value[y, x] += max(v_prev, v_cur)

    for y in range(t_y - 1, -1, -1):
        path[y, index] = 1
        if index != 0 and (index == y or value[y - 1, index] < value[y - 1, index - 1]):
            index = index - 1