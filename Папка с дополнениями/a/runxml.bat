@if /%1 == / Goto Simplest
XMLTest 192.168.23.163:1995 %1
@goto end
:Simplest
XMLTest 192.168.23.163:1995 test.xml
XMLTest 192.168.23.163:1995 .LastResult
:end
@pause