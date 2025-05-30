# TODO(rg): Add handling of utest_main2 as per CMakeLists
sources_utest = [
  'utest_main.c',
  'test_min.c',
  'test_amax.c',
  'test_ismin.c',
  'test_rotmg.c',
  'test_axpy.c',
  'test_dotu.c',
  'test_dsdot.c',
  'test_swap.c',
  'test_rot.c',
  'test_dnrm2.c',
  'test_zscal.c',
  'test_amin.c',
  'test_axpby.c',
]

dir_ext = 'test_extensions'
sources_utest_ext = [
  'utest_main.c',
  dir_ext / 'xerbla.c',
  dir_ext / 'common.c',
  dir_ext / 'test_isamin.c',
  dir_ext / 'test_idamin.c',
  dir_ext / 'test_icamin.c',
  dir_ext / 'test_izamin.c',
  dir_ext / 'test_ssum.c',
  dir_ext / 'test_dsum.c',
  dir_ext / 'test_scsum.c',
  dir_ext / 'test_dzsum.c',
  dir_ext / 'test_saxpby.c',
  dir_ext / 'test_daxpby.c',
  dir_ext / 'test_caxpby.c',
  dir_ext / 'test_zaxpby.c',
  dir_ext / 'test_zaxpyc.c',
  dir_ext / 'test_caxpyc.c',
  dir_ext / 'test_samin.c',
  dir_ext / 'test_damin.c',
  dir_ext / 'test_scamin.c',
  dir_ext / 'test_dzamin.c',
  dir_ext / 'test_scamax.c',
  dir_ext / 'test_dzamax.c',
  dir_ext / 'test_drotmg.c',
  dir_ext / 'test_srotmg.c',
  dir_ext / 'test_zrotg.c',
  dir_ext / 'test_crotg.c',
  dir_ext / 'test_crot.c',
  dir_ext / 'test_zrot.c',
  dir_ext / 'test_zscal.c',
  dir_ext / 'test_cscal.c',
  dir_ext / 'test_domatcopy.c',
  dir_ext / 'test_somatcopy.c',
  dir_ext / 'test_zomatcopy.c',
  dir_ext / 'test_comatcopy.c',
  dir_ext / 'test_simatcopy.c',
  dir_ext / 'test_dimatcopy.c',
  dir_ext / 'test_cimatcopy.c',
  dir_ext / 'test_zimatcopy.c',
  dir_ext / 'test_sgeadd.c',
  dir_ext / 'test_dgeadd.c',
  dir_ext / 'test_cgeadd.c',
  dir_ext / 'test_zgeadd.c',
  dir_ext / 'test_cgemv_t.c',
  dir_ext / 'test_zgemv_t.c',
  dir_ext / 'test_cgemv_n.c',
  dir_ext / 'test_zgemv_n.c',
  dir_ext / 'test_sgemmt.c',
  dir_ext / 'test_dgemmt.c',
  dir_ext / 'test_cgemmt.c',
  dir_ext / 'test_zgemmt.c',
  dir_ext / 'test_ztrmv.c',
  dir_ext / 'test_ctrmv.c',
  dir_ext / 'test_ztrsv.c',
  dir_ext / 'test_ctrsv.c',
  dir_ext / 'test_zgemm.c',
  dir_ext / 'test_cgemm.c',
  dir_ext / 'test_zgbmv.c',
  dir_ext / 'test_cgbmv.c',
  dir_ext / 'test_zspmv.c',
  dir_ext / 'test_cspmv.c',
  dir_ext / 'test_zsbmv.c',
  dir_ext / 'test_csbmv.c',
]

utest_inc = _inc + [include_directories('.')]

# TODO(rg): Can this be fixed?
# ‘strsignal’ in utest, seems like a false positive
_utest_nowarn = cc.get_supported_arguments('-Wno-implicit-function-declaration')

openblas_utest_exec = executable(
  'openblas_utest',
  sources: sources_utest,
  link_with: openblas,
  dependencies: threads_dep,
  include_directories: utest_inc,
  c_args: _cargs + _utest_nowarn,
)

openblas_utest_ext_exec = executable(
  'openblas_utest_ext',
  sources: sources_utest_ext,
  link_with: openblas,
  dependencies: threads_dep,
  # This hack is required as `utest/test_extensions/common.c` needs
  # `common.h` from the source root, not `utest/test_extensions` directory
  # one. Also, `config.h` is needed that lives in the build directory.
  implicit_include_directories: false,
  c_args: _cargs + _utest_nowarn + [f'-I@_msproot@', f'-I@_mbproot@'],
)

test('openblas_utest_tests', openblas_utest_exec)
test('openblas_utest_tests', openblas_utest_ext_exec)
