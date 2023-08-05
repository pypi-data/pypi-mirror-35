#ifndef CGYM_CORE_TYPES_DISCRETE_H_
#define CGYM_CORE_TYPES_DISCRETE_H_

//#include "Core/Types/Space.h"
#include "Core/Math/Random.h"

namespace orenda
{

struct FDiscrete
{
public:
	FDiscrete()
		: X(0)
	{}

	FDiscrete(int Num)
		: X(Num)
	{}

	inline int Sample() const
	{
		return math::UniformRandomInt(0, X-1);
	}

	inline bool Contains(int Num) const
	{
		return Num >= 0 && Num < X;
	}

	/*
	 * Implicit static conversions to int
	 * - These conversions allow a FDiscrete object to be easily compared to an int
	 * - Also, we can pass int type into a function that expects a FDiscrete object and the compiler will
	 *   take care of all the conversions automatically.
	 */
	inline constexpr operator int&() { return X; };

	inline operator int() const { return X; }

private:
	int X;
};

} // namespace orenda

#endif //CGYM_CORE_TYPES_DISCRETE_H_
