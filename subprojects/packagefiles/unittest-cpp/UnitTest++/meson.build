unittest_cpp_src += files(
  'AssertException.cpp',
  'Checks.cpp',
  'CompositeTestReporter.cpp',
  'CurrentTest.cpp',
  'DeferredTestReporter.cpp',
  'DeferredTestResult.cpp',
  'MemoryOutStream.cpp',
  'ReportAssert.cpp',
  'RequiredCheckException.cpp',
  'RequiredCheckTestReporter.cpp',
  'Test.cpp',
  'TestDetails.cpp',
  'TestList.cpp',
  'TestReporter.cpp',
  'TestReporterStdout.cpp',
  'TestResults.cpp',
  'TestRunner.cpp',
  'ThrowingTestReporter.cpp',
  'TimeConstraint.cpp',
  'XmlTestReporter.cpp',
)

if host_machine.system() == 'windows'
  subdir('Win32')
else
  subdir('Posix')
endif
