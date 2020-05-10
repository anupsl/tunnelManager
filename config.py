
'''
Legend for port numbers:
    All the port numbers are 4 digits xxxx.
    First two digits represent application / DB type
        89 - Main DB
        88 - Warehouse DB
        87 - Billdump DB
        85 - Campaign DB
        84 - Meta DB
        83 - CommSys DB
        82 - Timeline DB
        65 - Conuest CubeManager DB
        899 - NSE_LIVY_ENDPOINT_SERVICE

        988, 987 - CommSys Thrift
        919, 918 - Loyalty Thrift
        919, 918, 917 - EMF_THRIFT_SERVICE
        909 - REED_SERVICE
        912 - Recommender Thrift
        809 - Timeline Thrift
        923 - FACEBOOK_LISTENER_THRIFT_SERVICE 9234
        924 - FACEBOOK_GATEWAY_THRIFT_SERVICE 9232
        819 - VENENO_LISTENER_THRIFT_SERVICE 8092
        999 - CAMPAIGN_SHARD_THRIFT_SERVICE 9998
        933 - LUCI_THRIFT_SERVICE 9333
	    960 - DRACARYS_THRIFT_SERVICE 3000
        810 - DARK_KNIGHT_THRIFT_SERVICE

        60 - Import Service

        50 - Gateway Controller

        21 - Zookeeper
        20 - Export Fileservice

        2701* - INTOUCH_DB_MONGO_MASTER
        2702* - SHARINGAN_DB_MONGO
        2703* - EMF_DB_MONGO_MASTER

    Third digit represent shard number
    Fourth digit represent cluster:
        
        1 - Nightly
        2 - Staging
        3 - More / APAC2 
        4 - India / APAC
        5 - EU
        7 - China
'''


config={

    "8911" : {"ip" : "10.99.1.95" , "remotePort" : "3306" , "cluster" : "nightly" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8921" : {"ip" : "nightly-shard2.cluster-c43r9ukzzdvy.us-east-1.rds.amazonaws.com" , "remotePort" : "3306" , "cluster" : "nightly" , "comment" : "INTOUCH_DB_MYSQL_MASTER 2"},
    "8711" : {"ip" : "10.99.1.58" , "remotePort" : "3306" , "cluster" : "nightly" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8411" : {"ip" : "10.99.1.109" , "remotePort" : "3306" , "cluster" : "nightly" , "comment" : "INTOUCH_META_DB_MYSQL"},  
    "9881" : {"ip" : "internal-a3a770e58637c11eab0aa16725a7a5a4-405739740.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "nightly" , "comment" : "NSADMIN_THRIFT_SERVICE 1"},
    "9891" : {"ip" : "internal-a54a2c999637c11eab0aa16725a7a5a4-868219889.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "nightly" , "comment" : "COMMENGINE_THRIFT_SERVICE"},
    "9681" : {"ip" : "10.99.1.178" , "remotePort" : "80" , "cluster" : "nightly" , "comment" : "CommDeliveryServer"},
    "9191" : {"ip" : "internal-a50ab52e45f7911eab0aa16725a7a5a4-1125318020.us-east-1.elb.amazonaws.com" , "remotePort" : "9199" , "cluster" : "nightly" , "comment" : "EMF_THRIFT_SERVICE 1"},
    "9091" : {"ip" : "10.99.1.160" , "remotePort" : "9554" , "cluster" : "nightly" , "comment" : "REED_SERVICE"},
    "8091" : {"ip" : "10.99.1.160" , "remotePort" : "8099" , "cluster" : "nightly" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},    
    "9231" : {"ip" : "10.99.1.161" , "remotePort" : "9234" , "cluster" : "nightly" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9241" : {"ip" : "internal-a888d4838535111eab0aa16725a7a5a4-1745093351.us-east-1.elb.amazonaws.com" , "remotePort" : "9232" , "cluster" : "nightly" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8191" : {"ip" : "internal-ad2ff5872534011eab0aa16725a7a5a4-1120112670.us-east-1.elb.amazonaws.com" , "remotePort" : "8092" , "cluster" : "nightly" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},  
    "9331" : {"ip" : "internal-ac129548a31e711eab0aa16725a7a5a4-1931548090.us-east-1.elb.amazonaws.com" , "remotePort" : "9333" , "cluster" : "nightly" , "comment" : "LUCI_THRIFT_SERVICE"},
    "9601" : {"ip" : "internal-ae94e45f158a311eab0aa16725a7a5a4-1828900016.us-east-1.elb.amazonaws.com" , "remotePort" : "3000" , "cluster" : "nightly" , "comment" : "DRACARYS_THRIFT_SERVICE"}, 
    "8101" : {"ip" : "internal-a5e173c034e5c11eab0aa16725a7a5a4-931134293.us-east-1.elb.amazonaws.com" , "remotePort" : "8100" , "cluster" : "nightly" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},
    "9801" : {"ip" : "internal-ac1507e66588e11eab0aa16725a7a5a4-70314921.us-east-1.elb.amazonaws.com" , "remotePort" : "9800" , "cluster" : "nightly" , "comment" : "PEB_THRIFT_SERVICE"},
    "9991" : {"ip" : "internal-ab87f2e60675811eab0aa16725a7a5a4-754301310.us-east-1.elb.amazonaws.com" , "remotePort" : "9998" , "cluster" : "nightly" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "6081" : {"ip" : "10.99.0.249" , "remotePort" : "80" , "cluster" : "nightly" , "comment" : "ImportService"},
    "2181" : {"ip" : "10.99.0.249" , "remotePort" : "2181" , "cluster" : "nightly" , "comment" : "Zookeeper"},
    "2001" : {"ip" : "10.99.0.128" , "remotePort" : "8001" , "cluster" : "nightly" , "comment" : "ExportFileservice"},
    "27011" : {"ip" : "10.99.1.233" , "remotePort" : "27017" , "cluster" : "nightly" , "comment" : "INTOUCH_DB_MONGO_MASTER"},
    "27051" : {"ip" : "10.99.1.201" , "remotePort" : "27017" , "cluster" : "nightly" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "8991" : {"ip" : "10.99.100.67" , "remotePort" : "8998" , "cluster" : "nightly" , "comment" : "NSE_LIVY_ENDPOINT_SERVICE"},
    "9981" : {"ip" : "10.99.0.66" , "remotePort" : "9630" , "cluster" : "nightly" , "comment" : "SUBSCRIPTION_THRIFT_SERVICE"},
    "8891" : {"ip" : "internal-a1b0edc7dca6911e9a307167cf1e1fdc-1692941177.us-east-1.elb.amazonaws.com" , "remotePort" : "8045" , "cluster" : "nightly" , "comment" : "REON_METADATA_API_THRIFT_SERVICE"},

    "8912" : {"ip" : "10.85.1.154" , "remotePort" : "3306" , "cluster" : "staging" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8922" : {"ip" : "10.85.1.244" , "remotePort" : "3306" , "cluster" : "staging" , "comment" : "INTOUCH_DB_MYSQL_MASTER 2"},
    "8712" : {"ip" : "10.85.1.181" , "remotePort" : "3306" , "cluster" : "staging" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8412" : {"ip" : "10.85.1.77" , "remotePort" : "3306" , "cluster" : "staging" , "comment" : "INTOUCH_META_DB_MYSQL"},
    "9882" : {"ip" : "internal-a4c464ce4679311eab48e164296b057c-608085073.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "staging" , "comment" : "NSADMIN_THRIFT_SERVICE 1"},
    "9892" : {"ip" : "internal-a624c2202679311eab48e164296b057c-2112598645.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "staging" , "comment" : "COMMENGINE_THRIFT_SERVICE"},
    "9682" : {"ip" : "10.85.1.12" , "remotePort" : "80" , "cluster" : "staging" , "comment" : "CommDeliveryServer"},
    "9192" : {"ip" : "internal-a4efeba9a693711eab48e164296b057c-2055514582.us-east-1.elb.amazonaws.com" , "remotePort" : "9199" , "cluster" : "staging" , "comment" : "EMF_THRIFT_SERVICE"},
    "9092" : {"ip" : "10.85.1.15" , "remotePort" : "9554" , "cluster" : "staging" , "comment" : "REED_SERVICE"},    
    "8092" : {"ip" : "10.85.1.12" , "remotePort" : "8099" , "cluster" : "staging" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},
    "9232" : {"ip" : "10.85.1.12" , "remotePort" : "9234" , "cluster" : "staging" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9242" : {"ip" : "internal-a1f5d347a5e2c11eab48e164296b057c-1611577973.us-east-1.elb.amazonaws.com" , "remotePort" : "9232" , "cluster" : "staging" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8192" : {"ip" : "internal-a298b26ae5f0211eab48e164296b057c-278185546.us-east-1.elb.amazonaws.com" , "remotePort" : "8092" , "cluster" : "staging" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},    
    "9332" : {"ip" : "internal-a65fef8c23b6e11ea889616bedbec371-716243941.us-east-1.elb.amazonaws.com" , "remotePort" : "9333" , "cluster" : "staging" , "comment" : "LUCI_THRIFT_SERVICE"},
    "9602" : {"ip" : "internal-ab0cec1ff682c11eab48e164296b057c-1457962851.us-east-1.elb.amazonaws.com" , "remotePort" : "3000" , "cluster" : "staging" , "comment" : "DRACARYS_THRIFT_SERVICE"},
    "8102" : {"ip" : "internal-ab82d23805c6711eab48e164296b057c-3199185.us-east-1.elb.amazonaws.com" , "remotePort" : "8100" , "cluster" : "staging" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},
    "9992" : {"ip" : "internal-a6cbc76a968f511eab48e164296b057c-185901834.us-east-1.elb.amazonaws.com" , "remotePort" : "9998" , "cluster" : "staging" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "9802" : {"ip" : "internal-ac84a8d2d678b11eab48e164296b057c-419535914.us-east-1.elb.amazonaws.com" , "remotePort" : "9800" , "cluster" : "staging" , "comment" : "PEB_THRIFT_SERVICE"},
    "6082" : {"ip" : "10.85.1.11" , "remotePort" : "80" , "cluster" : "staging" , "comment" : "ImportService"},
    "2182" : {"ip" : "10.85.0.10" , "remotePort" : "2181" , "cluster" : "staging" , "comment" : "Zookeeper"},
    "2002" : {"ip" : "10.85.1.14" , "remotePort" : "8001" , "cluster" : "staging" , "comment" : "ExportFileservice"},
    "27012" : {"ip" : "10.85.1.240" , "remotePort" : "27017" , "cluster" : "staging" , "comment" : "INTOUCH_DB_MONGO_MASTER"},
    "27052" : {"ip" : "10.85.1.240" , "remotePort" : "27017" , "cluster" : "staging" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "27022" : {"ip" : "10.85.1.125" , "remotePort" : "27017" , "cluster" : "staging" , "comment" : "SHARINGAN_DB_MONGO"},
    "8892" : {"ip" : "10.85.10.217" , "remotePort" : "8045" , "cluster" : "staging" , "comment" : "REON_METADATA_API_THRIFT_SERVICE"},
    
    "8913" : {"ip" : "10.8.11.53" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8923" : {"ip" : "10.8.7.244" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 2"},
    "8933" : {"ip" : "10.8.11.140" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 3"},
    "8943" : {"ip" : "10.8.4.164" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 4"},
    "8953" : {"ip" : "10.8.5.137" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 5"},
    "8963" : {"ip" : "10.8.2.116" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 6"},
    "8973" : {"ip" : "10.8.8.241" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_MASTER 7"},
    "8713" : {"ip" : "10.8.1.160" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8513" : {"ip" : "10.8.5.79" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "CAMPAIGN_SHARD_DB_MYSQL"},
    "8413" : {"ip" : "10.8.3.132" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "INTOUCH_META_DB_MYSQL"},
    "8313" : {"ip" : "10.8.7.26" , "remotePort" : "3306" , "cluster" : "more" , "comment" : "NSADMIN_DB_MYSQL"},          
    "9883" : {"ip" : "internal-ac7098e1b693b11ea8dc506ebe775b0c-1718876928.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "more" , "comment" : "NSADMIN_THRIFT_SERVICE 1"},
    #"9873" : {"ip" : "10.8.6.96" , "remotePort" : "9888" , "cluster" : "more" , "comment" : "NSADMIN_THRIFT_SERVICE 2"},
    "9893" : {"ip" : "internal-a37105a34693c11ea8dc506ebe775b0c-585737468.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "more" , "comment" : "COMMENGINE_THRIFT_SERVICE"},
    "9193" : {"ip" : "internal-aba82fe3a6a0511ea8dc506ebe775b0c-64848748.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9199" , "cluster" : "more" , "comment" : "EMF_THRIFT_SERVICE 1"},
    "8093" : {"ip" : "10.8.7.9" , "remotePort" : "8099" , "cluster" : "more" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},    
    "9233" : {"ip" : "10.8.5.64" , "remotePort" : "9234" , "cluster" : "more" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9243" : {"ip" : "internal-a8f7c19525e4111ea8dc506ebe775b0c-1590549612.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9232" , "cluster" : "more" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8193" : {"ip" : "internal-ae890038c616211ea8dc506ebe775b0c-168320251.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "8092" , "cluster" : "more" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},
    "9333" : {"ip" : "internal-ac03b082258ba11ea8dc506ebe775b0c-1401336283.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9333" , "cluster" : "more" , "comment" : "LUCI_THRIFT_SERVICE"},  
    "9603" : {"ip" : "internal-a79bb4bfe6a0411ea8dc506ebe775b0c-480076022.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "3000" , "cluster" : "more" , "comment" : "DRACARYS_THRIFT_SERVICE"},
    "9613" : {"ip" : "10.8.15.180" , "remotePort" : "8090" , "cluster" : "more" , "comment" : "CRON_THRIFT_SERVICE"},
    "8103" : {"ip" : "internal-a956eb9115d8411ea8dc506ebe775b0c-969735976.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "8100" , "cluster" : "more" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},
    "9993" : {"ip" : "internal-a5093d1be6a0511ea8dc506ebe775b0c-37797650.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9998" , "cluster" : "more" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "9803" : {"ip" : "internal-ab8ff98d9687011ea8dc506ebe775b0c-1112248706.ap-southeast-1.elb.amazonaws.com" , "remotePort" : "9800" , "cluster" : "more" , "comment" : "PEB_THRIFT_SERVICE"},
    "6083" : {"ip" : "10.8.87.91" , "remotePort" : "80" , "cluster" : "more" , "comment" : "ImportService"},
    "2003" : {"ip" : "10.8.2.10" , "remotePort" : "8001" , "cluster" : "more" , "comment" : "ExportFileService"},
    "27013" : {"ip" : "10.8.7.96" , "remotePort" : "27017" , "cluster" : "more" , "comment" : "INTOUCH_DB_MONGO_MASTER"},  
    "27053" : {"ip" : "10.8.7.20" , "remotePort" : "27017" , "cluster" : "more" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "27023" : {"ip" : "10.8.10.201" , "remotePort" : "27017" , "cluster" : "more" , "comment" : "SHARINGAN_DB_MONGO"},    
    "27033" : {"ip" : "10.8.9.217" , "remotePort" : "27017" , "cluster" : "more" , "comment" : "EMF_DB_MONGO_MASTER"},
    "8893" : {"ip" : "10.8.180.151" , "remotePort" : "8045" , "cluster" : "more" , "comment" : "REON_METADATA_API_THRIFT_SERVICE"},

    "8914" : {"ip" : "172.16.9.145" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8924" : {"ip" : "172.16.5.126" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "INTOUCH_DB_MYSQL_MASTER 2"},
    "8714" : {"ip" : "172.16.9.5" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8514" : {"ip" : "172.16.9.197" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "CAMPAIGN_SHARD_DB_MYSQL"},
    "8414" : {"ip" : "172.16.9.249" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "INTOUCH_META_DB_MYSQL"},
    "8314" : {"ip" : "172.16.9.206" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "NSADMIN_DB_MYSQL"},
    "8214" : {"ip" : "172.16.9.186" , "remotePort" : "3306" , "cluster" : "india" , "comment" : "TIMELINE_DB_MYSQL"},   
    "9194" : {"ip" : "internal-ae582bf7d6a0611eaaf9e0a52dbe7ce2-1992079977.us-east-1.elb.amazonaws.com" , "remotePort" : "9199" , "cluster" : "india" , "comment" : "EMF_THRIFT_SERVICE 1"},
    "9884" : {"ip" : "internal-a3513dc4d694011eaaf9e0a52dbe7ce2-1434723337.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "india" , "comment" : "NSADMIN_THRIFT_SERVICE 1"},
    #"9874" : {"ip" : "172.16.8.80" , "remotePort" : "9888" , "cluster" : "india" , "comment" : "NSADMIN_THRIFT_SERVICE 2"},
    "9894" : {"ip" : "internal-a9501c91b694011eaaf9e0a52dbe7ce2-1742065646.us-east-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "india" , "comment" : "COMMENGINE_THRIFT_SERVICE"},  
    "8094" : {"ip" : "172.16.5.96" , "remotePort" : "8099" , "cluster" : "india" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},    
    "9234" : {"ip" : "172.16.4.52" , "remotePort" : "9234" , "cluster" : "india" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9244" : {"ip" : "internal-aecf2e18d5e3811eaaf9e0a52dbe7ce2-335863619.us-east-1.elb.amazonaws.com" , "remotePort" : "9232" , "cluster" : "india" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8194" : {"ip" : "internal-a793571365f2911eaaf9e0a52dbe7ce2-1345943981.us-east-1.elb.amazonaws.com" , "remotePort" : "8092" , "cluster" : "india" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},
    "9334" : {"ip" : "internal-a93ce079257fa11eaaf9e0a52dbe7ce2-1136494459.us-east-1.elb.amazonaws.com" , "remotePort" : "9333" , "cluster" : "india" , "comment" : "LUCI_THRIFT_SERVICE"},
    "9604" : {"ip" : "internal-af696fbc96a0711eaaf9e0a52dbe7ce2-780867165.us-east-1.elb.amazonaws.com" , "remotePort" : "3000" , "cluster" : "india" , "comment" : "DRACARYS_THRIFT_SERVICE"},
    "8104" : {"ip" : "internal-a8c8b543b5e3711eaaf9e0a52dbe7ce2-651884694.us-east-1.elb.amazonaws.com" , "remotePort" : "8100" , "cluster" : "india" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},
    "9994" : {"ip" : "internal-ac291b0416a0411eaaf9e0a52dbe7ce2-370640.us-east-1.elb.amazonaws.com" , "remotePort" : "9998" , "cluster" : "india" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "9804" : {"ip" : "internal-addb70b4b687111eaaf9e0a52dbe7ce2-1647085515.us-east-1.elb.amazonaws.com" , "remotePort" : "9800" , "cluster" : "india" , "comment" : "PEB_THRIFT_SERVICE"},
    "6084" : {"ip" : "intouch.capillary.co.in" , "remotePort" : "80" , "cluster" : "india" , "comment" : "ImportService"},
    "2004" : {"ip" : "172.16.5.109" , "remotePort" : "8001" , "cluster" : "india" , "comment" : "ExportFileService"},
    "27014" : {"ip" : "172.16.9.220" , "remotePort" : "27017" , "cluster" : "india" , "comment" : "INTOUCH_DB_MONGO_MASTER"}, 
    "27054" : {"ip" : "172.16.9.201" , "remotePort" : "27017" , "cluster" : "india" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "27024" : {"ip" : "172.16.9.220" , "remotePort" : "27017" , "cluster" : "india" , "comment" : "SHARINGAN_DB_MONGO"},
    "27034" : {"ip" : "172.16.9.69" , "remotePort" : "27017" , "cluster" : "india" , "comment" : "EMF_DB_MONGO_MASTER"},
    "8894" : {"ip" : "172.16.7.107" , "remotePort" : "8045" , "cluster" : "india" , "comment" : "REON_METADATA_API_THRIFT_SERVICE"},

    "8915" : {"ip" : "10.4.22.176" , "remotePort" : "3306" , "cluster" : "eu" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8925": {"ip": "eushard2dbmaster.capillary.internal", "remotePort": "3306", "cluster": "eu",
             "comment": "INTOUCH_DB_MYSQL_MASTER 2"},
    "8715" : {"ip" : "10.4.29.117" , "remotePort" : "3306" , "cluster" : "eu" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8515" : {"ip" : "10.4.26.22" , "remotePort" : "3306" , "cluster" : "eu" , "comment" : "CAMPAIGN_SHARD_DB_MYSQL"},
    "8415" : {"ip" : "10.4.25.26" , "remotePort" : "3306" , "cluster" : "eu" , "comment" : "INTOUCH_META_DB_MYSQL"},
    "8315" : {"ip" : "10.4.27.28" , "remotePort" : "3306" , "cluster" : "eu" , "comment" : "NSADMIN_DB_MYSQL"},
    "9885" : {"ip" : "internal-a01ac6b2268cb11eabba30276efc5b65-9532669.eu-west-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "eu" , "comment" : "NSADMIN_THRIFT_SERVICE"},
    "9895" : {"ip" : "internal-a891c670c68cb11eabba30276efc5b65-467320882.eu-west-1.elb.amazonaws.com" , "remotePort" : "9888" , "cluster" : "eu" , "comment" : "COMMENGINE_THRIFT_SERVICE"},
    "9195" : {"ip" : "internal-a6be07655699211eabba30276efc5b65-295202503.eu-west-1.elb.amazonaws.com" , "remotePort" : "9199" , "cluster" : "eu" , "comment" : "EMF_THRIFT_SERVICE 2"},    
    "8095" : {"ip" : "10.4.25.88" , "remotePort" : "8099" , "cluster" : "eu" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},    
    "9235" : {"ip" : "10.4.24.115" , "remotePort" : "9234" , "cluster" : "eu" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9245" : {"ip" : "internal-a0c94ae295e8911eabba30276efc5b65-225559572.eu-west-1.elb.amazonaws.com" , "remotePort" : "9232" , "cluster" : "eu" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8195" : {"ip" : "internal-a79b4e74161b111eabba30276efc5b65-1626753420.eu-west-1.elb.amazonaws.com" , "remotePort" : "8092" , "cluster" : "eu" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},
    "9335" : {"ip" : "internal-a0d93faea4e0711eabba30276efc5b65-1716183587.eu-west-1.elb.amazonaws.com" , "remotePort" : "9333" , "cluster" : "eu" , "comment" : "LUCI_THRIFT_SERVICE"},  
    "9605" : {"ip" : "internal-a23b328c8698f11eabba30276efc5b65-1976836564.eu-west-1.elb.amazonaws.com" , "remotePort" : "3000" , "cluster" : "eu" , "comment" : "DRACARYS_THRIFT_SERVICE"},
    "8105" : {"ip" : "internal-a2c1e3bda5e8711eabba30276efc5b65-538092890.eu-west-1.elb.amazonaws.com" , "remotePort" : "8100" , "cluster" : "eu" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},
    "9995" : {"ip" : "internal-a816433ff6a5811eabba30276efc5b65-263344480.eu-west-1.elb.amazonaws.com" , "remotePort" : "9998" , "cluster" : "eu" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "9805" : {"ip" : "internal-a1b3e2abc67fa11eabba30276efc5b65-573234227.eu-west-1.elb.amazonaws.com" , "remotePort" : "9800" , "cluster" : "eu" , "comment" : "PEB_THRIFT_SERVICE"},    
    "6085" : {"ip" : "eu.intouch.capillarytech.com" , "remotePort" : "80" , "cluster" : "eu" , "comment" : "ImportService"},
    "2005" : {"ip" : "10.4.34.10" , "remotePort" : "8001" , "cluster" : "eu" , "comment" : "ExportFileService"},
    "27015" : {"ip" : "10.4.19.104", "remotePort" : "27017" , "cluster" : "eu" , "comment" : "INTOUCH_DB_MONGO_MASTER"},
    "27055" : {"ip" : "10.4.28.8" , "remotePort" : "27017" , "cluster" : "eu" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "27025" : {"ip" : "10.4.11.48", "remotePort" : "27017" , "cluster" : "eu" , "comment" : "SHARINGAN_DB_MONGO"},
    "27035" : {"ip" : "10.4.16.26" , "remotePort" : "27017" , "cluster" : "eu" , "comment" : "EMF_DB_MONGO_MASTER"},
    "8895" : {"ip" : "10.4.180.105" , "remotePort" : "8045" , "cluster" : "eu" , "comment" : "REON_METADATA_API_THRIFT_SERVICE"},

    "8917" : {"ip" : "10.10.17.223" , "remotePort" : "3306" , "cluster" : "china" , "comment" : "INTOUCH_DB_MYSQL_MASTER 1"},
    "8717" : {"ip" : "10.10.25.132" , "remotePort" : "3306" , "cluster" : "china" , "comment" : "INTOUCH_DB_MYSQL_BILLDUMP"},
    "8417" : {"ip" : "10.10.25.254" , "remotePort" : "3306" , "cluster" : "china" , "comment" : "INTOUCH_META_DB_MYSQL"},
    "8317" : {"ip" : "10.10.22.211" , "remotePort" : "3306" , "cluster" : "china" , "comment" : "NSADMIN_DB_MYSQL"},  
    "9887" : {"ip" : "internal-a85a1422b67a611ea8e7502c70127532-1533537213.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9888" , "cluster" : "china" , "comment" : "NSADMIN_THRIFT_SERVICE"},
    "9897" : {"ip" : "internal-a030d19da67a711ea8e7502c70127532-2145571619.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9888" , "cluster" : "china" , "comment" : "COMMENGINE_THRIFT_SERVICE"},
    "9197" : {"ip" : "internal-ad34e7e12694811ea8e7502c70127532-1951824870.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9199" , "cluster" : "china" , "comment" : "EMF_THRIFT_SERVICE"},
    "8107" : {"ip" : "10.10.20.15" , "remotePort" : "8100" , "cluster" : "china" , "comment" : "DARK_KNIGHT_THRIFT_SERVICE"},    
    "8097" : {"ip" : "10.10.20.15" , "remotePort" : "8099" , "cluster" : "china" , "comment" : "TEMPORAL_ENGINE_THRIFT_SERVICE"},    
    "9237" : {"ip" : "10.10.20.15" , "remotePort" : "9234" , "cluster" : "china" , "comment" : "FACEBOOK_LISTENER_THRIFT_SERVICE"},
    "9247" : {"ip" : "10.10.20.15" , "remotePort" : "9232" , "cluster" : "china" , "comment" : "FACEBOOK_GATEWAY_THRIFT_SERVICE"},
    "8197" : {"ip" : "internal-ab716f53b615c11ea8e7502c70127532-1615619502.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "8092" , "cluster" : "china" , "comment" : "VENENO_LISTENER_THRIFT_SERVICE"},
    "9337" : {"ip" : "internal-ad9ab248e4ceb11ea8e7502c70127532-678881878.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9333" , "cluster" : "china" , "comment" : "LUCI_THRIFT_SERVICE"},  
    "9607" : {"ip" : "internal-a84e2c0fb693d11ea8e7502c70127532-1143950483.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "3000" , "cluster" : "china" , "comment" : "DRACARYS_THRIFT_SERVICE"},
    "9807" : {"ip" : "internal-a61c32de2679d11ea8e7502c70127532-6006852.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9800" , "cluster" : "china" , "comment" : "PEB_THRIFT_SERVICE"},
    "9997" : {"ip" : "internal-ab379be7c69f711ea8e7502c70127532-1702108096.cn-north-1.elb.amazonaws.com.cn" , "remotePort" : "9998" , "cluster" : "china" , "comment" : "CAMPAIGN_SHARD_THRIFT_SERVICE"},
    "6087" : {"ip" : "intouch.capillarytech.cn.com" , "remotePort" : "80" , "cluster" : "china" , "comment" : "ImportService"},
    "2007" : {"ip" : "10.10.45.69" , "remotePort" : "8001" , "cluster" : "china" , "comment" : "ExportFileService"},
    "27017" : {"ip" : "10.10.23.4" , "remotePort" : "27017" , "cluster" : "china" , "comment" : "INTOUCH_DB_MONGO_MASTER"},
    "27057" : {"ip" : "10.10.28.130" , "remotePort" : "27017" , "cluster" : "china" , "comment" : "CAMPAIGNS_DB_MONGO_MASTER"}, 
    "27027" : {"ip" : "10.10.40.104" , "remotePort" : "27017" , "cluster" : "china" , "comment" : "SHARINGAN_DB_MONGO"},
    "27037" : {"ip" : "10.10.20.153" , "remotePort" : "27017" , "cluster" : "china" , "comment" : "EMF_DB_MONGO_MASTER"},
}




















