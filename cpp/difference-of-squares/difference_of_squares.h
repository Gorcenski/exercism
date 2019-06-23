#if !defined(SQUARES_H)
#define SQUARES_H
// #define EXERCISM_RUN_ALL_TESTS

#include <math.h>

namespace squares {
    inline int square_of_sum(const int& n)
    {
        // sum_{i=1}^n i = n(n+1) / 2
        return pow(n * (n + 1), 2) / 4;
    }

    inline int sum_of_squares(const int& n)
    {
        // sum_{i=1}^n i = n(n+1)(2n+1) / 6
        return n * (n + 1) * (2 * n + 1) / 6;
    }

    inline int difference(const int& n)
    {
        return square_of_sum(n) - sum_of_squares(n);
    }
}

#endif