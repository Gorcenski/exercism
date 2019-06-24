#if !defined(TRIANGLE_H)
#define TRIANGLE_H
#define EXERCISM_RUN_ALL_TESTS

#include <algorithm>
#include <cmath>

namespace triangle {
    enum flavor { equilateral, isosceles, scalene, degenerate};

    /* Stolen shamelessly from TAOCP */
    inline bool essentiallyEqual(float a, float b, float epsilon)
    {
        return std::abs(a - b) <= ( (std::abs(a) > std::abs(b) ? std::abs(b) : std::abs(a)) * epsilon);
    }

    inline bool definitelyGreaterThan(float a, float b, float epsilon)
    {
        return (a - b) > ( (std::abs(a) < std::abs(b) ? std::abs(b) : std::abs(a)) * epsilon);
    }

    inline flavor kind(float a, float b, float c)
    {
        /**
         * The triangle inequality tells us that 2 * max(a,b,c) <= a + b + c, with equality
         * occurring iff the triangle is degenerate. WLOG, assume that a >= b >= c. If c is
         * strictly negative, then we must have (a + b) + c < 2a + c < 2a = 2 * max(a,b,c).
         * Assume 2 * max(a,b,c) == a + b + c. Then the sum of two sides equals the third,
         * which by definition means the triangle is degenerate. On the other hand, assume
         * the triangle is degenerate. Then, WLOG, a = b + c, so max(a,b,c) = a, and
         * a + b + c = 2 * a = 2 * max(a,b,c). Finally, if the perimeter is identically
         * zero, then one of {a, b, c} must be less than zero, or all three must be zero.
         */
        float n = 2 * std::max({a, b, c});
        float perimeter = a + b + c;
        float epsilon = std::numeric_limits<float>::epsilon();
        if (definitelyGreaterThan(n, perimeter, epsilon) || (perimeter == 0))
        {
            throw std::domain_error("This triangle breaks the law.");
        }
        else if (essentiallyEqual(n, perimeter, epsilon))
        {
            return flavor::degenerate;
        }
        else
        {
            bool ab_eq = essentiallyEqual(a, b, epsilon);
            bool bc_eq = essentiallyEqual(b, c, epsilon);
            bool ac_eq = essentiallyEqual(a, c, epsilon);
            if (ab_eq && bc_eq)
            {
                return flavor::equilateral;
            }
            else if (ab_eq || bc_eq || ac_eq)
            {
                return flavor::isosceles;
            }
            else
            {
                return flavor::scalene;
            }   
        }
    }

}

#endif