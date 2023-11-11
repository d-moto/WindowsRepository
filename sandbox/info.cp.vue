<template>
    <div>
        <!--{{Syoudo}}-->
        <!--{{Next_Time}}-->

        <!--Infomation文字-->
        <div style="width:1000px;">
            <p style="font: bold 35px sans-serif; color: gray; margin-top: 10px; ">Information</p>
        </div>
        <!--{{State_of_window}}
    {{State_rist}}-->
        <!--
        {{ AlarmONDisplayList}}

    ++++++++++++++++{{Weather}}
            -->


        <div style="text-align: -webkit-center; padding: 0px;width:1000px;">
            <!--info4カード書式統一用div-->
            <!--<div style="width: 400px; height: 150px; background-color: aquamarine; overflow: scroll; ">
                {{listMessage}}
            </div>-->
            <!--住所確認ボタン-->
            <div style=" margin-left: 825px; margin-top:-55px; z-index: 998; position:relative;">
                <button type="button" class="btn btn-sm shadow-none ps-3 pe-3 " style="border-width: 4px; border: 1px solid lightgray; border-radius: 3px; background-color: whitesmoke; color: dimgrey; width: 100px; height: 75px; "
                        @click="openModal('Address')" @tap="openModal('Address')">
                    <span class="material-icons-outlined" style="font-size: 45px;margin-top:-6px;">
                        home
                    </span>
                    <div style="margin-top: -8px; font-size: 18px;">Address</div>
                </button>
            </div>

            <!--環境値・RCAuto・さらに表示-->
            <div class="info_card">
                <table style="height:150px; border-bottom:3px dotted gray;">
                    <!--2023/0709-->
                    <tr style="border-bottom:3px dotted gray;">
                        <td>
                            <table>
                                <tr>
                                    <td>
                                        <!--101-->
                                        <div v-if="State_of_roll_curtein101.open || State_of_roll_curtein101.close" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:-70px; margin-right:30px;">　<!--left:20px 現在共有部のみ表示の為位置調整に仕使用-->
                                                <!--<div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein101.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein101.open" style="width: 100%;  margin-top: 12px; font-size: 15px; ">
                                                        101部屋<br />電動ST<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein101.close" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        101部屋<br />電動ST<br />全閉
                                                    </p>
                                                </div>-->
                                            </div>
                                        </div>
                                        <!--102-->
                                        <div v-if="State_of_roll_curtein102.open || State_of_roll_curtein102.close" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:-70px; margin-right:30px;"><!--left:20px 現在共有部のみ表示の為位置調整に仕使用-->
                                                <!--<div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein102.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein102.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        102部屋<br />電動ST<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein102.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        102部屋<br />電動ST<br />全閉
                                                    </p>
                                                </div>-->
                                            </div>
                                        </div>
                                        <!--103-->
                                        <div v-if="State_of_roll_curtein103_1.open || State_of_roll_curtein103_1.close" style="display: inline-block">
                                            <div style="width: 110px; height: 120px; margin-left: -100px; margin-right: 30px;"><!--元々left-10 共有部表示のみの為位置調整に使用中-->
                                                <!--<div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein103_1.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein103_1.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        103部屋-1<br />電動ST<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein103_1.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        103部屋-1<br />電動ST<br />全閉
                                                    </p>
                                                </div>-->
                                            </div>
                                        </div>
                                        <div v-if="State_of_roll_curtein103_2.open || State_of_roll_curtein103_2.close" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:-110px; margin-right:30px;"> <!--元々left:20-->
                                                <!--<div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein103_2.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein103_2.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        103部屋-2<br />電動ST<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein103_2.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        103部屋-2<br />電動ST<br />全閉
                                                    </p>
                                                </div>-->
                                            </div>
                                        </div>

                                        <!--201-->
                                        <div v-if="State_of_roll_curtein201_1.open || State_of_roll_curtein201_1.close || State_of_roll_curtein201_1.half_open" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left: -10px; margin-right: 30px;">
                                                <div style="width:100%;  height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', background: State_of_roll_curtein201_1.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein201_1.open" style=" width: 100%; font-size: 15px; border-top: 12px; ">
                                                        201部屋-1<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein201_1.close" style=" width:100%; margin-top:12px;font-size:15px;">
                                                        201部屋-1<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curtein201_1.half_open" style="width: 100%; border-top: 12px solid #a0d8ef; background-color: #a0d8ef; font-size: 15px; ">
                                                        201部屋-1<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>

                                        <div v-if="State_of_roll_curtein201_2.open || State_of_roll_curtein201_2.close || State_of_roll_curtein201_2.half_open" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:20px; margin-right:30px;">
                                                <div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein201_2.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein201_2.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        201部屋-2<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein201_2.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        201部屋-2<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curtein201_2.half_open" style="width: 100%; border-top: 12px solid #a0d8ef; background-color: #a0d8ef; font-size: 15px; ">
                                                        201部屋-2<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>

                                        <!--202-->
                                        <div v-if="State_of_roll_curtein202.open || State_of_roll_curtein202.close || State_of_roll_curtein202.half_open" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:20px; margin-right:30px;">
                                                <div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein202.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein202.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        202部屋<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein202.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        202部屋<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curtein202.half_open" style="width: 100%; border-top: 12px solid #a0d8ef; background-color: #a0d8ef; font-size: 15px; ">
                                                        202部屋<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>

                                        <!--203-->
                                        <div v-if="State_of_roll_curtein203_1.open || State_of_roll_curtein203_1.close || State_of_roll_curtein203_1.half_open" style="display: inline-block">
                                            <div style="width: 110px; height: 120px; margin-left: -10px; margin-right: 30px;">
                                                <div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein203_1.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein203_1.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        203部屋-1<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein203_1.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        203部屋-1<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curtein203_1.half_open" style="width: 100%; border-top: 12px solid #a0d8ef; background-color: #a0d8ef; font-size: 15px; ">
                                                        203部屋-1<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-if="State_of_roll_curtein203_2.open || State_of_roll_curtein203_2.close || State_of_roll_curtein203_2.half_open" style="display: inline-block">
                                            <div style="width: 110px;  height: 120px; margin-left:20px; margin-right:30px;">
                                                <div style="width:100%; height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curtein203_2.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curtein203_2.open" style="width: 100%; margin-top: 12px; font-size: 15px;">
                                                        203部屋-2<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curtein203_2.close" style="width:100%; margin-top:12px;font-size:15px;">
                                                        203部屋-2<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curtein203_2.half_open" style="width: 100%; border-top: 12px solid #a0d8ef; background-color: #a0d8ef; font-size: 15px; ">
                                                        203部屋-2<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                        <!--Share用表示-->
                                        <div v-if="State_of_roll_curteinShare1.open || State_of_roll_curteinShare1.close || State_of_roll_curteinShare1.half_open" style="display: inline-block">
                                            <div style="width: 110px;   height: 120px; margin-left:20px; margin-right:30px;">
                                                <div style="width:100%;  height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%', backgroundColor: State_of_roll_curteinShare1.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curteinShare1.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        共有部-1<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curteinShare1.close" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        共有部-1<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curteinShare1.half_open" style="width: 100%; border-top: 12px solid #a0d8ef;  background-color: #a0d8ef; font-size: 15px; ">
                                                        共有部-1<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-if="State_of_roll_curteinShare2.open || State_of_roll_curteinShare2.close || State_of_roll_curteinShare2.half_open" style="display: inline-block">
                                            <div style="width: 110px;   height: 120px; margin-left:20px; margin-right:30px;">
                                                <div style="width:100%;  height:10%; border:2px solid gray;"></div>
                                                <div :style="{ width: '90%', height: '90%', border: '2px solid gray', marginLeft: '6%',  backgroundColor: State_of_roll_curteinShare2.open ? '#a0d8ef' : 'transparent' }">
                                                    <p v-if="State_of_roll_curteinShare2.open" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        共有部-2<br />RC<br />全開
                                                    </p>
                                                    <p v-if="State_of_roll_curteinShare2.close" style="width: 100%;  margin-top: 12px; font-size: 15px;">
                                                        共有部-2<br />RC<br />全閉
                                                    </p>
                                                    <p v-if="State_of_roll_curteinShare2.half_open" style="width: 100%; border-top: 12px solid #a0d8ef;  background-color: #a0d8ef; font-size: 15px; ">
                                                        共有部-2<br />RC<br />開
                                                    </p>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                    <!--各ページ表示用共有スペース-->
                                    <td>
                                        <div v-show="State_of_roll_curteinS.open">
                                            <div style="width: 110px; height: 120px;">
                                                <div style="width:100%;height:10%;border:2px solid gray;"></div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; background-color: #a0d8ef; margin-left: 6%;">
                                                    <div style="width:100%; margin-top:12px;font-size:15px;">
                                                        共有部<br />RC<br />全開
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-show="State_of_roll_curteinS.close">
                                            <div style="width: 110px; height: 120px;">
                                                <div style="width:100%;height:10%;border:2px solid gray;"></div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; margin-left: 6%;">
                                                    <div style="width:100%;background-color:white;margin-top:12px;font-size:15px;">
                                                        共有部<br />RC<br />全閉

                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-show="State_of_roll_curteinS.half_open">
                                            <div style="width: 110px;  height: 120px;">
                                                <div style="width:100%;height:10%; border:2px solid gray;"></div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; margin-left: 6%;">
                                                    <div style="width: 100%; margin-top: 1px; background-color: #a0d8ef; font-size: 15px;">
                                                        共有部<br />RC<br />開
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </td>
                                </tr>
                            </table>
                            <!--<table>
                        <tr>
                            <td>-->
                            <!--room101 S1-101 -->
                            <!--ここから0803-->
                            <!--<div v-if="State_of_roll_curtein101.open || State_of_roll_curtein101.close" >
                        <div style="display: inline-block;">
                            <div style="width: 110px; height: 120px; margin-left:95px; margin-right:-50px;">
                                <div style="width:100%;height:10%;border:2px solid gray;">
                                </div>
                                <div style="width: 90%; height: 90%; border: 2px solid gray; background-color: #a0d8ef; margin-left: 6%;">
                                    <p v-if="State_of_roll_curtein101.open" style="width:100%; margin-top:12px; font-size:15px;">
                                        部屋電動S1-101全開
                                    </p>
                                    <p v-if="State_of_roll_curtein101.close" style="width:100%; margin-top:12px; font-size:15px;">
                                        部屋電動S1-101全閉
                                    </p>
                                </div>
                            </div>
                        </div>
                            </div>
                        <div v-show="State_of_roll_curtein101.open">State_of_roll_curtein101.open is true</div>
                        <div v-show="State_of_roll_curtein101.close">State_of_roll_curtein101.close is true</div>-->
                            <!--room102 S2-102-->
                            <!--<div v-if="State_of_roll_curtein102.open || State_of_roll_curtein102.close">
                        <div style="display: inline-block;">
                            <div style="width: 110px;  height: 120px; margin-left:105px; margin-right:30px;">
                                <div style="width:100%; height:10%; border:2px solid gray;">
                                </div>
                                <div style="width: 90%;  height: 90%; border: 2px solid gray; margin-left: 6%;">
                                    <p v-if="State_of_roll_curtein102.open" style="width:100%;background-color:white; margin-top:12px;font-size:15px;">
                                        部屋電動S2-102全開
                                    </p>
                                    <p v-if="State_of_roll_curtein102.close" style="width:100%;background-color:white; margin-top:12px;font-size:15px;">
                                        部屋電動S2-102全閉
                                    </p>
                                </div>
                            </div>
                        </div>
                            </div>
                        <div v-show="State_of_roll_curtein102.open">State_of_roll_curtein102.open is true</div>
                        <div v-show="State_of_roll_curtein102.close">State_of_roll_curtein102.close is true</div>-->
                            <!--ここまで-->
                            <!--room103 S3-103 S4-103--以下コメントアウト0803-->
                            <!--<div v-if="State_of_roll_curtein103.open || State_of_roll_curtain103.close">
                        <div style="display: inline-block;">
                            <div style="width: 110px; height: 120px;  margin-left:105px; margin-right:-80px;">
                                <div style="width:100%;height:10%;border:2px solid gray;">
                                </div>
                                <div style="width: 90%; height: 90%; border: 2px solid gray; background-color: #a0d8ef; margin-left: 6%;">
                                    <p v-if="State_of_roll_curtein103.open" style="width:100%; margin-top:12px; font-size:15px;">
                                        部屋電動S3-103全開
                                    </p>
                                    <p v-if="State_of_roll_curtein103.close" style="width:100%; margin-top:12px; font-size:15px;">
                                        部屋電動S3-103全閉
                                    </p>
                                    <p v-if="State_of_roll_curtein103.open" style="width:100%; margin-top:12px; font-size:15px;">
                                        部屋電動S4-103全開
                                    </p>
                                    <p v-if="State_of_roll_curtein103.close" style="width:100%; margin-top:12px;font-size:15px;">
                                        部屋電動S4-103全閉
                                    </p>
                                </div>
                            </div>
                        </div>
                            </div>
                        <div v-show="State_of_roll_curtein103.open">State_of_roll_curtein103.open is true</div>
                        <div v-show="State_of_roll_curtein103.close">State_of_roll_curtein103.close is true</div>-->
                            <!--ここまで0803-->
                            <!--</td>
                                <td>
                                    <div>
                                        <div v-show="State_of_roll_curteinS.open">
                                            <div style="width: 110px; height: 120px;">
                                                <div style="width:100%;height:10%;border:2px solid gray;">
                                                </div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; background-color: #a0d8ef; margin-left: 6%;">
                                                    <div style="width:100%; margin-top:12px;font-size:15px;">
                                                        共有スペース<br />RC<br />開
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-show="State_of_roll_curteinS.close">
                                            <div style="width: 110px; height: 120px;">
                                                <div style="width:100%;height:10%;border:2px solid gray;">
                                                </div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; margin-left: 6%;">
                                                    <div style="width:100%;background-color:white;margin-top:12px;font-size:15px;">
                                                        共有スペース<br />RC<br />全閉
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                        <div v-show="State_of_roll_curteinS.half_open">
                                            <div style="width: 110px; height: 120px;">
                                                <div style="width:100%;height:10%;border:2px solid gray;">
                                                </div>
                                                <div style="width: 90%; height: 90%; border: 2px solid gray; margin-left: 6%;">
                                                    <div style="width: 100%; background-color:#a0d8ef; margin-top: 1px; font-size: 15px;">
                                                        共有スペース<br />RC<br />半開
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </td>
                            </tr>
                        </table>-->
                        </td>
                    </tr>
                </table>
                <table>
                    <tr>
                        <!--窓開閉の表示-->
                        <td>
                            <div v-show="State_of_window.open || State_of_window.close" style="border:3px solid; width:120px;height:120px;border-radius:50%;margin-left:10px;" v-bind:style="{'border-color': State_of_window.open ? 'orange' : 'navy'}">
                                <span v-show="State_of_window.open">
                                    <img src="../../../../../../dist/assets/maco/Weather/window_open.png" width="45" height="35" style="margin-bottom:6px;margin-top:10px;margin-left:0px;" />
                                </span>
                                <span v-show="State_of_window.close">
                                    <img src="../../../../../../dist/assets/maco/Weather/window_close.png" width="45" height="35" style="margin-bottom:6px;margin-top:10px;margin-left:0px;" />
                                </span>
                                <p v-show="State_of_window.open" style="font-size:18px;margin-top:-8px;">
                                    窓状況
                                    <br />
                                    開
                                </p>
                                <p v-show="State_of_window.close" style="font-size:18px;margin-top:-8px;">
                                    窓状況
                                    <br />
                                    閉
                                </p>

                            </div>
                        </td>
                        <td>

                            <div v-show="State_of_key.open || State_of_key.close" style="border:3px solid; width:120px;height:120px;border-radius:50%;margin-left:10px;" v-bind:style="{'border-color': State_of_key.open ? 'orange' : 'navy'}">
                                <span v-show="State_of_key.open" class="material-icons-outlined" style="margin-left: -24px; margin-top: 1px; font-size: 45px; position: absolute; color: red ">
                                    lock_open
                                </span>
                                <span v-show="State_of_key.close" class="material-icons-outlined" style="margin-left: -24px; margin-top: 1px; font-size: 45px; position: absolute; color: #3cb37a ">
                                    lock
                                </span>
                                <p v-show="State_of_key.open" style="font-size:18px; margin-top:45px;">
                                    鍵状況
                                    <br />
                                    開
                                </p>
                                <p v-show="State_of_key.close" style="font-size:18px; margin-top:45px;">
                                    鍵状況
                                    <br />
                                    閉
                                </p>
                            </div>
                        </td>



                        <!--照明色Kの表示（仮）-->

                        <td>
                            <div style="border: 3px solid; width: 120px; height: 120px; border-radius: 50%; margin-left: 0px;" v-bind:style="{'border-color': getColor(color_temperature)}">
                                <!--<div v-show="5000" style=""........-->
                                <span class="material-icons-outlined" :style="{'font-size': '45px', 'color': getColor(color_temperature)}">light</span>
                                <p style="font-size:18px;margin-top:-8px;">
                                    照明色
                                    <br />
                                    {{ getColorLabel(color_temperature) }} 
                                </p>
                            </div>
                        </td>



                        <!--照度目標値の表示-->
                        <td >
                            <div>
                                <div style="margin-top:20px;">
                                    <p style="font:bold 20px arial;">
                                        照度目標値
                                        <br />
                                    </p>
                                    <p v-show="State_of_ATauto.on" style="font:bold 20px arial;">
                                        {{NowBrightValue}} lx
                                    </p>
                                    <p v-show="State_of_ATauto.off" style="font:bold 20px arial;">
                                        - lx
                                    </p>
                                    <div style="width:110px;height:40px; margin-left:15px;margin-top:-5px;" class="Button" @click="jump_controllist">
                                        <div style="font-size:16px; margin:7px;padding-top:-10px;">制御の詳細</div>
                                    </div>
                                </div>
                            </div>
                        </td>
                    </tr>
                </table>
            </div>



            <!--時間・日付・RC自動制御時間・照明色-->
            <div class="info_card" style="margin-left:5px;">
                <table style="width:100%;height:100%;margin-top:10px">
                    <tr style="color: #989595; height: 100px;">
                        <td style="width:70%;">
                            <span style="font: 100px arial;padding-left:20%">{{Zikan}}</span>
                        </td>
                        <td style="font: 35px arial; padding-left: 10%">
                            {{Hiduke}}
                            <br />
                            {{Youbi}}
                        </td>
                    </tr>
                    <tr>
                        <td v-show="is_enable_botton.notShare">
                            <div style="border: 1px solid lightgray; border-radius: 3px; height:150px; width: 235px;  background-color: whitesmoke; margin-left: 5px; margin-top: -1px " @click="openModal('Alarm')" @tap="openModal('Alarm')">
                                <p style="font-size:20px; margin-top:15px; margin-bottom:25px;"><b>アラーム設定</b></p>
                                <!--20230625追加start-->
                                <p style="font-size:15px;" v-for="box in AlarmONDisplayList" :key="box.Hour + box.Minute">
                                    <span v-if="box.State === 'TRUE'">{{ box.Hour }}:{{ box.Minute }}:{{ box.Day }}</span>
                                </p>
                                <!--20230625追加end-->
                            </div>
                        </td>
                        <td v-show="is_enable_botton.notShare" style="padding-right:2px;">
                            <!--padding-rightで右側の余白を増やした-->
                            <div style="border: 1px solid lightgray;  border-radius: 3px;width: 100px;height:85px; margin-left: -70px; margin-top: 60px; background-color: whitesmoke;" @click="GoodMorning_Click()">
                                <span class="material-icons-outlined" style="font-size: 55px; margin-left: -1px; margin-top: 15px; color: orange;">
                                    light_mode
                                </span>
                            </div>
                        </td>
                        <td v-show="is_enable_botton.notShare" style="padding-right:2px;">
                            <div style="border: 1px solid lightgray; border-radius: 4px; width: 100px;  height:85px; margin-left:-90px; margin-top:60px; background-color: whitesmoke; " @click="Night_Click()">
                                <!--<div style="width: 100px; height: 150px; border: 2px solid lightgray; border-radius: 3px; margin-left: 860px; margin-top: -150px;">一括ボタン</div>-->
                                <span class="material-icons-outlined" style="font-size: 55px; margin-left: -1px;  margin-top: 15px; color: steelblue;">
                                    dark_mode
                                </span>
                            </div>
                        </td>
                        <td v-show="is_enable_botton.Share">これはShareの値がtrueの時に表示される。つまりShareページのinformationの時だけ、この文章は、出てくるよ</td>
                    </tr>
                </table>
            </div>

            <!--チャット-->
            <div class="info_card" style="padding-top:0px">
                <!--<p style="font-size:20px">集いの場</p>
                <div style="text-align:center;margin-top:20px;height:250px">
                    <div style="width: 468px;  overflow: auto; -ms-overflow-style: none; height:250px;">
                        <template v-for="(MessageHistory,i) in Chat" :key="i">
                            <table style="background-color: lightgray; text-align: left; width:250px;">
                                <tr style="font:bold 10px arial;">
                                    {{MessageHistory.SendTime}}
                                </tr>
                                <tr style="font:bold 15px arial">
                                    {{MessageHistory.UserName}}: {{MessageHistory.Message}}
                                </tr>
                            </table>
                        </template>
                    </div>
                    <div style="width:100%;height:40px;">
                        <input type="text" v-model="ChatSendMessage" style="float: right">
                        <div style="background-color: lightgray; border-radius: 5%; width: 60px; float: left;" @click="ChatMessageSend()">送信</div>
                    </div>
                </div>-->

            </div>

            <!--天気予報-->
            <div class="info_card" style="margin-left:5px;color:gray;">
                <p style="font-size:20px; margin-bottom:0px;">現在の天気予報　:　大久保町</p>

                <!--2023 05 14 added-->
                <table style="border-bottom:3px dotted gray;">
                    <tr>
                        <td style="border:none; border-bottom: none; border-left: none; width:230px;">


                            <!--天気画像-->
                            <!--風の強さと風向き-->

                            <table style="width:230px;height:80px;margin-top:3px;">
                                <!--線-->

                                <tr>

                                    <td style="width:90px;">
                                        <!--以下試し0627-->
                                        <div>
                                            <span v-show="State_rist.Sunny" class="material-icons-outlined" style="margin-left: -25px; margin-top: -55px; font-size: 60px; position: absolute; color: #e8c778 ">
                                                wb_sunny
                                            </span>
                                        </div>
                                        <div>
                                            <span v-show="State_rist.Cloudy||State_rist.Rainy" class="material-icons-outlined" style="margin-left: -15px; margin-top: -60px; font-size: 50px; position: absolute; color: lightskyblue">
                                                wb_cloudy
                                            </span>
                                            <p v-show="State_rist.Rainy" style="position: absolute; margin-top: -15px; margin-left: 35px; font: bold 25px arial; color: lightskyblue; ">/ / /</p>

                                        </div>

                                    </td>



                                    <td>
                                        <div style="width: 1px; height:90px; transform: rotate(230deg); margin-top: 0px; margin-left: 0px; background-color: blue;"></div>
                                    </td>
                                    <td style="width:70px;">
                                        <span style="margin-left: 0.8%; ">
                                            <img src="../../../../../../dist/assets/maco/Weather/Wind.png" width="30" height="40" style="margin-bottom:0px;margin-top:20px;margin-left:0px;" />
                                        </span>
                                    </td>
                                    <td>
                                        <p style="margin-top:30px; font-size:10px; text-align:left;">
                                            {{Wind_Speed}} m<br />
                                            <span v-show="State_of_Wind_Direction.North">
                                                北
                                            </span>
                                            <span v-show="State_of_Wind_Direction.Sorth">
                                                南
                                            </span>
                                            <span v-show="State_of_Wind_Direction.West">
                                                西
                                            </span>
                                            <span v-show="State_of_Wind_Direction.East">
                                                東
                                            </span>
                                            <span v-show="State_of_Wind_Direction.North_West">
                                                北西
                                            </span>
                                            <span v-show="State_of_Wind_Direction.North_East">
                                                北東
                                            </span>
                                            <span v-show="State_of_Wind_Direction.Sorth_West">
                                                南西
                                            </span>
                                            <span v-show="State_of_Wind_Direction.North_East">
                                                南東
                                            </span>

                                            <!--{{Wind_direction}}-->
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>

                        <!--室内室外の気温と湿度-->
                        <td style="border: none; border-bottom: none; border-right: none; ">
                            <!--ここで棒線消した-->
                            <table style="width:230px;height:80px;margin-top:3px;">
                                <tr>
                                    <td style="width:50px;" rowspan="2">
                                        

                                        <span class="material-icons-outlined" style="font-size:55px;color:gray;">
                                            thermostat
                                        </span>
                                    </td>
                                    <td style="font: 20px arial; color: dimgray; width: 80px;">
                                        屋外：
                                    </td>
                                    <td style="font-size: 20px;">
                                        <p style="margin-top:-5px;">
                                            {{temp_out}}
                                        </p>
                                    </td>
                                    <td style="font-size: 20px;">
                                        <p v-show="temp_out!='0℃以下'" style="margin-top:-4px;">℃</p>
                                    </td>
                                </tr>

                                <tr>
                                    <!--ここ追加した棒線-->
                                    <td style="font: 20px arial; color: dimgray; width: 80px;">
                                        室内：
                                    </td>
                                    <td style="font-size: 20px;">
                                        <p style="margin-top:-5px;">
                                            {{temp_room}}
                                        </p>
                                    </td>
                                    <td style="font-size: 20px;">
                                        <p style="margin-top:-4px;">
                                            ℃
                                        </p>
                                    </td>
                                </tr>
                            </table>

                        </td>
                    </tr>
                </table>

                <!--三日間の天気予報-->
                <p style="font-size:20px; margin-bottom:0px;">3日間の天気予報　:　大久保町</p>
                <table style="border:none ;height:80px;width:100px;margin-left:5px">
                    <tr>
                    </tr>
                    <template v-for="(Model,i) in Weather.slice(0, 3)" :key="i">
                        <td v-if="i <= 2" style="width: 100px; text-align: center;" v-show="i<4">

                            <p style="font-size: 15px;margin-top:-5px; margin-bottom:0px;">
                                <span v-if="i == 0">{{Hiduke}} {{Youbi}}</span>
                                <span v-if="i == 1">{{HidukeTomorrow}} {{YoubiTomorrow}}</span>
                                <span v-if="i == 2">{{HidukeDayAfterTomorrow}} {{YoubiDayAfterTomorrow}}</span>
                            </p>

                            <img :src="Model.weathercode" style="width:100px;" />

                            <p style="font-size: 15px;margin-top:-5px;">
                                {{Model.tempsMax}}℃/ {{Model.tempsMin}}℃
                            </p>

                        </td>
                    </template>
                </table>
                <p style="font-size:10px;">出典：気象庁ホームページ (https://www.jma.go.jp/bosai/forecast/)</p>
            </div>
            <div style="padding: 30px;color:gray;">

                <Dialog v-model:visible="displayModal_Alarm" :style="{width: '1130px'}" :modal="true" @show="showModal('Alarm')">
                    <Alarm_Set />
                </Dialog>


                <!-- 住所確認 -->
                <Dialog class="p-0" v-model:visible="displayModal_Address" :style="{width: '900px'}" :modal="true" @show="showModal('Address')">
                    <!--<button style="top: 2px; right: 2px;" @click="displayModalAllOffError=false">
                </button>-->
                    <p style="font-size:30px; color:gray;">611-0033<br />京都府宇治市大久保町西ノ端１－３０</p>
                </Dialog>

            </div>

            <div style="padding: 30px;color:gray;">

                <Dialog v-model:visible="displayModal_Alarm" :style="{width: '1130px'}" :modal="true" @show="showModal('Alarm')">
                    <Alarm_Set />
                </Dialog>

            </div>

        </div>

    </div>
</template>

<script lang="ts">
    import { defineComponent, ref, watch, onMounted, inject } from 'vue';
    import Alarm_Set from './Alarm_Set.vue';

    import { DoWriteAddress } from '../common_ts/DoSendAddres';

    import Axios from 'axios';
    import { AddComma, DateHenkan, DateToyyyyMMdd, myParseInt, myParseFloat, DateTime } from '/@/components/common/composables/utils';
    import * as signalR from '@microsoft/signalr';
    import { isNullOrUndefined } from 'util';
    import { State } from 'howler';
   // import SettingRist_Body from '../pages/settingrist/SettingRist_Body.vue';//ここのURLがおかしかったよう。現在は使わなくていいはずなので取り合えずコメントアウトで画面が正常に立ち上がりました。
 
//import { min } from '../../../../../../../../AppData/Local/Microsoft/TypeScript/5.1/node_modules/moment/ts3.1-typings/moment';

    let AlarmONDisplayList = ref([]);
    const GetAlarmDate = (): void => {

        Axios({
            method: 'GET',
            url: 'api/MaCo/GetAlarm',
            params: {
                ROOM: 'R101',

            }
        }).then((res) => {

            let data: any = res.data;
            if (typeof data === 'string') {
                data = JSON.parse(data);
            }
            if (typeof data.strErrMsg !== 'undefined') {
                alert(data.strErrMsg);
                return false;
            }

            AlarmONDisplayList.value = [];
            for (let i = 0; i < data.length; i++) {
                let Alarm: any = {};
              
                Alarm.Hour = ("0" + data[i].HOUR).slice(-2);
                Alarm.Minute = ("0" + data[i].MINUTE).slice(-2);
                Alarm.State = data[i].TF;
                Alarm.Memo = data[i].MEMO;

                let WeekofDay = [];
               
                if (data[i].SUN == "TRUE") { WeekofDay.push("日") }
                if (data[i].MON == "TRUE") { WeekofDay.push("月") }
                if (data[i].TUE == "TRUE") { WeekofDay.push("火") }
                if (data[i].WED == "TRUE") { WeekofDay.push("水") }
                if (data[i].THU == "TRUE") { WeekofDay.push("木") }
                if (data[i].FRI == "TRUE") { WeekofDay.push("金") }
                if (data[i].SAT == "TRUE") { WeekofDay.push("土") }

                Alarm.Day = WeekofDay.toString();

                AlarmONDisplayList.value.push(Alarm);
            }

        }).catch(err => {

            alert("読み込み失敗");
        });
    };
    GetAlarmDate();





    export default defineComponent({
        props: {
            RoomName: String,
            UserName: String,
        },

        components: {
            Alarm_Set,
           // SettingRist_Body,
        },

        setup(props) {

            //目標照度値表示
            let Next_Time = ref(2500);


            let State_rist = ref(
                {
                    //現在の天気表示
                    Rainy: false,
                    Cloudy: false,
                    Sunny: false,
                    Snow: false,


                }
            );

            let State_of_Wind_Direction = ref(
                {
                    //現在の風向き
                    North: false,
                    South: false,
                    East: false,
                    West: false,
                    North_East: false,
                    South_West: false,
                    South_East: false,
                    North_West: false,
                }
            );

            let State_of_roll_curtein101 = ref(
                {
                    //シャッターの状態101/102
                    open: false,
                    close: false,
                }
            );

            let State_of_roll_curtein102 = ref(
                {
                    //シャッターの状態101/102
                    open: false,
                    close: false,
                }
            );


            let State_of_roll_curtein103_1 = ref(
                {
                    //シャッターの状態　103
                    open: false,
                    close: false,
                }
            );

            let State_of_roll_curtein103_2 = ref(
                {
                    //シャッターの状態　103
                    open: false,
                    close: false,
                }
            );

            let State_of_roll_curtein201_1 = ref(
                {
                    //シャッターの状態　201
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curtein201_2 = ref(
                {
                    //シャッターの状態　201
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curtein202 = ref(
                {
                    //シャッターの状態　202
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curtein203_1 = ref(
                {
                    //シャッターの状態　203
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curtein203_2 = ref(
                {
                    //シャッターの状態　203
                    open: false,
                    close: false,
                    half_open: false,
                }
            );


            let State_of_roll_curteinS = ref(
                {
                    //共有スペースカーテンの状態
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curteinShare1 = ref(
                {
                    //共有スペースカーテンの状態
                    open: false,
                    close: false,
                    half_open: false,
                }
            );

            let State_of_roll_curteinShare2 = ref(
                {
                    //共有スペースカーテンの状態
                    open: false,
                    close: false,
                    half_open: false,
                }
            );


            let State_of_window = ref(
                {
                    //窓の状態
                    open: false,
                    close: false,
                    non: false,
                }
            );


            let State_of_key = ref(
                {
                    //Shareの鍵の状態
                    open: false,
                    close: false,
                }
            );

            //おはようおやすみぼたん表示/非表示
            let is_enable_botton = ref(
                {
                    notShare: true,
                    Share: false,
                }
            );

            //LTATのONを見る
            let State_of_ATauto = ref(
                {
                    on: false,
                    off: false,
                }
            );

            let displayModal_Alarm = ref(null);
            let displayModal_Address = ref(null);
            //以下文はクリックするのに必要0717
            let globalVariable = ref(inject('myGlobalVariable'));
            let listMessage = ref({});
            let Syoudo = ref("");
            let LightLevel = ref({});
   

            //サンフレムの天気情報を取得
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage1();
                },
                { deep: true }
            )

            const listMessage1 = (): void => {

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = listMessage.value[i].VALUE;



                    if (room == "Other") {


                        if (func == "WT") {


                            if (name == "Weather") {



                                switch (value) {
                                    case "0":
                                        State_rist.value.Rainy = false;
                                        State_rist.value.Cloudy = true;
                                        State_rist.value.Sunny = false;
                                        break;

                                    case "1":
                                        State_rist.value.Rainy = true;
                                        State_rist.value.Cloudy = true;
                                        State_rist.value.Sunny = false;
                                        break;

                                    case "2":
                                        State_rist.value.Rainy = false;
                                        State_rist.value.Cloudy = false;
                                        State_rist.value.Sunny = true;
                                        break;
                                }
                            }
                        }
                    }
                }
            };

            //風速
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage2();
                },
                { deep: true }
            )

            const listMessage2 = (): void => {

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = listMessage.value[i].VALUE;



                    if (room == "Other") {


                        if (func == "WT") {


                            if (name == "WindS") {


                                Wind_Speed.value = value;

                            }
                            if (name == "WindDirection") {


                                Wind_direction.value = value;

                                switch (value) {
                                    case "0":
                                        State_of_Wind_Direction.value.North = true;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "1":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = true;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "2":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = true;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "3":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = true;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "4":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = true;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "5":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = true;
                                        break;

                                    case "6":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = true;
                                        State_of_Wind_Direction.value.North_East = false;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;

                                    case "7":
                                        State_of_Wind_Direction.value.North = false;
                                        State_of_Wind_Direction.value.South = false;
                                        State_of_Wind_Direction.value.East = false;
                                        State_of_Wind_Direction.value.West = false;
                                        State_of_Wind_Direction.value.North_East = true;
                                        State_of_Wind_Direction.value.North_West = false;
                                        State_of_Wind_Direction.value.South_East = false;
                                        State_of_Wind_Direction.value.South_West = false;
                                        break;
                                }
                            }
                            if (name == "Temp") {

                                temp_out.value = value;
                            }
                        }
                    }
                }
            };

            //シャッター開閉状態 101/102/103
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage10();
                },
                { deep: true }
            )


            const listMessage10 = (): void => {

                let MT_Count101 = 0;
                let MT_Count102 = 0;
                let MT_CountS0 = 0;


                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除
                    
                    if (func == "ST") {
                        if (action == "Height") {
                            switch (globalVariable.value.RoomName) {
                                case "R101":
                                    
                                    MT_Count101 += value;
                                    if (MT_Count101 < 1) {
                                        State_of_roll_curtein101.value.open = false;
                                        State_of_roll_curtein101.value.close = true;
                                    } else if (MT_Count101 >= 1) {
                                        State_of_roll_curtein101.value.open = true;
                                        State_of_roll_curtein101.value.close = false;
                                    }

                                    if (name !== "6") {
                                        if (name !== "7") {
                                            if (MT_CountS0 >= 1) {
                                                State_of_roll_curteinS.value.open = true;
                                                State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                            } else {
                                                State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                State_of_roll_curteinS.value.close = true;
                                            }
                                            break;
                                        }
                                    }

                                    State_of_roll_curtein102.value.open = false;
                                    State_of_roll_curtein102.value.close = false;
                                    State_of_roll_curtein103_1.value.open = false;
                                    State_of_roll_curtein103_1.value.close = false;
                                    State_of_roll_curtein103_2.value.open = false;
                                    State_of_roll_curtein103_2.value.close = false;
                                    break;

                                case "R102":
                                    
                                    MT_Count101 += value;
                                    if (MT_Count101 < 1) {
                                        State_of_roll_curtein102.value.open = false;
                                        State_of_roll_curtein102.value.close = true;
                                    } else if (MT_Count101 >= 1) {
                                        State_of_roll_curtein102.value.open = true;
                                        State_of_roll_curtein102.value.close = false;
                                    }

                                    if (name !== "6") {
                                        if (name !== "7") {
                                            if (MT_CountS0 >= 1) {
                                                State_of_roll_curteinS.value.open = true;
                                                State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                            } else {
                                                State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                State_of_roll_curteinS.value.close = true;
                                            }
                                            break;
                                        }
                                    }

                                    State_of_roll_curtein101.value.open = false;
                                    State_of_roll_curtein101.value.close = false;
                                    State_of_roll_curtein103_1.value.open = false;
                                    State_of_roll_curtein103_1.value.close = false;
                                    State_of_roll_curtein103_2.value.open = false;
                                    State_of_roll_curtein103_2.value.close = false;
                                    break;

                                case "R103":
                                    if (name == "3") {
                                        
                                        MT_Count101 += value;
                                        if (MT_Count101 < 1) {
                                            State_of_roll_curtein103_1.value.open = false;
                                            State_of_roll_curtein103_1.value.close = true;
                                        } else if (MT_Count101 >= 1) {
                                            State_of_roll_curtein103_1.value.open = true;
                                            State_of_roll_curtein103_1.value.close = false;
                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein101.value.open = false;
                                        State_of_roll_curtein101.value.close = false;
                                        State_of_roll_curtein102.value.open = false;
                                        State_of_roll_curtein102.value.close = false;
                                        break;
                                    }

                                 case"R103":
                                    if (name == "4") {
                                        
                                        MT_Count102 += value;
                                        if (MT_Count102 < 1) {
                                            State_of_roll_curtein103_2.value.open = false;
                                            State_of_roll_curtein103_2.value.close = true;
                                        } else if (MT_Count102 >= 1) {
                                            State_of_roll_curtein103_2.value.open = true;
                                            State_of_roll_curtein103_2.value.close = false;
                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein101.value.open = false;
                                        State_of_roll_curtein101.value.close = false;
                                        State_of_roll_curtein102.value.open = false;
                                        State_of_roll_curtein102.value.close = false;
                                        break;
                                    }
                            }
                        }
                    }
                }
            };


            //ロールカーテン表示201-203
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage12();
                },
                { deep: true }
            )


            const listMessage12 = (): void => {

                let MT_Count201 = 0;
                let MT_Count202 = 0;
                let MT_Count203 = 0;
                let MT_Count204 = 0;
                let MT_Count205 = 0;
                let MT_CountS1 = 0;
                let MT_CountS2 = 0;
                let MT_CountS0 = 0;

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除

                    if (func == "RC") {
                        if (action == "Height") {
                            switch (globalVariable.value.RoomName) {
                                case "R201":
                                    if (name == "1") {
                                       
                                        MT_Count201 += value;
                                        if (MT_Count201 < 1) {
                                            State_of_roll_curtein201_1.value.open = false;
                                            State_of_roll_curtein201_1.value.close = true;
                                            State_of_roll_curtein201_1.value.half_open = false;
                                        } else if (MT_Count201 == 1) {
                                            State_of_roll_curtein201_1.value.open = false;
                                            State_of_roll_curtein201_1.value.close = false;
                                            State_of_roll_curtein201_1.value.half_open = true;

                                        } else if (MT_Count201 > 1) {
                                            State_of_roll_curtein201_1.value.open = true;
                                            State_of_roll_curtein201_1.value.close = false;
                                            State_of_roll_curtein201_1.value.half_open = false;

                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein202.value.open = false;
                                        State_of_roll_curtein202.value.half_open = false;
                                        State_of_roll_curtein202.value.close = false;
                                        State_of_roll_curtein203_1.value.open = false;
                                        State_of_roll_curtein203_1.value.half_open = false;
                                        State_of_roll_curtein203_1.value.close = false;
                                        State_of_roll_curtein203_2.value.open = false;
                                        State_of_roll_curtein203_2.value.half_open = false;
                                        State_of_roll_curtein203_2.value.close = false;
                                        break;
                                    }
                                    
                                    if (name == "2") {
                                        
                                        MT_Count202 += value;
                                        if (MT_Count202 < 1) {
                                            State_of_roll_curtein201_2.value.open = false;
                                            State_of_roll_curtein201_2.value.close = true;
                                            State_of_roll_curtein201_2.value.half_open = false;

                                        } else if (MT_Count202 == 1) {
                                            State_of_roll_curtein201_2.value.open = false;
                                            State_of_roll_curtein201_2.value.close = false;
                                            State_of_roll_curtein201_2.value.half_open = true;

                                        } else if (MT_Count202 > 1) {
                                            State_of_roll_curtein201_2.value.open = true;
                                            State_of_roll_curtein201_2.value.close = false;
                                            State_of_roll_curtein201_2.value.half_open = false;
                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein202.value.open = false;
                                        State_of_roll_curtein202.value.half_open = false;
                                        State_of_roll_curtein202.value.close = false;
                                        State_of_roll_curtein203_1.value.open = false;
                                        State_of_roll_curtein203_1.value.half_open = false;
                                        State_of_roll_curtein203_1.value.close = false;
                                        State_of_roll_curtein203_2.value.open = false;
                                        State_of_roll_curtein203_2.value.half_open = false;
                                        State_of_roll_curtein203_2.value.close = false;
                                        break;
                                    }
                                    break;

                                case "R202":
                                    if (name == "3") {
                                        MT_Count203 += value;
                                        if (MT_Count203 < 1) {
                                            State_of_roll_curtein202.value.open = false;
                                            State_of_roll_curtein202.value.close = true;
                                            State_of_roll_curtein202.value.half_open = false;


                                        } else if (MT_Count203 == 1) {
                                            State_of_roll_curtein202.value.open = false;
                                            State_of_roll_curtein202.value.close = false;
                                            State_of_roll_curtein202.value.half_open = true;


                                        } else if (MT_Count203 > 1) {
                                            State_of_roll_curtein202.value.open = true;
                                            State_of_roll_curtein202.value.close = false;
                                            State_of_roll_curtein202.value.half_open = false;


                                        }
                                    }

                                    if (name !== "6") {
                                        if (name !== "7") {
                                            if (MT_CountS0 >= 1) {
                                                State_of_roll_curteinS.value.open = true;
                                                State_of_roll_curteinS.value.close = false;

                                            } else {
                                                State_of_roll_curteinS.value.open = false;
                                                State_of_roll_curteinS.value.close = true;

                                            }
                                            break;
                                        }
                                    }

                                    State_of_roll_curtein201_1.value.open = false;
                                    State_of_roll_curtein201_1.value.half_open = false;
                                    State_of_roll_curtein201_1.value.close = false;
                                    State_of_roll_curtein201_2.value.open = false;
                                    State_of_roll_curtein201_2.value.half_open = false;
                                    State_of_roll_curtein201_2.value.close = false;
                                    State_of_roll_curtein203_1.value.open = false;
                                    State_of_roll_curtein203_1.value.half_open = false;
                                    State_of_roll_curtein203_1.value.close = false;
                                    State_of_roll_curtein203_2.value.open = false;
                                    State_of_roll_curtein203_2.value.half_open = false;
                                    State_of_roll_curtein203_2.value.close = false;
                                    break;

                                case "R203":
                                    if (name == "4") {
                                       
                                        MT_Count204 += value;
                                        if (MT_Count204 < 1) {
                                            State_of_roll_curtein203_1.value.open = false;
                                            State_of_roll_curtein203_1.value.close = true;
                                            State_of_roll_curtein203_1.value.half_open = false;
                                        } else if (MT_Count204 == 1) {
                                            State_of_roll_curtein203_1.value.open = false;
                                            State_of_roll_curtein203_1.value.close = false;
                                            State_of_roll_curtein203_1.value.half_open = true;
                                        } else if (MT_Count204 > 1) {
                                            State_of_roll_curtein203_1.value.open = true;
                                            State_of_roll_curtein203_1.value.close = false;
                                            State_of_roll_curtein203_1.value.half_open = false;
                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein201_1.value.open = false;
                                        State_of_roll_curtein201_1.value.half_open = false;
                                        State_of_roll_curtein201_1.value.close = false;
                                        State_of_roll_curtein201_2.value.open = false;
                                        State_of_roll_curtein201_2.value.half_open = false;
                                        State_of_roll_curtein201_2.value.close = false;
                                        State_of_roll_curtein202.value.open = false;
                                        State_of_roll_curtein202.value.half_open = false;
                                        State_of_roll_curtein202.value.close = false;
                                        break;
                                    }

                                    if (name == "5") {
                                        
                                        MT_Count205 += value;
                                        if (MT_Count205 < 1) {
                                            State_of_roll_curtein203_2.value.open = false;
                                            State_of_roll_curtein203_2.value.close = true;
                                            State_of_roll_curtein203_2.value.half_open = false;
                                        } else if (MT_Count205 == 1) {
                                            State_of_roll_curtein203_2.value.open = false;
                                            State_of_roll_curtein203_2.value.close = false;
                                            State_of_roll_curtein203_2.value.half_open = true;
                                        } else if (MT_Count205 > 1) {
                                            State_of_roll_curtein203_2.value.open = true;
                                            State_of_roll_curtein203_2.value.close = false;
                                            State_of_roll_curtein203_2.value.half_open = false;
                                        }

                                        if (name !== "6") {
                                            if (name !== "7") {
                                                if (MT_CountS0 >= 1) {
                                                    State_of_roll_curteinS.value.open = true;
                                                    State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                                } else {
                                                    State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                    State_of_roll_curteinS.value.close = true;
                                                }
                                                break;
                                            }
                                        }

                                        State_of_roll_curtein201_1.value.open = false;
                                        State_of_roll_curtein201_1.value.half_open = false;
                                        State_of_roll_curtein201_1.value.close = false;
                                        State_of_roll_curtein201_2.value.open = false;
                                        State_of_roll_curtein201_2.value.half_open = false;
                                        State_of_roll_curtein201_2.value.close = false;
                                        State_of_roll_curtein202.value.open = false;
                                        State_of_roll_curtein202.value.half_open = false;
                                        State_of_roll_curtein202.value.close = false;
                                        break;
                                    }


                            }
                        }
                    }
                }
            };

            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage15();
                },
                { deep: true }
            )


            const listMessage15 = (): void => {

                let MT_CountS1 = 0;
                let MT_CountS2 = 0;
                let MT_CountS0 = 0;

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除

                    if (func == "RC") {
                        if (action == "Height") {
                            switch (globalVariable.value.RoomName) {

                                case "Share":
                                    MT_CountS0 += value;

                                    if (name == "6") {
                                        State_of_roll_curteinS.value.open = false;
                                        State_of_roll_curteinS.value.close = false;
                                        State_of_roll_curteinS.value.half_open = false;


                                        MT_CountS1 += value;
                                        if (MT_CountS1 < 1) {
                                            State_of_roll_curteinShare1.value.open = false;
                                            State_of_roll_curteinShare1.value.close = true;
                                            State_of_roll_curteinShare1.value.half_open = false;

                                        } else if (MT_CountS1 == 1) {
                                            State_of_roll_curteinShare1.value.open = false;
                                            State_of_roll_curteinShare1.value.close = false;
                                            State_of_roll_curteinShare1.value.half_open = true;

                                        } else if (MT_CountS1 > 1) {
                                            State_of_roll_curteinShare1.value.open = true;
                                            State_of_roll_curteinShare1.value.close = false;
                                            State_of_roll_curteinShare1.value.half_open = false;
                                        }
                                    }

                                    if (name == "7") {
                                        State_of_roll_curteinS.value.open = false;
                                        State_of_roll_curteinS.value.close = false;
                                        State_of_roll_curteinS.value.half_open = false;

                                        MT_CountS2 += value;
                                        if (MT_CountS2 < 1) {
                                            State_of_roll_curteinShare2.value.open = false;
                                            State_of_roll_curteinShare2.value.close = true;
                                            State_of_roll_curteinShare2.value.half_open = false;
                                        } else if (MT_CountS2 == 1) {
                                            State_of_roll_curteinShare2.value.open = false;
                                            State_of_roll_curteinShare2.value.close = false;
                                            State_of_roll_curteinShare2.value.half_open = true;
                                        } else if (MT_CountS2 > 1) {
                                            State_of_roll_curteinShare2.value.open = true;
                                            State_of_roll_curteinShare2.value.close = false;
                                            State_of_roll_curteinShare2.value.half_open = false;
                                        }
                                        State_of_roll_curteinS.value.open = false;
                                        State_of_roll_curteinS.value.close = false;
                                        State_of_roll_curteinS.value.half_open = false;
                                        break;
                                    }

                                    if (name !== "6") {
                                        if (name !== "7") {
                                            if (MT_CountS0 >= 1) {
                                                State_of_roll_curteinS.value.open = true;
                                                State_of_roll_curteinS.value.close = false; // 追加：1以上の場合はcloseをfalseに
                                            } else {
                                                State_of_roll_curteinS.value.open = false; // 追加：1未満の場合はopenをfalseにする
                                                State_of_roll_curteinS.value.close = true;
                                            }
                                            break;
                                        }
                                    }

                            }
                        }
                    }
                }
            };


            ////照度目標値　仮アドレス：12290 使ってない
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage4();
                },
                { deep: true }
            )

            const listMessage4 = (): void => {

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = listMessage.value[i].VALUE;



                    if (room == globalVariable.value.RoomName) {


                        if (func.startsWith("LT")) {


                            if (name.startsWith("Indirect")) {

                                Target_LL.value = value;

                                if (action.startsWith("OFF")) {

                                    Target_LL.value = value;
                                }
                            }
                        }
                    }
                }
            };




            //照明色　アドレス：15291

            const initialColorTemperature = 0;
            let colorTemperature = initialColorTemperature;

            const getColor = (temperature) => {
                if (temperature >= 2 && temperature <= 3499) {
                    return '#d2691e'; // チョコレート色
                } else if (temperature >= 3500 && temperature <= 4999) {
                    return '#f4a460'; // オレンジ
                } else if (temperature >= 5000 && temperature <= 5999) {
                    return '#afeeee'; // 青白
                } else if (temperature >= 0 && temperature <= 1){
                    return 'lightgray'; // ライトグレー
                }
            };
            const getColorLabel = (temperature) => {
                if (temperature >= 0 && temperature <= 1) {
                    return 'OFF';
                } else {
                    return temperature + ' K';
                }
            };

            watch(listMessage, (newVal, oldVal) => {
                listMessage5();
            }, { deep: true });

            const listMessage5 = () => {
                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = listMessage.value[i].VALUE;

                    if (room == globalVariable.value.RoomName) {
                        if (func.startsWith("LT")) {
                            if (name.startsWith("Main")) {
                                if (action.startsWith("Tone")) {
                                    color_temperature.value = value;
                                }
                            }
                        }
                        if (name == "F1Share") {
                            color_temperature.value = value;
                        }
                    }
                }
            };






            //窓状況　アドレス：1534
            const listMessageWatcher = (newVal, oldVal) => {
                if (!State_of_window.value.non) { // もしくは非表示の判定に使用しているプロパティを指定
                    if (Array.isArray(listMessage.value) && listMessage.value.some(item => item.ROOM === "Share")) {
                        // "Share"の場合は処理をスキップ
                        return;
                    }

                    listMessage6();
                }
            };

            // watchをセットアップする
            const setupWatcher = () => {
                watch(() => listMessage.value, listMessageWatcher, { deep: true });
            };

            // watchを開始
            setupWatcher();

            const listMessage6 = () => {
               
                let MT_Count1 = 0;

                let flag = 0;

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除

                    // 以下のように条件をグループごとに判定
                    //ROOMがShareの場合に窓の開閉情報を表示しないための処理
                    //if文では、ROOMの値がShare以外の時に、MT_Count1 += valueの処理を実行。
                    //それ以外(ROOM=Share)では、flag=1を実行し、open,closeどちらもfalseにしている。
                    if (name.startsWith("WD")) {
                        if (func == "EN") {
                            if (action == "State") {
                                switch (globalVariable.value.RoomName) {
                                    case "R101":
                                        MT_Count1 += value;
                                        break;
                                    case "R102":
                                        MT_Count1 += value;
                                        break;
                                    case "R103":
                                        MT_Count1 += value;
                                        break;
                                    case "R201":
                                        MT_Count1 += value;
                                        break;
                                    case "R202":
                                        MT_Count1 += value;
                                        break;
                                    case "R203":
                                        MT_Count1 += value;
                                        break;
                                    case "Share":
                                        flag = 1;
                                        break;
                                }
                            }
                        }
                    }
                }

                // ここで表示したいことを記載
                if (flag == 1) {
                    State_of_window.value.open = false;
                    State_of_window.value.close = false;
                } else {
                    if (MT_Count1 < 1) {
                        State_of_window.value.open = false; // 追加：1未満の場合はopenをfalseにする
                        State_of_window.value.close = true;
                    } else if (MT_Count1 >= 1) {
                        State_of_window.value.open = true;
                        State_of_window.value.close = false; // 追加：1以上の場合はcloseをfalseにする
                    }
                }
            };


            //部屋室内温度(エアコンからの温度)　アドレス：15305
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage7();
                },
                { deep: true }
            )

            const listMessage7 = (): void => {

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = listMessage.value[i].VALUE;

                    if (room == globalVariable.value.RoomName) {


                        if (func.startsWith("AC")) {


                            if (name.startsWith("TempReference")) {

                                temp_room.value = value;

                                if (action.startsWith("State")) {

                                    temp_room.value = value;
                                }
                            }
                        }
                    }
                }
            };




            //共有スペース用鍵情報表示
            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                   listMessage9();
                },
                { deep: true }
            )


            const listMessage9 = (): void => {
            
                let MT_Count1 = 0;
                let flag = 0;

                
                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除

                    if (name.startsWith("Terrace")) {
                        if (func == "KEY") {
                            if (action == "State") {
                                switch (globalVariable.value.RoomName) {
                                    case "R101":
                                        MT_Count1 += value;
                                        break;
                                    case "R102":
                                        MT_Count1 += value;
                                        break;
                                    case "R103":
                                        MT_Count1 += value;
                                        break;
                                    case "R201":
                                        MT_Count1 += value;
                                        break;
                                    case "R202":
                                        MT_Count1 += value;
                                        break;
                                    case "R203":
                                        MT_Count1 += value;
                                        break;
                                    case "Share":
                                        MT_Count1 += value;
                                        flag = 1;
                                        break;
                                }
                            }
                        }
                    }
                
                }

                // ここで表示したいことを記載
                if (flag == 1) {
                    if (MT_Count1 >= 1) {
                        State_of_key.value.open = true;
                        State_of_key.value.close = false; // 追加：1以上の場合はcloseをfalseにする
                    } else if (MT_Count1 < 1) {
                        State_of_key.value.open = false; // 追加：1未満の場合はopenをfalseにする
                        State_of_key.value.close = true;
                    }
                } else {
                        State_of_key.value.open = false;
                        State_of_key.value.close = false; // 追加：1以上の場合はcloseをfalseにする
                }
            };
                    

            //is_enable_bottom
            //おはよう、おやすみボタンの表示・非表示の記述
            //roomがshareなら非表示・roomがshare以外なら表示
            watch(
                () => globalVariable.value.RoomName,
                (newVal, oldVal) => {
                    if (globalVariable.value.currentPage == "info") {
                        isEnableBotton();
                    }
                },
                { deep: true }
            )

            const isEnableBotton = (): void => {
                switch (globalVariable.value.RoomName) {
                    case "R101":
                    case "R102":
                    case "R103":
                    case "R201":
                    case "R202":
                    case "R203":
                        is_enable_botton.value.notShare = true;
                        is_enable_botton.value.Share = false;
                        break;
                    case "Share":
                        is_enable_botton.value.notShare = false;
                        is_enable_botton.value.Share = true;
                        break;
                }
            };


            //目標照度
            let SettingLightLevel_Array = ref([]);
            let NowBrightValue = ref({}); //書き足した0807
            let tmptime: any;　//書き足したけどコードじたいに意味はない



            watch(
                () => listMessage.value,
                (newVal, oldVal) => {

                    listMessage20();
                },
                { deep: true }
            )

            const listMessage20 = (): void => {
                debugger;
                let MT_Count3 = 0;

                for (let i in listMessage.value) {
                    let room = listMessage.value[i].ROOM;
                    let func = listMessage.value[i].FUNC;
                    let name = listMessage.value[i].NAME;
                    let action = listMessage.value[i].ACTION;
                    let value = Number(listMessage.value[i].VALUE); // Numberで文字列解除

                    if (func == "LTAT") {
                        if (action == "State") {
                            if (room == globalVariable.value.RoomName) {
                                switch (name) {
                                    case "Living":
                                        MT_Count3 += value;
                                        break;
                                    case "Share":
                                        MT_Count3 += value;
                                        break;
                                    case "WK":
                                        MT_Count3 += value;
                                        break;
                                }
                            }
                        }
                    }
                }



                // ここで表示したいことを記載
                if (MT_Count3 >= 1) {
                    State_of_ATauto.value.on = true;
                    State_of_ATauto.value.off = false; // 追加：1以上の場合はoffをfalseにする
                } else if (MT_Count3 < 1) {
                    State_of_ATauto.value.on = false; // 追加：1未満の場合はonをfalseにする
                    State_of_ATauto.value.off = true;
                }
                debugger;
                GetLightLevel();
            };
            



            const GetLightLevel = (): void => {
                debugger;
                Axios({
                    method: 'GET',
                    url: 'api/MaCo/GetSetting',
                    params: {
                        room: globalVariable.value.RoomName,
                        //room: "R101",
                        func: "SET",
                        name: "LIKE 'LTAT%'",

                    }
                    

                }).then((res) => {
                    let data: any = res.data;
                    
                    SettingLightLevel_Array.value = [];
                    //[{number:1},{number:2}~{number:5}]のような配列を作成
                    for (let i = 1; i < 6; i++) {
                        let SettingLightLevel_SequenceArray: any = {};
                        SettingLightLevel_SequenceArray.number = i;
                        SettingLightLevel_Array.value.push(SettingLightLevel_SequenceArray);
                        tmptime = "route10";
                    }

                    //dataからHour・Minute・burightの値を取得しSettingLightLevel_Arrayに追加
                    for (let ii in data) {
                        //HourのValue取得
                        if (data[ii].NAME.includes("Hour")) {
                            let number = data[ii].NAME.slice(-1);
                            for (let SLA in SettingLightLevel_Array.value) {
                                if (number == SettingLightLevel_Array.value[SLA].number) {
                                    SettingLightLevel_Array.value[SLA].Hour = data[ii].VALUE;
                                }
                            }
                        }
                        else if (data[ii].NAME.includes("Minute"))//MinuteのValue取得
                        {
                            let number = data[ii].NAME.slice(-1);
                            for (let SLA in SettingLightLevel_Array.value) {
                                if (number == SettingLightLevel_Array.value[SLA].number) {
                                    SettingLightLevel_Array.value[SLA].Minute = data[ii].VALUE;
                                }
                            }
                        }
                        else if (data[ii].NAME.includes("Bright"))  //BrightのValue取得
                        {
                            let number = data[ii].NAME.slice(-1);
                            for (let SLA in SettingLightLevel_Array.value) {
                                if (number == SettingLightLevel_Array.value[SLA].number) {
                                    SettingLightLevel_Array.value[SLA].Bright = data[ii].VALUE;
                                }
                            }
                        }
                        else  //ATのValue取得
                        {
                            let number = data[ii].NAME.slice(-1);
                            for (let SLA in SettingLightLevel_Array.value) {
                                if (number == SettingLightLevel_Array.value[SLA].number) {
                                    SettingLightLevel_Array.value[SLA].ATState = data[ii].VALUE;
                                }
                            }
                        }

                    }
                    //SettingLightLevel_Array内の連想配列にTimeを追加
                    for (let SLA in SettingLightLevel_Array.value) {
                        SettingLightLevel_Array.value[SLA].Time = SettingLightLevel_Array.value[SLA].Hour.toString() + SettingLightLevel_Array.value[SLA].Minute.toString();
                    }
                    //LightLevel_Check呼び出し
                    LightLevel_Check();

                }).catch(err => {

                    alert("読み込み失敗");
                });
            };

            //Info画面が表示された時に目標照度値読み出し
            watch(
                () => globalVariable.value.currentPage,
                (newVal, oldVal) => {
                    if (globalVariable.value.currentPage == "info") {
                        GetLightLevel();
                    }
                },
                { deep: true }
            )

            watch(
                () => globalVariable.value.RoomName,
                (newVal, oldVal) => {
                    if (globalVariable.value.currentPage == "info") {
                        GetLightLevel();
                    }
                },
                { deep: true }
            )



            //SettingLightLevel_Arrayから目標照度値をチェックする
            const LightLevel_Check = (): void => {
                //今の時間を取得
                let datetime = DateTime(new Date());
                //現在時刻を3～4桁の数字にする
                let NowTime = datetime.hour + datetime.minute;
                //tmptime.value = NowTime;

                Next_Time.value = 2500;//上書きのため　初期値

                let ATState_Counter = 0;
                let Min_Obj = 0;
                let Max_Time = 0;
                let mintime = 2500;
                

                for (let i in SettingLightLevel_Array.value) {
                    //有効になっている設定分のみ以下の処理に進む
                    if (Number(SettingLightLevel_Array.value[i].ATState) == 1) {
                       
                        ATState_Counter += Number(SettingLightLevel_Array.value[i].ATState);
                        //現在時刻より前に動いたAT設定をさがす　一個前の処理を取っている
                        if (NowTime >= Number(SettingLightLevel_Array.value[i].Time)) {
                           
                            if (Min_Obj < Number(SettingLightLevel_Array.value[i].Time)) {

                                //最終値が現在時刻より前の設定の中で最大値(現在時刻に最も近い値)になるよう上書きを繰り返す
                                NowBrightValue.value = SettingLightLevel_Array.value[i].Bright;
                                Min_Obj = Number(SettingLightLevel_Array.value[i].Time);
                            }
                        }
                        //NextTimeの値を取るためのif文　0807追加
                        if (NowTime < Number(SettingLightLevel_Array.value[i].Time)) {
                            
                            
                            if (Next_Time.value > Number(SettingLightLevel_Array.value[i].Time)) {
                                Next_Time.value = Number(SettingLightLevel_Array.value[i].Time)
                               
                            }
                        }
                    }
                }


                //上記全部該当しなかった時　一回も上書きしなかった時、かつ有効分(AUTO/ON)の情報を取る時
                if (Next_Time.value == 2500){
                    
                    for (let i in SettingLightLevel_Array.value) {
                        if (mintime > Number(SettingLightLevel_Array.value[i].Time) && Number(SettingLightLevel_Array.value[i].ATState)  == 1) {
                            mintime = Number(SettingLightLevel_Array.value[i].Time)


                        }

                    }
                Next_Time.value = mintime;//最小値

                 }


                //有効になっている設定が一つもないとき(AT無効状態)NowBrightValueに"-"を表示
                if (ATState_Counter == 0) {
                    NowBrightValue.value = "-"
                    tmptime = "route5";
                } else if (Min_Obj == 0)//ATは有効だが現在値よりも小さい時間の物がないとき(最後に動いた設定が昨日の値の時)有効AT設定の最大値をNowBrightValueに表示
                {
                    for (let i in SettingLightLevel_Array.value) {
                       
                        tmptime = "route6";
                        if (Number(SettingLightLevel_Array.value[i].ATState) == 1) {
                            tmptime = "route7";
                            if (Max_Time < SettingLightLevel_Array.value[i].Time) {
                                tmptime = "route8";
                                Max_Time = SettingLightLevel_Array.value[i].Time;
                                NowBrightValue.value = SettingLightLevel_Array.value[i].Bright;
                            }
                        }
                    }
                }
            }







            //日時用変数
            let Hiduke = ref(null);
            let Zikan = ref(null);
            let Heikin = ref(0);
            let Youbi = ref("");
            let Nen = ref("");
            let byou = ref(0);
            let Zikan2 = ref(null);


            //20230524///////////////////////////////////////////
            let HidukeTomorrow = ref(null)
            let HidukeDayAfterTomorrow = ref(null)
            let YoubiTomorrow = ref("")
            let YoubiDayAfterTomorrow = ref("")
            //20230524-end///////////////////////////////////////

            //住所表示Modal用変数
            let displayModalAllOffError = ref(null);

            //環境表示用変数
            let Wind_Speed = ref("");
            let Wind_direction = ref("");
            let RC_Auto = ref("");
            let Target_LL = ref("");
            let temp_out = ref("");
            let temp_room = ref("");
            let temp_humidity = ref("");
            let light_color = ref("");
            let color_temperature = ref();
            let old_color_temperature = ref();


            //チャット表示用変数
            let Chat = ref();
            let ChatSendMessage = ref()

            //表示用時間更新頻度
            onMounted(() => {
                Show();
                setInterval(Show, 10000);
            })

            //日付時間表示
            const Show = (): void => {
                //日付取得(util.tsの便利な処理を呼び出して処理をおねがいする)
                let datetime = DateTime(new Date());

                /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                //let tomorrowDate = new Date(datetime.year, datetime.month - 1, datetime.day + 1); //datetime.day + 1したら、8/10になる。
                //datetime.month , datetime.day の値は、一桁月または、日の場合、06のように必ず、二桁で表されるので、parseInt()関数でintとして、Date()関数に渡している。
                let tomorrowDate = new Date(datetime.year, parseInt(datetime.month) - 1, parseInt(datetime.day) + 1);
                let datetimeTomorrow = DateTime(tomorrowDate);
                let dayAfterTomorrowDate = new Date(datetime.year, parseInt(datetime.month) - 1, parseInt(datetime.day) + 2);
                let datetimeDayAfterTomorrow = DateTime(dayAfterTomorrowDate);
                ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                //曜日変換用配列
                let days = ["(日)", "(月)", "(火)", "(水)", "(木)", "(金)", "(土)"];
                //日付表示

                Nen.value = datetime.year;
                Hiduke.value = datetime.month + "/" + datetime.day;
                Zikan.value = datetime.hour + ":" + datetime.minute;
                Youbi.value = days[datetime.weeknumber];
                byou.value = datetime.time;
                Zikan2.value = datetime.hour +  datetime.minute;

                ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                //2,3日後の日付
                HidukeTomorrow.value = datetimeTomorrow.month + "/" + datetimeTomorrow.day;
                HidukeDayAfterTomorrow.value = datetimeDayAfterTomorrow.month + "/" + datetimeDayAfterTomorrow.day;
                YoubiTomorrow.value = days[datetimeTomorrow.weeknumber];
                YoubiDayAfterTomorrow.value = days[datetimeDayAfterTomorrow.weeknumber];
                ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
                
                if (Number(Zikan2.value) == Next_Time.value) {
              
                    GetLightLevel();
                }
            }

            ////SignalR使う宣言
            //var connection = new signalR.HubConnectionBuilder()
            //    //.withUrl('http://192.168.10.43:38077/signalr')
            //    .withUrl((<HTMLInputElement>document.getElementById("SignalR_URL")).value)
            //    .withAutomaticReconnect()
            //    .build();

            //// Transport fallback functionality is now built into start.
            //connection.start()
            //        console.log('connection started');
            //    })
            //    .then(() => {

            //    .catch(error => {
            //        console.error(error.message);
            //    });

            ////天気情報取得用SignalRグループ
            //connection.on('ReceiveWeather', (JsonStr) => {
            //    const data = JsonStr;
            //    ReceiveWeather.value = data;
            //    GetWeather(ReceiveWeather.value);
            //});

            ////チャットメッセージ取得用SignalRグループ
            //connection.on('ChatMessageReceive', (Message: string) => {
            //    debugger;
            //    Chat.value = Message;
            //});

            ////チャットメッセージ送信用SignalRグループ
            //const ChatMessageSend = (): void => {
            //    let SendDate = "";
            //    let SendTime = "";
            //    let datetime = DateTime(new Date());
            //    SendDate = datetime.year + "/" + datetime.month + "/" + datetime.day;
            //    SendTime = datetime.hour + ":" + datetime.minute;
            //    connection.invoke("ChatMessageSend", SendDate, SendTime, props.UserName, ChatSendMessage.value).catch(function (err) {
            //        return console.error(err.toString());
            //    });
            //}


            //おはようボタンとおやすみボタン
            const GoodMorning_Click = (): void => {

                let rooomname=globalVariable.value.RoomName;
                //DoWriteAddress(pRoom, pFunc, pName, pAction, pValue) ON/trueをしたい場合pValueに"１"を渡す
                const { result } = DoWriteAddress(rooomname, "SC", "Morning", "ON", "1");

            }

            const Night_Click = (): void => {

                let rooomname = globalVariable.value.RoomName;
                const { result } = DoWriteAddress(rooomname, "SC", "Night", "ON", "1");

            }

           
            //ダイアログOpenClose
            const openModal = (kind) => {
                switch (kind)
                {
                    case "Alarm":
                        displayModal_Alarm.value = true;
                        break;
                    case "Address":
                        displayModal_Address.value = true;
                        break;
                }
            };

            const showModal = (kind) => {
                let elms = document.querySelectorAll(".p-dialog-mask.p-component-overlay.p-component-overlay-enter");
                elms.forEach((elm) => {
                    elm.addEventListener('click', () => {
                        if (event.target !== event.currentTarget) {
                            return;
                        }
                        switch (kind) {
                            case "Alarm":
                                displayModal_Alarm.value = false;
                                break;
                            case "Address":
                                displayModal_Address.value = false;
                                break;
                        }
                    }, false);
                })
            };

            //天気表示用変数
            let ReceiveWeather = ref();
            let Weather = ref([]);

            const GetWeather = (ReceiveWeather): void => {
                Weather.value = ReceiveWeather;
            }
           
            // Transport fallback functionality is now built into start.
            globalVariable.value.connection.start()
                .then(() => {
                    console.log('connection started');
                })
                .catch(error => {
                    console.error(error.message);
                });

            //天気情報取得用SignalRグループ
            globalVariable.value.connection.on('ReceiveWeather', (JsonStr) => {
                const data = JsonStr;
                ReceiveWeather.value = data;
                GetWeather(ReceiveWeather.value);
            })

        
          
            //デバイス状態受取
            globalVariable.value.connection.on('RecieveInfo', (ROOM: string, FUNC: string, NAME: string, ACTION: string, VALUE: string) => {
                const data = { ROOM: ROOM, FUNC: FUNC, NAME: NAME, ACTION: ACTION, VALUE: VALUE };
                listMessage.value[ROOM + ":" + FUNC  + NAME  + ACTION] = data;
            });


            const jump_controllist = (): void => {

                globalVariable.value.currentPage = "settingrist";
            }


            return {
                jump_controllist,
                openModal,
                displayModal_Alarm,
                displayModal_Address,
                showModal,
                globalVariable,
                GetWeather,
                ReceiveWeather,
                Weather,
                listMessage,
                GoodMorning_Click,
                Night_Click,
                isEnableBotton,

                AddComma,
                Zikan,
                Zikan2,
                Hiduke,
                HidukeTomorrow,//明日明後日ようの数値をreturn.
                HidukeDayAfterTomorrow,//明日明後日ようの数値をreturn.
                Heikin,
             //   openModal,
                byou,
                Youbi,
                YoubiTomorrow,//明日明後日ようの数値をreturn.
                YoubiDayAfterTomorrow,//明日明後日ようの数値をreturn.
                Wind_Speed,
                Wind_direction,
                RC_Auto,
                Target_LL,
                temp_out,
                temp_room,
                temp_humidity,
                light_color,
                color_temperature,
                old_color_temperature,
                Nen,
                displayModalAllOffError,
                //ChatMessageSend,
                ChatSendMessage,
                Chat,
                GetAlarmDate,
                AlarmONDisplayList,
                State_rist,
                State_of_Wind_Direction,
                State_of_roll_curtein101,
                State_of_roll_curtein102,
                State_of_roll_curtein103_1,
                State_of_roll_curtein103_2,
                State_of_roll_curtein201_1,
                State_of_roll_curtein201_2,
                State_of_roll_curtein202,
                State_of_roll_curtein203_1,
                State_of_roll_curtein203_2,
                State_of_roll_curteinS,
                State_of_roll_curteinShare1,
                State_of_roll_curteinShare2,
                State_of_window,
                listMessage1,
                getColor,
                Syoudo,
                State_of_key,
                GetLightLevel,
                SettingLightLevel_Array,
                NowBrightValue,
                tmptime,
                Next_Time,
                is_enable_botton,
                State_of_ATauto,
                getColorLabel,
            }
        }
    })
</script>



<style lang="scss" scoped>
    .Button {
        background-color: whitesmoke;
        border-radius: 3px;
        color: gray;
        cursor: pointer;
        border:1px solid lightgray;
    }
    //制御詳細ボタンの文字
    .Button:active {
        background-color: gainsboro;
        border-radius: 3px;
        color: white;
    }
    //クリックした時の時のアクション

    .card.Answer {
        border-width: 6px;
        width: 105%;
        top: -130px;
        left: -4px;
        border-color: #EAEFF8;
    }

    .HEM_terms {
        width: 70%;
        text-align: left;
        padding-left: 30px;
        font: 13px arial;
    }

    .HEM_state {
        text-align: center;
        padding-left: 30px;
        font: 17px arial;
    }

    .HEM_line_T {
        height: 8px;
        background-color: #a2ca87;
    }

    .HEM_line_F {
        height: 8px;
        background-color: #ff8d8d;
    }

    .HEM_CL {
        background-color: #ffcccc;
    }

    .HEM_OP {
        background-color: #a2ca87;
    }

    .info_card {
        width: 480px;
        height: 300px;
        float: left; //左右が入れ替わる
        background-color: white;
        padding: 2px;
        margin-top: 5px; //上下の隙間幅
        border: 3px solid #e7e6e6;
        border-radius: 6px;
    }
    //info全体

    th {
        font-size: 10px;
        background-color: transparent;
        height: 30px;
    }

    table {
        text-align: center;
        width: 100%;
        font-size: 13px;
    }

    .RCue {
        width: 100%;
        height: 10%;
        border: 2px solid gray;
    }

    .RCwind {
        width: 90%;
        height: 90%;
        border: 2px solid gray;
        margin-left: 6%;
        background-color: #bdd7ee;
    }

    .RC {
        width: 100%;
        background-color: white;
        font-size: 13px;
    }


    .Lock_body {
        border: 2px solid red;
        width: 18px;
        height: 15px;
    }

    .Lock_hook_open {
        border: 2px solid red;
        width: 14px;
        height: 8px;
        border-radius: 50px 50px 0 0;
        border-bottom: 0;
        margin-left: 15px;
    }


    .card {
        border: 5px solid lightgray;
        border-radius: 14px;
    }

    .card.allOff {
        border-width: 6px;
        width: 105%;
        top: -200px;
        left: -4px;
        border-color: #748297;
    }

    .card.allOffError {
        border-width: 6px;
        width: 105%;
        top: -200px;
        left: -4px;
        border-color: #FCADAD;
    }

    .card.help {
        border-width: 6px;
        width: 105%;
        top: -130px;
        left: -4px;
        border-color: #EEEEEE;
    }

    .card.target {
        border-width: 6px;
        width: 105%;
        top: -140px;
        left: -10px;
        border-color: #EEEEEE;
    }
</style>