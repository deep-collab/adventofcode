import re

text = """
*who():mul(420,173)what()*~why() select()how()-mul(448,672)mul(914,202){^{why()];<&;/mul(748,792)what(),$from()what()when()mul(399,982)<;)]]mul(347,549)@;*);mul(655,663) @select()~%,$#mul(535,284)*--@()]+~mul(2,513)why()mul(239,99)!<mul(2,988)@mul(971,404)?&from()mul(660,516)-;what();how()+!why()mul(612,994)'[mul(253,728)<-mul(208,621)>?}( #]mul(162,534)#+how()}<&what();mul(685,182)mul(146,549)mul(659,511)mul(283,734)*/don't()/mul(579,121)what()mul(790,893)where()@)-{#!who()((mul(985,741)when(),$where()>do()<~''-~-mul(961,154),]select()(select()@what()mul(840,357)] when()mul(47,948))]?what()+*;+mul(331,33)who();&~~mul(983,456)mul(660,500)who()mul(414,834)where()^({>mul(961,732)#^]how() mul(869,618)mul(265,208)!when()*]mul(803,747)>*&+what()+,['mul(490,565)> >/*%mul(238,882)%+$;%&,/mul(629,355){{'/?-who():!mul(441,172):[?;mul(628,85)%%{how()]^>why()>mul(509,935)where()/]select()mul(727,783)?^@why()from()>&mul(75,582)<~!%from(){from() mul(616,901)''why()%-from()>>mul(568,812)%(*mul(833,395)$who()& ;how(112,924)why()?mul(734,354)mul(344,367):what()mul(884,545)when(753,136):{select()[mul(981,829)~!<who()>why()mul(444,22)mul(257,636)from()why();&mul(603,941)}-when()&mul(109,476)#)from()when()+;?,mul(149,108)mul(716,634)/~>:&#?mul(919,396)@why() (who()~!mul(949,950)~~:why()&mul(949,808)mul(678,162)&mul(862,475)?++:, mul(750,321)(# why()#{@/select(282,886)mul(953,52),~from()mul(408,319)?@*:#mul(308,330)select(895,376)&>#-when()do()!@*how(890,967)when()mul(607,743),^,when()}$*&mul(737,198))#[!?mul(979,606),-@+'mul(223,381)when(){+<when()%]{*mulwhere()how()<)*?&where()//mul(875,817)when()from()%how())@#]<who()mul(799,646)where()+((how():!+!why()mul(162,552)@?select()>;{mul(623,192)-}@when()@'who()select()how()#don't()!where()@@&}&mul(853,100)]{]~mul(501,746)-? *mul(599,24)mul(141,255)mul(922,727)*select()>how()$who(){+mul(544,731)/from()how()who();@select()mul(609,809)?$(/why()from())mul(498,52)]:when()mul(60,285)@'$)why() %<']do()!from()from()who()::mul(894,43)#@:$mul(731,263)why()select()who(){mul(516,369)how()who()do()$;&$/[;;[mul(655,571)]from()*what()mul(192,59)+]?select()mul(453,68)from()mul?+mul(281,2){why()]~{!,mul(823,635)^/)where()]who() @'$mul(660,562):%where()why()why()%~how()mul(437,42)mul(590,3)~-mul(428,918)>what()why()&?when(742,360)?mul(786,567)%from()when()-mul(367,375)*}why()mul(455,204)/]<,]+mul(819,196)from()@mul><when()+(where()^}&mul(605,973)&where()&^^<%why()[)mul(227,87)where()  }mul(762,536)$%~<:>mul(212,199)what()/where(462,172)~when()select()^mul(794,611)mul(484,833)( ?mul(877,152)]what()mul(758,157(][&+how(){>)mul(408,379);}{when()mul(731,259)#?how()mul(246,943)who()@what(830,854){-+>@~:don't()mul(703,111) #^what()<>^do()>,>^+!mul(57,220)#<${#why()when(457,676)>what()mul(199,247)mul(768,629)
)'how()<(/)'';mul(867,986))@mul(909,468)?>from()why():<*select(700,257)>don't()mul(294:why()/&^}select()[:{mul(96,677)from()#?-when()%&&'what()mul(806,612)who()@who()<$select()mul(491,724) mul(47,119)#)^who()'mul(526,381)mul(24,969)from()[;mul(189,60)$<>when(565,624)]+#what()<mul(175,572)#{when())+*(~<mul(993,825)where()from(467,409)from()#@+){mul(67,355)& from()!))where();}mul(808,139);<^who(842,199)*!+]{^mulfrom()mul(454,197)select()#how();?~$who()(!mul(854,101)>$[where()why()don't()[]):-who()',select(576,158)what()mul(79,672)--<>[-[mul(248,857)!<^when()]mul(881,761)^!):how()@mul(812,759)what()*>why()+~*-mul(993,256)${-when()mul-&/!what(781,304)why():mul(627,605) >(&%!where(){why(296,454)mul(990,864)!,&(select()'^mul(537,400)what()why()?-where()@:mul(752how(231,812)why()-how()where(956,169)mul(146,184)~}@%],$(who()@mul(716,486)+why()/what()+:{mul(42,180)$when()'][*how()>&mul(611,512)what(155,381):>;(mul(423,432)$,when()&where()mul(976,409)why()@ >why()~#-select()@mul(50,854)$@#mul(42,58)$when()!-#mul(326,406)~where(195,918)where()mul(3,647);['~];$how()why()what()mul(966,495)mul(324,653)mul(47,577)#+(*+^$)mul(144,392)/mul(135,506)what(729,718)don't()%'>mul(609,314)%:>*~mul(120,925)mul(765,209){select()$:#mul(741-$%!;mul(166,556)when(523,779)select())mul(820,823)%~:where())/{when()/mul+where()why()+{;mul(41,341)>~>+mul(960,552) do()who()mul(381,244)?(@+@mul(287,560)!mul(954,480)$where()mul(914,431)}!::what()(}!who()+mul(586,399)from()@why()?when()how()when()when()mul(802,73)mul(14,93)$what()why()%when()(mul(569,2): mul(793,2)mul(301,988){ mul(732,16)why()select()/^{mul(573,997)()*;;from()){mul(477,194) [mul(180,519)from()!where()@$mul(797,512/;select()?who()+how()mul(176,169)from()$<!mul(830,661)(+[mul(466,467)do(),{ ('<mul(145,237)[why()how(111,297)+from()&,mul(369,942)<<select()+;>when()&do()>*,when(277,359){mul(326,605)how()where()}<}:/mul(852,42)what()$)mul(12,636)mul(991,890)]^where()~'do()where()?when()-})@mul(283,368)!,@!$]$@ do()/#'why()-mul(972,409),mul(69how()!*+$where()')where(768,54)&mul(813,972)>select()]+] %#'?mul(701,332who()mul(471,905)+,mul(190,8)how()who()/mul(734,501)select()>how();from(){mul(533,838)who(386,331)how(356,935)[;}mul(373,528)%'*%mul(691,404)@'{^mul(885,376)why()-*mul(439,454)mul(743,477)((!what()][mul(606,298)[/who())how()[>mul(306,944)'when()'what()when()what();}@-mul(294,922)[why()don't()why())~![mul(516where(380,379)#who()mul(564,911)>?where()mul(53,783)#why(725,816)mul(646,866)+select()when()(mul(737,165)/mul(869,809)}mul(207,700)when(),&why()select()&@who()mul(773,864)when()$<(why()mul(320,655)^mul(131,141)when(),mul(634,514)select()&mul(483,605)+mul(934,936)where()]%:(who()]*from()mul(360,239)what(594,220)/%how()select():&#who(725,14)/mul(770,595~%%$]mul(213,299)*#[*mul(116,151)#<&!@>how()'from() mul(605,523)from()(who()mul(593,247)>select(),'who();mul(449,779)*how()+how()how()mul(956,857)do():~mul(826,140)^mul(224,267)<)who()?{-^~:mul(789,774)][*why()@-mul(443,401) what()mul(823,217)when(){*/why();>what(637,904),who()mul(264,561)]%-(how()how()mul(361,672)}when()(<!when()when()<mul(242,102)&;who()how()mul(621,459),where()select()$%$where()mul(882,598)
how()#what()where()$who())*<do()when()&[*(select(973,490)~mul(229,108)}%;%don't()mul(597,35)^mul(573,106)!]/{}]what()when()%?do()mul(374,846)?%from(74,478){who()mul(191,307)!}{#[)mul(372,182)(why()(do()mul(113,448)+>when()-mul(850,888)(:-'do()-+-&*mul(798,594)when()-^(<why()from()<mul(704,684)%/why()$don't()$}$when()from()-*-}mul(408,178)why()}+$-&how()mul(572,313)+@]&mul(400,367)how()when()]<who()<'mul(399,406)%]> )(mul(990,700)mul(822,80)mul(803,211)+ %]who()>*mul(614,212)where();how()what()mul(969,702)~[@mul(916,424)*(from()mul(119,685)<mul(889,37)from())$[who()[-(<how()mul(608,492)-[#]:how()mul(189,469),^>'mul(242,632),mul(236,192)&}(-;from()!mul(409,803)mul(26,832)mul(179,583)%;mul(331,141)&select()mul(586,628({)~:mul(201,618)$from()]what()?*mul(346,455)mul(186,191)where() -when() ~&[)why()mul(227,155){&~mul(572,168)(from()}-:when()#where()mul(532,271)when()??:)'mul(482,565)>/^;mul(849,201))&~~-how()$mul(537,900)?+)select()mul(562,60)how()mul(80,960)/&+'!what(),@@mul(741,753),do()!>from())(~mul(434,18)mul(662,562)-'why()mul(205,696)what();from()who()mul(656,755)mul(197,722)?@what()*?*'~mul(935,826)')'%}mul(675,242)/{~mul(119,521)+how()mul(644,874)select():from()mul(538,772)why()~[%#}how()&[mul(911,456)]when()where()$)?mul(422,424)?how()!when()]+mul(931,256%!#<mul(3,464){*}*/mul(618,975)(:,who()]mul(842,565>where()?when(689,268)-^<$mul(303,826)#what()$mul(400,12)~#mul(81,564)>}who())?/+$mul(871,726)?: [how()/}what()mul(694,277)>from()from()/**??)mul(395,609))^when()why()mul(615,463),why())@*when())select()mul(363,846)'&*)!]?)#mul(355,458)- don't()^ ^-'^what()-how()&mul(631,476)/where()^[+*>;mul(89,941)^$&}from(),'do())who()select()'^+& when();mul(434,156)(:@/select()>+from()*how()mul(508,595)mul(779(/&}mul(583,481)mul(624,130)$;??- :]^mul(66,470)mul(169,109)!{,@@]*)mul(984,230>}'%?#&~#don't()why()%,#<:$'mul(251,527):select()}mul(213,941)}^$#@mul(680,847)}$,)who()^~^why(),mul+){where()where()don't()^,#;when()>why()-:mul(226,208)-<from()<where()]what()&^*don't();)&from()^,mul(715,140)!<&how();{mul(300,628)($+ where(497,386);;what()how(612,199)mul(112,519))([mul(995,792)where(),{where():{$where(397,933)!mul(10,240),#who()mul(690when()%what()}~]where()do()^-'!from()!where():where()&mul(785,298)>who()#!~;<([mul(34,783)[when()from()]who()from()mul(421,685)mul(55,857)% -$/'when()]do()%mul(295,33)/mul(211,988)mul(492,249)select()//from()!mul(678,139)?what()why()?/!why()what()mul(62,558);~+ [don't()select()^from()~ +what()where(){-mul(46,220)why()>@~from()?{mul(78,499)/mul(13,468}{'[select()-}};do();]'}^(>-why()who()mul(458@~~who(),@;)why()/mul(56,660)mul(555,777)/$mul(660,540)@why()what()from()(!mul(317,310)^,&-+why()why()*mul(163,392)what(){}+}don't()why()%<select()}/mul(693,615% ]who()what();'>mul(593,212)+what()@mul(235,578)where()~?don't()select()&where()/#[~,+mul(540,363)who()mul(460,343)#where()select(63,367)'&^!mul(553,169)#^$ <why()mul(22,209)]?mul(129,490)]+mul(824,295)who()(!!mul(878,169)how()>mul(521,969)where()*&select()&~why()select()/{don't();mul(853,399)$mul(808,9))how() }when()don't()^>(-mul(938,463)/*#!/usr/bin/perl^)when():mul(751,26)
mul(542,820)select()$mul(103,40)]how()? :mul(682,891))mul(837,527)+when()  >mul(441,283)^ mul(603,169)select()%!mul(772,674)from()how()@^mul(222,674)from()who(),select(102,983)who()~[mul(697,571)$]:^from()~{?mul(763,249)}:,why()select(188,51)when()$select()how(412,892)[do()why()what(),&mul(258,614)mul(210,257)-)^mul(898,947)#mul(134,666)~,^mul(757,293)(where()!mul(977,413)when()))what(58,623)mul(706,330)who()where()who()select()mul(286,97) ]why())/mul(876,454)>}mul(412,509how() )+who()mul(402,110)/-%}where()when()do();^what())?()$]mul(257,787),from()!+~}*mul(250,775)<why()mul(826,349)!select()what()$mul(668,426)]/ {[mul(552,132)##why():mul(289,363)~',what()don't()%where()~who()what()#)@#mul(815,869)}where(){~}&mul(401,620)-where()]]!#+@mul(787,918)@}:mul(231,854(mul(488,659)?mul(267@when(211,508)where()*],mul(894,288)how(){mul(633,28)? (///&mul(235,462)&'how()mul(6,249)%~&!why()how();+)don't()?@,mul(291,493)mul(731,513)mul(650,232))+;![when()mul(244,943)mul(810,586~ ~mul(133,729))^&%''@~who()don't(){mul(850^'why()mul(91,172)^#&] who()%mul(403,294)-~)where())#<mul(224,258)+,}$$?when(925,148)mul(83,251)/mul(570,58),+how()why()mul(130,998):- ( what()where()[what(),mul(221,150)$$,do()%;%mul(920,992)[mul(314,990)#{select()&mul(265,592)mul(197,785)<(+{/? why(){~mul(144,77,!~select()-(*when()mul(227,184)?how()^? }mul(576,268)'>when()mul(735,684)why()(from(){)^how()from()!mul(749,268) how()mul(613,859)when(424,496)from()~^[mul(450,275)how()mul(41,682)when():when()what()when()*'[how()do()&'where(271,301)@}select()~mul(745,186)',[mul(585,614)what()^@when(224,919)/#>,-mul(374,69)-)< who()~when()why(),mul(30,174)-[what(357,897)where()who()@mul(10,444)'how()'when()what()&$mul(809,809)who()?+(~what();;mul(531,509)^^^%(~~mul(119,968){why();who(677,751)who()!mul(161,854)^^ how()](mul(481,323),/<how()why()&?mul(878,699)~ -mul(658,842)when()/!( ~ mul(593,125)^mul(486,116)+'!(#}:%@mul(922,260)~mul(163,921):what()'<what(120,761)/:select()don't()select()select()}<-when()?}mul(601,494)mul(184,68)mul(703,694)&;;!}![mul(255,743)who()* ^select()%mul(772,315)what()-mul(799,280):who()why();!what()]+what()how(847,982)mul(276,198);select()<*;>:,@mul(293,345)/)what()%!what()<~mul(959,852)/+$why()^<!-mul(756,324)how()>why()where(),@mul(281,314)#when()%]! -mul(347{why()select()why():)^~mul(10,106)%+?%when()mul(941,657)select()when()&,@@'@mul(250,253)#,what()mul(539,823);^*<[mul(422,155)who(){$:-&#mul:mul(61,174):why()'where()don't()select()<&+!/@&<-mul(596,236)~mul(339,838)'}mul(263,931)!how()mul(65,701)from()'/>/)mul(879,804)how() {*((mul(213,689)*[when()}what()?where())mul(727,958)mul(246,840)+mul(150,479)>?~from()*mul(552,678)?don't()$~?'mul(97,380)>mul(968,76)}#!from()mul(435,362why()#}when()*[how()'!#mul(357,345)}?why()[[mul(356,875)%when())$#mul{from()mul(289,657)from(681,624)'<;who()mul(514,298);{ mul-/[(:who():mul(789,109)where()%}what(435,852)mul(330,192)why();)$-]+mul(617,542)mul(244,889)?*%'>!mul(799,990)from()(mul(234,708)
@; ;?&]?#mul(577,752)%*)$&why()!%[mul(7,487)how(),@]select()$mul(38-?-+:^[from()#mul(252,810)who()]<+<who()how()]mul(85{$+who()mul(30,63)~who(743,434)~;mul(808,964)~?mul(459,384)>!)mul(976,357)[}mul(341,264)/#select(),%select()&mul(547,552)where()from()@+}#:mul(592,61)&how()what();select()!^select()(mul(273,4)'/^mul(446,170)%]]'~+mul(678,454)when()}select())/?#+}mul(180,876)-%%why()mul(255,652)]why()$#!mul(114,812)-?mul(207,511)<who()<>[$how()+}^mul(790,315)%who()/&<mul(631,708)+%+mul(674,272)when(792,225)&~how()}+how()mul(342 /where()how()who(){<{~mul(848,950)>]do()]#@why()/mul(743,708)mul(430,155)+what()(what()'who()$<;mul(700,543)mul(574,126)mul(139,29)who()what() mul(47,32)what() [;don't(),%who() ~}{mul(176,682)>@~select()when()# %,@mul(808,816):~^)where(629,778)%>+'@mul(177,383)mul(29;what()@*mul(324,53)?'?$~-mul(509,507)$}where(929,765) ~%]what()&mul(325,403)how()-<from()&where()}who(){mul(505,703)select(107,676)&mul(252,930)select()(@$?*;mul(143,564)from()':select()do()]mul(130,866)how()#?select()&@who(811,263)why()mul%[(;&;mul(818,893)mul(654,383)@(/&]?don't()*>when()@how()>mul(900,560)what();@)$select(723,538) +)'mul(899,730)},}$select()*~!from(872,462)mul(269,888)+//)<(how()mul(688,635)#>$+)mul(62,201)from()/@,*<,:{mul(808[!-from(),why()~@'{mul(719,116) don't()+where():)mul(139,220)what()*>who()mul(162,455)who()~mul(460,418)<>&?:/&}from():mul(238,979)&/!@'%~+mul(863,124)'~-*select()[@:do()why(124,979) [{'why():#who()how()mul(38,201)&/when();+mul(678,638):}>:$*select()mul(367,239),){*mul(512?>([what()@ do()[-&mul(39,285)mul(97,17)where(){^do()!:mul(347{who()'mul(316,561);mul(537,106)how(),(!mul(785,385)mul(13,891)~why()~[do()(+]who()<)mul(878,575[mul(295,693)#<where()(++mul(547,320))*-;>:!when()%why()mul(293,288);:what()>^^%(<$mul(640,998)from()}mul(340,293)mul(759,91)&(#mul(831,471)why()why()from()mulwho()who()[[<mul(703,622)how()select()select(712,26)mul(936,215)who();who()<[mul(615,207)*mul(662,445)what(670,709)when()!{mul(21,612)where()/from()~mul(144,583)how()!>^'*mul(210,542)where()%what()~?:,-don't()!mul(305,106)+#@!&,do()~%when()mul(318,660)from()when() why():$-[mul(589,949)@&do()?from()mul(455,593)${!*<~*why()#mul(371,828)where()%({ +%$mul(318,225):where()#-?#%mul(816,5)mul(363,524)mul(580,821)/where()what()*{where();mul(223];mul(830,758)~^ why()/?,>why()mul(787,428)( --'who()what()$~mul(314,163)[what()/*~<(</-mul(602,163)@!when()]mul(997,438)<>?#?[ &select())mul(746,865)mul(101,592))}mul(133,751),;',from()mul(226%how()select()/{$!#select(553,217)do()%}mul(538,699))~when()$?* (what()}mul(755,507)+from()who()who()]how(){--[mul(483,410):'  -do()where()$}mul(33,473)mul(835,106)$ {)mul(790,297)how()*where()select()where()*,mul(739,441)mul(561,91)]what()[select()%;what(){mul(601,44where()'):where()(/}<+;mul(956,550)}when()[mul(326,936)<where()~@-mul(238,48)/when()'what()'when()mul(331,847)where()'?don't()>where()how();!from()-mul!/$>?mul(133,674)}what()^*}from()~!mul(39,598)+ mul(119,823)where()$$'when()[mul(524,9)&<<@$-mul(473,929)<why()!:/#-mul(581,168)+-from()*@?mul(217,47)/who()what();select()&don't()+?;mul(840,326)what()<^^when()mul(618,587){select(870,163)how()what()mul(304,775)
what()(!what(),^$mul(929,706)**]+mul(518,107)from()@@!when()where()#] mul(353,511)<who()from()don't(){-^mul(269,200)(}mul(691,529)){@<~?where()mul(665,863)$^;{$#mul(571,747)[]mul,mul(641,438)(who()when(832,16)do()~why()who()why()<who()where()#,mul(571,105)!mul(322,339)who()?-:]&%mul(667,821)-] ?who()[,]{who()mul(822,144):select()mul(696,806)how()#,[,]mul(98,576)who(6,143)who()$;^>&mul(154,39)^*why()mul(454,972)>mul(819,718))!select() #{mul(176,840<why(53,917)do()]who()&<from()why()/mul(222,418)select()}mul(53,240)mul(561,784)~mul(304,320)mul(50,387)select()(@%<mul(185,493)when()!/;select()+,why()'mul(423,24)*%[-:what()?'mul(968,778)[?what()}!how()how()%%where()mul(694,257)~~&}how()<),)>mul(989,933)%mul(553,654)/where())+what()what()]%mul(293,835):#/'@-when())$'mul(548,948)?who()-where()when()/when()who()where()<don't()(&from()~why()~%-when(){mul(941,861)'when()who()mul(757,163)where(){'*who() {mul(430,376)(>[}@&when(225,152)do()why()!why()-;how()mul(941,10)when(798,196)[<:<select(592,80)<<mul(216,585)/how():@$<when()mul(730,717)don't()}[{[^who(677,991)]~mul(685,354)$~'*)^<?mul(231,11)@&$&>)%mul(9,571)from()#[*what()&&)$/mul(507,991):#?$$<('mul(959,970)^what()what()'where()%@from()%mul(508,137)}mul(230,238)<when():mul(874,283)${$+?-don't()&!select())who()from();where()/mul(837,931)when()how()(mul(345,324)>]<@!,who()where()#mul(636,897)?why()%]when()?/^)where()don't()select()>@+(!mul(215,107):;where();where()mul(237,981);who()[from()>*<mul(85,235) select()mul(696,477);(where()&/)*what()+ mul(838,830)don't()how()what()*$#>,,;mul(357,549)!{(mul(313,524):mul(172,631)-()mul(197,822)from(510,614);how():(>(mul(450,700)&when()@'when():>&mul(572,27)]select()how()/how()~ mul(427,506)'select()%&how(955,693)~$&[why()mul(670,224)@^'>;why()#where(38,295)mul(265,471)^mul(241,265)*#+{select()when()do()from()<why()mul(576,456)^don't()where()select()<)+?where(),&mul(670,731)mul(641,391)*?(what()#*;:mul(736,498)(from(656,887)from()&from()@do()~when(){why()mul(219,587)*?who()',what()+mul(581,478)${$-mul(316,750){+>^@>mul(444,279)}what()from(),!what()+mul(233,30))%/(&mul(24,452)how()who()where(241,512)>where(),from()^>[mul(337,620)+from(296,671)[~ who()where()}'mul(478,339)<don't()~+<*what()mul(812,697)]why()&why(644,814)when():what()when()mul(652,371)(];#(]?<what()+do()where(64,166)@when()&>@mul(963,388)who()[select()$&mul(268,170)!;select()*)mul(192,33)what()where()mul(497,317){<+do()mul(274,822)how()why()+mul(286,147)mul(377,935)mul(696,807)^when()select()>don't())from())!when()<^mul(799,142)'where()^who()mul(616,986)from()*/mul(697,100)%(select(698,850)don't()%{from(775,182)/@}/?]mul(208,63)~~],mul(15,121)({~mul(704,468)}select()from():?/[what(){mul(707,923),when()mul(253,50),-)how()^#*::select()mul(473,468)what()$#}#:/$how()+mul(569,78)]<>(when()mul(394,997)-mul(184,736)@(@/;%~what()mul(827,383)!#)who())'mul(27,745)-$mul(246,974)how()<,$,$#mul(211,698)select()! when()mul(40,60)]why()mul(98,533)?#)(mul(442,333)who()mul(645,711)how()why(507,343)<#,mul(267,790)select()from()/]]:select()~mul(27,928)/#mul(443,725)~how()@:why()how()%mul(963,554)%mul(490,273)(@ ;-$@$mul(309,347)(mul(830,444)+'}from(){how()#&:why()
"""

pattern = r"don't\(\).*?do\(\)"
pattern2 = r"don't\(\).*"
pattern3= r"(?<=mul\()\d{1,3},\d{1,3}(?=\))"

cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)
cleaned_text2 = re.sub(pattern2, 'restinpeacedick', cleaned_text, flags=re.DOTALL)
list = re.findall(pattern3, cleaned_text2)

magic_number = 0

for i in list:
    list2 = i.split(",")
    magic_number += int(list2[0]) * int(list2[1])

print(magic_number)
