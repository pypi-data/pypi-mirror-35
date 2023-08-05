#ifndef CGYM_ENVIRONMENTS_TOYTEXT_BLACKJACK_H_
#define CGYM_ENVIRONMENTS_TOYTEXT_BLACKJACK_H_

#include <vector>

#include "Environments/Interface/DiscreteEnvironment.h"
#include "Core/Types/Discrete.h"

namespace orenda
{

struct FPerson
{
	FPerson() = default;

	int SumCards() const;

	bool HasUsableAce() const;

	bool IsBusted() const;

	std::vector<int> Cards;

private:
	int SumCardsNoUsableAce() const;
};


class Blackjack : public IDiscreteEnvironment
{
public:
	Blackjack();

	~Blackjack() = default;

	FState Step(int In_Action) override;

	FState Reset() override;

private:
	void UpdateObservation() override;

	void DrawCard(FPerson *Person);

	int Score(const FPerson &Person);

private:
	FPerson Player;
	FPerson Dealer;
	std::vector<int> Deck;
};

} // namespace orenda

#endif //CGYM_ENVIRONMENTS_TOYTEXT_BLACKJACK_H_
