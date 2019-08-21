#if !defined(DNA_H)
#define DNA_H
#define EXERCISM_RUN_ALL_TESTS

#include <algorithm>
#include <iterator>
#include <map>
#include <stdexcept>
#include <string>
#include <vector>

namespace dna {
    class counter {
    private:
        const std::vector<char> _proteins{ 'A', 'T', 'C', 'G'};
        std::string _dna_string;
        std::map<char, int> _counts;

    public:
        explicit counter(const std::string& dna_string)
        {
            if (std::string::npos != dna_string.find_first_not_of(
                std::string(_proteins.begin(), _proteins.end())
            ))
            {
                throw std::invalid_argument("DNA string can only contain elements of {'A', 'T', 'G', 'C'}.");
            };
            _dna_string = dna_string;
        };

        std::map<char, int> nucleotide_counts() const {
            std::map<char, int> counts;
            std::transform(
                _proteins.begin(),
                _proteins.end(),
                std::inserter(counts, counts.end()),
                [&](const char &p) {
                    return std::make_pair(
                        p,
                        count(p)
                    );
                });
            return counts;
        };

        int count(const char& protein) const {
            if (std::find(_proteins.begin(), _proteins.end(), protein) == _proteins.end()) {
                throw std::invalid_argument("Argument protein must be one of {'A', 'T', 'G', 'C'}.");
            }
            return std::count(_dna_string.begin(), _dna_string.end(), protein);
        };
    };
}

#endif