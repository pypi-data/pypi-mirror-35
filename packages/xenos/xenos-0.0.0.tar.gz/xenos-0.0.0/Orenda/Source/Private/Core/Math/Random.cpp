#include "Core/Math/Random.h"

#include <random>

namespace orenda::math
{
	std::random_device Device;
	std::default_random_engine Generator(Device());

} // namespace math
