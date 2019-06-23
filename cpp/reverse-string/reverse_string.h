#define EXERCISM_RUN_ALL_TESTS
#if !defined(REVERSE_STRING_H)
#define REVERSE_STRING_H

#include <string>

namespace reverse_string {
    std::string reverse_string(std::string input)
    {
        std::string output;
        std::copy(input.crbegin(), input.crend(), std::back_inserter(output));

        return output;
    }
}

#endif