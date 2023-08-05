#include <utility>

#ifndef CYM_TRANSITIONALENVIRONMENT_H
#define CYM_TRANSITIONALENVIRONMENT_H

#include <vector>

namespace orenda
{

class ITransitionalEnvironment
{
public:
	ITransitionalEnvironment(int In_NumStates, int In_NumActions, std::vector<float> In_Probabilities)
		: NumStates(In_NumStates)
		, NumActions(In_NumActions)
		, Probabilities(std::move(In_Probabilities))
	{}


protected:
	int NumStates;
	int NumActions;
	std::vector<float> Probabilities;

};

} //namespace orenda

#endif //CYM_TRANSITIONALENVIRONMENT_H
