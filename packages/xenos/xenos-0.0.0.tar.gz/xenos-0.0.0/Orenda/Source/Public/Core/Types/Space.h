#ifndef CGYM_CORE_TYPES_SPACE_H
#define CGYM_CORE_TYPES_SPACE_H

#include <boost/variant.hpp>

namespace cym
{

template<class T>
class Space
{
public:
//	typedef boost::variant<int, float> T;

	inline auto Sample() // -> decltype(static_cast<T*>(this)->Sample())
	{
		return static_cast<T *>(this)->Sample();
	}

	inline bool Contains(boost::variant<int, float> X)
	{
		return static_cast<T*>(this)->Contains(X);
	}
};

} // namespace cym

#endif //CGYM_CORE_TYPES_SPACE_H
