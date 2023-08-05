import os

paymentTypesRUB = {
    'Юmoney'          : 'YandexMoneyNew', 
    'Тинькофф'        : 'TinkoffNew', 
    'Росбанк'         : 'RosBankNew', 
    'Райффайзен'      : 'RaiffeisenBank', 
    'QIWI'            : 'QIWI', 
    'МТС банк'        : 'MTSBank', 
    'Home Credit'     : 'HomeCreditBank', 
    'BinancePay (RUB)': 'RUBfiatbalance', 
    'Почта банк'      : 'PostBankNew', 
    'Payeer'          : 'Payeer', 
    'Уралсиб'         : 'UralsibBank', 
    'АК Барс'         : 'AkBarsBank', 
    'Мобильный'       : 'Mobiletopup', 
    'Advcash'         : 'Advcash', 
    'БКС'             : 'BCSBank', 
    'Реннесанс'       : 'RenaissanceCredit', 
    'Русский стандарт': 'RussianStandardBank', 
    'Банк Петербург'  : 'BankSaintPetersburg', 
    'ОТП'             : 'OTPBankRussia', 
    'Юникредит'       : 'UniCreditRussia', 
    'Европа кредит'   : 'CreditEuropeBank', 
    'Ситибанк'        : 'CitibankRussia', 
    'Альфа'           : 'ABank', 
    'Cash'            : 'CashInPerson'
}

paymentTypesKZT = {
	"Kaspi Bank"            : "KaspiBank",
	"HalykBank"             : "HalykBank",
	"CenterCredit Bank"     : "CenterCreditBank",
	"ForteBank"             : "ForteBank",
	"Jysan Bank"            : "JysanBank",
	"Altyn Bank"            : "AltynBank",
	"Eurasian Bank"         : "EurasianBank",
	"Home Credit Kazakhstan": "HomeCreditKazakhstan",
	"Freedom Bank"          : "FreedomBank",
	"Bank RBK"              : "BankRBK",
	"QIWI"                  : "QIWI",
	"RosBank"               : "RosBankNew",
	"Advcash"               : "Advcash",
	"Tinkoff"               : "TinkoffNew",
	"Elcart"                : "ELCART",
	"MICB"                  : "MICB",
	"BBVA"                  : "BBVABank",
	"Bank of Georgia"       : "BankofGeorgia",
	"KoronaPay"             : "KoronaPay",
	"MAIB"                  : "MAIB",
	"PUMB"                  : "PUMBBank"
}

paymentTypesIDR = {
    "BCA"          : "BCAMobile",
	"DANA"         : "DANA",
	"Mandiri"      : "MandiriPay",
	"Permata"      : "PermataMe",
	"OVO"          : "OVO",
	"GoPay"        : "GoPay",
	"Bank BRI"     : "BANKBRI",
	"SEA Bank"     : "SEAbank",
	"Yap! (BNI)"   : "YapBNI",
	"ShopeePay-SEA": "ShopeePay",
	"LinkAja"      : "LinkAja",
	"CIMB Niaga"   : "CIMBNiaga",
	"Bank Jago"    : "BankJago",
	"OCBC NISP"    : "OCBCNISP",
	"Jenius PayMe" : "JeniusPayMe",
	"Maybank"      : "Maybank",
	"NEO"          : "NEO",
	"Hana Bank"    : "HanaBank",
	"Blu"          : "Blu",
	"TMRW"         : "TMRW",
	"Danamon Bank" : "DanamonBank",
	"Sinarmas"     : "Sinarmas",
	"Wise"         : "Wise",
	"BCA Syariah"  : "BCASyariah",
	"CIMB"         : "CIMBPHP",
	"LINE Bank"    : "LINEBANK",
	"Ligo"         : "Ligo",
	"Moneygram"    : "MoneyGram",
	"NEO"          : "NEOPayIraq",
	"Nobu Bank"    : "NobuBank",
	"OSKO"         : "OKSO",
	"Western Union": "WesternUnion"
}

paymentTypesGEL = {
	"Bank of Georgia": "Bank of Georgia",
	"TBC Bank"       : "TBCbank",
	"Credo Bank"     : "CREDOBANK",
	"Liberty Bank"   : "LIBERTYBANK",
	"KoronaPay"      : "KoronaPay",
	"Tinkoff"        : "TinkoffNew",
	"Wise"           : "Wise",
	"RosBank"        : "RosBankNew",
	"Humo"           : "Humo",
	"SWIFT"          : "SWIFT",
	"Western Union"  : "WesternUnion",
	"Raiffeisenbank" : "RaiffeisenBank"
}

paymentTypesTRY = {
    "Ziraat": "Ziraat",
	"Garanti": "Garanti",
	"DenizBank": "DenizBank",
	"Kuveyt Turk": "KuveytTurk",
	"Papara": "Papara",
	"VakifBank": "VakifBank",
	"OLDUBIL": "Oldubil",
	"QNB": "QNB",
	"ISBANK": "ISBANK",
	"Akbank": "Akbank",
	"alBaraka": "alBaraka",
	"HalkBank": "HALKBANK",
	"Fibabanka": "Fibabanka",
	"Wise": "Wise",
	"Advcash": "Advcash",
	"Revolut": "Revolut",
	"AirTM": "AirTM",
	"ING": "ING",
	"Bakai Bank": "BAKAIBANK",
	"BCA": "BCAMobile",
	"Western Union": "WesternUnion",
	"Burgan Bank": "BurganBank",
	"CashU": "CashU",
	"Cashapp": "Cashapp",
	"Kaspi Bank": "KaspiBank",
	"Moneygram": "MoneyGram",
	"Paysend.com": "Paysend",
	"RosBank": "RosBankNew"
}

paymentTypes = {
    "RUB": paymentTypesRUB,
    "TRY": paymentTypesTRY,
    "KZT": paymentTypesKZT,
    "GEL": paymentTypesGEL,
    "IDR": paymentTypesIDR
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

from p2p_crypto import user_agent
USER_AGENT=user_agent.USER_AGENT