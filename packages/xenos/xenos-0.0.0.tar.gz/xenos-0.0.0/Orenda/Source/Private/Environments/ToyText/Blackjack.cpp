#include "Environments/ToyText/Blackjack.h"

#include <iostream>
#include <algorithm>
#include <numeric>

#include "Core/Types/Discrete.h"
#include "Core/Math/Random.h"

namespace orenda
{

int FPerson::SumCards() const
{
	if (HasUsableAce())
		return SumCardsNoUsableAce() + 10;

	return SumCardsNoUsableAce();
}

int FPerson::SumCardsNoUsableAce() const
{
	return std::accumulate(Cards.begin(), Cards.end(), 0);
}

bool FPerson::HasUsableAce() const
{
	if (std::find(Cards.begin(), Cards.end(), 1) != Cards.end())
	{
		return SumCardsNoUsableAce() + 10 <= 21;
	}

	return false;
}

bool FPerson::IsBusted() const
{
	return SumCards() > 21;
}

Blackjack::Blackjack()
		: Player(FPerson())
		, Dealer(FPerson())
		, Deck({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10})
{
	ActionSpace = FDiscrete(2);

	ObservationSpace = std::vector<FDiscrete>({FDiscrete(31), FDiscrete(11), FDiscrete(2)});

	Reset();
}


FState Blackjack::Reset()
{
	if (State.Observation.empty())
		State.Observation = std::vector<int>(3, 0);
	else
		std::fill(State.Observation.begin(), State.Observation.end(), 0);

	// Remove previous cards (if any)
	Player.Cards.clear();
	Dealer.Cards.clear();

	State.Reward = 0.0f;
	State.bDone = false;

	// Draw two cards for each player and dealer
	for (int i = 0; i < 2; ++i)
	{
		DrawCard(&Player);
		DrawCard(&Dealer);
	}

	// Update the observation state
	UpdateObservation();

	return State;
}

FState Blackjack::Step(int In_Action)
{
	if (!ActionSpace.Contains(In_Action))
	{
		std::cout << "Action doesn't exists. Returning the previous state." << std::endl;
		return State;
	}

	if (In_Action == 1) // Hit: Add a card to players hand and return
	{
		DrawCard(&Player);

		if (Player.IsBusted())
		{
			State.bDone = true;
			State.Reward = -1.0f;
		}
	}
	else // Stick: Play out the dealers hand, and score
	{
		State.bDone = true;

		while (Dealer.SumCards() < 17)
			DrawCard(&Dealer);

		State.Reward = static_cast<float>(Score(Player) > Score(Dealer)) -
				 static_cast<float>(Score(Player) < Score(Dealer));
	}

	UpdateObservation();

	return State;
}

void Blackjack::DrawCard(FPerson *Person)
{
//	int Card = cym::math::RandomChoice(Deck, std::vector<int>(Deck.size(), 1));
	int Card = Deck[orenda::math::UniformRandomInt(0, static_cast<int>(Deck.size()) - 1)];
	Person->Cards.emplace_back(Card);
}

void Blackjack::UpdateObservation()
{
	State.Observation[0] = Player.SumCards();
	State.Observation[1] = Dealer.Cards[0];
	State.Observation[2] = Player.HasUsableAce();
}

int Blackjack::Score(const FPerson &Person)
{
	return Person.IsBusted() ? 0 : Person.SumCards();
}

} // namespace orenda