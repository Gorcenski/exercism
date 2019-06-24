#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H
#define EXERCISM_RUN_ALL_TESTS

namespace space_age {
    class space_age {
    private:
        static constexpr int _seconds_per_earth_year = 31557600;
        static constexpr double _mercury = 0.2408467;
        static constexpr double _venus = 0.61519726;
        static constexpr double _earth = 1.0;
        static constexpr double _mars = 1.8808158;
        static constexpr double _jupiter = 11.862615;
        static constexpr double _saturn = 29.447498 ;
        static constexpr double _uranus = 84.016846;
        static constexpr double _neptune = 164.79132;

        long long _seconds;
        double convert(double period) const
        {
            return _seconds / (_seconds_per_earth_year * period);
        }

    public:
        explicit space_age(const long long seconds)
        {
            _seconds = seconds;
        }

        long long seconds() const
        {
            return _seconds;
        }

        double on_mercury() const
        {
            return convert(_mercury);
        }

        double on_venus() const
        {
            return convert(_venus);
        }

        double on_earth() const
        {
            return convert(_earth);
        }

        double on_mars() const
        {
            return convert(_mars);
        }

        double on_jupiter() const
        {
            return convert(_jupiter);
        }

        double on_saturn() const
        {
            return convert(_saturn);
        }

        double on_uranus() const
        {
            return convert(_uranus);
        }

        double on_neptune() const
        {
            return convert(_neptune);
        }
    };
}

#endif