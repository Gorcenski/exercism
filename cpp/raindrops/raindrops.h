#if !defined(RAINDROPS_H)
#define RAINDROPS_H
#define EXERCISM_RUN_ALL_TESTS

#include <complex>
#include <iterator>
#include <map>
#include <sstream>
#include <string>
#include <vector>

namespace raindrops {
    typedef std::map<int, std::string>::value_type kv_pair;
    static constexpr float epsilon = std::numeric_limits<float>::epsilon();

    class get_sound
    {
    private:
        int num;
        static bool essentiallyEqual(const std::complex<double>& a, const std::complex<double>& b, const float epsilon)
        {
            return std::abs(a - b) <= ( (std::abs(a) > std::abs(b) ? std::abs(b) : std::abs(a)) * epsilon);
        }

    public:
        get_sound(int n) : num(n) { }

        std::string operator () (kv_pair const& p) const
        {
            std::complex<double> two_pi_i_n = std::complex<double>(0, 2 * num * M_PI);
            auto val = exp(two_pi_i_n / std::complex<double>(p.first, 0));
            return essentiallyEqual(val, 1, epsilon) ? p.second : "";
        }
    };

    inline std::string convert(const int n,
                               const std::map<int, std::string>& drops = {
                                   {3, "Pling"},
                                   {5, "Plang"},
                                   {7, "Plong"}
                               })
    {
        
        std::vector<std::string> strings;
        std::transform(drops.begin(), drops.end(),
            std::inserter(strings, strings.begin()),
            get_sound(n)
        );
        std::string result;
        std::for_each(strings.begin(), strings.end(), [&](const std::string &p) { result += p; });
        return result.empty() ? std::to_string(n) : result;
    }
}

#endif