
tst_include = include_directories('../include', '../src', '../deps')
getopt = '../deps/getopt.c'
tinycthread = '../deps/tinycthread.c'

#@ Flags
c_flags = []
if is_posix
  c_flags += '-D_DEFAULT_SOURCE'
endif
if sys_os == 'darwin'
  c_flags += '-D_DARWIN_C_SOURCE'
endif

if sys_os == 'windows' and sys_cc.get_argument_syntax() == 'gcc'
  c_flags += '-D_USE_MATH_DEFINES'
endif

#@ Test executables
tests = {
  'allocator': [],
  'clipboard': [getopt],
  'events': [getopt],
  'msaa': [getopt],
  'glfwinfo': [getopt],
  'iconify': [getopt],
  'monitors': [getopt],
  'reopen': [],
  'cursor': [],
  'empty': [tinycthread],
  'gamma': [],
  'icon': [],
  'inputlag': [getopt],
  'joysticks': [],
  'tearing': [],
  'threads': [tinycthread],
  'timeout': [],
  'title': [],
  'triangle-vulkan': [],
  'window': [getopt],
}
foreach name, dep : tests
  src = [name + '.c', dep]
  executable(
    name,
    src,
    include_directories: tst_include,
    c_args: c_flags,
    dependencies: [glfw_dep, deps],
    build_by_default: true,
    install: get_option('install'),
    install_dir: opt_libdir / 'GLFW' / 'tests',
  )
endforeach
