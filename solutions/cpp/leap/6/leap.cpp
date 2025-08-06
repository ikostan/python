#include "leap.h"

namespace leap {
	//The tricky thing here is that a leap year in the Gregorian calendar occurs:
	bool is_leap_year(int year) {

		//on every year that is evenly divisible by 4
		//except every year that is evenly divisible by 100
		//unless the year is also evenly divisible by 400
		return (year % 4 == 0 && year % 100 != 0) || (year % 100 == 0 && year % 400 == 0);	
	}
}  // namespace leap
