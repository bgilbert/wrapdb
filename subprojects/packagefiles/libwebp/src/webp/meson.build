config_h = configure_file(
  configuration: cdata,
  input: 'config.h.meson',
  output: 'config.h',
)

headers = []

if build_libwebp.found()
  headers += ['decode.h', 'encode.h', 'types.h']
endif

if build_libwebpdecoder.found()
  headers += ['decode.h', 'types.h']
endif

if build_libwebpdemux.found()
  headers += ['demux.h', 'mux_types.h']
endif

if build_libwebpmux.found()
  headers += ['mux.h', 'mux_types.h']
endif

install_headers(
  headers,
  subdir: 'webp',
)
