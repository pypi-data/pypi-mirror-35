#define BOOST_SIMD_NO_STRICT_ALIASING 1
#include <pythonic/core.hpp>
#include <pythonic/python/core.hpp>
#include <pythonic/types/bool.hpp>
#include <pythonic/types/int.hpp>
#ifdef _OPENMP
#include <omp.h>
#endif
#include <pythonic/include/types/float64.hpp>
#include <pythonic/include/types/ndarray.hpp>
#include <pythonic/include/types/numpy_texpr.hpp>
#include <pythonic/types/ndarray.hpp>
#include <pythonic/types/float64.hpp>
#include <pythonic/types/numpy_texpr.hpp>
#include <pythonic/include/types/str.hpp>
#include <pythonic/include/operator_/ne.hpp>
#include <pythonic/include/numpy/log.hpp>
#include <pythonic/include/__builtin__/enumerate.hpp>
#include <pythonic/include/types/slice.hpp>
#include <pythonic/include/operator_/div.hpp>
#include <pythonic/include/__builtin__/assert.hpp>
#include <pythonic/include/numpy/square.hpp>
#include <pythonic/include/numpy/ones.hpp>
#include <pythonic/include/numpy/empty.hpp>
#include <pythonic/include/operator_/eq.hpp>
#include <pythonic/include/__builtin__/getattr.hpp>
#include <pythonic/include/__builtin__/tuple.hpp>
#include <pythonic/include/numpy/zeros.hpp>
#include <pythonic/include/__builtin__/range.hpp>
#include <pythonic/include/operator_/idiv.hpp>
#include <pythonic/types/str.hpp>
#include <pythonic/operator_/ne.hpp>
#include <pythonic/numpy/log.hpp>
#include <pythonic/__builtin__/enumerate.hpp>
#include <pythonic/types/slice.hpp>
#include <pythonic/operator_/div.hpp>
#include <pythonic/__builtin__/assert.hpp>
#include <pythonic/numpy/square.hpp>
#include <pythonic/numpy/ones.hpp>
#include <pythonic/numpy/empty.hpp>
#include <pythonic/operator_/eq.hpp>
#include <pythonic/__builtin__/getattr.hpp>
#include <pythonic/__builtin__/tuple.hpp>
#include <pythonic/numpy/zeros.hpp>
#include <pythonic/__builtin__/range.hpp>
#include <pythonic/operator_/idiv.hpp>
namespace __pythran_tps_pythran
{
  struct compute_tps_matrix
  {
    typedef void callable;
    typedef void pure;
    template <typename argument_type0 , typename argument_type1 >
    struct type
    {
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::empty{})>::type>::type __type0;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
      typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type1>())) __type2;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type2>::type>::type>::type __type3;
      typedef long __type4;
      typedef decltype((std::declval<__type3>() + std::declval<__type4>())) __type5;
      typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type6;
      typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type6>())) __type7;
      typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type7>::type>::type>::type __type8;
      typedef decltype((std::declval<__type5>() + std::declval<__type8>())) __type9;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type7>::type>::type>::type __type10;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type9>(), std::declval<__type10>())) __type11;
      typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type11>()))>::type __type12;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type13;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type3>(), std::declval<__type10>())) __type14;
      typedef typename pythonic::assignable<decltype(std::declval<__type13>()(std::declval<__type14>()))>::type __type15;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::enumerate{})>::type>::type __type16;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type17;
      typedef decltype(std::declval<__type17>()(std::declval<__type8>())) __type18;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type18>::type::iterator>::value_type>::type __type19;
      typedef decltype(std::declval<__type1>()[std::declval<__type19>()]) __type20;
      typedef decltype(std::declval<__type16>()(std::declval<__type20>())) __type21;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type21>::type::iterator>::value_type>::type __type22;
      typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type22>::type>::type>::type __type23;
      typedef decltype(std::declval<__type6>()[std::declval<__type19>()]) __type24;
      typedef decltype(std::declval<__type16>()(std::declval<__type24>())) __type25;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type25>::type::iterator>::value_type>::type __type26;
      typedef typename std::tuple_element<0,typename std::remove_reference<__type26>::type>::type __type27;
      typedef typename pythonic::lazy<__type27>::type __type28;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type23>(), std::declval<__type28>())) __type29;
      typedef indexable<__type29> __type30;
      typedef typename __combined<__type15,__type30>::type __type31;
      typedef decltype(std::declval<__type17>()(std::declval<__type3>())) __type32;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type32>::type::iterator>::value_type>::type __type33;
      typedef typename __combined<__type23,__type33>::type __type34;
      typedef decltype(std::declval<__type17>()(std::declval<__type10>())) __type35;
      typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type35>::type::iterator>::value_type>::type __type36;
      typedef decltype(pythonic::types::make_tuple(std::declval<__type34>(), std::declval<__type36>())) __type37;
      typedef indexable<__type37> __type38;
      typedef typename __combined<__type31,__type38>::type __type39;
      typedef typename __combined<__type39,__type30>::type __type40;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type41;
      typedef typename std::tuple_element<1,typename std::remove_reference<__type26>::type>::type __type42;
      typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type22>::type>::type>::type __type43;
      typedef decltype((std::declval<__type42>() - std::declval<__type43>())) __type44;
      typedef decltype(std::declval<__type41>()(std::declval<__type44>())) __type45;
      typedef container<typename std::remove_reference<__type45>::type> __type46;
      typedef typename __combined<__type40,__type46>::type __type47;
      typedef typename __combined<__type31,__type46>::type __type48;
      typedef typename pythonic::assignable<decltype(std::declval<__type48>()[std::declval<__type37>()])>::type __type49;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::log{})>::type>::type __type50;
      typedef decltype(std::declval<__type50>()(std::declval<__type49>())) __type51;
      typedef decltype((std::declval<__type49>() * std::declval<__type51>())) __type52;
      typedef decltype((pythonic::operator_::div(std::declval<__type52>(), std::declval<__type4>()))) __type53;
      typedef container<typename std::remove_reference<__type53>::type> __type54;
      typedef typename __combined<__type47,__type54>::type __type55;
      typedef typename __combined<__type55,__type38>::type __type56;
      typedef typename __combined<__type56,__type54>::type __type57;
      typedef container<typename std::remove_reference<__type57>::type> __type58;
      typedef typename __combined<__type12,__type58>::type __type59;
      typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::ones{})>::type>::type __type60;
      typedef decltype(std::declval<__type60>()(std::declval<__type10>())) __type61;
      typedef container<typename std::remove_reference<__type61>::type> __type62;
      typedef typename __combined<__type59,__type62>::type __type63;
      typedef container<typename std::remove_reference<__type6>::type> __type64;
      typedef typename pythonic::returnable<typename __combined<__type63,__type64>::type>::type result_type;
    }  
    ;
    template <typename argument_type0 , typename argument_type1 >
    typename type<argument_type0, argument_type1>::result_type operator()(argument_type0&& new_pos, argument_type1&& centers) const
    ;
  }  ;
  template <typename argument_type0 , typename argument_type1 >
  typename compute_tps_matrix::type<argument_type0, argument_type1>::result_type compute_tps_matrix::operator()(argument_type0&& new_pos, argument_type1&& centers) const
  {
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::zeros{})>::type>::type __type0;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type1>::type>::type __type1;
    typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type1>())) __type2;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type2>::type>::type>::type __type3;
    typedef typename std::remove_cv<typename std::remove_reference<argument_type0>::type>::type __type4;
    typedef decltype(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(std::declval<__type4>())) __type5;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type5>::type>::type>::type __type6;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type3>(), std::declval<__type6>())) __type7;
    typedef typename pythonic::assignable<decltype(std::declval<__type0>()(std::declval<__type7>()))>::type __type8;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::enumerate{})>::type>::type __type9;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::__builtin__::functor::range{})>::type>::type __type10;
    typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type5>::type>::type>::type __type11;
    typedef decltype(std::declval<__type10>()(std::declval<__type11>())) __type12;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type12>::type::iterator>::value_type>::type __type13;
    typedef decltype(std::declval<__type1>()[std::declval<__type13>()]) __type14;
    typedef decltype(std::declval<__type9>()(std::declval<__type14>())) __type15;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type15>::type::iterator>::value_type>::type __type16;
    typedef typename pythonic::assignable<typename std::tuple_element<0,typename std::remove_reference<__type16>::type>::type>::type __type17;
    typedef decltype(std::declval<__type4>()[std::declval<__type13>()]) __type18;
    typedef decltype(std::declval<__type9>()(std::declval<__type18>())) __type19;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type19>::type::iterator>::value_type>::type __type20;
    typedef typename std::tuple_element<0,typename std::remove_reference<__type20>::type>::type __type21;
    typedef typename pythonic::lazy<__type21>::type __type22;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type17>(), std::declval<__type22>())) __type23;
    typedef indexable<__type23> __type24;
    typedef typename __combined<__type8,__type24>::type __type25;
    typedef decltype(std::declval<__type10>()(std::declval<__type3>())) __type26;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type26>::type::iterator>::value_type>::type __type27;
    typedef typename __combined<__type17,__type27>::type __type28;
    typedef decltype(std::declval<__type10>()(std::declval<__type6>())) __type29;
    typedef typename std::remove_cv<typename std::iterator_traits<typename std::remove_reference<__type29>::type::iterator>::value_type>::type __type30;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type28>(), std::declval<__type30>())) __type31;
    typedef indexable<__type31> __type32;
    typedef typename __combined<__type25,__type32>::type __type33;
    typedef typename __combined<__type33,__type24>::type __type34;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::square{})>::type>::type __type35;
    typedef typename std::tuple_element<1,typename std::remove_reference<__type20>::type>::type __type36;
    typedef typename pythonic::assignable<typename std::tuple_element<1,typename std::remove_reference<__type16>::type>::type>::type __type37;
    typedef decltype((std::declval<__type36>() - std::declval<__type37>())) __type38;
    typedef decltype(std::declval<__type35>()(std::declval<__type38>())) __type39;
    typedef container<typename std::remove_reference<__type39>::type> __type40;
    typedef typename __combined<__type34,__type40>::type __type41;
    typedef typename __combined<__type25,__type40>::type __type42;
    typedef typename pythonic::assignable<decltype(std::declval<__type42>()[std::declval<__type31>()])>::type __type43;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::log{})>::type>::type __type44;
    typedef decltype(std::declval<__type44>()(std::declval<__type43>())) __type45;
    typedef decltype((std::declval<__type43>() * std::declval<__type45>())) __type46;
    typedef long __type47;
    typedef decltype((pythonic::operator_::div(std::declval<__type46>(), std::declval<__type47>()))) __type48;
    typedef container<typename std::remove_reference<__type48>::type> __type49;
    typedef typename __combined<__type41,__type49>::type __type50;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::empty{})>::type>::type __type51;
    typedef decltype((std::declval<__type3>() + std::declval<__type47>())) __type52;
    typedef decltype((std::declval<__type52>() + std::declval<__type11>())) __type53;
    typedef decltype(pythonic::types::make_tuple(std::declval<__type53>(), std::declval<__type6>())) __type54;
    typedef typename pythonic::assignable<decltype(std::declval<__type51>()(std::declval<__type54>()))>::type __type55;
    typedef typename __combined<__type50,__type32>::type __type56;
    typedef typename __combined<__type56,__type49>::type __type57;
    typedef container<typename std::remove_reference<__type57>::type> __type58;
    typedef typename __combined<__type55,__type58>::type __type59;
    typedef typename std::remove_cv<typename std::remove_reference<decltype(pythonic::numpy::functor::ones{})>::type>::type __type60;
    typedef decltype(std::declval<__type60>()(std::declval<__type6>())) __type61;
    typedef container<typename std::remove_reference<__type61>::type> __type62;
    typedef typename __combined<__type59,__type62>::type __type63;
    typedef container<typename std::remove_reference<__type4>::type> __type64;
    typename pythonic::assignable<typename __combined<__type17,__type27>::type>::type ic;
    typename pythonic::assignable<decltype(std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(new_pos)))>::type d = std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(new_pos));
    typename pythonic::assignable<decltype(std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(new_pos)))>::type nb_new_pos = std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(new_pos));
    ;
    typename pythonic::assignable<decltype(std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(centers)))>::type nb_centers = std::get<1>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(centers));
    pythonic::pythran_assert((pythonic::operator_::eq(d, std::get<0>(pythonic::__builtin__::getattr<pythonic::types::attr::SHAPE>(centers)))));
    typename pythonic::assignable<typename __combined<__type50,__type32>::type>::type EM = pythonic::numpy::functor::zeros{}(pythonic::types::make_tuple(nb_centers, nb_new_pos));
    {
      long  __target140006559571528 = d;
      for (long  ind_d=0L; ind_d < __target140006559571528; ind_d += 1L)
      {
        {
          for (auto&& __tuple0: pythonic::__builtin__::functor::enumerate{}(centers.fast(ind_d)))
          {
            typename pythonic::assignable<decltype(std::get<1>(__tuple0))>::type center = std::get<1>(__tuple0);
            ic = std::get<0>(__tuple0);
            {
              for (auto&& __tuple1: pythonic::__builtin__::functor::enumerate{}(new_pos.fast(ind_d)))
              {
                ;
                typename pythonic::lazy<decltype(std::get<0>(__tuple1))>::type inp = std::get<0>(__tuple1);
                EM[pythonic::types::make_tuple(ic, inp)] += pythonic::numpy::functor::square{}((std::get<1>(__tuple1) - center));
              }
            }
          }
        }
      }
    }
    {
      long  __target140006559432832 = nb_centers;
      for ( ic=0L; ic < __target140006559432832; ic += 1L)
      {
        {
          long  __target140006559548136 = nb_new_pos;
          for (long  inp_=0L; inp_ < __target140006559548136; inp_ += 1L)
          {
            typename pythonic::assignable<typename pythonic::assignable<decltype(std::declval<__type42>()[std::declval<__type31>()])>::type>::type tmp = EM[pythonic::types::make_tuple(ic, inp_)];
            if ((pythonic::operator_::ne(tmp, 0L)))
            {
              EM[pythonic::types::make_tuple(ic, inp_)] = (pythonic::operator_::div((tmp * pythonic::numpy::functor::log{}(tmp)), 2L));
            }
          }
        }
      }
      if (ic == __target140006559432832)
      ic -= 1L;
    }
    typename pythonic::assignable<typename __combined<__type63,__type64>::type>::type EM_ret = pythonic::numpy::functor::empty{}(pythonic::types::make_tuple(((nb_centers + 1L) + d), nb_new_pos));
    EM_ret(pythonic::types::contiguous_slice(pythonic::__builtin__::None,nb_centers),pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)) = EM;
    EM_ret(nb_centers,pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)) = pythonic::numpy::functor::ones{}(nb_new_pos);
    EM_ret(pythonic::types::contiguous_slice((nb_centers + 1L),((nb_centers + 1L) + d)),pythonic::types::contiguous_slice(pythonic::__builtin__::None,pythonic::__builtin__::None)) = new_pos;
    return EM_ret;
  }
}
#include <pythonic/python/exception_handler.hpp>
#ifdef ENABLE_PYTHON_MODULE
typename __pythran_tps_pythran::compute_tps_matrix::type<pythonic::types::ndarray<double,2>, pythonic::types::ndarray<double,2>>::result_type compute_tps_matrix0(pythonic::types::ndarray<double,2>&& new_pos, pythonic::types::ndarray<double,2>&& centers) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_tps_pythran::compute_tps_matrix()(new_pos, centers);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_tps_pythran::compute_tps_matrix::type<pythonic::types::ndarray<double,2>, pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>::result_type compute_tps_matrix1(pythonic::types::ndarray<double,2>&& new_pos, pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>&& centers) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_tps_pythran::compute_tps_matrix()(new_pos, centers);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_tps_pythran::compute_tps_matrix::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>, pythonic::types::ndarray<double,2>>::result_type compute_tps_matrix2(pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>&& new_pos, pythonic::types::ndarray<double,2>&& centers) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_tps_pythran::compute_tps_matrix()(new_pos, centers);
                                PyEval_RestoreThread(_save);
                                return res;
                            }
                            catch(...) {
                                PyEval_RestoreThread(_save);
                                throw;
                            }
                            ;
}
typename __pythran_tps_pythran::compute_tps_matrix::type<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>, pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>::result_type compute_tps_matrix3(pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>&& new_pos, pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>&& centers) 
{
  
                            PyThreadState *_save = PyEval_SaveThread();
                            try {
                                auto res = __pythran_tps_pythran::compute_tps_matrix()(new_pos, centers);
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
__pythran_wrap_compute_tps_matrix0(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"new_pos","centers", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,2>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,2>>(args_obj[1]))
        return to_python(compute_tps_matrix0(from_python<pythonic::types::ndarray<double,2>>(args_obj[0]), from_python<pythonic::types::ndarray<double,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_tps_matrix1(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"new_pos","centers", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::ndarray<double,2>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[1]))
        return to_python(compute_tps_matrix1(from_python<pythonic::types::ndarray<double,2>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_tps_matrix2(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"new_pos","centers", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[0]) && is_convertible<pythonic::types::ndarray<double,2>>(args_obj[1]))
        return to_python(compute_tps_matrix2(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[0]), from_python<pythonic::types::ndarray<double,2>>(args_obj[1])));
    else {
        return nullptr;
    }
}

static PyObject *
__pythran_wrap_compute_tps_matrix3(PyObject *self, PyObject *args, PyObject *kw)
{
    PyObject* args_obj[2+1];
    char const* keywords[] = {"new_pos","centers", nullptr};
    if(! PyArg_ParseTupleAndKeywords(args, kw, "OO",
                                     (char**)keywords, &args_obj[0], &args_obj[1]))
        return nullptr;
    if(is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[0]) && is_convertible<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[1]))
        return to_python(compute_tps_matrix3(from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[0]), from_python<pythonic::types::numpy_texpr<pythonic::types::ndarray<double,2>>>(args_obj[1])));
    else {
        return nullptr;
    }
}

            static PyObject *
            __pythran_wrapall_compute_tps_matrix(PyObject *self, PyObject *args, PyObject *kw)
            {
                return pythonic::handle_python_exception([self, args, kw]()
                -> PyObject* {

if(PyObject* obj = __pythran_wrap_compute_tps_matrix0(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_tps_matrix1(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_tps_matrix2(self, args, kw))
    return obj;
PyErr_Clear();


if(PyObject* obj = __pythran_wrap_compute_tps_matrix3(self, args, kw))
    return obj;
PyErr_Clear();

                return pythonic::python::raise_invalid_argument(
                               "compute_tps_matrix", "   compute_tps_matrix(float64[:,:],float64[:,:])\n   compute_tps_matrix(float64[:,:],float64[:,:].T)\n   compute_tps_matrix(float64[:,:].T,float64[:,:])\n   compute_tps_matrix(float64[:,:].T,float64[:,:].T)", args, kw);
                });
            }


static PyMethodDef Methods[] = {
    {
    "compute_tps_matrix",
    (PyCFunction)__pythran_wrapall_compute_tps_matrix,
    METH_VARARGS | METH_KEYWORDS,
    "calculate the thin plate spline (tps) interpolation at a set of points\n\n    Supported prototypes:\n\n    - compute_tps_matrix(float64[:,:], float64[:,:])\n    - compute_tps_matrix(float64[:,:], float64[:,:].T)\n    - compute_tps_matrix(float64[:,:].T, float64[:,:])\n    - compute_tps_matrix(float64[:,:].T, float64[:,:].T)\n\n    Parameters\n    ----------\n\n    dsites: np.array\n        ``[nb_dim, M]`` array representing the postions of the M\n        'observation' sites, with nb_dim the space dimension.\n\n    centers: np.array\n        ``[nb_dim, N]`` array representing the postions of the N centers,\n        sources of the tps.\n\n    Returns\n    -------\n\n    EM : np.array\n        ``[(N+nb_dim), M]`` matrix representing the contributions at the M sites.\n\n        From unit sources located at each of the N centers, +\n        (nb_dim+1) columns representing the contribution of the linear\n        gradient part.\n\n    Notes\n    -----\n\n    >>> U_interp = np.dot(U_tps, EM)\n\n"},
    {NULL, NULL, 0, NULL}
};


#if PY_MAJOR_VERSION >= 3
  static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "tps_pythran",            /* m_name */
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
PYTHRAN_MODULE_INIT(tps_pythran)(void)
#ifndef _WIN32
__attribute__ ((visibility("default")))
__attribute__ ((externally_visible))
#endif
;
PyMODINIT_FUNC
PYTHRAN_MODULE_INIT(tps_pythran)(void) {
    #ifdef PYTHONIC_TYPES_NDARRAY_HPP
        import_array()
    #endif
    #if PY_MAJOR_VERSION >= 3
    PyObject* theModule = PyModule_Create(&moduledef);
    #else
    PyObject* theModule = Py_InitModule3("tps_pythran",
                                         Methods,
                                         ""
    );
    #endif
    if(! theModule)
        PYTHRAN_RETURN;
    PyObject * theDoc = Py_BuildValue("(sss)",
                                      "0.8.6",
                                      "2018-08-29 11:47:14.056845",
                                      "e6b80bc6b4ad5f83ed9756bf289979123960cb66de131867efb4b8de4f20af42");
    if(! theDoc)
        PYTHRAN_RETURN;
    PyModule_AddObject(theModule,
                       "__pythran__",
                       theDoc);


    PYTHRAN_RETURN;
}

#endif