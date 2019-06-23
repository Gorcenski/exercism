#define EXERCISM_RUN_ALL_TESTS
#if !defined(REVERSE_STRING_H)
#define REVERSE_STRING_H

#include <string>

namespace reverse_string {
    inline std::string reverse_string(const std::string& input)
    {
        return std::string(input.crbegin(), input.crend());
    }
}

#endif