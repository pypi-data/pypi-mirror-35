#ifndef CGYM_CORE_TYPES_TUPLE_H_
#define CGYM_CORE_TYPES_TUPLE_H_

#include <memory>

// TODO: To be implemented either as a wrapper around std::tuple (or hana::tuple) or as completely new data type
/*

template<typename First, typename... Rest>
struct Tuple: public Tuple<Rest...>
{
	Tuple(First first, Rest... rest): Tuple<Rest...>(rest...), first(first) {}

	First first;
};


template<typename First>
struct Tuple<First>
{
	Tuple(First first): first(first) {}

	First first;
};


template<int index, typename First, typename... Rest>
struct GetImpl
{
	static auto value(const Tuple<First, Rest...>* t) -> decltype(GetImpl<index - 1, Rest...>::value(t))
	{
		return GetImpl<index - 1, Rest...>::value(t);
	}
};


template<typename First, typename... Rest>
struct GetImpl<0, First, Rest...>
{
	static First value(const Tuple<First, Rest...>* t)
	{
		return t->first;
	}
};


template<int index, typename First, typename... Rest>
auto get(const Tuple<First, Rest...>& t) -> decltype(GetImpl<index, First, Rest...>::value(&t))
{
	return GetImpl<index, First, Rest...>::value(&t);
}


*/


//template<typename THead, typename... TRest>
//struct Tuple : public Tuple<TRest>...
//{
//	Tuple(THead In_Head, TRest... Rest) : Tuple<TRest...>(Rest...), Head(In_Head) {}
//
//	THead Head;
//};
//
//
//template<typename THead>
//struct Tuple<THead>
//{
//	Tuple(THead In_Head) : Head(In_Head) {};
//
//	THead Head;
//};
//
//template<int Index, typename THead, typename... TRest>
//struct GetImpl
//{
//	static auto Value(const Tuple<THead, TRest...>* t) -> decltype(GetImpl<Index - 1, TRest...>::Value(t))
//	{
//		return GetImpl<Index - 1, TRest...>::Value(t);
//	}
//};
//
//template<typename THead, typename... TRest>
//struct GetImpl<0, THead, TRest...>
//{
//	static THead Value(const Tuple<THead, TRest...>* t)
//	{
//		return t->Head;
//	}
//};
//
//
//template<int Index, typename THead, typename... TRest>
//auto Get(const Tuple<THead, TRest...>& t) -> decltype(GetImpl<Index, THead, TRest...>::Value(&t))
//{
//	return GetImpl<Index, THead, TRest...>::Value((&t));
//}

#endif //CGYM_CORE_TYPES_TUPLE_H_
