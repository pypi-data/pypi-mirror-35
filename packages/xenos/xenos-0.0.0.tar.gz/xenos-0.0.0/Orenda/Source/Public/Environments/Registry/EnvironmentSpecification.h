#ifndef CGYM_ENVIRONMENTSPECIFICATION_H
#define CGYM_ENVIRONMENTSPECIFICATION_H

#include <string>
#include <limits>
#include <unordered_map>

struct EnvironmentSpecification
{
public:
	EnvironmentSpecification() = default;

	std::string Name;

	// Evaluation Parameters
	int Trials;
	int RewardThreshold;

	// Environments Properties
	bool NonDeterministic;

	int MaxEpisodeSteps;

	int MaxEpisodeSeconds;
};


#endif //CGYM_ENVIRONMENTSPECIFICATION_H
