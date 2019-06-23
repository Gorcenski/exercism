#if !defined(SPACE_AGE_H)
#define SPACE_AGE_H
#define EXERCISM_RUN_ALL_TESTS

namespace space_age {
    class space_age {
    private:
        const double _mercury = 0.2408467;
        const double _venus = 0.61519726;
        const double _earth = 1.0;
        const double _mars = 1.8808158;
        const double _jupiter = 11.862615;
        const double _saturn = 29.447498 ;
        const double _uranus = 84.016846;
        const double _neptune = 164.79132;

        long _seconds;
        inline double convert(const double& period) const
        {
            const long seconds_per_earth_year = 31557600; // seconds per Earth year
            return _seconds / (seconds_per_earth_year * period);
        }

    public:
        space_age(const long& seconds)
        {
            _seconds = seconds;
        }

        int seconds() const
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