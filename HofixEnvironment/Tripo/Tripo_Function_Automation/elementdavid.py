# 公共文本
# 登录界面
import time

import elementdavid

web = "http://tripo.hotfix.travelconnect.co/#/login"
# web = "http://tripo.staging.travelconnect.co/#/login"
# web = "https://system.tripo.ai/#/login"

textaccount = "david"
textpassword = "Travel2021"
textcompanycode = "TC0139"
# textcompanycode = "TC0002"
# 抬头
textphone = "1340462788"
textdiscount = "100"

#抬頭備註部分
textrisephone = "電話1212344774"
textrisemobile = "手機121234548"
textrisefax = "傳真13245127"
textriseEmail = "電郵123454@hk.com"
textriseprovince = "省份信息"
textrisecity = "城市信息"
textriseaddress = "地址信息第一段有13個字：\n信息第二段有22個字：信息第二段有22個字：\n信息第三段有44個字：信息第三段有44個字：信息第三段有44個字：信息第三段有44個字："
textriseremark = "備註信息第一段有13個字：\n信息第二段有22個字：信息第二段有22個字：\n信息第三段有44個字：信息第三段有44個字：信息第三段有44個字：信息第三段有44個字："
textriseremark1 = "備註1信息第一段有14個字：\n信息第二段有22個字：信息第二段有22個字：\n信息第三段有44個字：信息第三段有44個字：信息第三段有44個字：信息第三段有44個字："
textriseremark2 = "備註2信息第一段有14個字：\n信息第二段有22個字：信息第二段有22個字：\n信息第三段有44個字：信息第三段有44個字：信息第三段有44個字：信息第三段有44個字："
textriseremark3 = "備註3信息第一段有14個字：\n信息第二段有22個字：信息第二段有22個字：\n信息第三段有44個字：信息第三段有44個字：信息第三段有44個字：信息第三段有44個字："



#退款申請

textbooking_invoice_item_refundapplication_contactperson = "david"
textbooking_invoice_item_refundapplication_phone = "123456789"
textbooking_invoice_item_refundapplication_remark = "機票項目退款申請的退款提示"
textbooking_invoice_item_refundapplication_description = "機票項目退款申請的說明"
textbooking_invoice_item_refundapplication_xo_remark = "發票機票項目同步創建xo 的退款申請的退款提示"
textbooking_invoice_item_refundapplication_invoice_remark = "xo機票項目同步創建invoice 的退款申請的退款提示"

# api机票
texttrip = "tpe"
textreturn = "nrt"
# 手输机票
textcontentpnr1 = "--- TST SFP ---\nRP/HKGH222X8/HKGH222X8            IC/SU  23FEB22/0719Z   594DUK\nHKGH222X8/0122IC/20FEB22\n  1.TUMULAK/RICKY INF\n  2  SU 053 E 21FEB 1 LEDSVO         FLWN\n  3  AF4364 Y 21FEB 1 SVOCDG         FLWN\n     OPERATED BY AEROFLOT\n  4  AF 006 U 21FEB 1 CDGJFK         FLWN\n  5 MIS 1A HK1 HKG 30DEC-MOL MAESTRO"
textcontentpnr2 = "--- TST SFP ---\nRP/HKGH222X8/HKGH222X8            IC/SU  23FEB22/0719Z   594DUK\nHKGH222X8/0122IC/20FEB22\n  1.TUMULAK/RICKY INF\n  2  SU 053 E 21FEB 1 PVGSVO         FLWN\n  3  AF4364 Y 21FEB 1 SVOCDG         FLWN\n     OPERATED BY AEROFLOT\n  4  AF 006 U 21FEB 1 CDGJFK         FLWN\n  5 MIS 1A HK1 HKG 30DEC-MOL MAESTRO"
textcontentapipnr1 = "5MU524"
textbasicfare_invoice1 = "301"
textbasicfare_xo1 = "300"
texttickettax_invoice1 = "301"
texttickettax_xo1 = "300"

textbasicfare_invoice2 = "401"
textbasicfare_xo2 = "400"
texttickettax_invoice2 = "401"
texttickettax_xo2 = "400"

# 酒店
texthotel_search1 = "手输酒店一"
texthotelcity1 = "香港"
texthotelcountry1 = "中国"
texthotelpropertytype1 = "hotel住宿類型"
texthotelroomplan1 = "hotel房間計劃"
texthotelspecial1 = "hote特別"
texthotelfare_invoice1 = "501"
texthotelfare_xo1 = "500"
texthotelfare_unit1 = "hotelunit1"
texthotelfare_remark1 = "酒店備註第一段有13個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："

texthotel_search2 = "手输酒店二"
texthotelcity2 = "香港"
texthotelcountry2 = "中国"
texthotelpropertytype2 = "hotel住宿類型"
texthotelroomplan2 = "hotel房間計劃"
texthotelspecial2 = "hote特別"
texthotelfare_invoice2 = "601"
texthotelfare_xo2 = "600"
texthotelfare_unit2 = "hotelunit2"
texthotelfare_remark2 = "酒店備註第一段有13個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："
# 其他费用
textothercharge_invoice1 = "701"
textothercharge_xo1 = "700"
textothercharge_unit1 = "msicunit1"
textothercharge_remark1 = "其他費用備註第一段有15個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："
textothercharge_invoice2 = "801"
textothercharge_xo2 = "800"
textothercharge_unit2 = "msicunit2"
textothercharge_remark2 = "其他費用備註第一段有15個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："

#一日游
textdaytour_invoice1 = "901"
textdaytour_xo1 = "900"
textdaytour_unit1 = "tourunit1"
textdaytour_remark1 = "一日遊備註第一段有14個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："
textdaytour_itemremark1 = "一日遊項目備註第一段有16個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："

textdaytour_invoice2 = "1001"
textdaytour_xo2 = "1000"
textdaytour_unit2 = "tourunit2"
textdaytour_remark2 = "一日遊備註第一段有14個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："
textdaytour_itemremark2 = "一日遊項目備註第一段有16個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："
textdaytour_invoice3 = "1001"
textdaytour_xo3 = "1000"

#團
textgroupname1 = "團名1"
textgroupcontacts1 = "David1"
textgroupdescription1 = "套票說明第一段有13個字：\n說明第二段有22個字：說明第二段有22個字：\n說明第三段有44個字：說明第三段有44個字：說明第三段有44個字：說明第三段有44個字："
textgroupremark1 = "套票備註第一段有13個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："

textgroupname2 = "團名2"
textgroupcontacts2 = "David2"
textgroupdescription2 = "套票說明第一段有13個字：\n說明第二段有22個字：說明第二段有22個字：\n說明第三段有44個字：說明第三段有44個字：說明第三段有44個字：說明第三段有44個字："
textgroupremark2 = "套票備註第一段有13個字：\n備註第二段有22個字：備註第二段有22個字：\n備註第三段有44個字：備註第三段有44個字：備註第三段有44個字：備註第三段有44個字："

#乘客
textpassengerfirstname1 = "f_ticket"
textpassengersecondname1 = "s_ticket"
textpassengerfirstname2 = "f_hotel"
textpassengersecondname2 = "s-hotel"
textpassengerfirstname3 = "f_msic"
textpassengersecondname3 = "s-msic"
textpassengerfirstname4 = "f_tour"
textpassengersecondname4 = "s-tour"
textpassengerfirstname5 = "f_group"
textpassengersecondname5 = "s-group"



# 公共element

webaccount = ".ant-row:nth-child(1) .ant-input"
webpassword = ".ant-input-affix-wrapper > .ant-input"
webcompanycode = ".ant-row:nth-child(3) .ant-input"
weblogin = ".login-button"

# 抬头
# 发票
createinvoce = ".btn-bar-line-2 > .ant-btn:nth-child(3)"
fieldinvoice_popcustomer = ".select-customer .PopoverSearchTable > .ant-input"  # 弹出客户
#报价单
createquotation = ".btn-bar:nth-child(3) > .ant-btn:nth-child(3)"
fieldquotation_popustomer = ".quotation-detail .ant-input"
#xo
createxo = ".btn-bar-line-2 > .ant-btn:nth-child(2)"
fieldxo_popustomer = ".value-el"
fieldxo_customer = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"
fieldxo_next = ".ant-btn:nth-child(1)"
fieldxo_popsupplier = ".supplier-box .PopoverSearchTable > .ant-input"
fieldxo_supplier = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2) > .line-clamp"

fieldxo_popconsultant = "#infoForm_FollowID > div > div"
fieldxo_consultant = "li.ant-select-dropdown-menu-item:nth-child(1)"


#詢價單
fieldbooking = ".bottom-detail .font-ari"
# fieldbooking_invoice = ".ant-tabs-nav-container:nth-child(2) .ant-tabs-tab:nth-child(2)"
# fieldbooking_invoice = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[2]/div/div[1]/div[2]/div/div/div[1]/div/div/div/div/div[1]/div[2]"

fieldbooking_invoice = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div > div > div > div > div > div > div:nth-of-type(2)"
fieldbooking_invoice_item = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div > div.clearfix.control-bar > label > span.ant-checkbox > input"

#報價單轉發票和xo部分
fieldbooking_quotation = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-bar.ant-tabs-top-bar.ant-tabs-card-bar > div > div > div > div > div:nth-child(1) > div.ant-tabs-tab-active.ant-tabs-tab"
fieldbooking_quotation_item = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div > div.clearfix.control-bar > label > span.ant-checkbox > input"
fieldbooking_quotation_item_xo_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(4)"
fieldbooking_quotation_item_invoice_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(3)"
#xo轉報價單單部分
fieldbooking_supplier = ".quote-list > div:nth-child(2) > span:nth-child(2)"
fieldbooking_xo = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1)"
fieldbooking_xo_item = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"
fieldbooking_xo_item_quotation_confirm = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(6)"


#發票轉xo部分
fieldbooking_invoice_item_xo = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(4)"
fieldbooking_invoice_item_xo_item = "div#content > div > div:nth-of-type(2) > div > label > span > input"
fieldbooking_invoice_item_xo_confirm = "div#content > div > div:nth-of-type(4) > button"


#報價單編輯

#發票編輯
#xo編輯
#報價單、發票、xo編輯
fieldbooking_invoice_edit = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div:nth-child(1) > div.clearfix.control-bar > i:nth-child(5) > svg"
fieldbooking_quotation_edit = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.list-detail.ant-spin-nested-loading > div > div.list.heighter > div:nth-child(1) > div.clearfix.control-bar > i:nth-child(4) > svg"
#發票複製：
fieldbooking_invoice_copy = "#content > div > div.bottom-bar > div > button:nth-child(1)"
#選擇複製到本地文件夾
fieldbooking_invoice_copy_local = "#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-body > div:nth-child(1)"
fieldbooking_invoice_copy_confirm ="#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > div > button.ant-btn.ant-btn-primary"
fieldbooking_quotation_copy_confirm ="#content > div > div.copy-mount-node > div > div > div.ant-modal-wrap > div > div.ant-modal-content > div.ant-modal-footer > button.PublicButton.ant-btn.ant-btn-primary"
#發票退款申請部分
fieldbooking_invoice_item_refundapplication = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(1)"
# fieldbooking_invoice_item_refundapplication_item = ".list-info > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"

fieldbooking_invoice_item_refundapplication_item = "#content > div > div.RefundApplicationContent > div.code-tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div > div.reset_tabs_card.two-tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.air-tickets.ant-tabs-tabpane.ant-tabs-tabpane-active > div.list-info > div > div:nth-child(2) > div.top > label > span > input"
fieldbooking_invoice_item_refundapplication_confirm = "button.ant-btn-primary:nth-child(1)"
fieldbooking_invoice_item_refundapplication_contactperson = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[1]/div[2]/div/span/input"
fieldbooking_invoice_item_refundapplication_phone = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[2]/div[2]/div/span/input"
fieldbooking_invoice_item_refundapplication_remark = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[8]/div[2]/div/span/div/div/div[1]/textarea"
fieldbooking_invoice_item_refundapplication_description = "/html/body/div/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[1]/div[2]/form/div[9]/div[2]/div/span/div/div/div[1]/textarea"
fieldbooking_invoice_item_refundapplication_calendar = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div/div[2]/form/div[6]/div[2]/div/span/span/span/div/input"  # 酒店日历
fieldbooking_invoice_item_refundapplication_xo = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div[2]"
fieldbooking_invoice_item_refundapplication_xo_remark = "/html/body/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[3]/div[2]/div[2]/form/div[2]/div[2]/div/span/textarea"
fieldbooking_invoice_item_refundapplication_submit = "/html/body/div[1]/div/div/div[2]/div/div[3]/button[2]"

#xo退款申請部分
fieldbooking_xo_item_refundapplication = ".ant-collapse-content-active > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > button:nth-child(2)"


#發票收款部分
fieldbooking_invoice_item_receipt = "div#content > div > div:nth-of-type(5) > div:nth-of-type(2) > div > div > div:nth-of-type(2) > div > div > div:nth-of-type(3) > div:nth-of-type(2) > div:nth-of-type(2) > div:nth-of-type(2) > div > button:nth-of-type(3)"
fieldbooking_invoice_item_receipt_allfare = "div#content > div > div:nth-of-type(3) > button"
fieldbooking_invoice_item_receipt_way = "#content > div > div.reset_tabs_card.tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.order-box > div > div:nth-child(1) > div.pay-input > div > div > div"
fieldbooking_invoice_item_receipt_waydefault = "div#dbfd488e-fa78-4853-c64f-f2222db1d9c8 > ul > li"
fieldbooking_invoice_item_receipt_bankchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[2]/div[2]/span/div[1]/div[2]/input"
fieldbooking_invoice_item_receipt_creditchage = "/html/body/div[1]/div/div/div[2]/div/div[5]/div[3]/div[1]/div[2]/div/div[3]/div[2]/span/div[1]/div[2]/input"

fieldbooking_invoice_item_receipt_comfirm = "#content > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary.ant-btn-lg"

#xo付款部分
fieldbooking_xo_item_receipt = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(5)"
fieldbooking_xo_item_receipt_comfirm = "button.ant-btn-lg:nth-child(2)"
fieldbooking_xo_item_refund = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(4)"

#xo收款部分



#發票退款部分
fieldbooking_invoice_item_refund = "#content > div > div.quote-container > div.detail.inltd.quotation-collapse > div > div.ant-collapse-item.ant-collapse-item-active > div.ant-collapse-content.ant-collapse-content-active > div > div > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.ListIcon.list-icon > div.bottom.control-bar > div > button:nth-child(3)"
fieldbooking_invoice_item_refund_fare = "/html/body/div/div/div/div[2]/div/div[2]/div/div/div/div/div/table/tbody/tr/td[6]/div/div[2]/input"
fieldbooking_invoice_item_refund_way = "#content > div > div.reset_tabs_card.tabs.ant-tabs.ant-tabs-top.ant-tabs-card.ant-tabs-no-animation > div.ant-tabs-content.ant-tabs-content-no-animated.ant-tabs-top-content.ant-tabs-card-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.order-box > div > div:nth-child(1) > div.pay-input > div > div > div"
fieldbooking_invoice_item_refund_waydefault = "div#dbfd488e-fa78-4853-c64f-f2222db1d9c8 > ul > li"
fieldbooking_invoice_item_refund_bankchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[1]/div[2]/span/div[1]/div[2]/input"
fieldbooking_invoice_item_refund_creditchage = "/html/body/div/div/div/div[2]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[2]/div[2]/span/div[1]/div[2]/input"
# fieldbooking_invoice_item_refund_comfirm = "#content > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary.ant-btn-lg"






#發票收款部分
textbooking_invoice_item_receipt_bankchage = "1"
textbooking_invoice_item_receipt_creditchage = "2"
#發票退款部分
textbooking_invoice_item_refund_fare = "1"
textbooking_invoice_item_refund_bankchage = "1"
textbooking_invoice_item_refund_creditchage = "2"
#最后提交
fieldfinalamount = ".total-amount:nth-child(2)"
#fieldfinalcheck = ".confirm-bar > .ant-btn ant-btn-primary ant-btn-lg"
# fieldfinalcheck = ".ant-btn:nth-child(2)"
fieldfinalcheck = "#content > div > div.bottom-bar > div > button"
# fieldfinalcheck = "//button[@type='button']"



#打印本回詢價單
# fieldbooking_printout_booking = "#content > div > div > div.btn-bar > button"
fieldbooking_printout_booking = "#content > div > div > div.btn-bar > button.PublicButton.ant-btn.ant-btn-primary"


#公共頁頭部分

defaultcustomer = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"  # 选择第一个客户
fieldphone = "#infoForm_Mobile" #电话
fielddiscount = ".ant-input-number-input-wrap > #infoForm_Discount" #折扣
fieldpaymentmethod = "#infoForm_PaymentType > div > div"
fieldpaymentmethoddefault = "//li[contains(.,\'Bank in')]"



#公共抬頭備註部分
fildrisephone = "#infoForm_Phone"
fildrisemobile = "#infoForm_Mobile"
fildrisefax = "#infoForm_Fax"
fildriseEmail = "#infoForm_Email"
fildriseprovince = "#infoForm_AddressProvince"
fildrisecity = "#infoForm_AddressCity"
fildriseaddress = "#infoForm_Address"
fildriseremark = "//div[@id=\'content\']/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div/div/div[2]/div/span/div/div/div/textarea"
fildriseremark1 = "//div[@id=\'content\']/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div[2]/div/div[2]/div/span/div/div/div/textarea"
fildriseremark2 = "//div[@id=\'content\']/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div[3]/div/div[2]/div/span/div/div/div/textarea"
fildriseremark3 = "//div[@id=\'content\']/div/div[2]/div/div[3]/div/div[2]/form/div[2]/div/div[4]/div/div[2]/div/span/div/div/div/textarea"

# api机票
fieldtrip = "#from\\[0\\] .ant-select-selection__placeholder"  # 点击去程
searchtrip = "#from\\[0\\] .ant-select-search__field"
defaulttrip = "//li[contains(.,\'台北所有機場\')]"
fieldreturn = "#to\\[0\\] .ant-select-selection__placeholder"  # 点击回程
searchreturn = "#to\\[0\\] .ant-select-search__field"
defaultreturn = "//li[contains(.,\'東京所有機場\')]"
fieldcalendar = "#fromCityDate\\[0\\] .ant-calendar-picker-input"  # 点击日历选项
fieldcalendarmonth = ".ant-calendar-next-month-btn"  # 点击下一个月
fieldcalendarday = "tr:nth-child(5) > .ant-calendar-cell:nth-child(3) > .ant-calendar-date"
#fieldroute_search = ".ant-form-item-children > .ant-btn"
fieldroute_search = ".ant-form-item-children > .ant-btn:nth-child(1)"
defaultroute1 = ".item-v1:nth-child(1) .ant-btn"  # 选择自动搜索机票的第一个行程
defaultroute2 = ".item-v1:nth-child(2) .ant-btn"  # 选择自动搜索机票的第二个行程
# 手输机票
fieldhandticket = ".tickets > .ant-tabs > .ant-tabs-bar .ant-tabs-tab:nth-child(2)"
fieldhandapiticket = "#content > div > div.manual-control-add-route > div > div.body > div > div.ant-radio-group.ant-radio-group-outline.ant-radio-group-default > label:nth-child(2) > span.ant-radio > input"
fieldfetchpnr = ".ant-col:nth-child(2) > .ant-btn:nth-child(1)"
fieldcontentpnr = ".body-content-1 > .ant-input"
fieldnextpnr1 = ".ture-page-button > .ant-btn:nth-child(2)"
fieldtickettype1 = "div.airline-ticket-item:nth-child(3) > div:nth-child(2) > div:nth-child(1) > label:nth-child(1) > span:nth-child(1) > input:nth-child(1)"

fieldnextpnr2 = ".action-button > button:nth-child(2)"
fieldnextapipnr2 = "#content > div > div.manual-control-add-route > div > div.footer.has-next-step > div.action-button > button:nth-child(3)"
# fieldtickettype1 = "#content > div > div.tickets > div > div.ant-tabs-content.ant-tabs-content-animated.ant-tabs-top-content > div.ant-tabs-tabpane.ant-tabs-tabpane-active > div.custom-flight.other-fee > div > div.custom-flight-table-contain.form > div:nth-child(3) > div:nth-child(1) > div.ant-checkbox-group > label:nth-child(1) > span.ant-checkbox > input"  # x选择第一个机票类型


fieldbasicfare_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div/div[2]/div[2]/input"
fieldbasicfare_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[6]/div[2]/div[2]/input"
fieldtickettax_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[4]/div[2]/div[2]/input"
fieldtickettax_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[2]/div[2]/div/div[2]/div[4]/div/div[9]/div[2]/div[2]/input"
fieldhandticketsubmit = ".custom-flight-btn > .ant-btn"

# 酒店项目
# fieldhotel = "css=.ant-tabs-tab:nth-child(3)"
# fieldhotel = "//div[contains(.,\'酒店\')]"
fieldhotel = ".tickets > .ant-tabs > .ant-tabs-bar .ant-tabs-tab:nth-child(3)"
fieldhotelcontent = ".ant-select-selection--multiple > .ant-select-selection__rendered"
fieldhotel_search = ".ant-select-search:nth-child(1) .ant-select-search__field"
fieldhotelcity = "City"
fieldhotelcountry = "Country"
fieldhotelcalendar = "#CheckInDate .ant-calendar-picker-input"  # 酒店日历
fieldhotelroomtype = "//div[@id=\'RoomType\']/div/div"
fieldhotelpropertytype = "TotherType"
fieldhotelroomplan = "RoomPlan"
fieldhotelspecial = "Special"
fieldhoteltype1 = "#IfPostpone"

fieldhotelroomtypedefault = ".ant-select-dropdown-menu-item-active"
fieldhotelfare_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[2]/div/div[2]/input"
fieldhotelfare_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[3]/div/div[2]/input"
fieldhotelfare_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[5]/input[2]"
fieldhotelfare_remark = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[3]/div[2]/div/div[3]/div/div[2]/div/div[2]/div/div/div[6]/textarea"
fieldhoteladd = ".add-hotel > .custom-fee-bar > .ant-btn"

# 其他费用
fieldothercharge = ".ant-tabs-tab:nth-child(4)"
fieldotherchargecontent = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[1]/div/div"  # 通用其他费用栏位
# fieldotherchargecontent1 = ".select-has-search-icon .ant-select-selection__placeholder"  #第一次点击其他费用栏位
fieldotherchargeitem1 = "//li[contains(.,\'機票服務:機票服務\')]"
# fieldotherchargeitem1 = "/html/body/div[2]/div/div/div/ul/li[1]"
fieldotherchargeitem2 = "//li[contains(.,\'機票升級:機票升級\')]"
# fieldotherchargeitem2 = "/html/body/div[2]/div/div/div/ul/li[2]"

fieldothercharge_invoice = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[2]/div[2]/input"
fieldothercharge_xo = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/div[3]/div[2]/input"
fieldothercharge_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/input"
fieldothercharge_remark = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[4]/div[2]/div[3]/textarea[2]"

fieldotherchargeadd = ".other-fee > .custom-fee-bar > .ant-btn"


# 一日游
fielddaytour = ".ant-tabs-tab:nth-child(5)"
fielddaytourcontent = ".ant-row-flex .ant-row .PopoverSearchTable > .ant-input"
fielddaytouritem1 = ".ant-table-row:nth-child(1) > .ant-table-column-has-actions:nth-child(2)"
fielddaytourcalendar = "#StartDate .ant-calendar-picker-input"
#StartDate .ant-calendar-picker-input
fielddaytour_invoice = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[5]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[2]/div/div[2]/input"
fielddaytour_xo = "/html/body/div[1]/div/div/div[2]/div/div[3]/div/div[3]/div[5]/div[2]/div/div[1]/div/div[2]/div[1]/div/div[3]/div/div[2]/input"
fielddaytour_unit = "//div[@id=\'content\']/div/div[3]/div/div[3]/div[5]/div[2]/div/div/div/div[2]/div/div/div[5]/input[2]"
fielddaytour_remark = "//textarea[@id=\'Remarks\']"
fielddaytour_itemremark = "//div[@id='content']/div/div[3]/div/div[3]/div[5]/div[2]/div/div/div/div[2]/div/div/div[6]/textarea"

fielddaytouradd = ".AddDaytour .ant-btn"
fielddaytouritem2 = ".ant-table-row:nth-child(2) > .ant-table-column-has-actions:nth-child(2)"

#发票下一页
shoppingcart = ".icon-container use"
nextpage = ".create-button"

#發票下一頁添加其他項目
fildnextpageadditem = "/html/body/div[1]/div/div/div[2]/div/div[1]/button"

#团
fieldgroup = "//span[contains(.,'套票')]"
fieldgroupadd = ".add-icon > svg"
fieldgroupcontent1 = ".ant-select-selection--multiple > .ant-select-selection__rendered"
fieldgroupdefault1 = ".ant-select-dropdown-menu-item-active"
fieldgroupitem2 = ".ant-select-dropdown-menu-item:nth-child(2)"
#fieldgroupitem2 = ".ant-select-dropdown ant-select-dropdown--multiple ant-select-dropdown-placement-bottomLeft > ul > li:nth-child(2)"
#fieldgroupitem2 = ".ant-select-dropdown-menu-item-active"
fieldgroupitem3 = ".ant-select-dropdown-menu-item:nth-child(3)"
fieldgroupitem4 = ".ant-select-dropdown-menu-item:nth-child(4)"
fieldgroupitem5 = ".ant-select-dropdown-menu-item:nth-child(5)"
fieldgroupitem6 = ".ant-select-dropdown-menu-item:nth-child(6)"
fieldgroupitem7 = ".ant-select-dropdown-menu-item:nth-child(7)"
fieldgroupitem8 = ".ant-select-dropdown-menu-item:nth-child(8)"
fieldgroupitem9 = ".ant-select-dropdown-menu-item:nth-child(9)"
fieldgroupname1 = ".line-2 > .item-box:nth-child(1) > .ant-input"
fieldgroupcontacts1 = ".line-2 > .item-box:nth-child(2) > .ant-input"
fieldgroupautofare1 = ".line-4 > .ant-btn-primary"
fieldgroupdescription = "//div[@id='content']/div/div[3]/div[3]/div[5]/div[2]/div/div/div[3]/div/textarea"
fieldgroupremark = "//div[@id='content']/div/div[3]/div[3]/div[5]/div[2]/div/div/div[3]/div[2]/textarea"


fieldgroupcontent2 ="//div[5]/div[2]/div/div[2]/div/div[3]/div/div"
fieldgroupname2 = ".item:nth-child(2) > .line-2 > .item-box:nth-child(1) > .ant-input"
fieldgroupcontacts2 = "item:nth-child(2) > .line-2 > .item-box:nth-child(2) > .ant-input"
fieldgroupautofare2 = ".item:nth-child(2) .ant-btn-primary"

#乘客
# fieldpassenger = ".ant-tabs-tab:nth-child(6) > .tab-badge"
fieldpassenger = "#passenger"
fieldpassengerfirstname = "#passagerForm_firstname"
fieldpassengersecondname = "#passagerForm_secondname"
fieldpassengeradd = ".line > .ant-btn"
fieldpassengerdefault = "/html/body/div[1]/div/div/div[2]/div/div[3]/div[3]/div[6]/div[2]/div/form/div/div[6]/table/tbody/tr/td[1]/span/label/span/input"










# 文本
