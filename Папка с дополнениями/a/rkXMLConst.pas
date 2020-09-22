unit rkXMLConst;

interface

// "!" � ����������� �������� �������������� ��������
// Q... - ��� ��������
// R... - ��� �������

const
  QueryMainTag='RK7Query';

  {--> ��������� ���� ������� }
  QueryCMDTag='RK7CMD'; 
    QAttrCmdName='CMD'; // �������, �������� QCmd...
    QAttrReqSysVer = 'ReqSysVer'; //��������� ������ ���������
  {<-- ��������� ���� ������� }

  {--> ��������� ����� ������ �� ���� ��� }
  QTagRK7Command='RK7Command';// c 7.3.4.0 ��������� ��� � RK7Query - ����� ���� �����
    //QAttrCmdName='CMD'; // �������, �������� QCmd...
  {<-- ��������� ����� ������ �� ���� ��� }

  ResultMainTag='RK7QueryResult';
    RAttrProcessed='Processed';// c 7.3.4.0 ���������� ������� ����������� (�� ����������) ������ (� ������ QueryCMDTag 1 ��� 0)
    RAttrStatus='Status';
      RStatusOk='Ok';
      RStatusNoChanges = 'No changes'; // ���� � ����������� ������� xml �� ��������� (� ������ 2)
      RStatusStarted='Execution Started';
      RStatusQueryParseError='Query Parse Error';
      RStatusBadParameters='Bad Query Parameters';
      RStatusQueryExecutingError='Query Executing Error';
      RStatusResultWritingError='Result Writing Error';
      RStatusResultInternalError='Query Processing Internal Error';
    RAttrErrorText='ErrorText';
    RAttrRK7ErrorN='RK7ErrorN';
    RAttrServerVersion='ServerVersion';//c 7.3.3.3
  RTagCommandResult='CommandResult';//c 7.3.4.0 ��������� � ResultMainTag, ���� ������������ QTagRK7Command, � �� QueryCMDTag
    RAttrCmdName = QAttrCmdName;
    //RAttrStatus='Status';
    //RAttrErrorText='ErrorText';
    //RAttrRK7ErrorN='RK7ErrorN';
    RAttrWorkTime='WorkTime';

  {������� ���������� ����� ��� ��������� ������� � ������� ������� (� 7.3.3.18)}
  QCmdGetSystemInfo='GetSystemInfo';
    //��������
    RTagInfo = 'SystemInfo';
     RAttrCashServVer = 'CashServerVersion';
     RAttrSystemTime  = 'SystemTime';
     RAttrShiftDate   = 'ShiftDate';
     RAttrNetName = 'NetName';
     RAttrReqSysVer = QAttrReqSysVer;
  QCmdGetReferenceList='GetRefList';// �������� ������ ���������
    // No parameters
    //�������
    RTagReferencesList = 'RK7RefList';
      RTagReference = 'RK7Reference';
        RAttrReferenceName = 'RefName';
        RAttrDataVersion = 'DataVersion';
        RAttrCount='Count';

  QCmdGetReferenceData='GetRefData';// �������� ���������
    QAttrReferenceName='RefName';// ! �������� ���������
    QAttrRefItemIdent='RefItemIdent';// � 7.1.17.10 ������������� �������� (���� ���� ��������� ���� �������), ���� �����, �� �������� ���� RK7Reference �� �������, ����� (��. QAttrPropMask) ������� ��� ������� �������� (� �� ���������!)
    QAttrPropMask='PropMask';// � 7.1.17.10 ����� ������� - ����� �������� ������������ ������ �������. * - ��� ��������, ����� - ������. ��� ��������� �������� ���������� ��������� ������ ���� � ��������, ���� ������������ ������� ������ ��� ������ �������� - �������� ���� ������. ��� ������������ ������� ��������� ��������� ����� ������������ �������� "items.(...)"  ��� "{...}". � ������ ������������� �������� ������ �������� ����� ��������� ���������� ����������� �� ������� ���������. ��������: "*,RIChildItems.(!AltName),{Name}"
    QAttrWithMacroProp='WithMacroProp'; // 7.3.2.16 - ���� 1, �� ��������� ������������ ��������
    QAttrMacroPropTags='MacroPropTags'; // 7.4.2.17 - ���� 1, �� ��������� ������������ �������� ��������� PropXXX, ��� XXX ����� ����� ����� ����������� (�� ^)
    QAttrWithChildItems='WithChildItems';// 7.3.3.0 - ���� 0-��� �������� ���������, 1 - ������ �������� ������ ����������� � ������� RIChildItems ���������, 2 - ���� � ������� items ������ �� ������ ������������, 3 - � �������� ������ ����������� � ���� �� ������ ������������ � ������� RIChildItems ���������. ����������� �������������� RIChildItems, ����� �������������� � �����. ���� ����� ��������� � ������� �������
    QAttrIgnoreEnums='IgnoreEnums';// 7.3.3.0 - ���� 0 - ������������� ���� ��� ������, 1 - ������������� ���� � �� ��������� ��� �����
    QAttrIgnoreDefaults='IgnoreDefaults';// 7.3.3.2 - ���� 1 - �� ������ ���������, ���� �������� ������� "�� ���������"
    QAttrOnlyActive='OnlyActive';//7.4.2.0 - ���� 1 ������� ������ �������� ��������

    //�����
    RAttrBlobNames='BlobNames';//������ ��� BLOB �����
    RTagItems='Items';
      RTagItem='Item';
        RAttrIdent='Ident';
    RTagChildItems='RIChildItems';
    RTagPropPrefix='Prop';//� 7.4.2.17 ���� MacroPropTags=1 - ������� ����� ������� ������������ �������
      RTagProperty='Property';//��� ������ ���� ������������� ��������
        //RAttrIdent='Ident'; - ������������� ������������� �������� (������������� ��������������� �������)
        RAttrValue='Value';// �������� ������������� ��������
  //QCmdGetRefItemBlob='GetRefItemBlob'; - ���������� // � 7.1.17.0 �������� BLOB �������� �������� ��������� - ������������ ������� (��������, �������������� base64)
    //QAttrReferenceName='RefName';// ! �������� ���������
    //QAttrRefItemIdent='RefItemIdent';// ! ������������� ��������
    //QAttrEncodeBase64='EncodeBase64';// ���� 1 �� ���� ���������� base64, ���� 0 ��� �� ������ - �� ����������. �� ������������� ������������ 0, ��� ��� �� ANSI ������� ������ XML (�� �� ������������� ��� UTF-8)
  QCmdGetItemBlob='GetItemBlob';// � 7.3.4.0 �������� BLOB �������� �������� ��������� - ������������ ������� �������������� base64
    //QAttrReferenceName='RefName';// ! �������� ���������
    //QAttrRefItemIdent='RefItemIdent';// ! ������������� ��������
    QAttrEncodeBase64='EncodeBase64';// ���� 1 ��� �� ������(������� �� ����������� QCmdGetRefItemBlob), �� ���� ���������� base64, ���� 0 - �� ����������. �� ������������� ������������ 0, ��� ��� �� ANSI ������� ������ XML (�� �� ������������� ��� UTF-8)
    QAttrRefBlobName='RefBlobName';// ��� BLOB (����), ���� �� ������ - ������ ������
    QAttrUnpackedBlob='UnpackedBlob';// ���� 1 - ���� �����������, ���� �������� � ������ ����

  { --> ������ � ������� � 7.3.4.0, ����� ��� ��������� ������� � ������� ������� }
  QCmdGetFile='GetFile'; //���������� ����� ������ ���� ����������
    QAttrPathName='PathName';// ! ��� ����� � ������������� ����
    QAttrFileOffset='FileOffset';
    QAttrFileSize='FileSize';
  QCmdGetDirectory='GetDirectory'; //���������� ����������
    //QAttrPathName='PathName';// ! ��� ���������� � ������������� ����
    QAttrFileMask='FileMask'; // �������������� �����, �� ��������� *.*
    QAttrWithContent='WithContent'; // ��� �������� 1 ������ RTagFile ���������� �����
    //�������
    RTagFile='File';
      RAttrFileName='FileName';
      RAttrSize='Size';
      RAttrDate='Date';//YYYYMMDD
      RAttrTime='Time';//HH:MM:SS
  QCmdPutFile='PutFile'; //���������� ����� ������ ����
    //QAttrPathName='PathName';// ! ��� ����� � ������������� ����
    //QAttrFileOffset='FileOffset'; ��� �������� -1(�� ���������) ���� ��������� ����������, ��� ������� 0 ������������� ������
  QCmdDelFile='DelFile'; //���������� ����� ������ ����
    //QAttrPathName='PathName';// ! ��� ����� � ������ � ������������� ����
    //�������
    RAttrFilesProcessed='FilesProcessed';// ���������� �������� ������
  { <-- ������ � ������� }

    

implementation
end.