def entering_pair_nums(n):
    for i in range(n):
        pair_nums = list(map(int, input().split()))
        yield i + 1, pair_nums


def cnt_pref_sum(arr, n):
    arr_pref_sum = [0]

    for i in range(1, n):
        t, arr_t = arr[i]
        dif = arr_t[1] - arr[i-1][1][1]

        if dif > 0:
            arr_pref_sum.append(arr_pref_sum[i-1] + dif)

        else:
            arr_pref_sum.append(arr_pref_sum[i-1])

    return arr_pref_sum

def cnt_sum_height(arr, m, pref_sum):
    for i in range(0, m):
        begin = arr[i][1][0] - 1
        end = arr[i][1][1] - 1

        print(abs(pref_sum[end] - pref_sum[begin]))


def main():
    n = int(input())
    data_peaks = list(entering_pair_nums(n))
    print(data_peaks)

    m = int(input())
    data_tracks = list(entering_pair_nums(m))
    print(data_tracks)

    arr_pref_sum = cnt_pref_sum(data_peaks, n)
    print(arr_pref_sum)

    cnt_sum_height(data_tracks, m, arr_pref_sum)


if __name__ == '__main__':
    main()