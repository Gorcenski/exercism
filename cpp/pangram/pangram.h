#define EXERCISM_RUN_ALL_TESTS
#if !defined(PANGRAM_H)
#define PANGRAM_H

#include <numeric>
#include <string>
#include <vector>

namespace pangram {
    inline bool is_pangram(std::string const &input) {
        std::string input_lower = std::string(input.begin(), input.end());
        std::transform(
            input.begin(), input.end(), input_lower.begin(),
            [](unsigned char c) { return std::tolower(c); }
        );
        
        std::vector<char> alphabet(26);
        std::iota(std::begin(alphabet), std::end(alphabet), 'a');
        auto result = std::accumulate(alphabet.begin(), alphabet.end(), true,
            [&input_lower](bool x, char y) {
                return x && (std::count(input_lower.begin(), input_lower.end(), y) > 0);
            }
        );
        return result;
    }
}
#endif