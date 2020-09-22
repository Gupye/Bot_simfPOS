unit XMLIntc;

interface
// �����: ����������� � ���� ����� �� �������� �������������, � ������������ �
//        ����� ���������� ��������������� 

// "!" � ����������� �������� �������������� ��������
// Q... - ��� ��������
// R... - ��� �������

const
(* ���������o � rkXMLConst
  QueryMainTag='RK7Query';
  QueryCMDTag='RK7CMD'; // ������ ��� ����� �������
    QAttrCmdName='CMD'; //�������� QCmd...
    QAttrReqSysVer = 'ReqSysVer'; //��������� ������ ���������
  QTagRK7Command='RK7Command';// c 7.3.4.0 ��������� ��� � RK7Query - ����� ���� �����
    //QAttrCmdName='CMD'; //�������� QCmd...

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
    RAttrErrorText='ErrorText';
    RAttrRK7ErrorN='RK7ErrorN';
    RAttrServerVersion='ServerVersion';//c 7.3.3.3
  RTagCommandResult='CommandResult';//c 7.3.4.0 ��������� � ResultMainTag, ���� ������������ QTagRK7Command, � �� QueryCMDTag
    RAttrCmdName = QAttrCmdName;
    //RAttrStatus='Status';
    //RAttrErrorText='ErrorText';
    //RAttrRK7ErrorN='RK7ErrorN';
    RAttrWorkTime='WorkTime';

//   *** ������� ***

      {������� ���������� ����� ��� ��������� ������� � ������� ������� (� 7.3.3.18)}
      QCmdGetSystemInfo='GetSystemInfo';
        //��������
        RTagInfo = 'SystemInfo';
         // RAttrCashServVer = 'CashServerVersion';
         // RAttrSystemTime  = 'SystemTime';
         // RAttrShiftDate   = 'ShiftDate';
         RAttrNetName = 'NetName';
         RAttrReqSysVer = QAttrReqSysVer;
         RCash = 'Cash';                // �������� �������� ������� (��� ������� � �����), refItem   
         RCashGroup = 'CashGroup';      // ������� �������� ������, refItem   
         RRestaurant = 'Restaurant';    // ������� ��������, refItem   
      QCmdGetReferenceList='GetRefList';// �������� ������ ���������
        // No parameters
        //�������
        RTagReferencesList = 'RK7RefList';
          RTagReference = 'RK7Reference';
            RAttrReferenceName = 'RefName';
            RAttrDataVersion = 'DataVersion';
            //RAttrCount='Count';
      QCmdGetReferenceData='GetRefData';// �������� ���������
        QAttrReferenceName='RefName';// ! �������� ���������
        QAttrRefItemIdent='RefItemIdent';// � 7.1.17.10 ������������� �������� (���� ���� ��������� ���� �������), ���� �����, �� �������� ���� RK7Reference �� �������, ����� (��. QAttrPropMask) ������� ��� ������� �������� (� �� ���������!)
        QAttrPropMask='PropMask';// � 7.1.17.10 ����� ������� - ����� �������� ������������ ������ �������. * - ��� ��������, ����� - ������. ��� ��������� �������� ���������� ��������� ������ ���� � ��������, ���� ������������ ������� ������ ��� ������ �������� - �������� ���� ������. ��� ������������ ������� ��������� ��������� ����� ������������ �������� "items.(...)"  ��� "{...}". � ������ ������������� �������� ������ �������� ����� ��������� ���������� ����������� �� ������� ���������. ��������: "*,RIChildItems.(!AltName),{Name}"
        QAttrWithMacroProp='WithMacroProp'; // 7.3.2.16 - ���� 1, �� ��������� ������������ ��������
        QAttrWithChildItems='WithChildItems';// 7.3.3.0 - ���� 0-��� �������� ���������, 1 - ������ �������� ������ ����������� � ������� RIChildItems ���������, 2 - ���� � ������� items ������ �� ������ ������������, 3 - � �������� ������ ����������� � ���� �� ������ ������������ � ������� RIChildItems ���������. ����������� �������������� RIChildItems, ����� �������������� � �����. ���� ����� ��������� � ������� �������
        QAttrIgnoreEnums='IgnoreEnums';// 7.3.3.0 - ���� 0 - ������������� ���� ��� ������, 1 - ������������� ���� � �� ��������� ��� �����
        QAttrIgnoreDefaults='IgnoreDefaults';// 7.3.3.2 - ���� 1 - �� ������ ���������, ���� �������� ������� "�� ���������"
        QAttrOnlyActive='OnlyActive';//� 7.4.2.0 - ���� 1 ������� ������ �������� ��������
        QAttrMacroPropTags='MacroPropTags'; // 7.4.2.17 - ���� 1, �� ��������� ������������ �������� ��������� PropXXX, ��� XXX ����� ����� ����� ����������� (�� ^)
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
        RTagChildItems='RIChildItems';
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
      { <-- ������ � ������� }*)

{
    <xs:complexType name="refitem">
      <xs:choice>
        <xs:attribute name="id" type="xs:positiveInteger"/>
        <xs:attribute name="code" type="xs:positiveInteger"/>
      </xs:choice>
    </xs:complexType>
}
      // �������� ���������� � ������� (ver 2)
      QCmdGetSystemInfo2 = 'GetSystemInfo2';
        RTagInfo = 'SystemInfo';
//       RAttrRestCode  = 'RestCode';
         RAttrProcessID = 'ProcessID';
         RCash = 'Cash';           // �������� �������� ������� (��� ������� � �����), refItem
         RCashGroup = 'CashGroup'; // ������� �������� ������, refItem
         RRestaurant= 'Restaurant';// ������� ��������, refItem
         RCommonShift = 'CommonShift';
//         RAttrShiftDate   = 'ShiftDate';  // ���������� ����, dateTime
           RAttrShiftNum    = 'ShiftNum';   // ����� ����� �����
           RAttrShiftStartTime = 'ShiftStartTime'; // ������ ����� �����, dateTime

      {������� ���������� ������ �������� ������}
      {--> �������� �������� ��������� }
      QCmdGetParamValue = 'GetParamValue';
        QAttrParamName = 'ParamName';    // ! ��������� ��� ���������
//      QAttrVisitID = 'VisitID';        // ID ������
//      QAttrOrderID = 'OrderID';        // ID ������
//      QAttrDateTime    = 'DateTime';   // �����, �� ������� ����� �������� �������� ��������� (dd.mm.yyyy hh:mm ��� YYYYMMDD hh:mm)
        QAttrStationID   = 'StationID';  // ID �������, ���� �� ����� �� ������������ StationCode
        QAttrStationCode = 'StationCode';// ��� �������
        QAttrWaiterID   = 'WaiterID';    // ID ���������, ���� �� �����, �� ������������ WaiterCode
        QAttrWaiterCode = 'WaiterCode';  // ��� ���������
        QAttrTableID   = 'TableID';      // ID �����, ���� �� �����, �� ������������ TableCode
        QAttrTableCode = 'TableCode';    // ��� �����
        QAttrGuestTypeID  = 'GuestTypeID';  // ID ���� ������, ���� �� �����, �� ������������ GuestTypeCode
        QAttrGuestTypeCode= 'GuestTypeCode';// ��� ���� ������


        // �������� xml
        RAttrParamName = QAttrParamName;
        RAttrParamValue = 'Value'; // �������� ���������
      {<-- �������� �������� ��������� }

      {--> �������� ������� �������� ��� ������������� }
      QCmdGetUsageValue = 'GetUsageValue';
        QAttrUsageName = 'name';         // ! ��� �������������
        QAttrUsageParam = 'param';       // �������� ��� �������������
//      QAttrDateTime    = 'dateTime';   // �����, ���� �� ������ �� �������
//      QOrder          = 'Order';       // �����, orderElement
//      QStation      = 'Station';       // �������, refItem
//      QWaiter           = 'Waiter';    // ��������, refItem
//      QTable        = 'Table';         // ����, refitem
//      QGuestType    = 'GuestType';     // ��� ������, refitem
        // �������� xml
        RAttrUsageName = 'name';    // ��� �������������
        RAttrUsageParam = 'param';  // �������� ��� �������������
        RUsageValue = 'Value'; // ��������� ������, refItem
      {<-- �������� �������� ��������� }

      {-->  ��������� MCR ��������� }
      QCmdParseMCR = 'ParseMCR';
        QAttrData = 'data'; // ��������� ������
      // �������� xml
        RMcrItemTag = 'Item';
//        RAttrCardCode = 'cardCode'; //! ��� �����
          RAttrScope = 'scope';       // �������, string
          RMCRItem = 'MCR';           // !MCR ��������
          RObjectItem = 'Object';     // ������, refItem
      {<--  ��������� MCR ��������� }


      QCmdGetOrders='GetOrders';//��. ����� 12043 "Orders list for XML"
        //�������
//        RTagOrderLists='OrdersList';
      QCmdGetReceipts='GetReceipts';
        //�������
        RTagReceipts='ReceiptsList';
          RAttrCount='Count';
      QCmdGetReceiptList='GetReceiptList';
//      QAttrLineGuid = 'line_guid';         // ������ �� guid ����
//      QROrder       = 'Order';             // ������ �� ������
//      RTagReceipts='ReceiptsList';
          RReceiptItem = 'Receipt';
//          QROrder       = 'Order';
            QRCloseStation= 'CloseStation';   // �������, �� ������� ������� ���, refItem
            QRPrintStation= 'PrintStation';   // �������, �� ������� ��� ��� ����������, refItem
            QRCashier     = 'Cashier';        // ������, refItem
//          QRAttrLineGuid= 'lineguid';       // guid ����
            RsAttrCheckNum = 'checknum';      // ����� ����, int
            RAttrSum      = 'sum';            // ����� ����, int
            RsAttrDeleteTime= 'deletetime';   // ����� �������� ����, dateTime
            RsAttrPrintTime= 'printtime';     // ����� ������ ����, dateTime
            RsAttrStartDateTime= 'starttime'; // ����� ������ ������������ ����, dateTime
            RsAttrBillTime = 'billtime';      // ����� ������ �������, dateTime
            RAttrState    = 'state';          // ������ ����, int
//          QRAttrSeat    = 'seat';           // ����� ����������� �����, int
            RDeleteManager = 'DeleteManager'; // ��������, ��������� ���, refItem
            RDeleteReason  = 'DeleteReason';  // �������, �� ������� ������ ���, refItem

      QCmdGetPrintLayout='GetPrintLayout'; // �������� ������ ��� ������ (��������� ����� CDATA)
        QLayout = 'Layout';           // ����� ������, refItem
        QDocument = 'Document';       // ��� ���������, refItem. ������������, ���� �� ����� Layout. ������� ������ ���������� �����
        //QAttrEncodeBase64='EncodeBase64'; // ������������ ����� � base64
//      QOrder  = 'Order';            // �����, orderElement
        QReceiptNum = 'ReceiptNum';   // ����� ����, int
          QAttrLayoutFilters='LayoutFilters'; // ������� ������ ���� <����>=��������[{;<����=��������>}]
          QAttrDataSourceParams='DataSourceParams'; // ��������� ����� ���� <����>=��������[{;<����=��������>}]
          QAttrFileFormat  = 'format';      // ������ ������: text, xml, xls

      QCmdGetDocByLayout='GetDocByLayout';// �������� ������ �� ������ ������
//      QLayout = 'Layout';           // !����� ������, refItem
//      QOrder  = 'Order';            // �����, orderElement
        QAttrReceiptNum='ReceiptNum'; // ����� ����, ������ ���� �����, ���� ����� ����/�������, ���� c 7.1.17.10 ����� ������ QAttrOrderName ��� QAttrVisit+QAttrOrderIdent
        QAttrVisit='Visit';
        QAttrOrderIdent='OrderIdent';
        QAttrOrderName='OrderName'; // c 7.1.17.17 ��� ������, ����� ���� ����� ������ QAttrReceiptNum ��� QAttrVisit+QAttrOrderIdent
        //QAttrLayoutParams='LayoutParams'; ���������� // ��������� ������ ���� <����>=��������[{;<����=��������>}]
//      QAttrLayoutFilters='LayoutFilters'; // c 7.3.4.0 ������� ������ ���� <����>=��������[{;<����=��������>}]
//      QAttrDataSourceParams='DataSourceParams'; // c 7.3.4.0 ��������� ����� ���� <����>=��������[{;<����=��������>}]
        QAttrTextReport='TextReport';// � 7.4.3.4 - ��� 1 �������� ����� � ���� ������ (� �� XML)
        //�������
        RAttrLayoutResultTag='LayoutResult';
          RAttrLayoutCode='LayoutCode';
          RAttrLayoutFilters=QAttrLayoutFilters;
          RAttrDataSourceParams=QAttrDataSourceParams;

      { <-- ������� ���������� }

      {������ �������� ������}
      QCmdDeleteReceipt='DeleteReceipt';
        //QAttrReceiptNum='ReceiptNum'; // ! ����� ����
        QAttrManagerPassword='ManagerPassword';// ! ������ ���������, �� �������� ��������� ��������, �� ������
        QDeleteReason='DeleteReason'; // !������� �������� ����, refItem
        QMaket = 'Maket'; // ! ������������� ��������� ��� �������� ����, refItem
        QManager = 'Manager';//! ��������, �� �������� ��������� ��������, refItem
      QCmdUndoReceipt='UndoReceipt';//������������
        //PAttrReceiptNum='ReceiptNum'; !
        //QAttrManagerPassword='ManagerPassword';// ! ������ ���������, �� �������� ��������� ��������, �� ������
        //QManager = 'Manager' //! ��������, �� �������� ��������� �������������, refItem
        //QDeleteReason='DeleteReason'; // ������� ������������� ����, refItem
        //QMaket = 'Maket'; // ! ������������� ��������� ��� ������������� ����, refItem
      QCmdWaiterMessage='WaiterMessage';//������� ��������� ���������
//      QWaiter           = 'Waiter';     // !��������, �������� ���������� ���������, refItem
//      QManager          = 'Manager';    // ��������, �� ����� �������� ���������� ���������, refItem
        QRAttrText        = 'text';       // !T���� ���������
        QRAttrExpireTime  = 'expireTime'; // !����� ����� ���������
        QRAttrParam       = 'param';      // �������� ��� ��������� (��� ��������� �������� - 1 �����)
        QRAttrMessageType = 'messageType';// ��� ���������, string rkClass.MessageTypes
        // �������� xml
        QRMessage         = 'Message';
          QRAttrMessageID = 'id';         // id ���������
      QCmdGetWaiterMessages='GetWaiterMessages';//�������� ������ ��������� ���������
        QRWaiter          = 'Waiter';     // ��������, refitem
//      QRMessage         = 'Message';
//        RAttrMessageID  = 'id';         // id ���������
//        QRAttrText      = 'text';       // ����� ���������
//        QRAttrParam     = 'param';      // �������� ���������
          RAttrCreateTime = 'createTime'; // ����� �������� ���������
//       QRAttrExpireTime = 'expireTime'; // ����� ����������� ���������
          RAttrRepeatCount= 'repeatCount';// ����� ����������
//       QRAttrMessageType= 'messageType';// ��� ���������
      QCmdDelWaiterMessages = 'DelWaiterMessages';// ������� ��������� ��������� (������ id)
//      QRMessage         = 'Message';    // ���������
//        QRAttrMessageID = 'id';         // id ���������

      {-->  �������� ������� �� ����� }
      QCmdGetDishesRest = 'GetDishRest';
//      QDishItem     = 'Dish';       // �����, refitem
        // xml-�����
//      QAttrQuantity='quantity';   // ! ����� ���������� � �������� �����
      {<--  �������� ������� �� ����� }
      {-->  �������� ������ �������� ����, ������� ����������� ����� }
      QCmdGetDishesRests = 'GetDishRests';
        // xml-�����
      RDishRestItem = 'DishRest';           // �����, refitem
//        RAttrQuantity='quantity';   // ���������� (� �������� �����)
        RAttrProhibited='prohibited'; // ���� - ����� ��������� � �������
      {<--  �������� ������ �������� ����, ������� ����������� ����� }

      {-->  �������� ������� ���� }
      QCmdSetDishRests='SetDishRests';//� 7.3.3.0 ���������� ������� ���� - ������ ����� ����� QDishRest
        QAuthor = 'Author'; // ��������, refItem
        QDishRest = 'DishRest';// �����, refItem + unbounded
          QAttrQuantity = 'Quantity';//!����� ���������� � �������� �����
          QAttrProhibited = 'prohibited'; // ���� - ����� ��������� � �������
      {<--  �������� ������� ���� }
       
      QCmdSetDishRate='SetDishRate';//�������� ����� �������/�����������
        //QAttrDishIdent  = 'DishIdent'; // �� �����    (integer)
        QAttrGuestCode    = 'GuestCode'; // �� �����    (string, ��������������)
        QAttrRating       = 'Rating';    // �������     (integer, 2 �����: 4,51 = 451, ��������������)
        //QAttrComment    = 'Comment';   // ����������� (UTF8String, ��������������)
      QCmdProcessOperation='ProcessOperation';//� 7.3.4.5 ������� ��������� �������� �������� ���, ��� ����� �������� ���� ��������� �� �����
        QAttrOperationIdent='OperationIdent';//! Ident ��������
        QAttrParameter='Parameter';//�������� ��������
//      QAttrStationID   = 'StationID'; // ID �������
        QAttrPerson      = 'Person'; //Ident ��������� ��������
        QAttrSessionUNI  = 'SessionUNI';
        //QAttrVisit='Visit'; // ���������� ������������� ������, ������������ ��������� � QAttrOrderIdent
        //QAttrOrderIdent='OrderIdent';// ���������� ������������� ������ � ������, ������������ ��������� � QAttrVisit
        QAttrMenuItemIdent='MenuItemIdent';// ������������� �����
        //QAttrQuantity='Quantity';//����� ���������� � �������� �����
      { --> ������� ��� ���  }
      QCmdKDSGetRefsData='KDSGetRefsData'; // �������� ������ ������������
        QAttrDataBuildMode='BuildMode';
        QAttrXMLUOTFldName='UOTField';
        QAttrXMLTblFldName='TableField';
        QAttrXMLUseCharset='UseCharset';
      QCmdKDSGetDishData='KDSGetDishData'; // �������� ������ �������/����
      QCmdKDSSetDishData='KDSSetDishData'; // ������ ������ �������/����
      QCmdKDSSetDishFlag='KDSSetDishFlag'; // ������ ������ �������/����
        QAttrDishIdent = 'DishIdent'; // KDSIdent
        QAttrDishState = 'DishState'; // ��������� ����� (dsSent, dsInit, dsDone, dsTake)
        QAttrDishFlag  = 'DishFlag';  // ���� ����� (kdfCanDelete)
        QAttrDishFlagValue = 'Value';
      QCmdKDSGetSystemInfo='KDSGetSystemInfo';// ��������� ��������� ����
        //�������
        RTagKDSInfo = 'KDSSystemInfo';
          RAttrCashServVer = 'CashServerVersion';
          RAttrSystemTime  = 'SystemTime';
          RAttrShiftDate   = 'ShiftDate';   //������� ���� ����� YYYYMMDD, ����� ���� 0, ���� �� �������
          RAttrShiftNumber = 'ShiftNumber'; //����� ������� ����� �����, ����� ���� 0, ���� �� �������
          RAttrRestCode    = 'RestCode';
          RBusunessPeriod   = 'BusinessPeriod'; // ������ ������, refItem
      { <-- ������� ��� ���  }
      { --> ������� ��� Brunswick }
      QCmdBrunswickData = 'VectorBrunswickData'; // ������ ������ �� Brunswick Vector
        QAttrReceiptID  = 'receipt_id';   // ! ����� ����
        QAttrReceiptDate= 'receipt_date'; // ��������� ����
        QAttrTotalMoney = 'total_money';  // ! The sum of the entire receipt, NOT including any transaction tax.
        QAttrTransactionTax = 'transaction_tax'; // ! The transaction tax supplied to the receipt. May be 0 if no transaction tax exists.
        QAttrTerminalID = 'terminal';     // ID ���������
        QAttrClerkID    = 'clerk';        // ID ���������
        QAttrLane       = 'lane';         // ! ����� ������� - Last lane bowled on (e.g. after a transfer). ��������, ���� ������ �� ������� ������ � ������ ���������������� ����������. ���� ���������� � ����� ������, ���� ������ ��������������� DeviceCode, ���� �� ������, DeviceCode ������ ���� �� ����� ��� 0
        QAttrDeviceCode = 'DeviceCode';   // ��� ���������������� ����������, 0 ��� ��� - ���������� � ����� �� ������ 
        QAttrGameSDate= 'GameStartDate';  // ���� ������ ���� YYYYMMDD ��� dd.mm.yyyy
        QAttrGameSTime= 'GameStartTime';  // ����� ������ ���� hh:mm:ss
        QAttrGameEDate= 'GameEndDate';
        QAttrGameETime= 'GameEndTime';
      { <-- ������� ��� Brunswick }
      { --> ������� ��� ������������ }
      QCmdAddReserv = 'AddReservation'; // �������� �����
        QAttrSource = 'Source';      // �������� ����� (�� ���� ������, integer)
        QReservations  = 'Reservations';//������ ������ ����� (tag='Reserv') � ����������:
          QTagReserv = 'Reserv';
            QAttrReservID  = 'ID';          // ID �����
//          QAttrTableID   = 'TableID';     // ID ����� (���� �� �����, ������������ HallID + TableName)
            QAttrStatus    = 'Status';      // ������ ����� (��� ����������� ������������)
                                            // 0 - ����� ���� ����� �������
                                            // 1 - ����� �������������
                                            // 2 - ����� ������� �� ������� �����������
                                            // 3 - ����� �������� ����������
                                            // 4 - �� ������ ����� ������ ������
                                            // 5 - ����� ����� ������� � ������

            QAttrHallID    = 'HallID';      // ID ����� ����
            QAttrTableName = 'TableName';   // ��� �����
            QAttrGuestsCount= 'GuestsCount'; // ���-�� ������
            QAttrReservDate= 'ReservDate';  // ���� ����� (YYYYMMDD ��� dd.mm.yyyy)
            QAttrReservTime= 'ReservTime';  // ����� ����� (hh:mm)
            QAttrReservDur = 'Duration';    // ������������ ����� (� ���)
            QAttrClientName= 'ClientName';  // ��� �������
            QAttrCardCode  = 'CardCode';    // ��� ��� ����� �������
            QAttrIntfCode  = 'IntfCode';    // ��� ���������� ����� ������� (�� ��������� 1)
            QAttrIntfID    = 'IntfID';      // ID ���������� ����� �������
            QAttrComment   = 'Comment';     // �����������
      ROrder = 'Order';
//      RAttrVisit = 'visit';
        RAttrOrderIdent = 'orderIdent';
      QCmdDelReserv = 'DelReservation'; // ������� ����� (��������� ��� � AddReservation)
      QCmdGetReservRes = 'GetReservationResults';// ���������� ������������
        RResResults = 'ResResults';
          RTagReserv = 'Reserv';
            RAttrReservID = QAttrReservID;     // ID �����
            RAttrStartTime = 'StartTime';
            RAttrOrderSum  = 'OrderSum';    // ����� ������ �����}
            RAttrHallID    = QAttrHallID;
            RAttrTableName = QAttrTableName;
            RAttrReservDur = QAttrReservDur;
      { <-- ������� ��� ������������ }

      QCmdCreateVisit  = 'CreateVisit'; // ������� �����
//      QGuestType    = 'GuestType';        // ��� ������, refitem
//      QAttrPersistentComment='persistentComment';// ����������� �����������
//      QAttrNonpersistentComment='nonPersistentComment';// ������������� �����������
        QTagGuests       = 'Guests';        // ������ ������
//        QAttrGuestLabel= 'guestLabel';    // ����� �����
//        QAttrCardCode  = 'cardCode';      // ��� ����� �����
//        QAttrClientID  = 'clientID';      // id �������, bigint
//        QAttrAddressID = 'addressID';     // id ������ ��������, bigint
//        QInterface  = 'Interface';        // ��������� � ����� �����, refitem
        // �������� xml
        RAttrVisitID      = 'VisitID';      // ID ������������ ������
//      RAttrGuid         = 'guid';         // GUID ������������ ������

      QCmdCloseVisit      = 'CloseVisit'; // ������� �����
        QAttrVisitID = RAttrVisitID;    // ID ������������ ������

      QCmdCreateOrder = 'CreateOrder'; // ������� �����. ������ ������ ����� (tag='Order') � ����������:
//      QTable        = 'Table';      // ����, refitem
//      QWaiter       = 'Waiter';     // ������� ��������, refitem
//      QOrderType    = 'OrderType';  // ��� ������, refitem
//      QOrderCategory= 'OrderCategory';// ��������� ������, refitem
//      QDefaulter    = 'Defaulter';  // ������������, refitem
        QStation      = 'Station';    // !�������, �� ������� ��������� �����, refItem
//      QGuestType    = 'GuestType';  // ��� ������, refitem
//      QAttrPromoCode= 'promoCode';  // ��������, normilizedstring
//      QAttrPersistentComment='persistentComment';// ����������� �����������
//      QAttrNonpersistentComment='nonPersistentComment';// ������������� �����������
//      QTagGuests       = 'Guests';        // ������ ������
//        QAttrCardCode  = 'cardCode';      // ��� ����� �����
//        QAttrClientID  = 'clientID';      // id �������, bigint
//        QAttrAddressID = 'addressID';     // id ������ ��������, bigint
//        QInterface  = 'Interface';        // ��������� � ����� �����, refitem
        // �������� xml
        RTagOrder = 'Order'; // �����
  //      RAttrVisitID      = 'VisitID';      // ID ������������ ������
          RAttrOrderID      = 'OrderID';      // ID ������������ ������

    QCmdUpdateOrder = 'UpdateOrder'; // �������� �������� ������ (������)
//      QAttrVisit    = 'Visit';
//      QAttrOrderIdent='OrderIdent';
        QAttrExtSource= 'ExtSource';  // id-���������, ��������� �����, int
        QAttrExtID    = 'ExtID';      // ������� id ������, ��� ������ �� ���������� ���������, int
//      QTable        = 'Table';      // ����, refitem
//      QWaiter       = 'Waiter';     // ������� ��������, refitem
//      QOrderType    = 'OrderType';  // ��� ������, refitem
//      QDefaulter    = 'Defaulter';  // ������������, refitem
//      QGuestType    = 'GuestType';  // ��� ������, refitem
//      QTagGuests       = 'Guests';  // ������ ������, �������� anyname
//        QAttrGuestLabel= 'guestLabel'; // ����� �����
//        QAttrCardCode  = 'cardCode';// ��� ����� �����
//        QAttrClientID  = 'clientID';      // id �������, bigint
//        QAttrAddressID = 'addressID';     // id ������ ��������, bigint
//        QInterface  = 'Interface';  // ��������� � ����� �����, refitem
        QTagExtraTables = 'ExtraTables'; // ������ �������������� ������, �������� table
//      QAttrPersistentComment='persistentComment';// ����������� �����������, string
//      QAttrNonpersistentComment='nonPersistentComment';// ������������� �����������, string
                      
    {--> ������ ����������� ������ (����������, ������������ ������ ��� SaveOrder) }
    QCmdWriteOrderData = 'WriteOrderData';
     QTagSession = 'Session';      // �����. ������ ������ Dishes, ����� ����� ����� ���� �����
//     QAttrVisitID = 'VisitID';     // ! ID ������, ������������ ����� ���������� QCmdCreateOrder
//     QAttrOrderID = 'OrderID';     // ! ID ������, ������������ ����� ���������� QCmdCreateOrder
       QAttrSessionID = 'SessionID'; // ���� SessionID <> 0, �� �������������� �����, ����� ��������� �����
       QAttrIsDraft  = 'isDraft';    // �������, ��� ����� �������� ����������, boolean
       QAttrCourseCode = 'CourseCode';// ��� ������� ������, � ������� ����� �������� �����
       QAttrCourseID   = 'CourseID';  // ID ������� ������. ���� �� �����, �� ������������ CourseCode
                                        // ! ����������� ���� QAttrStationCode ���� QAttrStationID
//     QAttrStationCode = 'StationCode';// ��� �������, �� ����� ������� ����� �������� �����
     //QAttrStationID   = 'StationID'; // ID �������, ���� �� ����� �� ������������ StationCode
      QTagDishes = 'Dishes';          // ������ ����. ������ ������ ����� (tag = 'Dish')
                                        // ! ����������� ���� QAttrItemID ���� QAttrCode
       QAttrItemID      = 'ID';       // ID �����
       QAttrCode        = 'Code';     // ��� ����� (������������ ���� �� ����� ID)
//      QAttrQuantity  = 'Quantity'; // ! ���������� ����� (����� ���������� � �������� �����)
       QAttrWeight      = 'Weight';   // ��� ����� (� �������� �����), ���� �����, ����������� ����������
      QTagModifiers      = 'Modifiers';// ������������ �����. ������ ������ ����� (tag = 'Modifier')
    // �������� xml
//   RAttrOrderSum    = 'OrderSum'; // ����� ������
     RattrToPaySum    = 'ToPaySum'; // ����� ������ � ������
     RAttrPriceListSum= 'PriceListSum'; // ����� �� ������������
     RCookMin         = 'CookMin';  // ����� ������������� ���� ������ (������������ �� ����� ������������� ���� ����)
     RTagSession      = 'Session'; // �����
       //RAttrVisitID
       //RAttrOrderID
       RAttrSessionID = QAttrSessionID;
       //RAttrOpened
       RAttrStationID = QAttrStationID;
       RAttrStationCode = QAttrStationCode;
       RAttrStationName = 'StationName';
       RAttrCourseID = QAttrCourseID;
       RAttrCourseCode = QAttrCourseCode;
       RAttrCourseName = 'CourseName';
    {<-- ������ ����������� ������ }
    QCmdCloseCommonShift = 'CloseCommonShift';
      //QAttrManagerCode = 'ManagerCode';// ��� ���������
      //QAttrManagerID='ManagerID';// ��� ���������
      QRManager = 'Manager';
      QAttrCloseAnyCase='CloseAnyCase';//1-��������� � ����� ������, �����, ������ ���� �������
      //������� - ���������� � �������� �����, ����� - ������(��������������) �� ����� ��������
      RAttrCommonShiftNum = 'CommonShiftNum';
      RAttrCommonShiftDate = 'CommonShiftDate';
    QCmdCloseCashShift = 'CloseCashShift';
//      QRManager = 'Manager';
//      QRStation = 'Station';
//      QRMaket   = 'Maket';
      //������� - ���������� � �������� �����, ����� - ������(��������������) �� ����� ��������
      RAttrCashShiftNum = 'ShiftNum';
    {--> ������ ����������� ������ (����������, ������������ ������ ��� GetOrder) }
    QCmdReadOrderData = 'ReadOrderData';
//     QAttrVisitID = 'VisitID';     // ID ������
//     QAttrOrderID = 'OrderID';     // ID ������
       QAttrNeedIdents = 'NeedIdents';// ���� 1, �� � �������������� xml ����������� �������������� ���� ���������
       QAttrNeedCodes  = 'NeedCodes'; // ���� 1, �� � �������������� xml ����������� ���� ���� ���������
       QAttrNeedNames  = 'NeedNames'; // ���� 1, �� � �������������� xml ����������� ����� ���� ���������
    //�������
      //RTagSession = 'Session';      // ������ �������. ������ ������ Dishes
        RTagDishes       = 'Dishes';  // ������ ����. ������ ������ ����� (tag = RTagItem)
          RTagDish       = 'Dish';    // �����
            RAttrRefItemID='ID';
            RAttrQuantity=QAttrQuantity;
            RAttrPrice   = 'Price';     // ���� �����/������������ (� ��������, ����� ������ �� 100)
            RTagModifers = 'Modifiers'; // ������ �������������, ������ ������ ����� (Tag=Modifier)

    // �������� xml: ����� ����� � ��������� ������������ ������� QCmdWriteOrderData
      // ������������� � ������ �������� ������� Opened:
      RAttrOpened = 'Opened'; // ����� �� ������������� ���������� ������
    {<-- ������ ����������� ������ }

    {--> ������ ����������� ������, �������� ��. qryGetOrder.xsd � resGetOrder.xsd }
    QCmdGetOrder = 'GetOrder';
      QOrder     = 'Order';      // !�����, orderElement
      // �������� xml
//      ROrder = 'Order';
//        RAttrVisit = 'visit';
//        RAttrOrderIdent = 'orderIdent';
//      RAttrOrderSum   = 'orderSum'; // ����� ������
        RAttrUnpaidSum  = 'unpaidSum'; // ����� ������ � ������
        RAttrDiscountSum= 'discountSum'; // ����� ������
//      RAttrTotalPieces  = 'totalPieces';// ����� ������ ���� ���� ������
//      RAttrPersistentComment='persistentComment';// ����������� �����������
//      RAttrNonpersistentComment='nonPersistentComment';// ������������� �����������
      ROrderType = 'OrderType';  // ��� ������, refItem
      ROrderCategory='OrderCategory'; // ��������� ������, refItem
      RTable = 'Table';               // ����, refItem
      RGuestType = 'GuestType';       // ��� ������, refItem
      RSessionItem  = 'Session'; // ������ ������� ������, ��. rkXmlUtl.SessionItem + unbounded
      RDeliveryBlock  = 'DeliveryBlock';  // ���� � ������ ��������
        RAttrTravelTime= 'travelTime';    // ����� � ����
        RAttrDeliveryTime='deliveryTime'; // ����� �������
        RAttrZoneID   = 'zoneID';         // ID ���� ��������
        RAttrZoneName = 'zoneName';       // ��� ���� ��������
        RAttrOrderPrefix = 'orderPrefix'; // ������� ��� ������ ������
    {<-- ������ ����������� ������ }

    {--> ������� ��� ��������� ������ ���� �� ������ }
    QCmdGetOrderMenu = 'GetOrderMenu'; // �������� ������ ���� � �������������, ��������� � ������������ ������
//      QAttrVisitID = 'VisitID';    // ID ������, �� �������� ����� �������� ������ ����
      QAttrOrderID = 'OrderID';    // ID ������, �� �������� ����� �������� ������ ����
//    QAttrStationID   = 'StationID'; // ID �������, ���� �� ����� �� ������������ StationCode
//    QAttrStationCode = 'StationCode';// ��� ������� (�� ������� ������� ���� � ��)
//    QAttrTableID   = 'TableID';  // ID �����, ���� �� �����, �� ������������ TableCode
//    QAttrTableCode = 'TableCode';// ��� �����
//    QAttrWaiterCode='WaiterCode';//��� ���������
//    QAttrWaiterID  = 'WaiterID'; // ID ���������, ���� �� �����, �� ������������ WaiterCode
      QAttrDateTime    = 'DateTime';  // �����, �� ������� ����� �������� ������ ���� (dd.mm.yyyy hh:mm ��� YYYYMMDD hh:mm)
      QAttrCheckRests  = 'checkrests'; // ����� �� ��������� ������� ����
      // �������� xml
      //RTagDishes       = 'Dishes';    // ������ ����. ������ ������ ����� (tag = RTagItem)
        //RAttrPrice       = 'Price';   // ���� ����� (� ��������)
        //QRAttrQuantity   = 'quantity';// ������� ����� (� �������� �����)

      RTagModifiers    = QTagModifiers; // ������ ��������������. ������ ������ ����� (tag = RTagItem)
        //RTagItem='Item'
          RAttrItemID      = 'Ident';        // ID �����/������������
          //RAttrPrice       = 'Price';     // ���� �����/������������ (� ��������, ����� ������ �� 100)
      RTagOrderTypes = 'OrderTypes';    // ������ ����� ������. ������ ������ ����� (tag = RCOTItem)
//        RAttrItemID      = 'Ident';
    {<-- ������� ��� ��������� ������ ���� �� ������ }
      {--> �������� ������ �������, ���������� QCmdGetOrders }
      QCmdGetOrderList = 'GetOrderList';
//      QAttrNeedIdents = 'NeedIdents';// ���� 1, �� � �������������� xml ����������� �������������� ���� ���������
//      QAttrNeedCodes  = 'NeedCodes'; // ���� 1, �� � �������������� xml ����������� ���� ���� ���������
//      QAttrNeedNames  = 'NeedNames'; // ���� 1, �� � �������������� xml ����������� ����� ���� ���������
        QAttrOnlyOpened = 'OnlyOpened';// ���� 1, �� � �������������� xml ����������� ������ �������� ������
        QRAttrLastVersion = 'lastversion'; // ���������� ��������� �������. ���� ������ ������� ������� ��������� � lastversion, �� ������������ "No changes", ����� ������� ����� 
//      QWaiter         = 'Waiter';    // ��������, refItem. ���� �����, �� � �������������� xml ����������� ������ ������ ����� ���������
//      QTable          = 'Table';     // ����, refItem. ���� �����, �� ������������ ������ ������ ����� �����
      // �������� xml
        //QRAttrLastVersion = 'lastversion';    // ������ ������� ������� 
        RTagVisit='Visit';             // ������������� ������
          //RAttrVisitID='VisitID';             // ������������� ������
          RAttrFinished     = 'Finished';       // �������� ����� ��� ���
          RAttrGuestTypeCode= QAttrGuestTypeCode;  // ��� ���� ������
          RAttrGuestTypeID  = QAttrGuestTypeID;    // ID ���� ������
          RAttrGuestTypeName= 'GuestTypeName';     // ��� ���� ������
          RAttrGuestsCount = QAttrGuestsCount;       // ���-�� ������
          RAttrPersistentComment='PersistentComment';// ����������� �����������
          RAttrNonpersistentComment='NonPersistentComment';// ������������� �����������
          RExternalID = 'ExternalID';
            RAttrExtSource= QAttrExtSource;     // id-���������, ��������� �����, int
            RAttrExtID = QAttrExtID;            // ������� id ������, ��� ������ �� ���������� ���������
          RTagGuests  = QTagGuests;        // ������ ������
          RAttrCardCode  = QAttrCardCode;      // ��� ����� �����
          RAttrIntfID    = QAttrIntfID;        // ID ���������� ����� �����
          RAttrIntfCode  = QAttrIntfCode;      // ��� ���������� ����� �����
          RAttrIntfName  = 'IntfName';         // ��� ����������
          RAttrGuestLabel = 'GuestLabel';
          RAttrSeatClosed = 'closed';          // ������� ����, ��� ����� �������
          RTagOrders = 'Orders'; // ������ ������� � ������. ������ ������ ����� (tag = 'Order')
            //ROrderTag = 'Order'; // �����
              RAttrVersion      = 'Version';         // ������ ������, � 7.4.8.0
              RAttrCRC32        = 'crc32';           // ����������� �����, � 7.5.2.257
              RAttrGuid         = 'guid';            // GUID, � 7.5.2.267
              RAttrLocked       = 'locked';          // ���� "����� ������������", � 7.5.2.366
              
              RAttrOrderName    = 'OrderName';       // ��� ������ (���� �������� - ��� �����, ����� ����������), � 7.4.8.1
              RAttrOrderURL     = 'url';             // URL ������ ��� ����� code.ucs.ru    
              RAttrTableCode    = QAttrTableCode;    // ��� �����
              RAttrWaiterCode   = QAttrWaiterCode;   // ��� �������� ���������
              RAttrLockedByCode = 'LockedByCode';    // ��� ���������, ���������� �����
              RAttrOrdCategCode = 'OrderCategCode';  // ��� ��������� ������
              RAttrOrdTypeCode  = 'OrderTypeCode';   // ��� ���� ������
              RAttrDefaulterCode= 'DefaulterCode';   // ��� ���� �������������
              RAttrTableID      = QAttrTableID;      // ID �����
              RAttrWaiterID     = QAttrWaiterID;     // ID �������� ���������
              RAttrLockedByID   = 'LockedByID';      // ID ���������, ���������� �����
              RAttrOrdCategID   = 'OrderCategID';      // ID ��������� ������
              RAttrOrdTypeID    = 'OrderTypeID';       // ID ���� ������
              RAttrDefaulterID  = 'DefaulterID';     // ID ���� ������������� ������
//              RAttrTableName   = QAttrTableName    // ��� �����
              RAttrWaiterName   = 'WaiterName';      // ��� �������� ���������
              RAttrLockedByName = 'LockedByName';    // ��� �a�������, ���������� �����
              RAttrOrdCategName = 'OrdCategName';    // ��� ��������� ������
              RAttrOrdTypeName  = 'OrdTypeName';     // ��� ���� ������
              RAttrDefaulterName= 'DefaulterName';   // ��� ���� �������������
              RAttrCreateTime2  = 'CreateTime';      // ���� � ����� �������� ������
              RAttrFinishTime   = 'FinishTime';      // ���� � ����� ���������� ������
              RAttrBillTime     = 'BillTime';        // ���� � ����� ������ �������
              RAttrDessertTime  = 'DessertTime';     // ���� � ����� ���������� �������
              //RAttrOrderSum     = 'OrderSum';      // ����� ������
              RAttrTotalPieces  = 'TotalPieces';     // ����� ������ ���� ���� ������
              RAttrPrepaySum    = 'PrepaySum';       // ����� ���������� ���������
              RAttrPromisedSum  = 'PromisedSum';     // ����� ���������� ���������
              RAttrPromoCode    = 'promoCode';       // �����-���
              RAttrPaid         = 'paid';            // ���� - ����� �������
              RAttrBill         = 'Bill';            // ���� �� � ������ ������
              RAttrBySeats      = 'bySeats';         // ���� - ����� ��������� �� ������
              RAttrReadyExists  = 'ReadyExists';     // ���� - � ������ ���� ��������������, �� ����������� �����
              RAttrWeightNeeded = 'WeightNeeded';    // ���� - � ������ ���� ����� � ������ "��������� �������� ����"
              RAttrReceiptError = 'ReceiptError';    // ���� �� � ������ ��������� ���    
              RAttrDessert      = 'Dessert';         // ���� � ������ ������ ��� ���
              RTagExternalID    = 'ExternalID';      // ������ ������� id ������, unbounded
//              RAttrExtSource  = AttrExtSource;     // id-���������, ��������� �����, int
//              RAttrExtID      = QAttrExtID;        // ������� id ������, ��� ������ �� ���������� ���������
              RTagExtraTables = 'ExtraTables'; // ������ �������������� ������, �������� item
                RExtraTableItem = 'item';            // ������ � �����, refitem + unbounded
//                RAttrID       = 'id';              // id �����
//                RAttrCode     = 'code';            // ��� �����

      {<-- �������� ������ ������� }

      {-->  �������� �����������: ������ ����������� }
      QCmdTerminalAuthStart = 'TerminalAuthStart';
//      QOrder          = 'Order';         // ! �����, orderElement
        QCurrency       = 'Currency';      // ! ������
//      QWaiter         = 'Waiter';        // ! ������
        QAttrAmount     = 'amount';        // ! ����� � ������
        QAttrAsPrepay   = 'asPrepayment';  // �������� ������ ��� ����������. ����� ��� ������ ����
      {<--  �������� �����������: ������ ����������� }

      {-->  �������� �����������: ������ }
      QCmdTerminalAuthPay = 'TerminalAuthPay';
//      QOrder          = 'Order';         // ! �����, orderElement
        QAttrTransactionID = 'transactionID';// ID ����������, int
        QAttrExtTransactionInfo='extTransactionInfo'; // ������ ��� �����������, String
        QAttrAuthCode = 'authCode';        // ��� �����������
        QAttrOwner    = 'owner';           // �������� �����
//      QAttrCardCode   = 'cardCode';      // ����� ����� (��� �����������)
      {<-- �������� �����������: ������ }

      {-->  �������� �����������: ������ }
      QCmdTerminalAuthError = 'TerminalAuthError';
//      QOrder          = 'Order';         // ! �����, orderElement
        QAttrErrorText='errorText';        // ����� ������
      {<-- �������� �����������: ������ }

      {-->  ����� ���������� �� ������� (�� �����������, � ������ �����) }
      QCmdLoginOnStation = 'LoginOnStation';
//      QStation      = 'Station';  // ! �������
//      QWaiter       = 'Waiter'    // ��������
        QAttrPassword = 'password'; // ! ������ ���������
//      QAttrCardCode = 'cardCode'; // ��� �������� ��������� (���� �����, �� Code � Password �� ������������)
      // �������� xml
      RAttrEmployeeID = 'EmployeeID';// ID ���������
      RTagOpRights    = 'OpRights'; // ������ ���� �� ��������. ������ ������ ����� (tag = 'oper')
        RTagOper      = 'oper';     // id ��������, �� ������� � ��������� ���� �����
      RTagObjRights   = 'ObjRights';// ������ ���� �� �������. ������ ������ ����� (tag = 'right')
        RTagRight     = 'right';    // id ����� �� ������
      RTagTables      = 'Tables';   // ������ ��������� ������
        RTagTable     = 'table';    // id �����
//    RTagOrders      = 'Orders';   // ������ ��������� �������
//      RTagOrder     = 'Order';    // �����, orderElement
          RAttrOwnOrder = 'own_order'; // ���� "���� �����"
          //
      {<--  ����� ���������� �� ������� }

      {-->  ���������������� ���������� }
      QCmdRegisterEmployee = 'RegisterEmployee';
//      QStation      = 'Station';  // ! �������, refItem
//      QWaiter       = 'Waiter'    // ! ��������, refItem
//      QManager      = 'Manager'   // ! ��������, �� ����� �������� ����������� �����������, refItem
        QPosition     = 'Position'; // ������� ������������, refItem + unbounded
        QAttrIsCashStation = 'iscashstation'; // ���� "������������ ������� ��� �������� �������", boolean
      // �������� xml
//    QRWaiter = 'Waiter'; // ��������, refItem
//    QRDrawer = 'Drawer'; // ����, refItem
      {<--  ���������������� ���������� }

      {-->  �������� ����������� ���������� }
      QCmdUnregisterEmployee = 'UnregisterEmployee';
//      QStation      = 'Station';  // ! �������, refItem
//      QWaiter       = 'Waiter'    // ! ��������, refItem
      {<--  �������� ����������� ���������� }

      {-->  ����� ��������� �� ���� �������� }
      QCmdFindEmployee = 'FindEmployee';
//      QAttrCardCode = 'CardCode';    // ��� �������� ���������
      // �������� xml
//      QRWaiter = 'Waiter';// ��������, refItem
      {<--  ����� ��������� �� ���� �������� }

      {-->  �������� �� ��������� ������ ��� �������� ���� }
      QCmdGetEmployeeInfo = 'GetEmployeeInfo';
//      QWaiter           = 'Waiter';   // !��������, �������� ���������� ���������, refItem
      // �������� xml
      QRDrawer       = 'Drawer';    // ����, refItem
//    RTagOpRights    = 'OpRights'; // ������ ���� �� ��������. ������ ������ ����� (tag = 'oper')
//      RTagOper      = 'oper';     // id ��������, �� ������� � ��������� ���� �����
//    RTagObjRights   = 'ObjRights';// ������ ���� �� �������. ������ ������ ����� (tag = 'right')
//      RTagRight     = 'right';    // id ����� �� ������
//    RTagTables      = 'Tables';   // ������ ��������� ������
//      RTagTable     = 'table';    // id �����
      {<--  �������� �� ��������� ������ ��� �������� ���� }

      {-->  �������� ������ ���������� }
      QCmdGetWaiterList = 'GetWaiterList';
//      QTable         = 'Table';    // ����
        QAttrRegisteredOnly = 'registeredOnly'; // ���� 1, �� ������������ ������ ������������������ � ����� ���������
      // �������� xml
      RTagWaiters     = 'Waiters';   // ������ ����������
        RTagWaiter      = 'waiter';    // id ���������
//        QRDrawer      = 'Drawer';    // ����, refItem
//        QRStation     = 'Station';   // ������� �������, �� ������� ��������� ��������, refItem    
      {<--  �������� ������ ���������� }
      {-->  ���������� ����� ��� }
      QCmdApplyPersonalCard = 'ApplyPersonalCard';
//      QAttrVisit    = 'Visit';          // !�����
//      QAttrOrderIdent='OrderIdent';     // !�����
//      QAttrCardCode  = 'CardCode';      // !��� ����� �����, string
//      QInterface  = 'Interface';        // !���������, refitem
        QCashier    = 'Cashier';          // ������, refitem
//      QStation    = 'Station';          // !�������, refitem
      {<--  ���������� ����� ��� }
      {-->  ������ ���������� ����� ��� }
      QCmdUndoPersonalCard = 'UndoPersonalCard';
//      QOrder        = 'Order';          // !�����, orderElement
//      QAttrCardCode  = 'cardCode';      // !��� ����� �����, string
//      QInterface  = 'Interface';        // !���������, refitem
//      QCashier    = 'Cashier';          // ������, refitem
      {<--  ������ ���������� ����� ��� }

      {-->  ������ ����������� ������ }
      QCmdSaveOrder = 'SaveOrder';
//      QOrder     = 'Order';           // !�����, orderElement
        QLockStation = 'LockStation';   // ��������, �� ����� ������� ����������� �����
//        QAttrVisitID = 'visit';       // ! ID ������
//        QAttrOrderID = 'orderIdent';  // ! ID ������
        QAttrDeferred = 'deferred';     // ���������������� ����� (����). ��� ����������� � ������� ����� ����������� ������������� ����� � �����.
        QAttrDontCheckXMLLicense = 'dontcheckLicense'; // �������� �������� �������� �� ���������� ������. �� ���������� ����� �����
        QSessionItem = 'Session';       // ������ ������� ������, ��. rkXmlUtl.SessionItem + unbounded
//        QAttrSessionID = 'sessionID'; // ���� SessionID <> 0, �� �������������� �����, ����� ��������� �����
          QAttrRemindTime= 'remindTime';// ! �����, � �������� ����� ������ ���� ������, datetime
//        QAttrIsDraft  = 'isDraft';    // �������, ��� ����� �������� ����������, boolean
//        QStation      = 'Station';    // �������, refitem
//        QAuthor       = 'Author';     // ��������, �� ����� �������� ��������� �����, refitem
          QCourse       = 'Course';     // ������� ������, refitem
          QDishItem     = 'Dish';       // �����, refitem + unbounded
//          QAttrQuantity='quantity';//!����� ���������� � �������� �����
            QAttrPrice  = 'price';      // ���� ����� � ��������, integer
            QAttrSeat   = 'seat';       // ����� ����������� �����, integer
            QModiItem   = 'Modi';       // �����������, refitem + unbounded
              QAttrCount  = 'count';    // ! ���������� �������������, integer
          QComboItem    = 'Combo';      // ����� �����, Dish + unbounded
//          QAttrQuantity='quantity';   // ! ����� ���������� � �������� �����
//          QAttrSeat   = 'seat';       // ����� ����������� �����, integer
            QComboCompItem= 'Component';// ��������� ����� �����
//            QAttrCount  = 'count';    // ! ���������� �����������, integer
//            QAttrPrice  = 'price';    // ���� ���������� � ��������, integer
//            QModiItem   = 'Modi';     // �����������, refitem + unbounded
          QPrepayItem   = 'Prepay';     // ����������, refitem + unbounded
//          QAttrAmount = 'amount';     // ! ����� ���������� (� ��������), integer
//          QAttrCardCode='cardCode';   // ��� ��������, string
//          QAttrSeat   = 'seat';       // ����� ����������� �����, integer
            QReason     = 'Reason';     // �������, �� ������� ������� ����������, refitem
      // �������� xml
//    ROrder = 'Order';
        RSAttrVisit     = 'visit';
        RsAttrOrderIdent= 'orderIdent';
        RAttrBasicSum   = 'basicSum';   // ����� � ������ � ������� ������
        RAttrNationalSum= 'nationalSum';// ����� � ������ � ������������ ������

      RErrorItem = 'Error';             // ������ �� ������, unbounded
//      RAttrErrorText  ='ErrorText';   // ����� ������
//      RAttrRK7ErrorN  ='RK7ErrorN';   // ��� ������
        RFaultyTag      = 'FaultyTag';
          RAny          = 'any';        // ��� ��������� xml-�������, �� ��������� �������� ��������� ������
//      RSessionItem    = QSessionItem; // ����� + unbounded
          RsAttrSessionID= 'sessionID';
      QCmdLoadOrderFromXML  = 'LoadOrderFromXML'; // ���������� ��������
      {<--  ������ ����������� ������ }

      {-->  �������� ������������ ������ }
      QCmdValidateOrder = 'ValidateOrder';
//      QTable          = 'Table';          // ����, refitem
///     QOrderCategory  = 'OrderCategory';  // ��������� ������, refitem
//      QGuestType      = 'GuestType';      // ��� ������, refitem
//      QSessionItem = 'Session';           // ����� + unbounded, ��. SaveOrder.QSessionItem
      // �������� xml
//    RErrorItem = 'Error';        // ������ �� ������, unbounded, ��. SaveOrder.RErrorItem
//        RAttrSessionID = 'sessionID';
      {<--  �������� ������������ ������ }

      {-->  ���������� ����� ������ }
      QCmdCalcOrder = 'CalcOrder';
//      QSessionItem = 'Session';           // ����� + unbounded, ��. SaveOrder.QSessionItem
      // �������� xml
      // ROrder = 'Order';
//        QSessionItem = 'Session';         // ����� + unbounded, ��. SaveOrder.QSessionItem
      {<--  ���������� ����� ������ }
      {-->  ���������� ����� ������ [2] }
      QCmdCalcOrder2 = 'CalcOrder2';
//      QROrder = 'Order';                  // !�����
        QRPaymentsTag = 'Payments';         // ������ �����, �������� ����������
//        RPayItem    = 'Pay';              // ������, refItem
            QRAttrAmount = 'amount';        // ����� ������ (� ��������), integer

      // �������� xml
//    QRPaymentsTag = 'Payments';           // ������ ���� �����, �������� ����� ��������
//      RPayItem      = 'Pay';              // ������, ��. rkXmlUtl.RPayItem

      {<--  ���������� ����� ������ [2]}

      {-->  �������� ����� }
      QCmdPayOrder = 'PayOrder';
        QAttrCalcBySeats  = 'calcBySeats';// ���������� ����� �� ������ (����� ����� ���)
//      QOrder            = 'Order';      // !�����
//        QAttrVisit      = 'visit';
//        QAttrOrderIdent = 'orderIdent';
//      QCashier          = 'Cashier';    // !������, refitem
//      QStation          = 'Station';    // !�������, refitem
        QPaymentItem      = 'Payment';    // ������, refItem + unbounded
//        QRAttrExtTransactionInfo='extTransactionInfo'; // ������� ��� �����������, string
//        QAttrCardCode   = 'cardCode';   // ��� ��� ����� �������
//        QAttrAmount     = 'amount';     // !����� � ������ (� ��������)
          QTipCharge      = 'TipCharge';  // ������� ��� ������, refItem
          QAttrTipAmount  = 'tipAmount';  // ����� ������ (� ��������)
          QAttrTerminalDetail = 'TerminalMaket'; //������������� ��������� ��� �����������
        QReceiptMaket   = 'ReceiptMaket'; // !������������� ��������� ��� ����, refItem
        QInvoiceMaket   = 'InvoiceMaket'; // ������������� ��������� ��� ���� �������, refItem
      // �������� xml
//    RPrintCheckItem     = 'PrintCheck';   // ������ �����, ��. rkXmlUtl.RPrintCheckItem + unbounded
      {<--  �������� ����� }

      {-->  �������� � ������ ������� ������ }
      QCmdChangeSessionCourse = 'ChangeSessionCourse';
//      QOrder            = 'Order';      // !�����
//      QCourse           = 'Course';     // ������� ������, refitem
//      QAttrIsDraft      = 'isDraft';    // ������� "��������", boolean
        QEmployee         = 'Employee';   // !��������, ����������� ��������
        QCourseFrom       = 'CourseFrom'; // ���� �����, �� ��������� �������� ��� ������ � ����� �������� ������
//      QSessionItem      = 'Session';    // ���� �����, �� ��������� �������� ������ ���� ����� � ����� UNI
          QAttrUNI        = 'uni';
      {<--  �������� � ������ ������� ������ }

      {-->  ���������� ������ }
      QCmdPrintBill = 'PrintBill';
        QAttrBySeats      = 'bySeats';    // ������� �� ������ (����� ����� ������)
//      QOrder            = 'Order';      // !�����
//      QCashier          = 'Cashier';    // !������, refItem
//      QStation          = 'Station';    // !�������, refItem
//      QMaket            = 'Maket';      // !������������� ��������� ��� �������, refItem
      {<--  ���������� ������ }

      {-->  ���������� ���������������� �������� }
      QCmdPrintMaket = 'PrintMaket';
//      QOrder            = 'Order';      // �����
//      QStation          = 'Station';    // !�������, refItem
//      QMaket            = 'Maket';      // ������������� ���������, refItem. ������ ���� ������ ���� �� 2-�: ��� Maket ��� Document
//      QDocument         = 'Document';   // ��� ��������� ��� ������, refItem. ������ ���� ������ ���� �� 2-�: ��� Maket ��� Document
//      QAttrLayoutFilters='LayoutFilters'; // ������ ������ ���� <����>=��������[{;<����=��������>}]
//      QAttrDataSourceParams='DataSourceParams'; // ��������� ����� ���� <����>=��������[{;<����=��������>}]
      {<--  ���������� ���������������� �������� }

      {-->  ���������� "�����" ������ � Esc ������������������� � ������� RK7 (��. escape.dat) ��� online ��� ���������� ��� ������ ������ }
      QCmdPrintRawData = 'PrintRawData';
        QPrinter       = 'Printer';       // �������, refItem
//      QOrder         = 'Order';         // �����, orderElement
        QRawData       = 'RawData';       //������ � ������, �������������� base64
        QAttrTimeout   = 'Timeout';       //������� �������� ���������� ����������, ��� 0 ��� ������ ����������� �������� � ������� ��� ������

      QCmdPrintDataXML = 'PrintDataXML';
        QPurpose       = 'Purpose';       // ���������� ������, refItem, ������ ���� � �������� "�� ��������"
        //QAttrTimeout   = 'Timeout';       //������� �������� ���������� ����������, ��� 0 ��� ������ ����������� �������� � ������� ��� ������
        QUnfiscal      = 'Unfiscal';      // ��. �������� �������������� ��������
      {<--  ���������� "�����" ������ }

      {-->  �������� ������ }
      QCmdUndoBill = 'UndoBill';
//      QOrder            = 'Order';      // !�����
//      QCashier          = 'Cashier';    // !������, refItem
//      QStation          = 'Station';    // !�������, refItem
//      QAttrSeat         = 'seat';       // �����, ��� �������� ������ ����� �������, integer
      {<--  �������� ������ }

      {-->  ������� ���������� ����� }
      QCmdCloseSeat = 'CloseSeat';
//      QOrder            = 'Order';      // �����, orderElement
//      QAttrSeat         = 'seat';       // ����� ����������� �����, integer
      {<--  ������� ���������� ����� }

      {-->  ������� �������� ���������� �����}
      QCmdOpenSeat = 'OpenSeat';
//      QOrder            = 'Order';      // �����, orderElement
//      QAttrSeat         = 'seat';       // ����� ����������� �����, integer
      {<--  ������� �������� ���������� �����}

      {-->  ������� ���� ����� �������� }
      QCmdTransferDishes = 'TransferDishes';
        QOrderSource      = 'OrderSource';// !����� ��������, orderElement
        QOrderDest        = 'OrderDest';  // !����� ��������, orderElement
        QDishes           = 'Dishes';     //
//        QDishItem       = 'Dish';       // �����, undounded
//          QAttrUNI        = 'uni';      // !uni �����
//          QAttrQuantity='quantity';     // ���������� � �������� �����, ���� �� ������ �� ����������� ��� �����
      {<--  ������� ���� ����� �������� }

      {-->  ��������� ���������� ������ (�� 10 ���) }
      QCmdLockOrder = 'LockOrder';
    //  QOrder          = 'Order';      // !�����, orderItem
        QAttrLockTime   = 'lockTime';   // �� ����� ����� ������������� �����
      {<--  ��������: ��������� ���������� ������ }

      {-->  ������ ���������� � ����� ��� }
      QCmdGetCardInfo = 'GetCardInfo';
//      QAttrCardCode = 'cardCode';  // ! ��� �����
//      QInterface  = 'Interface';   // ! ��������� � �����, refitem
      // �������� xml
      RCardInfo = 'CardInfo';
//      RAttrCardCode = 'cardCode';// ��� �����, string
        RAttrHolder = 'holder';   // ��������, string
        RAttrMaxAmount = 'maxAmount'; // ����. ����� (� ��������), integer
        RAttrAmount = 'amount';   // ������� (� ��������), integer
        RAttrMaxDisc= 'maxDisc';  // ����.����� ������ (� ��������), integer
        RDopInfo='DopInfo';       // ���.����, string
//      RMessage = 'Message';     // ��������� ��� ������, string
        RPrintMessage='PrintMessage'; // ��������� ��� ������, string
        ROutBuf = 'OutBuf';       // �������� �����, base64
          RAttrOutKind = 'kind';  // ��� ������ � ������, integer
        RDiscount  = 'Discount';  // ������, refItem
        RBonusType = 'BonusType'; // ��� ������, refItem
        RDefaulter = 'Defaulter'; // ������������, refItem
        RCurrency  = 'Currency';  // ������, refItem
          RAttrSubAcc = 'subacc'; // ����� ��������, integer
//        RAttrMaxAmount = 'maxAmount'; // ����. ����� (� ��������), integer
//        RAttrAmount = 'amount';   // ������� (� ��������), integer
      {<--  ������ ���������� � ����� ��� }

      {-->  ������ AnyInfo � FarCards }
      QCmdFarCardsAnyInfoRaw = 'FarCardsAnyInfoRaw';
//      QInterface  = 'Interface';   // ! ��������� � �����, refitem
//      QRawData       = 'RawData';  //! ������ � ������, �������������� base64
      // �������� xml
      RRawData       = QRawData;  //! ������ � ������, �������������� base64
      QCmdFarCardsAnyInfoXML = 'FarCardsAnyInfoXML';
//      QInterface  = 'Interface';   // ! ��������� � �����, refitem
      QXMLData       = 'XMLData';  //! ������ � XML ������� ��� �������� � Farcards
      // �������� xml
      RXMLData       = QXMLData;

      {-->  ��������� ������ ����� }
      QCmdMakeCardDeposit = 'MakeCardDeposit';
//      QStation      = 'Station';   // ! �������, refItem
//      QInterface    = 'Interface'; // ! ��������� � �����, refItem
//      QCashier    = 'Cashier';     // ! ������, �� ����� �������� �������� ��������, refItem
//      QCurrency     = 'Currency';  // ! ������, refItem
        QDepositReason='Reason';     // ������� ��������/�������, refItem
//      QInterface  = 'Interface';   //   ��������� � ����� �����, refitem
//        QAttrAmount = 'amount';    // ! ����� (� ��������), integer
//        QAttrCardCode = 'cardCode';// ! ��� �����, string
      {<-- ��������� ������ ����� }

      {-->  ����������/������� ����� }
      QCmdChangeDrawerBalance = 'ChangeDrawerBalance';
//      QStation      = 'Station';   // ! �������, refItem
//      QCashier      = 'Cashier';   // ! ������, �� ����� �������� �������� ��������, refItem
        QRCurrency    = 'Currency';  // ! ������, refItem
//      QRDrawer      = 'Drawer';    //   ����, refItem
//      QMaket        = 'Maket';     //   ������������� ��������� ��� ������ ��������/����������, refItem
//      QDepositReason= 'Reason';    //   ������� ��������/�������, refItem
//        QAttrAmount = 'amount';    // ! ����� +/- (� ��������), integer
      {<--  ����������/������� ����� }

      {-->  �������� ������� ����� � ����� }
      QCmdGetDrawerBalance = 'GetDrawerBalance';
//      QStation      = 'Station';   // ! �������, refItem
//      QRDrawer      = 'Drawer';    //   ����, refItem
      // �������� xml
      RItemTag = 'Item';
//      QRCurrency = 'Currency';     //   ������, refItem
//      QRDrawer      = 'Drawer';    //   ����, refItem
        QRPrinter     = 'Printer';   //   �������, refItem
//      QRAttrAmount  = 'amount';    //   ����� (� ��������), integer
      {<--  �������� ������� ����� � ����� }

      {-->  ������ �� �������� �������� }
      QCmdCheckLicense = 'CheckLicense';
        QAttrLicense = 'license'; // ��� ��������, enum('WebMon', 'WebRep', 'XMLSaveOrder')             
//      QRestaurant     = 'Restaurant'; // !��������. ���� �� ������, �� ������� �������
      {<--  ������ �� �������� �������� }
      {-->  ������� ����-������� }
      QCmdCreateInvoice = 'CreateInvoice';
    //  QOrder          = 'Order';      // !�����, orderItem
//    QRInvoice                = 'Invoice';
//      QRAttrInvoiceRegNo     = 'regno';    // ���
//      QRAttrInvoiceName      = 'name';     // ������������ �����������
//      QRAttrInvoiceAddress   = 'address';  // �����
//      QRAttrInvoiceExtraInfo = 'extrainfo';// ���.����
//      QRAttrInvoiceComment   = 'comment';  // �����������
      // �������� xml
//    QRInvoice                = 'Invoice'; // ��������� ���������
      {<--  ������� ����-������� }
      {-->  �������� ���������� � ����-������� }
      QCmdGetInvoice = 'GetInvoice';
    //  QOrder          = 'Order';      // �����, orderItem
//    QRInvoice                = 'Invoice';
//      QRAttrGuid             = 'guid';
      // �������� xml
//    QRInvoice                = 'Invoice'; // ��. QCmdCreateInvoice.QRInvoice
      {<--  �������� ���������� � ����-������� }

      QCmdXmlTransport = 'XmlTransport';
      QCmdLogicalDevices='LogicalDevices';
//      QStation      = 'Station';   // ! �������, refItem
        RLogicalDevices = 'LogicalDevices';
          RLogicalDevice = 'LogicalDevice';
  //          RAttrID='id';
  //          RAttrName = 'name';
  //          RAttrGuid = 'guid';
  //          RAttrCode = 'code';
            RAttrDriver = 'driver';
            RAttrNumber = 'number';
            RAttrModClass   = 'modClass';
      QCmdListDeviceMenu='ListDeviceMenu';
//      QStation      = 'Station';   // ! �������, refItem
        QDevice     = 'Device'; // ! refItem
        RDeviceMenu = 'DeviceMenu';
          RAttrCaption = 'caption';
          RAttrOperationId = 'operationId';
            RDialogInfo = 'DIALOGINFO';
              //RAttrCaption = 'caption';
      QCmdCallDeviceMenu='CallDeviceMenu';
//      QStation      = 'Station';   // ! �������, refItem
//      QDevice     = 'Device'; // ! refItem
        QMenuOperation = 'MENUOPERATION';
          QAttrOperationId = RAttrOperationId;
            QDialogInfo = RDialogInfo;


implementation

end.
