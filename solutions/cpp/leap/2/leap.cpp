#include "leap.h"

namespace leap {
	bool is_leap_year(int year) {

		//on every year that is evenly divisible by 4
		if (year % 4 == 0) {
			return true;
		}
		else {
			return false;
		}
	
	}
}  // namespace leap
