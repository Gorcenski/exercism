#define EXERCISM_RUN_ALL_TESTS
#if !defined(HAMMING_H)
#define HAMMING_H

#include <string>

namespace hamming {
    size_t compute(std::string string1, std::string string2)
    {
        if (string1.length() != string2.length()) {
            throw std::domain_error("Strings must be of equal length");
        }
        size_t h = 0;
        for (size_t i = 0; i < string1.length(); i++)
        {
            // use operator[] instead of .at() because we can guarantee the index doesn't overflow
            if (string1[i] != string2[i])
            {
                h++;
            }
        }
        return h;
    }
}

#endif