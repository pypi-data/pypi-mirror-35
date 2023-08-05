#ifndef CGYM_ENVRIONMENTS_INTERFACE_CRTPENVIRONMENT_H_
#define CGYM_ENVRIONMENTS_INTERFACE_CRTPENVIRONMENT_H_

//#include <variant>

namespace orenda
{

template<class TClass>
class WEnvironment : public TClass
{
public:
//	inline void Step(std::variant<int, float> Action)
//	{
//		static_cast<TClass*>(this)->Tick(
//				std::get<typename TClass::TAction>(Action));
//	}

	inline auto Step(int Action)
	{
		return static_cast<TClass*>(this)->Tick(Action);
	}

	inline auto Reset()
	{
		return static_cast<TClass*>(this)->Restart();
	}

	inline auto GetActionSpace()
	{
		return static_cast<TClass*>(this)->GetActionSpace();
	}

	inline auto GetObservationSpace()
	{
		return static_cast<TClass*>(this)->GetObservationSpace();
	}

	inline auto GetObservation()
	{
		return static_cast<TClass*>(this)->GetObservation();
	}

	inline float GetReward()
	{
		return static_cast<TClass*>(this)->GetReward();
	}

	inline bool IsDone()
	{
		return static_cast<TClass*>(this)->IsDone();
	}
};

} // namespace orenda

#endif //CGYM_ENVRIONMENTS_INTERFACE_CRTPENVIRONMENT_H_
