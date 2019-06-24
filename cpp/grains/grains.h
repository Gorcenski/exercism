#if !defined(GRAINS_H)
#define GRAINS_H
#define EXERCISM_RUN_ALL_TESTS

#include <climits>

namespace grains {
    inline unsigned long long square(int n)
    {
        return 1ULL << (n - 1);
    }

    inline unsigned long long total()
    {
        /**
         * the sum of the grains is equal to a 1 in the nth bit for all n;
         * and there are 64 bits in a ULL. So the sum is equal to ULLONG_MAX
        */
        return ULLONG_MAX;
    }
}

#endif