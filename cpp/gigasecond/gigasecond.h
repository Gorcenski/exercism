#if !defined(GIGASECOND_H)
#define GIGASECOND_H
#define EXERCISM_RUN_ALL_TESTS

#include "boost/date_time/posix_time/posix_time.hpp" //no i/o just types

namespace gigasecond {
    boost::posix_time::ptime advance(const boost::posix_time::ptime& start)
    {
        return start + boost::posix_time::seconds(1000000000);
    }
}

#endif