unit rk7xmli;

interface

uses windows,activex;

function CallRK7XMLRPC(AddressName: PChar; Request: PChar;
  RequestSize: integer; ResultFile: PChar;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function CallRK7XMLRPCToStream(AddressName: PChar; Request: PChar;
  RequestSize: integer; ResultStream: IStream;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
procedure SetUseTempFileLimit(aLimit:integer);stdcall;
function GetDLLVersion:integer;stdcall;
procedure SetCryptKey(Key:PChar);stdcall;//������� � ������ 134 (1.3.4.4)
//������ ��������� 2:
function CallRK7XMLRPC2(AddressName: PChar; ConnectName:PChar;
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� �������. ���� 0, �� ������������ ��������.
  ResultFile: PChar;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function CallRK7XMLRPCToStream2(AddressName: PChar; ConnectName,
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� �������. ���� 0, �� ������������ ��������.
  ResultStream: IStream;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function GetLastXMLResult(AddressName: PChar; ConnectName:PChar;
  out RequestNum: DWord; //������ ������������ ����� ���������� ������������ �������
  ResultFile: PChar; //��������� ��������, ���� ���� ������ �������� ������ ����������, ����� �������� �������� ���������
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;
function GetLastXMLResultToStream(AddressName: PChar; ConnectName: PChar;
  out RequestNum: DWord; //������ ������������ ����� ���������� ������������ �������
  ResultStream: IStream; //��������� ��������, ���� ���� ������ �������� ������ ����������, ����� �������� �������� ���������
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;

implementation

function CallRK7XMLRPC(AddressName: PChar; Request: PChar;
  RequestSize: integer; ResultFile: PChar;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;external 'RK7XML.dll';
function CallRK7XMLRPCToStream(AddressName: PChar; Request: PChar;
  RequestSize: integer; ResultStream: IStream;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall;external 'RK7XML.dll';
procedure SetUseTempFileLimit(aLimit:integer);stdcall;external 'RK7XML.dll';
function GetDLLVersion:integer;stdcall; external 'RK7XML.dll';
function CallRK7XMLRPC2(AddressName: PChar; ConnectName:PChar;
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� �������. ���� 0, �� ������������ ��������.
  ResultFile: PChar;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall; external 'RK7XML.dll';
function CallRK7XMLRPCToStream2(AddressName: PChar; ConnectName,
  Request: PChar; RequestSize: integer;
  var RequestNum: DWord; //� ��� �������. ���� 0, �� ������������ ��������.
  ResultStream: IStream;
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall; external 'RK7XML.dll';
function GetLastXMLResult(AddressName: PChar; ConnectName:PChar;
  out RequestNum: DWord; //������ ������������ ����� ���������� ������������ �������
  ResultFile: PChar; //��������� ��������, ���� ���� ������ �������� ������ ����������, ����� �������� �������� ���������
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall; external 'RK7XML.dll';
function GetLastXMLResultToStream(AddressName: PChar; ConnectName: PChar;
  out RequestNum: DWord; //������ ������������ ����� ���������� ������������ �������
  ResultStream: IStream; //��������� ��������, ���� ���� ������ �������� ������ ����������, ����� �������� �������� ���������
  ErrorBuf: PChar; ErrorBufSize: integer):BOOL;stdcall; external 'RK7XML.dll';
procedure SetCryptKey(Key:PChar);stdcall; external 'RK7XML.dll';

end.
