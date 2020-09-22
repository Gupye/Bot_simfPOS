����������⢨� � ���ᮢ� �ࢥ஬ � ������� XML ����ᮢ-�⢥⮢
����
1) �������� ����䥩� "XML Interface for Windows" �� �������� "���ன�⢠" � �ࢥ� � ���⠢��� ����
2) ᮧ���� ��⨢�� ����� � �ࠢ�筨�� "����䥩��"
3) ����� ᮧ���� ᢮� ������ �� ��ࠧ栬 ����⮢, ᮤ�ঠ�� � �������� XML
4) ��뢠�� �१ RK7XML.dll, ����䥩�� ����� RK7XMLi.pas

  �㭪�� CallRK7XMLRPC ��ࠬ����:
  AddressName - ����:����
  Request - XML �����
  RequestSize - ����� XML �����
  ResultFile - ��� 䠩��, �㤠 ᢠ���� १����
  ErrorBuf - �㤠 ����� ������� �訡�� �裡 � �.�.
  ErrorBufSize - ࠧ��� ErrorBuf

  �㭪�� CallRK7XMLRPCToStream - � �� ᠬ��, �� १���� ���� � IStream
  ��ࠬ����:
  AddressName - ����:����
  Request - XML �����
  RequestSize - ����� XML �����
  ResultStream - IStream - ��⮪, �㤠 ᢠ���� १����
  ErrorBuf - �㤠 ����� ������� �訡�� �裡 � �.�.
  ErrorBufSize - ࠧ��� ErrorBuf

  �㭪�� SetUseTempFileLimit - ������ �����, �� ����襬 ࠧ��� १���� �㤥� ᮧ��� �६���� 䠩�. �� 㬮�砭�� - 1000000.

  �㭪�� GetDLLVersion - ������� ����� DLL

  �㭪�� SetCryptKey - ��⠭����� ���� ��� ��஢���� (����� ���� ࠧ�� ��� ࠧ��� ���ᮢ�� �ࢥ஢, ��⠭���������� � ��ࠬ��� XML ����䥩�)


����� ��⮪��� 2 �।�����祭� ��� �����⢫���� ����஫� �� �믮������� ������ �ࢥ஬. � ��諮� ���ᨨ �뫮 ���������� 㧭���, �믮������ �� ��᫥���� �����, �᫨ �������� ࠧ�� �裡 ��᫥ ��砫� ��ࠡ�⪨ �����.
����� ��� �⮣� ������� ���� �㭪樨 GetLastXMLResult � GetLastXMLResultToStream. �᫨ �⢥� ��᫥ �믮������ ����� �� 㤠���� ��ࠢ���, �� �࠭���� �� �ࢥ� ������ �� ᯥ樠�쭮�� ����� (�� �맮�� ��� �㭪権) ��� �� ᫥���饣� �����. �᫨ �⢥� �� �ᯥ譮 ��᫠�, �� �� �ࢥ� �� �࠭����. � �� ��砥 �ᥣ�� ����� 㧭��� ����� ��᫥����� �믮�������� ����� (��� �����⭮�� ConnectName).

ConnectName - �ந����쭠� Null-terminated ��ப� - �����䨪��� �������
RequestNum - ��᫥����⥫�� ����� �����, ������� �� ������ �����䨪����� ������� �⤥�쭮. ���� ��।���� 0, ���� �㤥� �ᯮ�짮��� ��।���� ����� �����.

function CallRK7XMLRPC2(AddressName: PChar; ConnectName:PChar;
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� ��஭�. �᫨ 0, � ���������� �ࢥ஬.
  ResultFile: PChar;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function CallRK7XMLRPCToStream2(AddressName: PChar; ConnectName,
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� ��஭�. �᫨ 0, � ���������� �ࢥ஬.
  ResultStream: IStream;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function GetLastXMLResult(AddressName: PChar; ConnectName:PChar;
  out RequestNum: DWord; //�ᥣ�� �����頥��� ����� ��᫥����� �믮�������� �����
  ResultFile: PChar; //१���� ��������, �᫨ �뫠 �訡�� ��।�� ������ १����, ��᫥ �ᯥ譮� ��।�� ��ࠥ���
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function GetLastXMLResultToStream(AddressName: PChar; ConnectName: PChar;
  out RequestNum: DWord; //�ᥣ�� �����頥��� ����� ��᫥����� �믮�������� �����
  ResultStream: IStream; //१���� ��������, �᫨ �뫠 �訡�� ��।�� ������ १����, ��᫥ �ᯥ譮� ��।�� ��ࠥ���
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
