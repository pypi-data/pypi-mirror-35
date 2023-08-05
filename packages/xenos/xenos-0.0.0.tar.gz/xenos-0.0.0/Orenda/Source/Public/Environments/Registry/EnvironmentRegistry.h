#ifndef CGYM_ENVIRONMENTS_ENVRIONMENTS_REGISTRY_H_
#define CGYM_ENVIRONMENTS_ENVRIONMENTS_REGISTRY_H_

#include <memory>

//#include "Environments/Interface/Environment_CRTP.h"
#include "Environments/ToyText/Blackjack.h"


namespace orenda
{

// TODO: Do we need to allow additional input arguments?
// TODO: Allow user-defined Allocators
template<class TClass /*, class... TArgs*/>
static TClass Make(/*TArgs... Args*/)
{
	return TClass(/*Args...*/);
}

struct Environments
{
	typedef Blackjack TBlackjack;
};


} // namespace orenda

#endif //CGYM_ENVIRONMENTS_ENVRIONMENTS_REGISTRY_H_