#if !defined(GIGASECOND_H)
#define GIGASECOND_H
#define EXERCISM_RUN_ALL_TESTS

#include "boost/date_time/posix_time/posix_time.hpp" //no i/o just types

namespace gigasecond {
    const boost::posix_time::time_duration gigasecond = boost::posix_time::seconds(1000000000);
    boost::posix_time::ptime advance(boost::posix_time::ptime start)
    {
        return start + gigasecond;        
    }
}

#endif