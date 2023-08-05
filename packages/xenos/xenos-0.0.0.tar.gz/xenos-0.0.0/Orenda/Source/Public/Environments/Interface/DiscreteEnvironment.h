#ifndef CGYM_ENVIRONMENTS_DISCRETE_ENVIRONMENT_H_
#define CGYM_ENVIRONMENTS_DISCRETE_ENVIRONMENT_H_

#include "Environments/Interface/Environment_CRTP.h"
#include "Core/Types/Discrete.h"

namespace orenda
{

struct FState
{
	typedef int TAction;
	typedef std::vector<int> TObservation;

	TObservation Observation;
	float Reward;
	bool bDone;
};


class IDiscreteEnvironment
{
public:
	virtual ~IDiscreteEnvironment() = default;

	virtual FState Step(int Action) = 0;

	virtual FState Reset() = 0;

	inline FDiscrete GetActionSpace() const { return ActionSpace; }

	inline std::vector<FDiscrete> GetObservationSpace() const { return ObservationSpace; }

	inline FState::TObservation GetObservation() const { return State.Observation; }

	inline float GetReward() const { return State.Reward; }

	inline bool IsDone() const { return State.bDone; }

protected:
	virtual void UpdateObservation() = 0;

protected:
	// Action Space might be used often in each Tick call to check if input is valid, i.e. ActionSpace.Contains(InputAction)
	// Therefore, we keep the complete object in the class
	FDiscrete ActionSpace;

	// Observation Space is not used often so we keep a pointer to it.
	std::vector<FDiscrete> ObservationSpace;

	FState State;
};

} // namespace orenda

#endif //CGYM_ENVIRONMENTS_DISCRETE_ENVIRONMENT_H_
