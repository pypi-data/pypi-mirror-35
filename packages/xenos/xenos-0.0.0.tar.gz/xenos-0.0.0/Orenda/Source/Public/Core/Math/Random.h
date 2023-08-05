#ifndef CGYM_CORE_MATH_RANDOM_H
#define CGYM_CORE_MATH_RANDOM_H


#include <random>
#include <array>

namespace orenda::math
{

extern std::random_device Device;
extern std::default_random_engine Generator;

/*
 * Changes the default_random_engine generator seed to a user set value.
 * @param Seed: An intereger value representing new value of seed.
 */
static inline void SetSeed(int Seed)
{
	Generator.seed(Seed);
}

/*
 * Returns a uniformly distributed random number between [0, 1.0).
 * @return A random float or double number in the range [0, 1).
 */
template<class T>
static inline T Rand()
{
	std::uniform_real_distribution<T> Distribution(0.0, 1.0);
	return Distribution(Generator);
}

/*
 * Produces a uniformly distributed random integer in the closed interval [a, b]
 * @param a: Lower range
 * @param b: Upper range
 * @return A random int number in the range [a, b]
 */
static inline int UniformRandomInt(int a, int b)
{
	std::uniform_int_distribution<int> Distribution(a, b);
	return Distribution(Generator);
}

/*
 * Chooses a random sample from the input Sample array given the distribution Probabilities of the samples.
 * @param Samples: Input sample array of type T and size N
 * @param Probabilities: Distribution probability of each sample in the Samples array of size N. The probabilities can
 * 						 have a different type U.
 * @return A randomly selected sample from the Samples list based on the given Probabilities.
 */
template<class T, class U, size_t N>
static inline T RandomChoice(const std::array<T, N>& Samples, const std::array<U, N>& Probabilities)
{
	std::discrete_distribution<T> Distribution(Probabilities.begin(), Probabilities.end());
	return Samples[Distribution(Generator)];
}

/*
 * Chooses a random sample from the input Sample vector given the distribution Probabilities of the samples.
 * @param Samples: Input sample vector of type T.
 * @param Probabilities: Distribution probability of each sample in the Samples vector. The probabilities can
 * 						 have a different type U.
 * @return A randomly selected sample from the Samples list based on the given Probabilities.
 * @pre-condition: Input parameters Samples and Probabilities must have the same size.
 * @throws std::length_error if the the inputs are of different sizes.
 */
template<class T, class U>
static inline T RandomChoice(const std::vector<T>& Samples, const std::vector<U>& Probabilities)
{
	if (Samples.size() != Probabilities.size())
		throw std::length_error("input samples and probabilities must have the same length.");

	std::discrete_distribution<T> Distribution(Probabilities.begin(), Probabilities.end());

	return Samples[Distribution(Generator)];
}

} // namespace orenda::math

#endif //CGYM_CORE_MATH_RANDOM_H
