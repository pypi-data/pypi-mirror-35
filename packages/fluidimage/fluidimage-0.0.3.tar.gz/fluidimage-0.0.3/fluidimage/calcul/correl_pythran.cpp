#define BOOST_SIMD_NO_STRICT_ALIASING 1
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/numpy_texpr.hpp>
#include <pythonic/include/types/float32.hpp>
#include <pythonic/include/types/ndarray.hpp>
#include <pythonic/include/types/int.hpp>
#include <pythonic/types/float32.hpp>
#include <pythonic/types/ndarray.hpp>
#include <pythonic/types/int.hpp>
#include <pythonic/types/numpy_texpr.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/include/numpy/float32.hpp>
#include <pythonic/include/operator_/ifloordiv.hpp>
#include <pythonic/include/operator_/div.hpp>
#include <pythonic/include/__builtin__/min.hpp>
#include <pythonic/include/__builtin__/max.hpp>
#include <pythonic/include/numpy/square.hpp>
#include <pythonic/include/numpy/empty.hpp>
#include <pythonic/include/__builtin__/getattr.hpp>
#include <pythonic/include/__builtin__/tuple.hpp>
#include <pythonic/include/__builtin__/range.hpp>
#include <pythonic/include/operator_/floordiv.hpp>
#include <pythonic/include/operator_/idiv.hpp>
#include <pythonic/include/__builtin__/int_.hpp>
#include <pythonic/include/numpy/sqrt.hpp>
#include <pythonic/include/numpy/sum.hpp>
#include <pythonic/types/str.hpp>
#include <pythonic/numpy/float32.hpp>
#include <pythonic/operator_/ifloordiv.hpp>
#include <pythonic/operator_/div.hpp>
#include <pythonic/__builtin__/min.hpp>
#include <pythonic/__builtin__/max.hpp>
#include <pythonic/numpy/square.hpp>
#include <pythonic/numpy/empty.hpp>
#include <pythonic/__builtin__/getattr.hpp>
#include <pythonic/__builtin__/tuple.hpp>
#include <pythonic/__builtin__/range.hpp>
#include <pythonic/operator_/floordiv.hpp>
#include <pythonic/operator_/idiv.hpp>
#include <pythonic/__builtin__/int_.hpp>
#include <pythonic/numpy/sqrt.hpp>
#include <pythonic/numpy/sum.hpp>
namespace __pythran_correl_pythran
{
  struct correl_pythran
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::empty{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::int_{})>::type>::type __type1;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type2;
      typedef decltype(std::declval<__type1>()(std::declval<__type2>())) __type3;
      typedef long __type4;
      typedef decltype((std::declval<__type3>() * std::declval<__type4>())) __type5;
      typedef decltype((std::declval<__type5>() + std::declval<__type4>())) __type6;
      typedef decltype((std::declval<__type5>() * std::declval<__type3>())) __type7;
      typedef decltype((std::declval<__type7>() * std::declval<__type4>())) __type8;
      typedef decltype((std::declval<__type6>() + std::declval<__type8>())) __type9;
      typedef decltype((std::declval<__type9>() + std::declval<__type4>())) __type10;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type10>(), std::declval<__type10>())) __type11;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float32{})>::type>::type __type12;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type11>(), std::declval<__type12>()))>::type __type13;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type14;
      typedef decltype((std::declval<__type2>() + std::declval<__type4>())) __type15;
      typedef decltype(std::declval<__type14>()(std::declval<__type15>())) __type16;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type16>::type::iterator>::value_type>::type __type17;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type17>())) __type18;
      typedef indexable<__type18> __type19;
      typedef typename __combined<__type13,__type19>::type __type20;
      typedef decltype(std::declval<__type14>()(std::declval<__type2>())) __type21;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type21>::type::iterator>::value_type>::type __type22;
      typedef decltype((std::declval<__type22>() + std::declval<__type2>())) __type23;
      typedef decltype((std::declval<__type23>() + std::declval<__type4>())) __type24;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type24>())) __type25;
      typedef indexable<__type25> __type26;
      typedef typename __combined<__type20,__type26>::type __type27;
      typedef typename __combined<__type17,__type22>::type __type28;
      typedef decltype((std::declval<__type28>() + std::declval<__type2>())) __type29;
      typedef decltype((std::declval<__type29>() + std::declval<__type4>())) __type30;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type30>(), std::declval<__type17>())) __type31;
      typedef indexable<__type31> __type32;
      typedef typename __combined<__type27,__type32>::type __type33;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type30>(), std::declval<__type24>())) __type34;
      typedef indexable<__type34> __type35;
      typedef typename __combined<__type33,__type35>::type __type36;
      typedef typename pythonic::assignable<double>::type __type37;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type38;
      typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type38>())) __type39;
      typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type39>::type>::type>::type __type40;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::min{})>::type>::type __type41;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type42;
      typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type42>())) __type43;
      typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type43>::type>::type>::type __type44;
      typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type44>(), std::declval<__type4>()))) __type45;
      typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type40>(), std::declval<__type4>()))) __type46;
      typedef decltype((std::declval<__type45>() - std::declval<__type46>())) __type47;
      typedef decltype((-std::declval<__type2>())) __type48;
      typedef typename pythonic::assignable<decltype((std::declval<__type48>() + std::declval<__type17>()))>::type __type49;
      typedef decltype((std::declval<__type47>() + std::declval<__type49>())) __type50;
      typedef decltype(std::declval<__type41>()(std::declval<__type50>(), std::declval<__type4>())) __type51;
      typedef typename pythonic::assignable<decltype((std::declval<__type40>() + std::declval<__type51>()))>::type __type52;
      typedef decltype(std::declval<__type14>()(std::declval<__type52>())) __type53;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type53>::type::iterator>::value_type>::type __type54;
      typedef typename pythonic::assignable<decltype((-std::declval<__type51>()))>::type __type55;
      typedef decltype((std::declval<__type54>() + std::declval<__type55>())) __type56;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type39>::type>::type>::type __type57;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type43>::type>::type>::type __type58;
      typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type58>(), std::declval<__type4>()))) __type59;
      typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type57>(), std::declval<__type4>()))) __type60;
      typedef decltype((std::declval<__type59>() - std::declval<__type60>())) __type61;
      typedef decltype((std::declval<__type61>() + std::declval<__type49>())) __type62;
      typedef decltype(std::declval<__type41>()(std::declval<__type62>(), std::declval<__type4>())) __type63;
      typedef decltype((std::declval<__type57>() + std::declval<__type63>())) __type64;
      typedef typename pythonic::lazy<__type64>::type __type65;
      typedef decltype(std::declval<__type14>()(std::declval<__type65>())) __type66;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type66>::type::iterator>::value_type>::type __type67;
      typedef typename pythonic::assignable<decltype((-std::declval<__type63>()))>::type __type68;
      typedef decltype((std::declval<__type67>() + std::declval<__type68>())) __type69;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type56>(), std::declval<__type69>())) __type70;
      typedef decltype(std::declval<__type38>()[std::declval<__type70>()]) __type71;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::max{})>::type>::type __type72;
      typedef typename pythonic::assignable<decltype(std::declval<__type72>()(std::declval<__type4>(), std::declval<__type50>()))>::type __type73;
      typedef decltype((std::declval<__type73>() + std::declval<__type54>())) __type74;
      typedef typename pythonic::assignable<decltype(std::declval<__type72>()(std::declval<__type4>(), std::declval<__type62>()))>::type __type75;
      typedef decltype((std::declval<__type75>() + std::declval<__type67>())) __type76;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type74>(), std::declval<__type76>())) __type77;
      typedef decltype(std::declval<__type42>()[std::declval<__type77>()]) __type78;
      typedef decltype((std::declval<__type71>() * std::declval<__type78>())) __type79;
      typedef decltype((std::declval<__type37>() + std::declval<__type79>())) __type80;
      typedef typename __combined<__type37,__type80>::type __type81;
      typedef typename __combined<__type81,__type79>::type __type82;
      typedef decltype((std::declval<__type65>() * std::declval<__type52>())) __type83;
      typedef decltype((pythonic::operator_::div(std::declval<__type82>(), std::declval<__type83>()))) __type84;
      typedef container<typename std::remove_reference<__type84>::type> __type85;
      typedef typename __combined<__type36,__type85>::type __type86;
      typedef typename __combined<__type86,__type19>::type __type87;
      typedef typename __combined<__type87,__type85>::type __type88;
      typedef decltype((std::declval<__type59>() + std::declval<__type60>())) __type89;
      typedef typename pythonic::assignable<decltype((std::declval<__type22>() + std::declval<__type4>()))>::type __type90;
      typedef decltype((std::declval<__type89>() + std::declval<__type90>())) __type91;
      typedef decltype((std::declval<__type91>() - std::declval<__type58>())) __type92;
      typedef decltype(std::declval<__type72>()(std::declval<__type92>(), std::declval<__type4>())) __type93;
      typedef decltype((std::declval<__type57>() - std::declval<__type93>())) __type94;
      typedef typename pythonic::lazy<__type94>::type __type95;
      typedef decltype(std::declval<__type14>()(std::declval<__type95>())) __type96;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type96>::type::iterator>::value_type>::type __type97;
      typedef typename pythonic::assignable<long>::type __type98;
      typedef typename __combined<__type68,__type98>::type __type99;
      typedef decltype((std::declval<__type97>() + std::declval<__type99>())) __type100;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type56>(), std::declval<__type100>())) __type101;
      typedef decltype(std::declval<__type38>()[std::declval<__type101>()]) __type102;
      typedef typename pythonic::assignable<decltype((std::declval<__type61>() + std::declval<__type90>()))>::type __type103;
      typedef typename __combined<__type75,__type103>::type __type104;
      typedef decltype((std::declval<__type104>() + std::declval<__type97>())) __type105;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type74>(), std::declval<__type105>())) __type106;
      typedef decltype(std::declval<__type42>()[std::declval<__type106>()]) __type107;
      typedef decltype((std::declval<__type102>() * std::declval<__type107>())) __type108;
      typedef decltype((std::declval<__type37>() + std::declval<__type108>())) __type109;
      typedef typename __combined<__type37,__type109>::type __type110;
      typedef typename __combined<__type110,__type108>::type __type111;
      typedef decltype((std::declval<__type95>() * std::declval<__type52>())) __type112;
      typedef decltype((pythonic::operator_::div(std::declval<__type111>(), std::declval<__type112>()))) __type113;
      typedef container<typename std::remove_reference<__type113>::type> __type114;
      typedef typename __combined<__type88,__type114>::type __type115;
      typedef typename __combined<__type115,__type26>::type __type116;
      typedef typename __combined<__type116,__type114>::type __type117;
      typedef decltype((std::declval<__type45>() + std::declval<__type46>())) __type118;
      typedef typename pythonic::assignable<decltype((std::declval<__type28>() + std::declval<__type4>()))>::type __type119;
      typedef decltype((std::declval<__type118>() + std::declval<__type119>())) __type120;
      typedef decltype((std::declval<__type120>() - std::declval<__type44>())) __type121;
      typedef decltype(std::declval<__type72>()(std::declval<__type121>(), std::declval<__type4>())) __type122;
      typedef typename pythonic::assignable<decltype((std::declval<__type40>() - std::declval<__type122>()))>::type __type123;
      typedef typename __combined<__type52,__type123>::type __type124;
      typedef decltype(std::declval<__type14>()(std::declval<__type124>())) __type125;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type125>::type::iterator>::value_type>::type __type126;
      typedef typename __combined<__type54,__type126>::type __type127;
      typedef typename __combined<__type55,__type98>::type __type128;
      typedef decltype((std::declval<__type127>() + std::declval<__type128>())) __type129;
      typedef decltype((std::declval<__type67>() + std::declval<__type99>())) __type130;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type129>(), std::declval<__type130>())) __type131;
      typedef decltype(std::declval<__type38>()[std::declval<__type131>()]) __type132;
      typedef typename pythonic::assignable<decltype((std::declval<__type47>() + std::declval<__type119>()))>::type __type133;
      typedef typename __combined<__type73,__type133>::type __type134;
      typedef decltype((std::declval<__type134>() + std::declval<__type127>())) __type135;
      typedef decltype((std::declval<__type104>() + std::declval<__type67>())) __type136;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type135>(), std::declval<__type136>())) __type137;
      typedef decltype(std::declval<__type42>()[std::declval<__type137>()]) __type138;
      typedef decltype((std::declval<__type132>() * std::declval<__type138>())) __type139;
      typedef decltype((std::declval<__type37>() + std::declval<__type139>())) __type140;
      typedef typename __combined<__type37,__type140>::type __type141;
      typedef typename __combined<__type141,__type139>::type __type142;
      typedef decltype((std::declval<__type65>() * std::declval<__type124>())) __type143;
      typedef decltype((pythonic::operator_::div(std::declval<__type142>(), std::declval<__type143>()))) __type144;
      typedef container<typename std::remove_reference<__type144>::type> __type145;
      typedef typename __combined<__type117,__type145>::type __type146;
      typedef typename __combined<__type146,__type32>::type __type147;
      typedef typename __combined<__type147,__type145>::type __type148;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type129>(), std::declval<__type100>())) __type149;
      typedef decltype(std::declval<__type38>()[std::declval<__type149>()]) __type150;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type135>(), std::declval<__type105>())) __type151;
      typedef decltype(std::declval<__type42>()[std::declval<__type151>()]) __type152;
      typedef decltype((std::declval<__type150>() * std::declval<__type152>())) __type153;
      typedef decltype((std::declval<__type37>() + std::declval<__type153>())) __type154;
      typedef typename __combined<__type37,__type154>::type __type155;
      typedef typename __combined<__type155,__type153>::type __type156;
      typedef decltype((std::declval<__type95>() * std::declval<__type124>())) __type157;
      typedef decltype((pythonic::operator_::div(std::declval<__type156>(), std::declval<__type157>()))) __type158;
      typedef container<typename std::remove_reference<__type158>::type> __type159;
      typedef typename __combined<__type148,__type159>::type __type160;
      typedef typename __combined<__type160,__type35>::type __type161;
      typedef typename __combined<__type161,__type159>::type __type162;
      typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SIZE>(std::declval<__type38>())) __type163;
      typedef decltype((std::declval<__type162>() * std::declval<__type163>())) __type164;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sqrt{})>::type>::type __type165;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::sum{})>::type>::type __type166;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type167;
      typedef decltype(std::declval<__type167>()(std::declval<__type38>())) __type168;
      typedef decltype(std::declval<__type166>()(std::declval<__type168>())) __type169;
      typedef decltype(std::declval<__type167>()(std::declval<__type42>())) __type170;
      typedef decltype(std::declval<__type166>()(std::declval<__type170>())) __type171;
      typedef decltype((std::declval<__type169>() * std::declval<__type171>())) __type172;
      typedef decltype(std::declval<__type165>()(std::declval<__type172>())) __type173;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type164>(), std::declval<__type173>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
    typename type<argument_type0, argument_type1, argument_type2>::result_type operator()(argument_type0&& im0, argument_type1&& im1, argument_type2&& disp_max) const
    ;
  }  ;
  template <typename argument_type0 , typename argument_type1 , typename argument_type2 >
  typename correl_pythran::type<argument_type0, argument_type1, argument_type2>::result_type correl_pythran::operator()(argument_type0&& im0, argument_type1&& im1, argument_type2&& disp_max) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::empty{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::int_{})>::type>::type __type1;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type2>::type>::type __type2;
    typedef decltype(std::declval<__type1>()(std::declval<__type2>())) __type3;
    typedef long __type4;
    typedef decltype((std::declval<__type3>() * std::declval<__type4>())) __type5;
    typedef decltype((std::declval<__type5>() + std::declval<__type4>())) __type6;
    typedef decltype((std::declval<__type5>() * std::declval<__type3>())) __type7;
    typedef decltype((std::declval<__type7>() * std::declval<__type4>())) __type8;
    typedef decltype((std::declval<__type6>() + std::declval<__type8>())) __type9;
    typedef decltype((std::declval<__type9>() + std::declval<__type4>())) __type10;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type10>(), std::declval<__type10>())) __type11;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::float32{})>::type>::type __type12;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type11>(), std::declval<__type12>()))>::type __type13;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type14;
    typedef decltype((std::declval<__type2>() + std::declval<__type4>())) __type15;
    typedef decltype(std::declval<__type14>()(std::declval<__type15>())) __type16;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type16>::type::iterator>::value_type>::type __type17;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type17>())) __type18;
    typedef indexable<__type18> __type19;
    typedef typename __combined<__type13,__type19>::type __type20;
    typedef decltype(std::declval<__type14>()(std::declval<__type2>())) __type21;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type21>::type::iterator>::value_type>::type __type22;
    typedef decltype((std::declval<__type22>() + std::declval<__type2>())) __type23;
    typedef decltype((std::declval<__type23>() + std::declval<__type4>())) __type24;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type24>())) __type25;
    typedef indexable<__type25> __type26;
    typedef typename __combined<__type20,__type26>::type __type27;
    typedef typename __combined<__type17,__type22>::type __type28;
    typedef decltype((std::declval<__type28>() + std::declval<__type2>())) __type29;
    typedef decltype((std::declval<__type29>() + std::declval<__type4>())) __type30;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type30>(), std::declval<__type17>())) __type31;
    typedef indexable<__type31> __type32;
    typedef typename __combined<__type27,__type32>::type __type33;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type30>(), std::declval<__type24>())) __type34;
    typedef indexable<__type34> __type35;
    typedef typename __combined<__type33,__type35>::type __type36;
    typedef typename pythonic::assignable<double>::type __type37;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type38;
    typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type38>())) __type39;
    typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type39>::type>::type>::type __type40;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::min{})>::type>::type __type41;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type42;
    typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type42>())) __type43;
    typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type43>::type>::type>::type __type44;
    typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type44>(), std::declval<__type4>()))) __type45;
    typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type40>(), std::declval<__type4>()))) __type46;
    typedef decltype((std::declval<__type45>() - std::declval<__type46>())) __type47;
    typedef decltype((-std::declval<__type2>())) __type48;
    typedef typename pythonic::assignable<decltype((std::declval<__type48>() + std::declval<__type17>()))>::type __type49;
    typedef decltype((std::declval<__type47>() + std::declval<__type49>())) __type50;
    typedef decltype(std::declval<__type41>()(std::declval<__type50>(), std::declval<__type4>())) __type51;
    typedef typename pythonic::assignable<decltype((std::declval<__type40>() + std::declval<__type51>()))>::type __type52;
    typedef decltype(std::declval<__type14>()(std::declval<__type52>())) __type53;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type53>::type::iterator>::value_type>::type __type54;
    typedef typename pythonic::assignable<decltype((-std::declval<__type51>()))>::type __type55;
    typedef decltype((std::declval<__type54>() + std::declval<__type55>())) __type56;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type39>::type>::type>::type __type57;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type43>::type>::type>::type __type58;
    typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type58>(), std::declval<__type4>()))) __type59;
    typedef decltype((pythonic::operator_::functor::floordiv{}(std::declval<__type57>(), std::declval<__type4>()))) __type60;
    typedef decltype((std::declval<__type59>() - std::declval<__type60>())) __type61;
    typedef decltype((std::declval<__type61>() + std::declval<__type49>())) __type62;
    typedef decltype(std::declval<__type41>()(std::declval<__type62>(), std::declval<__type4>())) __type63;
    typedef decltype((std::declval<__type57>() + std::declval<__type63>())) __type64;
    typedef typename pythonic::lazy<__type64>::type __type65;
    typedef decltype(std::declval<__type14>()(std::declval<__type65>())) __type66;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type66>::type::iterator>::value_type>::type __type67;
    typedef typename pythonic::assignable<decltype((-std::declval<__type63>()))>::type __type68;
    typedef decltype((std::declval<__type67>() + std::declval<__type68>())) __type69;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type56>(), std::declval<__type69>())) __type70;
    typedef decltype(std::declval<__type38>()[std::declval<__type70>()]) __type71;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::max{})>::type>::type __type72;
    typedef typename pythonic::assignable<decltype(std::declval<__type72>()(std::declval<__type4>(), std::declval<__type50>()))>::type __type73;
    typedef decltype((std::declval<__type73>() + std::declval<__type54>())) __type74;
    typedef typename pythonic::assignable<decltype(std::declval<__type72>()(std::declval<__type4>(), std::declval<__type62>()))>::type __type75;
    typedef decltype((std::declval<__type75>() + std::declval<__type67>())) __type76;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type74>(), std::declval<__type76>())) __type77;
    typedef decltype(std::declval<__type42>()[std::declval<__type77>()]) __type78;
    typedef decltype((std::declval<__type71>() * std::declval<__type78>())) __type79;
    typedef decltype((std::declval<__type37>() + std::declval<__type79>())) __type80;
    typedef typename __combined<__type37,__type80>::type __type81;
    typedef typename __combined<__type81,__type79>::type __type82;
    typedef decltype((std::declval<__type65>() * std::declval<__type52>())) __type83;
    typedef decltype((pythonic::operator_::div(std::declval<__type82>(), std::declval<__type83>()))) __type84;
    typedef container<typename std::remove_reference<__type84>::type> __type85;
    typedef typename __combined<__type36,__type85>::type __type86;
    typedef typename __combined<__type86,__type19>::type __type87;
    typedef decltype((std::declval<__type59>() + std::declval<__type60>())) __type88;
    typedef typename pythonic::assignable<decltype((std::declval<__type22>() + std::declval<__type4>()))>::type __type89;
    typedef decltype((std::declval<__type88>() + std::declval<__type89>())) __type90;
    typedef decltype((std::declval<__type90>() - std::declval<__type58>())) __type91;
    typedef decltype(std::declval<__type72>()(std::declval<__type91>(), std::declval<__type4>())) __type92;
    typedef decltype((std::declval<__type57>() - std::declval<__type92>())) __type93;
    typedef typename pythonic::lazy<__type93>::type __type94;
    typedef decltype(std::declval<__type14>()(std::declval<__type94>())) __type95;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type95>::type::iterator>::value_type>::type __type96;
    typedef typename pythonic::assignable<long>::type __type97;
    typedef typename __combined<__type68,__type97>::type __type98;
    typedef decltype((std::declval<__type96>() + std::declval<__type98>())) __type99;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type56>(), std::declval<__type99>())) __type100;
    typedef decltype(std::declval<__type38>()[std::declval<__type100>()]) __type101;
    typedef typename pythonic::assignable<decltype((std::declval<__type61>() + std::declval<__type89>()))>::type __type102;
    typedef typename __combined<__type75,__type102>::type __type103;
    typedef decltype((std::declval<__type103>() + std::declval<__type96>())) __type104;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type74>(), std::declval<__type104>())) __type105;
    typedef decltype(std::declval<__type42>()[std::declval<__type105>()]) __type106;
    typedef decltype((std::declval<__type101>() * std::declval<__type106>())) __type107;
    typedef decltype((std::declval<__type37>() + std::declval<__type107>())) __type108;
    typedef typename __combined<__type37,__type108>::type __type109;
    typedef typename __combined<__type109,__type107>::type __type110;
    typedef decltype((std::declval<__type94>() * std::declval<__type52>())) __type111;
    typedef decltype((pythonic::operator_::div(std::declval<__type110>(), std::declval<__type111>()))) __type112;
    typedef container<typename std::remove_reference<__type112>::type> __type113;
    typedef typename __combined<__type87,__type113>::type __type114;
    typedef typename __combined<__type114,__type26>::type __type115;
    typedef decltype((std::declval<__type45>() + std::declval<__type46>())) __type116;
    typedef typename pythonic::assignable<decltype((std::declval<__type28>() + std::declval<__type4>()))>::type __type117;
    typedef decltype((std::declval<__type116>() + std::declval<__type117>())) __type118;
    typedef decltype((std::declval<__type118>() - std::declval<__type44>())) __type119;
    typedef decltype(std::declval<__type72>()(std::declval<__type119>(), std::declval<__type4>())) __type120;
    typedef typename pythonic::assignable<decltype((std::declval<__type40>() - std::declval<__type120>()))>::type __type121;
    typedef typename __combined<__type52,__type121>::type __type122;
    typedef decltype(std::declval<__type14>()(std::declval<__type122>())) __type123;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type123>::type::iterator>::value_type>::type __type124;
    typedef typename __combined<__type54,__type124>::type __type125;
    typedef typename __combined<__type55,__type97>::type __type126;
    typedef decltype((std::declval<__type125>() + std::declval<__type126>())) __type127;
    typedef decltype((std::declval<__type67>() + std::declval<__type98>())) __type128;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type127>(), std::declval<__type128>())) __type129;
    typedef decltype(std::declval<__type38>()[std::declval<__type129>()]) __type130;
    typedef typename pythonic::assignable<decltype((std::declval<__type47>() + std::declval<__type117>()))>::type __type131;
    typedef typename __combined<__type73,__type131>::type __type132;
    typedef decltype((std::declval<__type132>() + std::declval<__type125>())) __type133;
    typedef decltype((std::declval<__type103>() + std::declval<__type67>())) __type134;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type133>(), std::declval<__type134>())) __type135;
    typedef decltype(std::declval<__type42>()[std::declval<__type135>()]) __type136;
    typedef decltype((std::declval<__type130>() * std::declval<__type136>())) __type137;
    typedef decltype((std::declval<__type37>() + std::declval<__type137>())) __type138;
    typedef typename __combined<__type37,__type138>::type __type139;
    typedef typename __combined<__type139,__type137>::type __type140;
    typedef decltype((std::declval<__type65>() * std::declval<__type122>())) __type141;
    typedef decltype((pythonic::operator_::div(std::declval<__type140>(), std::declval<__type141>()))) __type142;
    typedef container<typename std::remove_reference<__type142>::type> __type143;
    typedef typename __combined<__type115,__type143>::type __type144;
    typedef typename __combined<__type144,__type32>::type __type145;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type127>(), std::declval<__type99>())) __type146;
    typedef decltype(std::declval<__type38>()[std::declval<__type146>()]) __type147;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type133>(), std::declval<__type104>())) __type148;
    typedef decltype(std::declval<__type42>()[std::declval<__type148>()]) __type149;
    typedef decltype((std::declval<__type147>() * std::declval<__type149>())) __type150;
    typedef decltype((std::declval<__type37>() + std::declval<__type150>())) __type151;
    typedef typename __combined<__type37,__type151>::type __type152;
    typedef typename __combined<__type152,__type150>::type __type153;
    typedef decltype((std::declval<__type94>() * std::declval<__type122>())) __type154;
    typedef decltype((pythonic::operator_::div(std::declval<__type153>(), std::declval<__type154>()))) __type155;
    typedef container<typename std::remove_reference<__type155>::type> __type156;
    typedef typename __combined<__type145,__type156>::type __type157;
    typename pythonic::assignable<typename __combined<__type73,__type131>::type>::type ny0dep;
    typename pythonic::assignable<typename __combined<__type68,__type97>::type>::type nx1dep;
    typename pythonic::assignable<typename __combined<__type55,__type97>::type>::type ny1dep;
    typename pythonic::assignable<typename __combined<__type17,__type22>::type>::type xiy;
    typename pythonic::assignable<typename __combined<__type52,__type121>::type>::type nymax;
    typename pythonic::assignable<typename __combined<__type75,__type102>::type>::type nx0dep;
    typename pythonic::assignable<typename __combined<__type54,__type124>::type>::type iy;
    ;
    ;
    typename pythonic::assignable<decltype(std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im0)))>::type ny0 = std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im0));
    typename pythonic::assignable<decltype(std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im0)))>::type nx0 = std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im0));
    typename pythonic::assignable<decltype(std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im1)))>::type ny1 = std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im1));
    typename pythonic::assignable<decltype(std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im1)))>::type nx1 = std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(im1));
    ;
    typename pythonic::assignable<typename __combined<__type157,__type35>::type>::type correl = pythonic::numpy::functor::empty{}(pythonic::types::make_tuple(((pythonic::__builtin__::functor::int_{}(disp_max) * 2L) + 1L), ((pythonic::__builtin__::functor::int_{}(disp_max) * 2L) + 1L)), pythonic::numpy::functor::float32{});
    {
      long  __target140006560318072 = (disp_max + 1L);
      for ( xiy=0L; xiy < __target140006560318072; xiy += 1L)
      {
        typename pythonic::assignable<decltype(((-disp_max) + xiy))>::type dispy = ((-disp_max) + xiy);
        nymax = (ny1 + pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(ny0, 2L)) - (pythonic::operator_::functor::floordiv{}(ny1, 2L))) + dispy), 0L));
        ny1dep = (-pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(ny0, 2L)) - (pythonic::operator_::functor::floordiv{}(ny1, 2L))) + dispy), 0L));
        ny0dep = pythonic::__builtin__::functor::max{}(0L, (((pythonic::operator_::functor::floordiv{}(ny0, 2L)) - (pythonic::operator_::functor::floordiv{}(ny1, 2L))) + dispy));
        {
          long  __target140006560343040 = (disp_max + 1L);
          for (long  xix=0L; xix < __target140006560343040; xix += 1L)
          {
            typename pythonic::assignable<decltype(((-disp_max) + xix))>::type dispx = ((-disp_max) + xix);
            typename pythonic::lazy<decltype((nx1 + pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx), 0L)))>::type nxmax = (nx1 + pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx), 0L));
            nx1dep = (-pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx), 0L));
            nx0dep = pythonic::__builtin__::functor::max{}(0L, (((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx));
            typename pythonic::assignable<typename __combined<__type81,__type79>::type>::type tmp = 0.0;
            {
              long  __target140006560362336 = nymax;
              for ( iy=0L; iy < __target140006560362336; iy += 1L)
              {
                {
                  long  __target140006560392808 = nxmax;
                  for (long  ix=0L; ix < __target140006560392808; ix += 1L)
                  {
                    tmp += (im1.fast(pythonic::types::make_tuple((iy + ny1dep), (ix + nx1dep))) * im0[pythonic::types::make_tuple((ny0dep + iy), (nx0dep + ix))]);
                  }
                }
              }
              if (iy == __target140006560362336)
              iy -= 1L;
            }
            correl.fast(pythonic::types::make_tuple(xiy, xix)) = (pythonic::operator_::div(tmp, (nxmax * nymax)));
          }
        }
        {
          long  __target140006560344440 = disp_max;
          for (long  xix_=0L; xix_ < __target140006560344440; xix_ += 1L)
          {
            typename pythonic::assignable<decltype((xix_ + 1L))>::type dispx_ = (xix_ + 1L);
            typename pythonic::lazy<decltype((nx1 - pythonic::__builtin__::functor::max{}(((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) + (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx_) - nx0), 0L)))>::type nxmax_ = (nx1 - pythonic::__builtin__::functor::max{}(((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) + (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx_) - nx0), 0L));
            nx1dep = 0L;
            nx0dep = (((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx_);
            typename pythonic::assignable<typename __combined<__type109,__type107>::type>::type tmp_ = 0.0;
            {
              long  __target140006559904600 = nymax;
              for ( iy=0L; iy < __target140006559904600; iy += 1L)
              {
                {
                  long  __target140006559906112 = nxmax_;
                  for (long  ix_=0L; ix_ < __target140006559906112; ix_ += 1L)
                  {
                    tmp_ += (im1.fast(pythonic::types::make_tuple((iy + ny1dep), (ix_ + nx1dep))) * im0[pythonic::types::make_tuple((ny0dep + iy), (nx0dep + ix_))]);
                  }
                }
              }
              if (iy == __target140006559904600)
              iy -= 1L;
            }
            correl[pythonic::types::make_tuple(xiy, ((xix_ + disp_max) + 1L))] = (pythonic::operator_::div(tmp_, (nxmax_ * nymax)));
          }
        }
      }
      if (xiy == __target140006560318072)
      xiy -= 1L;
    }
    {
      long  __target140006560318576 = disp_max;
      for ( xiy=0L; xiy < __target140006560318576; xiy += 1L)
      {
        typename pythonic::assignable<typename pythonic::assignable<decltype((std::declval<__type28>() + std::declval<__type4>()))>::type>::type dispy_ = (xiy + 1L);
        nymax = (ny1 - pythonic::__builtin__::functor::max{}(((((pythonic::operator_::functor::floordiv{}(ny0, 2L)) + (pythonic::operator_::functor::floordiv{}(ny1, 2L))) + dispy_) - ny0), 0L));
        ny1dep = 0L;
        ny0dep = (((pythonic::operator_::functor::floordiv{}(ny0, 2L)) - (pythonic::operator_::functor::floordiv{}(ny1, 2L))) + dispy_);
        {
          long  __target140006559954536 = (disp_max + 1L);
          for (long  xix__=0L; xix__ < __target140006559954536; xix__ += 1L)
          {
            typename pythonic::assignable<decltype(((-disp_max) + xix__))>::type dispx__ = ((-disp_max) + xix__);
            typename pythonic::lazy<decltype((nx1 + pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx__), 0L)))>::type nxmax__ = (nx1 + pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx__), 0L));
            nx1dep = (-pythonic::__builtin__::functor::min{}((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx__), 0L));
            nx0dep = pythonic::__builtin__::functor::max{}(0L, (((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx__));
            typename pythonic::assignable<typename __combined<__type139,__type137>::type>::type tmp__ = 0.0;
            {
              long  __target140006559976528 = nymax;
              for ( iy=0L; iy < __target140006559976528; iy += 1L)
              {
                {
                  long  __target140006559990616 = nxmax__;
                  for (long  ix__=0L; ix__ < __target140006559990616; ix__ += 1L)
                  {
                    tmp__ += (im1.fast(pythonic::types::make_tuple((iy + ny1dep), (ix__ + nx1dep))) * im0[pythonic::types::make_tuple((ny0dep + iy), (nx0dep + ix__))]);
                  }
                }
              }
              if (iy == __target140006559976528)
              iy -= 1L;
            }
            correl[pythonic::types::make_tuple(((xiy + disp_max) + 1L), xix__)] = (pythonic::operator_::div(tmp__, (nxmax__ * nymax)));
          }
        }
        {
          long  __target140006559954760 = disp_max;
          for (long  xix___=0L; xix___ < __target140006559954760; xix___ += 1L)
          {
            typename pythonic::assignable<decltype((xix___ + 1L))>::type dispx___ = (xix___ + 1L);
            typename pythonic::lazy<decltype((nx1 - pythonic::__builtin__::functor::max{}(((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) + (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx___) - nx0), 0L)))>::type nxmax___ = (nx1 - pythonic::__builtin__::functor::max{}(((((pythonic::operator_::functor::floordiv{}(nx0, 2L)) + (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx___) - nx0), 0L));
            nx1dep = 0L;
            nx0dep = (((pythonic::operator_::functor::floordiv{}(nx0, 2L)) - (pythonic::operator_::functor::floordiv{}(nx1, 2L))) + dispx___);
            typename pythonic::assignable<typename __combined<__type152,__type150>::type>::type tmp___ = 0.0;
            {
              long  __target140006560035280 = nymax;
              for ( iy=0L; iy < __target140006560035280; iy += 1L)
              {
                {
                  long  __target140006560036792 = nxmax___;
                  for (long  ix___=0L; ix___ < __target140006560036792; ix___ += 1L)
                  {
                    tmp___ += (im1.fast(pythonic::types::make_tuple((iy + ny1dep), (ix___ + nx1dep))) * im0[pythonic::types::make_tuple((ny0dep + iy), (nx0dep + ix___))]);
                  }
                }
              }
              if (iy == __target140006560035280)
              iy -= 1L;
            }
            correl[pythonic::types::make_tuple(((xiy + disp_max) + 1L), ((xix___ + disp_max) + 1L))] = (pythonic::operator_::div(tmp___, (nxmax___ * nymax)));
          }
        }
      }
      if (xiy == __target140006560318576)
      xiy -= 1L;
    }
    ;
    return pythonic::types::make_tuple((correl * pythonic::__builtin__::getattr<pythonic::types::attr::SIZE>(im1)), pythonic::numpy::functor::sqrt{}((pythonic::numpy::functor::sum{}(pythonic::numpy::functor::square{}(im1)) * pythonic::numpy::functor::sum{}(pythonic::numpy::functor::square{}(im0)))));
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
typename __pythran_correl_pythran::correl_pythran::type<pythonic::types::ndarray<float,2>, pythonic::types::ndarray<float,2>, long>::result_type correl_pythran0(pythonic::types::ndarray<float,2>&& im0, pythonic::types::ndarray<float,2>&& im1, long&& disp_max) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_correl_pythran::correl_pythran()(im0, im1, disp_max);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_correl_pythran::correl_pythran::type<pythonic::types::ndarray<float,2>, pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>, long>::result_type correl_pythran1(pythonic::types::ndarray<float,2>&& im0, pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>&& im1, long&& disp_max) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_correl_pythran::correl_pythran()(im0, im1, disp_max);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_correl_pythran::correl_pythran::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>, pythonic::types::ndarray<float,2>, long>::result_type correl_pythran2(pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>&& im0, pythonic::types::ndarray<float,2>&& im1, long&& disp_max) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_correl_pythran::correl_pythran()(im0, im1, disp_max);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_correl_pythran::correl_pythran::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>, long>::result_type correl_pythran3(pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>&& im0, pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>&& im1, long&& disp_max) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_correl_pythran::correl_pythran()(im0, im1, disp_max);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}

static PyObject *
__pythran_wrap_correl_pythran0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"im0","im1","disp_max", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<float,2>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<float,2>>(args_obj[1]) && is_convertible<long>(args_obj[2]))
        return to_python(correl_pythran0(from_python<pythonic::types::ndarray<float,2>>(args_obj[0]), from_python<pythonic::types::ndarray<float,2>>(args_obj[1]), from_python<long>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_correl_pythran1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"im0","im1","disp_max", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<float,2>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[1]) && is_convertible<long>(args_obj[2]))
        return to_python(correl_pythran1(from_python<pythonic::types::ndarray<float,2>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[1]), from_python<long>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_correl_pythran2(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"im0","im1","disp_max", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<float,2>>(args_obj[1]) && is_convertible<long>(args_obj[2]))
        return to_python(correl_pythran2(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[0]), from_python<pythonic::types::ndarray<float,2>>(args_obj[1]), from_python<long>(args_obj[2])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_correl_pythran3(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[3+1];
    char const* keywords[] = {"im0","im1","disp_max", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OOO",
                                     (char**)keywords, &args_obj[0], &args_obj[1], &args_obj[2]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[1]) && is_convertible<long>(args_obj[2]))
        return to_python(correl_pythran3(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<float,2>>>(args_obj[1]), from_python<long>(args_obj[2])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_correl_pythran(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_correl_pythran0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_correl_pythran1(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_correl_pythran2(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_correl_pythran3(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "correl_pythran", "   correl_pythran(float32[:,:],float32[:,:],int)\n   correl_pythran(float32[:,:],float32[:,:].T,int)\n   correl_pythran(float32[:,:].T,float32[:,:],int)\n   correl_pythran(float32[:,:].T,float32[:,:].T,int)", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "correl_pythran",
    (PyCFunction)__pythran_wrapall_correl_pythran,
    METH_VARARGS | METH_KEYWORDS,
    "Correlations by hand using only numpy.\n\n    Supported prototypes:\n\n    - correl_pythran(float32[:,:], float32[:,:], int)\n    - correl_pythran(float32[:,:], float32[:,:].T, int)\n    - correl_pythran(float32[:,:].T, float32[:,:], int)\n    - correl_pythran(float32[:,:].T, float32[:,:].T, int)\n\n    Parameters\n    ----------\n\n    im0, im1 : images\n      input images : 2D matrix\n\n    disp_max : int\n      displacement max.\n\n    Notes\n    -------\n\n    im1_shape inf to im0_shape\n\n    Returns\n    -------\n\n    the computing correlation (size of computed correlation = disp_max*2 + 1)\n\n"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "correl_pythran",            /* m_name */
    "",         /* m_doc */
    -1,                  /* m_size */
    Methods,             /* m_methods */
    NULL,                /* m_reload */
    NULL,                /* m_traverse */
    NULL,                /* m_clear */
    NULL,                /* m_free */
  };
#define PYTHRAN_RETURN return theModule
#define PYTHRAN_MODULE_INIT(s) PyInit_##s
#else
#define PYTHRAN_RETURN return
#define PYTHRAN_MODULE_INIT(s) init##s
#endif
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(correl_pythran)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
__attribute__ ((externally_visible))
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(correl_pythran)(void) {
    #ifdef PYTHONIC_TYPES_NDARRAY_HPP
        import_array()
    #endif
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("correl_pythran",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.8.6",
                                      "2018-08-29 11:47:13.526065",
                                      "63f25d202b10780e3aeebf130858360fc11a860e53d43c415058da4805cd6952");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif