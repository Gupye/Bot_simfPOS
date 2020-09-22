@if /%1 == / Goto Simplest
XMLTest 127.0.0.1:1995 %1
@goto end
:Simplest
XMLTest 127.0.0.1:1995 test.xml
XMLTest 127.0.0.1:1995 .LastResult
:end
@pause