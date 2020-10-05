def group_val(first='2020-01-01', second='2020-10-03'):
    a = f'''SELECT
      PrintChecks00."GLOBALIDENT" AS "PRINTCHECKID",
      GLOBALSHIFTS00."SHIFTDATE" AS "SHIFTDATE",
      Visits00."SIFR" AS "VISIT",
      Visits00."GUESTCNT" AS "GUESTCNT",
      PrintChecks00."STATE" AS "CHECKSTATE",
      CURRENCYTYPES00."NAME" AS "CURRENCYTYPE",
      GLOBALSHIFTS00."SHIFTNUM" AS "SHIFTNUM",
      Payments."BASICSUM" AS "BASICSUM",
      CASHES00."NAME" AS "STATION",
      CurrLines00."FISCREGUNFISCTYPE" AS "FISCREGUNFISCTYPE",
      Payments."STATE" AS "PAYSTATE",
      1 AS "CHECKQNT",
      CHANGEABLEORDERTYPES00."NAME" AS "ORDERTYPE",
      UNCHANGEABLEORDERTYPES00."NAME" AS "ORDERCATEGORY",
      CURRENCIES00."NAME" AS "CURRENCY",
      EMPLOYEES00."NAME" AS "CASHIER"
    FROM PAYMENTS
    LEFT JOIN CurrLines CurrLines00
      ON (CurrLines00.Visit = Payments.Visit) AND (CurrLines00.MidServer = Payments.MidServer) AND (CurrLines00.UNI = Payments.CurrLineUNI)
    LEFT JOIN PrintChecks PrintChecks00
      ON (PrintChecks00.Visit = CurrLines00.Visit) AND (PrintChecks00.MidServer = CurrLines00.MidServer) AND (PrintChecks00.UNI = CurrLines00.CheckUNI)
    LEFT JOIN OrderSessions OrderSessions00
      ON (OrderSessions00.Visit = Payments.Visit) AND (OrderSessions00.MidServer = Payments.MidServer) AND (OrderSessions00.UNI = Payments.SessionUNI)
    LEFT JOIN Orders Orders00
      ON (Orders00.Visit = OrderSessions00.Visit) AND (Orders00.MidServer = OrderSessions00.MidServer) AND (Orders00.IdentInVisit = OrderSessions00.OrderIdent)
    LEFT JOIN GLOBALSHIFTS GLOBALSHIFTS00
      ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
    LEFT JOIN Visits Visits00
      ON (Visits00.Sifr = Orders00.Visit) AND (Visits00.MidServer = Orders00.MidServer)
    LEFT JOIN CURRENCYTYPES CURRENCYTYPES00
      ON (CURRENCYTYPES00.SIFR = Payments.iHighLevelType)
    LEFT JOIN CASHES CASHES00
      ON (CASHES00.SIFR = Payments.iStation)
    LEFT JOIN CHANGEABLEORDERTYPES CHANGEABLEORDERTYPES00
      ON (CHANGEABLEORDERTYPES00.SIFR = Orders00.COT)
    LEFT JOIN UNCHANGEABLEORDERTYPES UNCHANGEABLEORDERTYPES00
      ON (UNCHANGEABLEORDERTYPES00.SIFR = Orders00.UOT)
    LEFT JOIN CURRENCIES CURRENCIES00
      ON (CURRENCIES00.SIFR = Payments.Sifr)
    LEFT JOIN EMPLOYEES EMPLOYEES00
      ON (EMPLOYEES00.SIFR = PrintChecks00.iAuthor)
    WHERE
      (Payments."IGNOREINREP" = 0)
      AND ((Payments."STATE" = 3) OR (Payments."STATE" = 4) OR (Payments."STATE" = 5) OR (Payments."STATE" = 6))AND 
       "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}' '''
    return a





def cards(first='2020-01-01', second='2020-10-03'):
    a = f'''SELECT
  CurrLines."BINDEDSUM" AS "BINDEDSUM",
  PaymentsExtra00."OWNER" AS "OWNER",
  PaymentsExtra00."CARDNUM" AS "CARDNUM",
  CASHGROUPS00."NETNAME" AS "NETNAME",
  RESTAURANTS00."NAME" AS "RESTAURANTNAME",
  PrintChecks00."CHECKNUM" AS "CHECKNUM",
  1 AS "CHECKCOUNT",
  trk7EnumsValues0B00.UserMName AS "CURRENCYFORMAT",
  GLOBALSHIFTS00."SHIFTNUM" AS "SHIFTNUM",
  GLOBALSHIFTS00."SHIFTDATE" AS "SHIFTDATE",
  PDSCards00."FOLDER3" AS "FOLDER3",
  CURRENCIES00."NAME" AS "NAME",
  PDSCards00."FOLDER2" AS "FOLDER2",
  PDSCards00."FOLDER1" AS "FOLDER1"
FROM CURRLINES
LEFT JOIN "PAYMENTSEXTRA" PaymentsExtra00
  ON (PaymentsExtra00."VISIT" = CurrLines."VISIT") AND (PaymentsExtra00."MIDSERVER" = CurrLines."MIDSERVER") AND (PaymentsExtra00."PAYUNI" = CurrLines."PAYUNIFOROWNERINFO")
LEFT JOIN "CASHGROUPS" CASHGROUPS00
  ON (CASHGROUPS00."SIFR" = CurrLines."MIDSERVER")
LEFT JOIN "RESTAURANTS" RESTAURANTS00
  ON (RESTAURANTS00."SIFR" = CASHGROUPS00."RESTAURANT")
LEFT JOIN "PRINTCHECKS" PrintChecks00
  ON (PrintChecks00."VISIT" = CurrLines."VISIT") AND (PrintChecks00."MIDSERVER" = CurrLines."MIDSERVER") AND (PrintChecks00."UNI" = CurrLines."CHECKUNI")
LEFT JOIN "CURRENCYTYPES" CURRENCYTYPES00
  ON (CURRENCYTYPES00."SIFR" = CurrLines."IHIGHLEVELTYPE")
LEFT JOIN trk7EnumsValues trk7EnumsValues0B00
  ON (trk7EnumsValues0B00.EnumData = CURRENCYTYPES00."CURRENCYFORMAT") AND (trk7EnumsValues0B00.EnumName = 'TPayLineType')
LEFT JOIN "ORDERS" Orders00
  ON (Orders00."VISIT" = PrintChecks00."VISIT") AND (Orders00."MIDSERVER" = PrintChecks00."MIDSERVER") AND (Orders00."IDENTINVISIT" = PrintChecks00."ORDERIDENT")
LEFT JOIN "GLOBALSHIFTS" GLOBALSHIFTS00
  ON (GLOBALSHIFTS00."MIDSERVER" = Orders00."MIDSERVER") AND (GLOBALSHIFTS00."SHIFTNUM" = Orders00."ICOMMONSHIFT")
LEFT JOIN "PDSCARDS" PDSCards00
  ON (PDSCards00."ACCOUNTIDENT" = PaymentsExtra00."ACCOUNTIDENT") AND (PDSCards00."MINTERFACE" = PaymentsExtra00."ADDBYINTERFACE")
LEFT JOIN "CURRENCIES" CURRENCIES00
  ON (CURRENCIES00."SIFR" = CurrLines."SIFR")
'''
    return a


def nacenck(first='2020-01-01', second='2020-10-02'):
    test = f'''
    
    SELECT
     NUMBERS.NUM AS "NUM",
     GS.SHIFTDATE AS "SHIFTDATE",
     BALANCE.NAME AS "NAME",
     BALANCE.CHECKCNT AS "CHECKCNT",
     BALANCE.B_SUM AS "B_SUM"

    FROM GLOBALSHIFTS GS
    INNER JOIN (
     
     SELECT 6 AS NUM
    
     ) NUMBERS ON (1 = 1)
    LEFT JOIN 
    (
     
     
     
     
     (
    SELECT DISTINCT
      CASE WHEN SUM(DISCPARTS.SUM)>0 THEN 
       CASE WHEN (CASE WHEN DISCPARTS.SUM>0 THEN SQLCONSTS00.NAME + EV.USERMNAME ELSE SQLCONSTS01.NAME + EV.USERMNAME END)  --30  --31
       IS NULL THEN 5 ELSE 4 END
      ELSE
       CASE WHEN (CASE WHEN DISCPARTS.SUM>0 THEN SQLCONSTS00.NAME + EV.USERMNAME ELSE SQLCONSTS01.NAME + EV.USERMNAME END)  --30  --31
       IS NULL THEN 7 ELSE 6 END END AS "NUM",                                                             
      ISNULL((CASE WHEN DISCPARTS.SUM>0 THEN SQLCONSTS00.NAME + EV.USERMNAME ELSE SQLCONSTS01.NAME + EV.USERMNAME END),  --30  --31 
       CASE WHEN SUM(DISCPARTS.SUM) > 0 THEN max(SQLCONSTS02.NAME) ELSE max(SQLCONSTS03.NAME) END) AS "NAME",    --32  --33        
      COUNT(distinct PCH.GLOBALIDENT) AS "CHECKCNT",
      SUM(DISCPARTS.SUM) AS "B_SUM",
      NULL AS "COST",
 
      O.ICOMMONSHIFT AS "SHIFTNUM",
      O.UOT AS "UOT",
      O.MIDSERVER AS "MIDSERVER"
     FROM DISCPARTS
     JOIN PayBindings PayBindings00
      ON (PayBindings00.Visit = DiscParts.Visit) AND (PayBindings00.MidServer = DiscParts.MidServer) AND (PayBindings00.UNI = DiscParts.BindingUNI)
     JOIN CurrLines CurrLines00
      ON (CurrLines00.Visit = PayBindings00.Visit) AND (CurrLines00.MidServer = PayBindings00.MidServer) AND (CurrLines00.UNI = PayBindings00.CurrUNI)
     JOIN DishDiscounts DD
      ON (DD.Visit = DiscParts.Visit) AND (DD.MidServer = DiscParts.MidServer) AND (DD.UNI = DiscParts.DiscLineUNI) AND DD.ISCHARGE=0
     JOIN OrderSessions OrderSessions00
      ON (OrderSessions00.Visit = DD.Visit) AND (OrderSessions00.MidServer = DD.MidServer) AND (OrderSessions00.UNI = DD.SessionUNI)
     JOIN Orders O
      ON (O.Visit = OrderSessions00.Visit) AND (O.MidServer = OrderSessions00.MidServer) AND (O.IdentInVisit = OrderSessions00.OrderIdent)
     JOIN GLOBALSHIFTS GLOBALSHIFTS00
      ON (GLOBALSHIFTS00.MidServer = O.MidServer) AND (GLOBALSHIFTS00.ShiftNum = O.iCommonShift) AND GLOBALSHIFTS00.STATUS = 3
     LEFT JOIN SQLCONSTS SQLCONSTS00 ON SQLCONSTS00.SIFR=30
     LEFT JOIN SQLCONSTS SQLCONSTS01 ON SQLCONSTS01.SIFR=31
     LEFT JOIN SQLCONSTS SQLCONSTS02 ON SQLCONSTS02.SIFR=32
     LEFT JOIN SQLCONSTS SQLCONSTS03 ON SQLCONSTS03.SIFR=33
     JOIN PrintChecks PCH
      ON (PCH.Visit = CurrLines00.Visit) AND (PCH.MidServer = CurrLines00.MidServer) AND (PCH.UNI = CurrLines00.CheckUNI)  AND PCH.STATE=6
     LEFT JOIN TRK7ENUMSVALUES EV ON EV.ENUMNAME ='TChargeSource' AND DD.CHARGESOURCE = EV.ENUMDATA
     LEFT JOIN DISCOUNTS DISCOUNTS00
      ON (DISCOUNTS00.SIFR = DD.Sifr)
     where (DiscParts."NONZERODISC" = 1)
     GROUP BY
      O.ICOMMONSHIFT,O.UOT,O.MIDSERVER, CASE WHEN DISCPARTS.SUM>0 THEN 1 ELSE 0 END,
      (CASE WHEN DISCPARTS.SUM>0 THEN SQLCONSTS00.NAME + EV.USERMNAME ELSE SQLCONSTS01.NAME + EV.USERMNAME END) 

     WITH ROLLUP
     HAVING O.ICOMMONSHIFT IS NOT NULL
      AND O.UOT IS NOT NULL
      AND O.MIDSERVER IS NOT NULL
      AND CASE WHEN DISCPARTS.SUM>0 THEN 1 ELSE 0 END IS NOT NULL
     )
    ) BALANCE ON (NUMBERS.NUM = BALANCE.NUM AND GS.SHIFTNUM = BALANCE.SHIFTNUM AND GS.MIDSERVER = BALANCE.MIDSERVER) 
    LEFT JOIN UNCHANGEABLEORDERTYPES UOT ON (UOT.SIFR = BALANCE.UOT)

    LEFT JOIN CASHGROUPS CG ON (CG.SIFR = BALANCE.MIDSERVER)
    LEFT JOIN RESTAURANTS R ON R.SIFR = CG.RESTAURANT
    
    WHERE (GS.STATUS = 3 OR BALANCE.NUM = 10 OR BALANCE.NUM = 11)
     AND NOT((NUMBERS.NUM = 0 OR NUMBERS.NUM = 4 OR NUMBERS.NUM = 6)
             AND BALANCE.NAME IS NULL) AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}'
     
    
    
    '''
    return test


def dencheck(first='2020-01-01', second='2020-10-02'):
    test = f'''SELECT
  
  
  Orders01."PAID" AS "PAID",
  DishVoids."PRLISTSUM" AS "PRLISTSUM"
FROM DISHVOIDS
JOIN SessionDishes SessionDishes00
  ON (SessionDishes00.Visit = DishVoids.Visit) AND (SessionDishes00.MidServer = DishVoids.MidServer) AND (SessionDishes00.UNI = DishVoids.DishUNI)
LEFT JOIN ORDERVOIDS ORDERVOIDS00
  ON (ORDERVOIDS00.SIFR = DishVoids.Sifr)
LEFT JOIN OrderSessions OrderSessions00
  ON (OrderSessions00.Visit = DishVoids.Visit) AND (OrderSessions00.MidServer = DishVoids.MidServer) AND (OrderSessions00.UNI = DishVoids.VoidSessionUNI)
LEFT JOIN Orders Orders00
  ON (Orders00.Visit = OrderSessions00.Visit) AND (Orders00.MidServer = OrderSessions00.MidServer) AND (Orders00.IdentInVisit = OrderSessions00.OrderIdent)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = Orders00.MainWaiter)
LEFT JOIN OrderSessions OrderSessions01
  ON (OrderSessions01.Visit = SessionDishes00.Visit) AND (OrderSessions01.MidServer = SessionDishes00.MidServer) AND (OrderSessions01.UNI = SessionDishes00.SessionUNI)
LEFT JOIN Orders Orders01
  ON (Orders01.Visit = OrderSessions01.Visit) AND (Orders01.MidServer = OrderSessions01.MidServer) AND (Orders01.IdentInVisit = OrderSessions01.OrderIdent)
LEFT JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders01.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders01.iCommonShift)
LEFT JOIN EMPLOYEES EMPLOYEES01
  ON (EMPLOYEES01.SIFR = DishVoids.iAuthor)
LEFT JOIN EMPLOYEES EMPLOYEES02
  ON (EMPLOYEES02.SIFR = SessionDishes00.iAuthor)
LEFT JOIN MENUITEMS MENUITEMS00
  ON (MENUITEMS00.SIFR = SessionDishes00.Sifr)
LEFT JOIN CASHES CASHES00
  ON (CASHES00.SIFR = OrderSessions00.iStation)
LEFT JOIN PrintChecks PrintChecks00
  ON (PrintChecks00.Visit = Orders01.Visit) AND (PrintChecks00.MidServer = Orders01.MidServer) AND (PrintChecks00.UNI = Orders01.LastCheckUNI)
WHERE
  (SessionDishes00."ISCOMBO" = 0)
  AND (SessionDishes00."CHARGEUNI" = 0)
  AND (DishVoids."ISUNPRINTEDDISH" = 0)
  AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}' '''
    return test


def delcheck(first='2020-01-01', second='2020-10-12'):
    test = f'''SELECT
  Shifts00."PRINTED" AS "CASHSHIFTPRINTED",
  PrintChecks."BINDEDSUM" AS "SUM"
 
  

FROM PRINTCHECKS
LEFT JOIN ORDERVOIDS ORDERVOIDS00
  ON (ORDERVOIDS00.SIFR = PrintChecks.iVoid)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = PrintChecks.iDeleteManager)
LEFT JOIN Orders Orders00
  ON (Orders00.Visit = PrintChecks.Visit) AND (Orders00.MidServer = PrintChecks.MidServer) AND (Orders00.IdentInVisit = PrintChecks.OrderIdent)
LEFT JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
LEFT JOIN Visits Visits00
  ON (Visits00.Sifr = Orders00.Visit) AND (Visits00.MidServer = Orders00.MidServer)
LEFT JOIN CASHES CASHES00
  ON (CASHES00.SIFR = PrintChecks.iCloseStation)
LEFT JOIN Shifts Shifts00
  ON (Shifts00.MidServer = PrintChecks.MidServer) AND (Shifts00.iStation = PrintChecks.iCloseStation) AND (Shifts00.ShiftNum = PrintChecks.iShift)
WHERE
  ((PrintChecks."STATE" = 7))
  AND (PrintChecks."IGNOREINREP" = 0)
  AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}' '''
    return test


def cat_eat(first='2020-01-01', second='2020-03-02'):
    test = f'''SELECT
  
  PayBindings."PAYSUM" AS "PAYSUM",
  
  CLASSIFICATORGROUPS0000.NAME AS "CATEGORY"
  
FROM PAYBINDINGS
JOIN CurrLines CurrLines00
  ON (CurrLines00.Visit = PayBindings.Visit) AND (CurrLines00.MidServer = PayBindings.MidServer) AND (CurrLines00.UNI = PayBindings.CurrUNI)
JOIN PrintChecks PrintChecks00
  ON (PrintChecks00.Visit = CurrLines00.Visit) AND (PrintChecks00.MidServer = CurrLines00.MidServer) AND (PrintChecks00.UNI = CurrLines00.CheckUNI)
LEFT JOIN SaleObjects SaleObjects00
  ON (SaleObjects00.Visit = PayBindings.Visit) AND (SaleObjects00.MidServer = PayBindings.MidServer) AND (SaleObjects00.DishUNI = PayBindings.DishUNI)
LEFT JOIN OrderSessions OrderSessions00
  ON (OrderSessions00.Visit = SaleObjects00.Visit) AND (OrderSessions00.MidServer = SaleObjects00.MidServer) AND (OrderSessions00.UNI = SaleObjects00.SessionUNI)
LEFT JOIN Orders Orders00
  ON (Orders00.Visit = OrderSessions00.Visit) AND (Orders00.MidServer = OrderSessions00.MidServer) AND (Orders00.IdentInVisit = OrderSessions00.OrderIdent)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = Orders00.MainWaiter)
LEFT JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
LEFT JOIN SessionDishes SessionDishes00
  ON (SessionDishes00.Visit = SaleObjects00.Visit) AND (SessionDishes00.MidServer = SaleObjects00.MidServer) AND (SessionDishes00.UNI = SaleObjects00.DishUNI)
LEFT JOIN MENUITEMS MENUITEMS00
  ON (MENUITEMS00.SIFR = SessionDishes00.Sifr)
LEFT JOIN DISHGROUPS DISHGROUPS0000
  ON (DISHGROUPS0000.CHILD = MENUITEMS00.SIFR) AND (DISHGROUPS0000.CLASSIFICATION = 2560)
LEFT JOIN CLASSIFICATORGROUPS CLASSIFICATORGROUPS0000
  ON CLASSIFICATORGROUPS0000.SIFR * 256 + CLASSIFICATORGROUPS0000.NumInGroup = DISHGROUPS0000.PARENT  
LEFT JOIN DishDiscounts DishDiscounts00
  ON (DishDiscounts00.Visit = SaleObjects00.Visit) AND (DishDiscounts00.MidServer = SaleObjects00.MidServer) AND (DishDiscounts00.UNI = SaleObjects00.ChargeUNI)
LEFT JOIN trk7EnumsValues trk7EnumsValues0D00
  ON (trk7EnumsValues0D00.EnumData = SaleObjects00.OBJKIND) AND (trk7EnumsValues0D00.EnumName = 'tSaleObjectKind')
LEFT JOIN Orders Orders01
  ON (Orders01.Visit = PayBindings.Visit) AND (Orders01.MidServer = PayBindings.MidServer) AND (Orders01.IdentInVisit = PayBindings.OrderIdent)
WHERE
  (PrintChecks00."IGNOREINREP" = 0)
  AND ((PrintChecks00."STATE" = 6))
  AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}'
   '''
    return test


def nacenck2(first='2020-01-01', second='2020-10-02'):
    test = f'''SELECT
  DiscParts."SUM" AS "SUM",


  PrintChecks00."CHECKNUM" AS "CHECKNUM",
  
  trk7EnumsValues1600.UserMName AS "CHARGESOURCE"

FROM DISCPARTS
JOIN PayBindings PayBindings00
  ON (PayBindings00.Visit = DiscParts.Visit) AND (PayBindings00.MidServer = DiscParts.MidServer) AND (PayBindings00.UNI = DiscParts.BindingUNI)
JOIN CurrLines CurrLines00
  ON (CurrLines00.Visit = PayBindings00.Visit) AND (CurrLines00.MidServer = PayBindings00.MidServer) AND (CurrLines00.UNI = PayBindings00.CurrUNI)
JOIN PrintChecks PrintChecks00
  ON (PrintChecks00.Visit = CurrLines00.Visit) AND (PrintChecks00.MidServer = CurrLines00.MidServer) AND (PrintChecks00.UNI = CurrLines00.CheckUNI)
JOIN DishDiscounts DishDiscounts00
  ON (DishDiscounts00.Visit = DiscParts.Visit) AND (DishDiscounts00.MidServer = DiscParts.MidServer) AND (DishDiscounts00.UNI = DiscParts.DiscLineUNI)
JOIN OrderSessions OrderSessions00
  ON (OrderSessions00.Visit = DishDiscounts00.Visit) AND (OrderSessions00.MidServer = DishDiscounts00.MidServer) AND (OrderSessions00.UNI = DishDiscounts00.SessionUNI)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = OrderSessions00.iAuthor)
LEFT JOIN DISCOUNTS DISCOUNTS00
  ON (DISCOUNTS00.SIFR = DishDiscounts00.Sifr)
JOIN Orders Orders00
  ON (Orders00.Visit = OrderSessions00.Visit) AND (Orders00.MidServer = OrderSessions00.MidServer) AND (Orders00.IdentInVisit = OrderSessions00.OrderIdent)
JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
LEFT JOIN SaleObjects SaleObjects00
  ON (SaleObjects00.Visit = PayBindings00.Visit) AND (SaleObjects00.MidServer = PayBindings00.MidServer) AND (SaleObjects00.DishUNI = PayBindings00.DishUNI)
LEFT JOIN CASHGROUPS CASHGROUPS00
  ON (CASHGROUPS00.SIFR = PayBindings00.Midserver)
LEFT JOIN CASHES CASHES00
  ON (CASHES00.SIFR = PrintChecks00.iCloseStation)
LEFT JOIN Orders Orders01
  ON (Orders01.Visit = PrintChecks00.Visit) AND (Orders01.MidServer = PrintChecks00.MidServer) AND (Orders01.IdentInVisit = PrintChecks00.OrderIdent)
LEFT JOIN EMPLOYEES EMPLOYEES01
  ON (EMPLOYEES01.SIFR = Orders01.MainWaiter)
LEFT JOIN CURRENCYTYPES CURRENCYTYPES00
  ON (CURRENCYTYPES00.SIFR = CurrLines00.iHighLevelType)
LEFT JOIN CURRENCIES CURRENCIES00
  ON (CURRENCIES00.SIFR = CurrLines00.Sifr)
LEFT JOIN trk7EnumsValues trk7EnumsValues1600
  ON (trk7EnumsValues1600.EnumData = DishDiscounts00.CHARGESOURCE) AND (trk7EnumsValues1600.EnumName = 'tChargeSource')
LEFT JOIN RESTAURANTS RESTAURANTS00
  ON (RESTAURANTS00.SIFR = CASHGROUPS00.Restaurant)
LEFT JOIN trk7EnumsValues trk7EnumsValues1C00
  ON (trk7EnumsValues1C00.EnumData = GLOBALSHIFTS00.STATUS) AND (trk7EnumsValues1C00.EnumName = 'TRecordStatus')
LEFT JOIN EMPLOYEES EMPLOYEES02
  ON (EMPLOYEES02.SIFR = DishDiscounts00.iAuthor)
WHERE
  ((PrintChecks00."STATE" = 6))
  AND (DishDiscounts00."ISCHARGE" = 0)
  AND (DiscParts."NONZERODISC" = 1)
  AND ((GLOBALSHIFTS00.STATUS = 3))
  AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}'



    '''
    return test


def cat_eatter(first='2020-01-01', second='2020-10-02'):
    test = f'''SELECT

  CLASSIFICATORGROUPS0000.NAME AS "CATEGORY",
  SaleObjects00."NAME" AS "DISH",
  PayBindings."QUANTITY" AS "QUANTITY",
  PayBindings."PAYSUM" AS "PAYSUM"
 
FROM PAYBINDINGS
JOIN CurrLines CurrLines00
  ON (CurrLines00.Visit = PayBindings.Visit) AND (CurrLines00.MidServer = PayBindings.MidServer) AND (CurrLines00.UNI = PayBindings.CurrUNI)
JOIN PrintChecks PrintChecks00
  ON (PrintChecks00.Visit = CurrLines00.Visit) AND (PrintChecks00.MidServer = CurrLines00.MidServer) AND (PrintChecks00.UNI = CurrLines00.CheckUNI)
JOIN Orders Orders00
  ON (Orders00.Visit = PayBindings.Visit) AND (Orders00.MidServer = PayBindings.MidServer) AND (Orders00.IdentInVisit = PayBindings.OrderIdent)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = Orders00.MainWaiter)
LEFT JOIN SaleObjects SaleObjects00
  ON (SaleObjects00.Visit = PayBindings.Visit) AND (SaleObjects00.MidServer = PayBindings.MidServer) AND (SaleObjects00.DishUNI = PayBindings.DishUNI)
LEFT JOIN SessionDishes SessionDishes00
  ON (SessionDishes00.Visit = SaleObjects00.Visit) AND (SessionDishes00.MidServer = SaleObjects00.MidServer) AND (SessionDishes00.UNI = SaleObjects00.DishUNI)
LEFT JOIN MENUITEMS MENUITEMS00
  ON (MENUITEMS00.SIFR = SessionDishes00.Sifr)
LEFT JOIN DISHGROUPS DISHGROUPS0000
  ON (DISHGROUPS0000.CHILD = MENUITEMS00.SIFR) AND (DISHGROUPS0000.CLASSIFICATION = 2560)
LEFT JOIN CLASSIFICATORGROUPS CLASSIFICATORGROUPS0000
  ON CLASSIFICATORGROUPS0000.SIFR * 256 + CLASSIFICATORGROUPS0000.NumInGroup = DISHGROUPS0000.PARENT  
LEFT JOIN DishDiscounts DishDiscounts00
  ON (DishDiscounts00.Visit = SaleObjects00.Visit) AND (DishDiscounts00.MidServer = SaleObjects00.MidServer) AND (DishDiscounts00.UNI = SaleObjects00.ChargeUNI)
LEFT JOIN UNCHANGEABLEORDERTYPES UNCHANGEABLEORDERTYPES00
  ON (UNCHANGEABLEORDERTYPES00.SIFR = Orders00.UOT)
JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
LEFT JOIN OrderSessions OrderSessions00
  ON (OrderSessions00.Visit = SaleObjects00.Visit) AND (OrderSessions00.MidServer = SaleObjects00.MidServer) AND (OrderSessions00.UNI = SaleObjects00.SessionUNI)
LEFT JOIN CASHES CASHES00
  ON (CASHES00.SIFR = PrintChecks00.iCloseStation)
LEFT JOIN CASHGROUPS CASHGROUPS00
  ON (CASHGROUPS00.SIFR = PayBindings.Midserver)
LEFT JOIN CURRENCYTYPES CURRENCYTYPES00
  ON (CURRENCYTYPES00.SIFR = CurrLines00.iHighLevelType)
LEFT JOIN CURRENCIES CURRENCIES00
  ON (CURRENCIES00.SIFR = CurrLines00.Sifr)
LEFT JOIN Shifts Shifts00
  ON (Shifts00.MidServer = PrintChecks00.MidServer) AND (Shifts00.iStation = PrintChecks00.iCloseStation) AND (Shifts00.ShiftNum = PrintChecks00.iShift)
LEFT JOIN TABLES TABLES00
  ON (TABLES00.SIFR = Orders00.TableID)
LEFT JOIN PaymentsExtra PaymentsExtra00
  ON (PaymentsExtra00.Visit = CurrLines00.Visit) AND (PaymentsExtra00.MidServer = CurrLines00.MidServer) AND (PaymentsExtra00.PayUNI = CurrLines00.PayUNIForOwnerInfo)
LEFT JOIN trk7EnumsValues trk7EnumsValues1E00
  ON (trk7EnumsValues1E00.EnumData = SaleObjects00.OBJKIND) AND (trk7EnumsValues1E00.EnumName = 'tSaleObjectKind')
LEFT JOIN RESTAURANTS RESTAURANTS00
  ON (RESTAURANTS00.SIFR = CASHGROUPS00.Restaurant)
LEFT JOIN EMPLOYEES EMPLOYEES01
  ON (EMPLOYEES01.SIFR = SaleObjects00.iAuthor)
LEFT JOIN SessionDishes SessionDishes01
  ON (SessionDishes01.Visit = SessionDishes00.Visit) AND (SessionDishes01.Midserver = SessionDishes00.Midserver) AND (SessionDishes01.UNI = SessionDishes00.ComboDishUNI)
LEFT JOIN MENUITEMS MENUITEMS01
  ON (MENUITEMS01.SIFR = SessionDishes01.Sifr)
LEFT JOIN trk7EnumsValues trk7EnumsValues3600
  ON (trk7EnumsValues3600.EnumData = GLOBALSHIFTS00.STATUS) AND (trk7EnumsValues3600.EnumName = 'TRecordStatus')
LEFT JOIN CATEGLIST CATEGLIST00
  ON (CATEGLIST00.SIFR = MENUITEMS00.PARENT)
LEFT JOIN Payments Payments00
  ON (Payments00.Visit = CurrLines00.Visit) AND (Payments00.MidServer = CurrLines00.MidServer) AND (Payments00.UNI = CurrLines00.PayUNIForOwnerInfo)
LEFT JOIN CURRENCIES CURRENCIES01
  ON (CURRENCIES01.SIFR = Payments00.Sifr)
LEFT JOIN DISHGROUPS DISHGROUPS0001
  ON (DISHGROUPS0001.CHILD = MENUITEMS00.SIFR) AND (DISHGROUPS0001.CLASSIFICATION = 3840)
LEFT JOIN CLASSIFICATORGROUPS CLASSIFICATORGROUPS0001
  ON CLASSIFICATORGROUPS0001.SIFR * 256 + CLASSIFICATORGROUPS0001.NumInGroup = DISHGROUPS0001.PARENT  
WHERE
  ((PrintChecks00."STATE" = 6))
  AND (PrintChecks00."IGNOREINREP" = 0)
  AND ((GLOBALSHIFTS00.STATUS = 3))
  AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}'



    '''
    return test

def den_list(first='2020-01-01', second='2020-10-02'):
    f = f'''SELECT
  MENUITEMS00."NAME" AS "DISH",

  DishVoids."QUANTITY" AS "QUANTITY",
  DishVoids."DATETIME" AS "DATETIME___3",
  EMPLOYEES01."NAME" AS "WAITER",
  DishVoids."PRLISTSUM" AS "PRLISTSUM",
  EMPLOYEES00."NAME" AS "DELETEPERSON"

  
FROM DISHVOIDS
JOIN SessionDishes SessionDishes00
  ON (SessionDishes00.Visit = DishVoids.Visit) AND (SessionDishes00.MidServer = DishVoids.MidServer) AND (SessionDishes00.UNI = DishVoids.DishUNI)
LEFT JOIN MENUITEMS MENUITEMS00
  ON (MENUITEMS00.SIFR = SessionDishes00.Sifr)
LEFT JOIN ORDERVOIDS ORDERVOIDS00
  ON (ORDERVOIDS00.SIFR = DishVoids.Sifr)
LEFT JOIN EMPLOYEES EMPLOYEES00
  ON (EMPLOYEES00.SIFR = DishVoids.iAuthor)
JOIN OrderSessions OrderSessions00
  ON (OrderSessions00.Visit = SessionDishes00.Visit) AND (OrderSessions00.MidServer = SessionDishes00.MidServer) AND (OrderSessions00.UNI = SessionDishes00.SessionUNI)
JOIN Orders Orders00
  ON (Orders00.Visit = OrderSessions00.Visit) AND (Orders00.MidServer = OrderSessions00.MidServer) AND (Orders00.IdentInVisit = OrderSessions00.OrderIdent)
LEFT JOIN EMPLOYEES EMPLOYEES01
  ON (EMPLOYEES01.SIFR = Orders00.MainWaiter)
LEFT JOIN OrderSessions OrderSessions01
  ON (OrderSessions01.Visit = DishVoids.Visit) AND (OrderSessions01.MidServer = DishVoids.MidServer) AND (OrderSessions01.UNI = DishVoids.VoidSessionUNI)
LEFT JOIN CASHES CASHES00
  ON (CASHES00.SIFR = OrderSessions01.iStation)
LEFT JOIN CASHES CASHES01
  ON (CASHES01.SIFR = OrderSessions00.iStation)
LEFT JOIN CASHGROUPS CASHGROUPS00
  ON (CASHGROUPS00.SIFR = DishVoids.Midserver)
JOIN GLOBALSHIFTS GLOBALSHIFTS00
  ON (GLOBALSHIFTS00.MidServer = Orders00.MidServer) AND (GLOBALSHIFTS00.ShiftNum = Orders00.iCommonShift)
LEFT JOIN RESTAURANTS RESTAURANTS00
  ON (RESTAURANTS00.SIFR = CASHGROUPS00.Restaurant)
LEFT JOIN trk7EnumsValues trk7EnumsValues1B00
  ON (trk7EnumsValues1B00.EnumData = GLOBALSHIFTS00.STATUS) AND (trk7EnumsValues1B00.EnumName = 'TRecordStatus')
WHERE
  ((GLOBALSHIFTS00.STATUS = 3))
  AND (DishVoids."ISUNPRINTEDDISH" = 0)
   AND "SHIFTDATE" >= '{first}' and "SHIFTDATE" <= '{second}' '''

    return f


def cards_dis(first='2020-01-01', second='2020-10-04'):
    a = f'''

SELECT  
  isnull(PDSCards00.FOLDER1,isnull(PDSCards01.FOLDER1,' '))+'-'+isnull(PDSCards00.FOLDER2,isnull(PDSCards01.FOLDER2,' '))+'-'+isnull(PDSCards00.FOLDER3,isnull(PDSCards01.FOLDER3,' ')) AS "DEP",
  sum(DiscParts."SUM") AS "DISCSUM",                                                                                                                   
  (CASE WHEN (ROW_NUMBER() OVER (PARTITION BY PrintChecks00."CHECKNUM",DishDiscounts00."HOLDER",CURRENCIES00.NAME ORDER BY PrintChecks00."CHECKNUM")=1) THEN 1 
	ELSE 0
	END)  AS "CHECKCOUNT", 
  Discounts00."NAME" AS "DISCOUNT",                                                                                                  
  DishDiscounts00."HOLDER" AS "HOLDER",                                                                                                                
  PrintChecks00."CHECKNUM" AS "CHECKNUM",                                                                                                              
  DishDiscounts00."CARDCODE" AS "CARDCODE",                                                                                                            
  sum(PayBindings00.PAYSUM) AS "BINDEDSUM",                                                                                                           
  GlobalShifts00."SHIFTNUM" AS "SHIFTNUM",                                                                                                             
  GlobalShifts00."SHIFTDATE" AS "SHIFTDATE",                                                                                                           
  CashGroups00."NETNAME" AS "NETNAME",
  CURRENCIES00."NAME" AS "CURRENCY",
  ORIGCURRENCIES."NAME" AS "ORIGCURRENCY",
  Restaurants00."NAME" AS "RESTAURANTNAME",
  (CASE WHEN (ROW_NUMBER() OVER (PARTITION BY Discounts00."NAME",                                   
								 DishDiscounts00."CARDCODE",                                                                              
								 GlobalShifts00."SHIFTNUM",                                                                                                             
								 GlobalShifts00."SHIFTDATE",                                                                                                           
								 CashGroups00."NETNAME",
								 Restaurants00."NAME" ORDER BY DishDiscounts00."CARDCODE")=1) THEN 1 
	ELSE 0
	END) AS "DISCOUNTVISIT"
FROM DISCPARTS                                                                                                                                         
LEFT JOIN PayBindings PayBindings00                                                                                                                    
  ON (PayBindings00.Visit = DiscParts.Visit) AND (PayBindings00.MidServer = DiscParts.MidServer) AND (PayBindings00.UNI = DiscParts.BindingUNI)     
LEFT JOIN CurrLines CurrLines00                                                                                                                        
  ON (CurrLines00.Visit = PayBindings00.Visit) AND (CurrLines00.MidServer = PayBindings00.MidServer) AND (CurrLines00.UNI = PayBindings00.CurrUNI)     
LEFT JOIN PAYMENTS PAYMENTS01
  ON (PAYMENTS01.Visit = CurrLines00.Visit) AND (PAYMENTS01.MidServer = CurrLines00.MidServer) AND (PAYMENTS01.UNI = CurrLines00.PayUNIForOwnerInfo )
LEFT JOIN PrintChecks PrintChecks00                                                                                                                    
  ON (PrintChecks00.Visit = CurrLines00.Visit) AND (PrintChecks00.MidServer = CurrLines00.MidServer) AND (PrintChecks00.UNI = CurrLines00.CheckUNI)    
LEFT JOIN trk7EnumsValues trk7EnumsValues0800                                                                                                          
  ON (trk7EnumsValues0800.EnumData = PrintChecks00.State) AND (trk7EnumsValues0800.EnumName = 'TDrawItemState')                                        
LEFT JOIN DishDiscounts DishDiscounts00                                                                                                                
  ON (DishDiscounts00.Visit = DiscParts.Visit) AND (DishDiscounts00.MidServer = DiscParts.MidServer) AND (DishDiscounts00.UNI = DiscParts.DiscLineUNI) 
LEFT JOIN Discounts Discounts00
  ON (Discounts00.SIFR = DishDiscounts00.Sifr)
LEFT JOIN Orders Orders00                                                                                                                              
  ON (Orders00.Visit = PrintChecks00.Visit) AND (Orders00.MidServer = PrintChecks00.MidServer) AND (Orders00.IdentInVisit = PrintChecks00.OrderIdent)  
LEFT JOIN GlobalShifts GlobalShifts00                                                                                                                  
  ON (GlobalShifts00.MidServer = Orders00.MidServer) AND (GlobalShifts00.ShiftNum = Orders00.iCommonShift)                                             
LEFT JOIN CashGroups CashGroups00                                                                                                                      
  ON (CashGroups00.SIFR = PrintChecks00.Midserver)                                                                                                     
LEFT JOIN Restaurants Restaurants00
  ON (Restaurants00.SIFR = CashGroups00.Restaurant)
LEFT JOIN PaymentsExtra PaymentsExtra00
  ON (PaymentsExtra00.Visit = CurrLines00.Visit) AND (PaymentsExtra00.MidServer = CurrLines00.MidServer) AND (PaymentsExtra00.PayUNI = CurrLines00.PayUNIForOwnerInfo)
LEFT JOIN PDSCards PDSCards00
  ON (PDSCards00.AccountIdent = PaymentsExtra00.AccountIdent) AND (PDSCards00.MInterface = PaymentsExtra00.AddByInterface)
LEFT JOIN PDSCards PDSCards01
  ON (PDSCards01.AccountIdent = DishDiscounts00.AccountIdent) AND (PDSCards01.MInterface = DishDiscounts00.MINTERFACE)
     AND PDSCards01.CARDCODE=DishDiscounts00.CARDCODE
LEFT JOIN CURRENCIES CURRENCIES00
  ON  CURRENCIES00.SIFR=CurrLines00.SIFR 
LEFT JOIN CURRENCIES ORIGCURRENCIES 
  ON  ORIGCURRENCIES.SIFR=PAYMENTS01.SIFR 
WHERE                                                                                                                                                  
  ((PrintChecks00.State = 6) OR (PrintChecks00.State = 7))                                                                                             
  and (DishDiscounts00."CARDCODE" <> '')                                                                              
group by
  isnull(PDSCards00.FOLDER1,isnull(PDSCards01.FOLDER1,' '))+'-'+isnull(PDSCards00.FOLDER2,isnull(PDSCards01.FOLDER2,' '))+'-'+isnull(PDSCards00.FOLDER3,isnull(PDSCards01.FOLDER3,' ')),
  DishDiscounts00."HOLDER", 
  PrintChecks00."CHECKNUM" ,
  DishDiscounts00."CARDCODE",
  GlobalShifts00."SHIFTNUM",
  GlobalShifts00."SHIFTDATE",
  CashGroups00."NETNAME",
  Restaurants00."NAME",
  Discounts00."NAME",
  CURRENCIES00.NAME,
  ORIGCURRENCIES.NAME
'''
    return a


