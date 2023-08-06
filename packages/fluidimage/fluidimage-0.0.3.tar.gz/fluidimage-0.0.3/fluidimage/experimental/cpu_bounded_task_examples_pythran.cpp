#define BOOST_SIMD_NO_STRICT_ALIASING 1
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/uint8.hpp>
#include <pythonic/include/types/ndarray.hpp>
#include <pythonic/include/types/numpy_texpr.hpp>
#include <pythonic/types/uint8.hpp>
#include <pythonic/types/ndarray.hpp>
#include <pythonic/types/numpy_texpr.hpp>
#include <pythonic/include/numpy/arange.hpp>
#include <pythonic/include/numpy/square.hpp>
#include <pythonic/include/numpy/multiply.hpp>
#include <pythonic/include/__builtin__/tuple.hpp>
#include <pythonic/numpy/arange.hpp>
#include <pythonic/numpy/square.hpp>
#include <pythonic/numpy/multiply.hpp>
#include <pythonic/__builtin__/tuple.hpp>
namespace __pythran_cpu_bounded_task_examples_pythran
{
  struct cpu2
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::multiply{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type1;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type2;
      typedef decltype(std::declval<__type0>()(std::declval<__type1>(), std::declval<__type2>())) __type3;
      typedef decltype(std::declval<__type0>()(std::declval<__type3>(), std::declval<__type2>())) __type4;
      typedef decltype(std::declval<__type0>()(std::declval<__type4>(), std::declval<__type2>())) __type5;
      typedef decltype(std::declval<__type0>()(std::declval<__type5>(), std::declval<__type2>())) __type6;
      typedef decltype(std::declval<__type0>()(std::declval<__type6>(), std::declval<__type2>())) __type7;
      typedef decltype(std::declval<__type0>()(std::declval<__type7>(), std::declval<__type2>())) __type8;
      typedef decltype(std::declval<__type0>()(std::declval<__type8>(), std::declval<__type2>())) __type9;
      typedef decltype(std::declval<__type0>()(std::declval<__type9>(), std::declval<__type2>())) __type10;
      typedef decltype(std::declval<__type0>()(std::declval<__type10>(), std::declval<__type2>())) __type11;
      typedef typename pythonic::returnable<decltype(std::declval<__type0>()(std::declval<__type11>(), std::declval<__type2>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 >
    typename type<argument_type0, argument_type1>::result_type operator()(argument_type0&& array1, argument_type1&& array2) const
    ;
  }  ;
  struct cpu1
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
      typedef decltype((std::declval<__type0>() * std::declval<__type1>())) __type2;
      typedef decltype((std::declval<__type2>() * std::declval<__type1>())) __type3;
      typedef decltype((std::declval<__type3>() * std::declval<__type1>())) __type4;
      typedef decltype((std::declval<__type4>() * std::declval<__type1>())) __type5;
      typedef decltype((std::declval<__type5>() * std::declval<__type1>())) __type6;
      typedef decltype((std::declval<__type6>() * std::declval<__type1>())) __type7;
      typedef decltype((std::declval<__type7>() * std::declval<__type1>())) __type8;
      typedef decltype((std::declval<__type8>() * std::declval<__type1>())) __type9;
      typedef decltype((std::declval<__type9>() * std::declval<__type1>())) __type10;
      typedef typename pythonic::assignable<decltype((std::declval<__type10>() * std::declval<__type1>()))>::type __type11;
      typedef typename pythonic::returnable<decltype(pythonic::types::make_tuple(std::declval<__type11>(), std::declval<__type11>()))>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 >
    typename type<argument_type0, argument_type1>::result_type operator()(argument_type0&& array1, argument_type1&& array2) const
    ;
  }  ;
  template <typename argument_type0 , typename argument_type1 >
  typename cpu2::type<argument_type0, argument_type1>::result_type cpu2::operator()(argument_type0&& array1, argument_type1&& array2) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::arange{})>::type>::type __type0;
    typedef long __type1;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type1>()))>::type __type2;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type3;
    typedef decltype(std::declval<__type3>()(std::declval<__type2>())) __type4;
    typedef decltype((std::declval<__type4>() * std::declval<__type2>())) __type5;
    typedef decltype((std::declval<__type5>() + std::declval<__type4>())) __type6;
    typedef decltype((std::declval<__type6>() + std::declval<__type1>())) __type7;
    typedef decltype((std::declval<__type2>() + std::declval<__type7>())) __type8;
    typedef typename __combined<__type2,__type8>::type __type9;
    typedef decltype(std::declval<__type3>()(std::declval<__type9>())) __type10;
    typedef decltype((std::declval<__type10>() * std::declval<__type9>())) __type11;
    typedef decltype((std::declval<__type11>() + std::declval<__type10>())) __type12;
    typedef decltype((std::declval<__type12>() + std::declval<__type1>())) __type13;
    typedef decltype((std::declval<__type9>() + std::declval<__type13>())) __type14;
    typedef typename __combined<__type9,__type14>::type __type15;
    typedef decltype(std::declval<__type3>()(std::declval<__type15>())) __type16;
    typedef decltype((std::declval<__type16>() * std::declval<__type15>())) __type17;
    typedef decltype((std::declval<__type17>() + std::declval<__type16>())) __type18;
    typedef decltype((std::declval<__type18>() + std::declval<__type1>())) __type19;
    typedef decltype((std::declval<__type15>() + std::declval<__type19>())) __type20;
    typedef typename __combined<__type15,__type20>::type __type21;
    typedef decltype(std::declval<__type3>()(std::declval<__type21>())) __type22;
    typedef decltype((std::declval<__type22>() * std::declval<__type21>())) __type23;
    typedef decltype((std::declval<__type23>() + std::declval<__type22>())) __type24;
    typedef decltype((std::declval<__type24>() + std::declval<__type1>())) __type25;
    typedef decltype((std::declval<__type21>() + std::declval<__type25>())) __type26;
    typedef typename __combined<__type21,__type26>::type __type27;
    typedef decltype(std::declval<__type3>()(std::declval<__type27>())) __type28;
    typedef decltype((std::declval<__type28>() * std::declval<__type27>())) __type29;
    typedef decltype((std::declval<__type29>() + std::declval<__type28>())) __type30;
    typedef decltype((std::declval<__type30>() + std::declval<__type1>())) __type31;
    typedef decltype((std::declval<__type27>() + std::declval<__type31>())) __type32;
    typedef typename __combined<__type27,__type32>::type __type33;
    typedef decltype(std::declval<__type3>()(std::declval<__type33>())) __type34;
    typedef decltype((std::declval<__type34>() * std::declval<__type33>())) __type35;
    typedef decltype((std::declval<__type35>() + std::declval<__type34>())) __type36;
    typedef decltype((std::declval<__type36>() + std::declval<__type1>())) __type37;
    typedef decltype((std::declval<__type33>() + std::declval<__type37>())) __type38;
    typedef typename __combined<__type33,__type38>::type __type39;
    typedef decltype(std::declval<__type3>()(std::declval<__type39>())) __type40;
    typedef decltype((std::declval<__type40>() * std::declval<__type39>())) __type41;
    typedef decltype((std::declval<__type41>() + std::declval<__type40>())) __type42;
    typedef decltype((std::declval<__type42>() + std::declval<__type1>())) __type43;
    typedef decltype((std::declval<__type39>() + std::declval<__type43>())) __type44;
    typedef typename __combined<__type39,__type44>::type __type45;
    typedef decltype(std::declval<__type3>()(std::declval<__type45>())) __type46;
    typedef decltype((std::declval<__type46>() * std::declval<__type45>())) __type47;
    typedef decltype((std::declval<__type47>() + std::declval<__type46>())) __type48;
    typedef decltype((std::declval<__type48>() + std::declval<__type1>())) __type49;
    typedef decltype((std::declval<__type45>() + std::declval<__type49>())) __type50;
    typedef typename __combined<__type45,__type50>::type __type51;
    typedef decltype(std::declval<__type3>()(std::declval<__type51>())) __type52;
    typedef decltype((std::declval<__type52>() * std::declval<__type51>())) __type53;
    typedef decltype((std::declval<__type53>() + std::declval<__type52>())) __type54;
    typedef decltype((std::declval<__type54>() + std::declval<__type1>())) __type55;
    typedef decltype((std::declval<__type51>() + std::declval<__type55>())) __type56;
    typedef typename __combined<__type51,__type56>::type __type57;
    typedef decltype(std::declval<__type3>()(std::declval<__type57>())) __type58;
    typedef decltype((std::declval<__type58>() * std::declval<__type57>())) __type59;
    typedef decltype((std::declval<__type59>() + std::declval<__type58>())) __type60;
    typedef decltype((std::declval<__type60>() + std::declval<__type1>())) __type61;
    typedef decltype((std::declval<__type57>() + std::declval<__type61>())) __type62;
    typedef typename pythonic::assignable<typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type1>()))>::type>::type __type63;
    typedef typename __combined<__type63,__type7>::type __type64;
    typedef typename __combined<__type64,__type13>::type __type65;
    typedef typename __combined<__type65,__type19>::type __type66;
    typedef typename __combined<__type66,__type25>::type __type67;
    typedef typename __combined<__type67,__type31>::type __type68;
    typedef typename __combined<__type68,__type37>::type __type69;
    typedef typename __combined<__type69,__type43>::type __type70;
    typedef typename __combined<__type70,__type49>::type __type71;
    typedef typename __combined<__type71,__type55>::type __type72;
    ;
    ;
    typename pythonic::assignable<typename __combined<__type57,__type62>::type>::type a = pythonic::numpy::functor::arange{}(100000000L);
    typename pythonic::assignable<typename __combined<__type72,__type61>::type>::type result = a;
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    return pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(pythonic::numpy::functor::multiply{}(array1, array2), array2), array2), array2), array2), array2), array2), array2), array2), array2);
  }
  template <typename argument_type0 , typename argument_type1 >
  typename cpu1::type<argument_type0, argument_type1>::result_type cpu1::operator()(argument_type0&& array1, argument_type1&& array2) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::arange{})>::type>::type __type0;
    typedef long __type1;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type1>()))>::type __type2;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type3;
    typedef decltype(std::declval<__type3>()(std::declval<__type2>())) __type4;
    typedef decltype((std::declval<__type4>() * std::declval<__type2>())) __type5;
    typedef decltype((std::declval<__type5>() + std::declval<__type4>())) __type6;
    typedef decltype((std::declval<__type6>() + std::declval<__type1>())) __type7;
    typedef decltype((std::declval<__type2>() + std::declval<__type7>())) __type8;
    typedef typename __combined<__type2,__type8>::type __type9;
    typedef decltype(std::declval<__type3>()(std::declval<__type9>())) __type10;
    typedef decltype((std::declval<__type10>() * std::declval<__type9>())) __type11;
    typedef decltype((std::declval<__type11>() + std::declval<__type10>())) __type12;
    typedef decltype((std::declval<__type12>() + std::declval<__type1>())) __type13;
    typedef decltype((std::declval<__type9>() + std::declval<__type13>())) __type14;
    typedef typename __combined<__type9,__type14>::type __type15;
    typedef decltype(std::declval<__type3>()(std::declval<__type15>())) __type16;
    typedef decltype((std::declval<__type16>() * std::declval<__type15>())) __type17;
    typedef decltype((std::declval<__type17>() + std::declval<__type16>())) __type18;
    typedef decltype((std::declval<__type18>() + std::declval<__type1>())) __type19;
    typedef decltype((std::declval<__type15>() + std::declval<__type19>())) __type20;
    typedef typename __combined<__type15,__type20>::type __type21;
    typedef decltype(std::declval<__type3>()(std::declval<__type21>())) __type22;
    typedef decltype((std::declval<__type22>() * std::declval<__type21>())) __type23;
    typedef decltype((std::declval<__type23>() + std::declval<__type22>())) __type24;
    typedef decltype((std::declval<__type24>() + std::declval<__type1>())) __type25;
    typedef decltype((std::declval<__type21>() + std::declval<__type25>())) __type26;
    typedef typename __combined<__type21,__type26>::type __type27;
    typedef decltype(std::declval<__type3>()(std::declval<__type27>())) __type28;
    typedef decltype((std::declval<__type28>() * std::declval<__type27>())) __type29;
    typedef decltype((std::declval<__type29>() + std::declval<__type28>())) __type30;
    typedef decltype((std::declval<__type30>() + std::declval<__type1>())) __type31;
    typedef decltype((std::declval<__type27>() + std::declval<__type31>())) __type32;
    typedef typename __combined<__type27,__type32>::type __type33;
    typedef decltype(std::declval<__type3>()(std::declval<__type33>())) __type34;
    typedef decltype((std::declval<__type34>() * std::declval<__type33>())) __type35;
    typedef decltype((std::declval<__type35>() + std::declval<__type34>())) __type36;
    typedef decltype((std::declval<__type36>() + std::declval<__type1>())) __type37;
    typedef decltype((std::declval<__type33>() + std::declval<__type37>())) __type38;
    typedef typename __combined<__type33,__type38>::type __type39;
    typedef decltype(std::declval<__type3>()(std::declval<__type39>())) __type40;
    typedef decltype((std::declval<__type40>() * std::declval<__type39>())) __type41;
    typedef decltype((std::declval<__type41>() + std::declval<__type40>())) __type42;
    typedef decltype((std::declval<__type42>() + std::declval<__type1>())) __type43;
    typedef decltype((std::declval<__type39>() + std::declval<__type43>())) __type44;
    typedef typename __combined<__type39,__type44>::type __type45;
    typedef decltype(std::declval<__type3>()(std::declval<__type45>())) __type46;
    typedef decltype((std::declval<__type46>() * std::declval<__type45>())) __type47;
    typedef decltype((std::declval<__type47>() + std::declval<__type46>())) __type48;
    typedef decltype((std::declval<__type48>() + std::declval<__type1>())) __type49;
    typedef decltype((std::declval<__type45>() + std::declval<__type49>())) __type50;
    typedef typename __combined<__type45,__type50>::type __type51;
    typedef decltype(std::declval<__type3>()(std::declval<__type51>())) __type52;
    typedef decltype((std::declval<__type52>() * std::declval<__type51>())) __type53;
    typedef decltype((std::declval<__type53>() + std::declval<__type52>())) __type54;
    typedef decltype((std::declval<__type54>() + std::declval<__type1>())) __type55;
    typedef decltype((std::declval<__type51>() + std::declval<__type55>())) __type56;
    typedef typename __combined<__type51,__type56>::type __type57;
    typedef decltype(std::declval<__type3>()(std::declval<__type57>())) __type58;
    typedef decltype((std::declval<__type58>() * std::declval<__type57>())) __type59;
    typedef decltype((std::declval<__type59>() + std::declval<__type58>())) __type60;
    typedef decltype((std::declval<__type60>() + std::declval<__type1>())) __type61;
    typedef decltype((std::declval<__type57>() + std::declval<__type61>())) __type62;
    typedef typename pythonic::assignable<typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type1>()))>::type>::type __type63;
    typedef typename __combined<__type63,__type7>::type __type64;
    typedef typename __combined<__type64,__type13>::type __type65;
    typedef typename __combined<__type65,__type19>::type __type66;
    typedef typename __combined<__type66,__type25>::type __type67;
    typedef typename __combined<__type67,__type31>::type __type68;
    typedef typename __combined<__type68,__type37>::type __type69;
    typedef typename __combined<__type69,__type43>::type __type70;
    typedef typename __combined<__type70,__type49>::type __type71;
    typedef typename __combined<__type71,__type55>::type __type72;
    ;
    ;
    typename pythonic::assignable<typename __combined<__type57,__type62>::type>::type a = pythonic::numpy::functor::arange{}(100000000L);
    typename pythonic::assignable<typename __combined<__type72,__type61>::type>::type result = a;
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    result += (((pythonic::numpy::functor::square{}(a) * a) + pythonic::numpy::functor::square{}(a)) + 2L);
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    ;
    typename pythonic::assignable<decltype(((((((((((array1 * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2))>::type array1___________ = ((((((((((array1 * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2) * array2);
    return pythonic::types::make_tuple(array1___________, array1___________);
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
typename __pythran_cpu_bounded_task_examples_pythran::cpu2::type<pythonic::types::ndarray<uint8_t,2>, pythonic::types::ndarray<uint8_t,2>>::result_type cpu20(pythonic::types::ndarray<uint8_t,2>&& array1, pythonic::types::ndarray<uint8_t,2>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu2()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu2::type<pythonic::types::ndarray<uint8_t,2>, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>::result_type cpu21(pythonic::types::ndarray<uint8_t,2>&& array1, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu2()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu2::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>, pythonic::types::ndarray<uint8_t,2>>::result_type cpu22(pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array1, pythonic::types::ndarray<uint8_t,2>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu2()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu2::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>::result_type cpu23(pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array1, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu2()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu1::type<pythonic::types::ndarray<uint8_t,2>, pythonic::types::ndarray<uint8_t,2>>::result_type cpu10(pythonic::types::ndarray<uint8_t,2>&& array1, pythonic::types::ndarray<uint8_t,2>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu1()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu1::type<pythonic::types::ndarray<uint8_t,2>, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>::result_type cpu11(pythonic::types::ndarray<uint8_t,2>&& array1, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu1()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu1::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>, pythonic::types::ndarray<uint8_t,2>>::result_type cpu12(pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array1, pythonic::types::ndarray<uint8_t,2>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu1()(array1, array2);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_cpu_bounded_task_examples_pythran::cpu1::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>::result_type cpu13(pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array1, pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>&& array2) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_cpu_bounded_task_examples_pythran::cpu1()(array1, array2);
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
__pythran_wrap_cpu20(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[1]))
        return to_python(cpu20(from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]), from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu21(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1]))
        return to_python(cpu21(from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu22(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[1]))
        return to_python(cpu22(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]), from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu23(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1]))
        return to_python(cpu23(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu10(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[1]))
        return to_python(cpu10(from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]), from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu11(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1]))
        return to_python(cpu11(from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu12(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<uint8_t,2>>(args_obj[1]))
        return to_python(cpu12(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]), from_python<pythonic::types::ndarray<uint8_t,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_cpu13(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"array1","array2", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1]))
        return to_python(cpu13(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<uint8_t,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_cpu2(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_cpu20(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu21(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu22(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu23(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "cpu2", "   cpu2(uint8[:,:],uint8[:,:])\n   cpu2(uint8[:,:],uint8[:,:].T)\n   cpu2(uint8[:,:].T,uint8[:,:])\n   cpu2(uint8[:,:].T,uint8[:,:].T)", args, kw);
                });
            }


            static PyObject *
            __pythran_wrapall_cpu1(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_cpu10(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu11(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu12(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_cpu13(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "cpu1", "   cpu1(uint8[:,:],uint8[:,:])\n   cpu1(uint8[:,:],uint8[:,:].T)\n   cpu1(uint8[:,:].T,uint8[:,:])\n   cpu1(uint8[:,:].T,uint8[:,:].T)", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "cpu2",
    (PyCFunction)__pythran_wrapall_cpu2,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - cpu2(uint8[:,:], uint8[:,:])\n    - cpu2(uint8[:,:], uint8[:,:].T)\n    - cpu2(uint8[:,:].T, uint8[:,:])\n    - cpu2(uint8[:,:].T, uint8[:,:].T)"},{
    "cpu1",
    (PyCFunction)__pythran_wrapall_cpu1,
    METH_VARARGS | METH_KEYWORDS,
    "Supported prototypes:\n\n    - cpu1(uint8[:,:], uint8[:,:])\n    - cpu1(uint8[:,:], uint8[:,:].T)\n    - cpu1(uint8[:,:].T, uint8[:,:])\n    - cpu1(uint8[:,:].T, uint8[:,:].T)"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "cpu_bounded_task_examples_pythran",            /* m_name */
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
PYTHRAN_MODULE_INIT(cpu_bounded_task_examples_pythran)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
__attribute__ ((externally_visible))
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(cpu_bounded_task_examples_pythran)(void) {
    #ifdef PYTHONIC_TYPES_NDARRAY_HPP
        import_array()
    #endif
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("cpu_bounded_task_examples_pythran",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.8.6",
                                      "2018-08-29 11:47:17.766070",
                                      "0de630c5e656a38a48261eb6225a8395780a9f62764cd1d3de42a857701c77e1");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif