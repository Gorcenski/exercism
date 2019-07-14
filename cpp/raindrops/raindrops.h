#if !defined(RAINDROPS_H)
#define RAINDROPS_H
#define EXERCISM_RUN_ALL_TESTS

#include <algorithm>
#include <complex>
#include <map>
#include <string>
#include <vector>

/**
 * Note to the reviewer: why did I solve it like this?
 * 
 * Because this problem is basically fizzbuzz, and I am well-familiar with fizzbuzz
 * and the elementary control flow concepts it is designed around. I wanted a more
 * challenging solution that would teach me some of the deeper features of the language,
 * e.g. how do I do something that looks like "map-reduce" in C++11? What is a functor?
 * How do iterators work?
 * 
 * So, rather than the elementary solution, I created a solution that leverages the
 * fact that the torsion subgroup of the circle group is the set of all nth roots of unity
 * for all n, and then did some string-munging from there.
 */
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
        std::string result;
        std::for_each(drops.begin(), drops.end(), [&](const kv_pair &p) { result += get_sound(n)(p); });
        return result.empty() ? std::to_string(n) : result;
    }
}

#endif