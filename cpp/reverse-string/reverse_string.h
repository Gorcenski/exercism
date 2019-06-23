#define EXERCISM_RUN_ALL_TESTS
#if !defined(REVERSE_STRING_H)
#define REVERSE_STRING_H

#include <string>

namespace reverse_string {
    std::string reverse_string(std::string input)
    {
        std::string output = input;
        std::string::size_type n = input.length();
        for (size_t i = 0; i < n; i++)
        {
            output[n - i - 1] = input[i];
        }
        return output;
    }
}

#endif